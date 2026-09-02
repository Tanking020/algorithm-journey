import torch
import torch.nn as nn
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# ============================================================
# 0. 固定随机种子（保证可复现）
# ============================================================
torch.manual_seed(42)
np.random.seed(42)

# ============================================================
# 1. 定义神经网络：输入 (x,y)，输出 u_hat(x,y)
#    【对比一维】Linear(1,50) -> Linear(2,50)
# ============================================================
class PINN2D(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(2, 50),    # 输入 (x, y)
            nn.Tanh(),
            nn.Linear(50, 50),
            nn.Tanh(),
            nn.Linear(50, 50),
            nn.Tanh(),
            nn.Linear(50, 1)     # 输出 u(x, y)
        )

    def forward(self, x):
        return self.net(x)


# ============================================================
# 2. 定义损失函数
#    总损失 = λ_b * MSE_b + MSE_f
#    【对比一维】u_xx -> (u_xx + u_yy)，边界点变 4 条边
# ============================================================
def pde_residual(model, x):
    """计算 PDE 残差：∇²u - f，希望趋近 0"""
    x.requires_grad = True
    u = model(x)                         # (N, 1)

    # 一阶导：对 (x, y) 同时求导
    grad = torch.autograd.grad(
        outputs=u,
        inputs=x,
        grad_outputs=torch.ones_like(u),
        create_graph=True,
        retain_graph=True
    )[0]                                 # (N, 2)

    u_x = grad[:, 0:1]                   # ∂u/∂x
    u_y = grad[:, 1:2]                   # ∂u/∂y

    # 二阶导
    u_xx = torch.autograd.grad(
        outputs=u_x, inputs=x,
        grad_outputs=torch.ones_like(u_x),
        create_graph=True, retain_graph=True
    )[0][:, 0:1]                         # ∂²u/∂x²

    u_yy = torch.autograd.grad(
        outputs=u_y, inputs=x,
        grad_outputs=torch.ones_like(u_y),
        create_graph=True, retain_graph=True
    )[0][:, 1:2]                         # ∂²u/∂y²

    # 源项 f(x,y) = -2π² sin(πx) sin(πy)
    f = -2 * np.pi**2 * torch.sin(np.pi * x[:, 0:1]) * torch.sin(np.pi * x[:, 1:2])

    # PDE 残差：∇²u - f = 0
    return u_xx + u_yy - f


def loss_fn(model, x_f, x_b, u_b):
    # ---------- 2.1 边界条件损失 MSE_b ----------
    u_pred_b = model(x_b)
    mse_b = torch.mean((u_pred_b - u_b) ** 2)

    # ---------- 2.2 PDE 残差损失 MSE_f ----------
    res = pde_residual(model, x_f)
    mse_f = torch.mean(res ** 2)

    # ---------- 2.3 总损失（边界加权） ----------
    lambda_b = 10.0
    total_loss = lambda_b * mse_b + mse_f
    return total_loss, mse_b, mse_f


# ============================================================
# 3. 准备训练数据
# ============================================================
# 边界点：四条边各采样 N_b 个点，每条边复制 25 份增强
# 【对比一维】2 个边界点 -> 4 条边
N_b_each = 100
x_bottom = torch.cat([torch.rand(N_b_each, 1), torch.zeros(N_b_each, 1)], dim=1)  # y=0
x_top    = torch.cat([torch.rand(N_b_each, 1), torch.ones(N_b_each, 1)],  dim=1)  # y=1
x_left   = torch.cat([torch.zeros(N_b_each, 1), torch.rand(N_b_each, 1)], dim=1)  # x=0
x_right  = torch.cat([torch.ones(N_b_each, 1),  torch.rand(N_b_each, 1)], dim=1)  # x=1

x_b = torch.cat([x_bottom, x_top, x_left, x_right], dim=0)  # (4*N_b_each, 2)
u_b = torch.zeros_like(x_b[:, :1])                          # 边界值全为 0

# 内部配点：单位正方形内随机撒 N_f 个点
N_f = 2000
x_f = torch.rand(N_f, 2)   # (x, y) ∈ [0,1] × [0,1]

# ============================================================
# 4. 训练
# ============================================================
model = PINN2D()
optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)
scheduler = torch.optim.lr_scheduler.StepLR(optimizer, step_size=2000, gamma=0.5)

epochs = 10000   # 二维建议多一点
loss_history = []
mse_b_history = []
mse_f_history = []

for step in range(epochs):
    optimizer.zero_grad()
    loss, mse_b, mse_f = loss_fn(model, x_f, x_b, u_b)
    loss.backward()
    optimizer.step()
    scheduler.step()

    loss_history.append(loss.item())
    mse_b_history.append(mse_b.item())
    mse_f_history.append(mse_f.item())

    if step % 1000 == 0:
        print(f"Step {step:5d} | Loss: {loss.item():.2e} | MSE_b: {mse_b.item():.2e} | MSE_f: {mse_f.item():.2e} | LR: {optimizer.param_groups[0]['lr']:.1e}")

# ============================================================
# 5. 误差量化
# ============================================================
n = 100
x_lin = torch.linspace(0, 1, n)
y_lin = torch.linspace(0, 1, n)
X, Y = torch.meshgrid(x_lin, y_lin, indexing='ij')
XY = torch.stack([X.flatten(), Y.flatten()], dim=1)   # (n*n, 2)

U_pred = model(XY).detach().numpy().reshape(n, n)
U_true = (np.sin(np.pi * X.numpy()) * np.sin(np.pi * Y.numpy())).reshape(n, n)

l2_error = np.linalg.norm(U_pred - U_true) / np.linalg.norm(U_true)
max_error = np.max(np.abs(U_pred - U_true))

print(f"\n=== 最终误差 ===")
print(f"Relative L2 error: {l2_error:.2e}")
print(f"Max absolute error: {max_error:.2e}")

# ============================================================
# 6. 画图
# ============================================================
fig = plt.figure(figsize=(18, 4.2))

# 左图：PINN 解 3D 曲面
ax1 = fig.add_subplot(1, 4, 1, projection='3d')
ax1.plot_surface(X.numpy(), Y.numpy(), U_pred, cmap='viridis', alpha=0.85)
ax1.set_title("PINN Solution")
ax1.set_xlabel("x")
ax1.set_ylabel("y")
ax1.set_zlabel("u")

# 中左：解析解 3D 曲面
ax2 = fig.add_subplot(1, 4, 2, projection='3d')
ax2.plot_surface(X.numpy(), Y.numpy(), U_true, cmap='plasma', alpha=0.85)
ax2.set_title("Exact: sin(πx)sin(πy)")
ax2.set_xlabel("x")
ax2.set_ylabel("y")

# 中右：绝对误差云图
ax3 = fig.add_subplot(1, 4, 3)
im = ax3.contourf(X.numpy(), Y.numpy(), np.abs(U_pred - U_true), levels=50, cmap='hot')
ax3.set_title(f"Abs Error (Max: {max_error:.2e})")
ax3.set_xlabel("x")
ax3.set_ylabel("y")
plt.colorbar(im, ax=ax3)

# 右图：损失曲线
ax4 = fig.add_subplot(1, 4, 4)
ax4.semilogy(loss_history, label='Total')
ax4.semilogy(mse_b_history, label='MSE_b')
ax4.semilogy(mse_f_history, label='MSE_f')
ax4.set_title("Loss Convergence")
ax4.set_xlabel("Epoch")
ax4.set_ylabel("Loss")
ax4.legend()
ax4.grid(alpha=0.3)

plt.tight_layout()
plt.show()