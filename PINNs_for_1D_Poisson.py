import torch
import torch.nn as nn
import numpy as np
import matplotlib.pyplot as plt

# ============================================================
# 0. 固定随机种子（保证可复现）
# ============================================================
torch.manual_seed(42)
np.random.seed(42)

# ============================================================
# 1. 定义神经网络：输入 x，输出 u_hat(x)
# ============================================================
class PINN(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(1, 50),
            nn.Tanh(),
            nn.Linear(50, 50),
            nn.Tanh(),
            nn.Linear(50, 50),
            nn.Tanh(),
            nn.Linear(50, 1)
        )

    def forward(self, x):
        return self.net(x)


# ============================================================
# 2. 定义损失函数
#    总损失 = λ_b * MSE_b + MSE_f
#    边界点复制 ×100 并加权，强制网络优先满足边界条件
# ============================================================
def loss_fn(model, x_f, x_b, u_b):
    # ---------- 2.1 边界条件损失 MSE_b ----------
    u_pred_b = model(x_b)
    mse_b = torch.mean((u_pred_b - u_b) ** 2)

    # ---------- 2.2 PDE 残差损失 MSE_f ----------
    x_f.requires_grad = True
    u_pred_f = model(x_f)

    u_x = torch.autograd.grad(
        outputs=u_pred_f,
        inputs=x_f,
        grad_outputs=torch.ones_like(u_pred_f),
        create_graph=True,
        retain_graph=True
    )[0]

    u_xx = torch.autograd.grad(
        outputs=u_x,
        inputs=x_f,
        grad_outputs=torch.ones_like(u_x),
        create_graph=True,
        retain_graph=True
    )[0]

    f = u_xx + torch.sin(x_f)
    mse_f = torch.mean(f ** 2)

    # ---------- 2.3 总损失（边界加权） ----------
    lambda_b = 10.0
    total_loss = lambda_b * mse_b + mse_f
    return total_loss, mse_b, mse_f


# ============================================================
# 3. 准备训练数据
# ============================================================
# 边界点：复制 100 份，强制网络精确满足边界条件
x_b_original = torch.tensor([[0.0], [2*np.pi]], dtype=torch.float32)
u_b_original = torch.tensor([[0.0], [0.0]], dtype=torch.float32)

x_b = x_b_original.repeat(100, 1)
u_b = u_b_original.repeat(100, 1)

# 内部配点：初始随机撒 200 个点
N_f = 200
x_f = torch.rand(N_f, 1) * 2 * np.pi

# ============================================================
# 4. 训练
# ============================================================
model = PINN()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

# 学习率衰减：每 2000 步衰减为原来的 0.5
scheduler = torch.optim.lr_scheduler.StepLR(optimizer, step_size=2000, gamma=0.5)

# 记录损失
loss_history = []
mse_b_history = []
mse_f_history = []

# 训练 5000 步
for step in range(5000):
    optimizer.zero_grad()
    loss, mse_b, mse_f = loss_fn(model, x_f, x_b, u_b)
    loss.backward()
    optimizer.step()
    scheduler.step()

    loss_history.append(loss.item())
    mse_b_history.append(mse_b.item())
    mse_f_history.append(mse_f.item())

    if step % 500 == 0:
        print(f"Step {step:5d} | Loss: {loss.item():.2e} | MSE_b: {mse_b.item():.2e} | MSE_f: {mse_f.item():.2e} | LR: {optimizer.param_groups[0]['lr']:.1e}")


# ============================================================
# 5. 误差量化
# ============================================================
x_test = torch.linspace(0, 2*np.pi, 200).reshape(-1, 1)
u_pred = model(x_test).detach().numpy()
u_true = np.sin(x_test.numpy())

l2_error = np.linalg.norm(u_pred - u_true) / np.linalg.norm(u_true)
max_error = np.max(np.abs(u_pred - u_true))

print(f"\n=== 最终误差 ===")
print(f"Relative L2 error: {l2_error:.2e}")
print(f"Max absolute error: {max_error:.2e}")


# ============================================================
# 6. 画图
# ============================================================
plt.figure(figsize=(15, 4))

# 左图：解对比
plt.subplot(1, 3, 1)
plt.plot(x_test.numpy(), u_true, 'g-', label='True: sin(x)', linewidth=2)
plt.plot(x_test.numpy(), u_pred, 'b--', label='PINN prediction', linewidth=2)
plt.legend()
plt.xlabel('x')
plt.ylabel('u(x)')
plt.title(f'PINN vs True (L2: {l2_error:.2e})')
plt.grid(alpha=0.3)

# 中图：损失下降
plt.subplot(1, 3, 2)
plt.semilogy(loss_history, label='Total')
plt.semilogy(mse_b_history, label='MSE_b')
plt.semilogy(mse_f_history, label='MSE_f')
plt.xlabel('Step')
plt.ylabel('Loss')
plt.title('Loss Convergence')
plt.legend()
plt.grid(alpha=0.3)

# 右图：绝对误差
plt.subplot(1, 3, 3)
abs_error = np.abs(u_pred - u_true)
plt.plot(x_test.numpy(), abs_error, 'r-', linewidth=2)
plt.xlabel('x')
plt.ylabel('|u_pred - u_true|')
plt.title(f'Pointwise Error (Max: {max_error:.2e})')
plt.grid(alpha=0.3)

plt.tight_layout()
plt.show()