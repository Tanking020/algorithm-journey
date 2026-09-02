import torch
import torch.nn as nn
import matplotlib.pyplot as plt
import numpy as np

# ---------------------------
# 1. 定义神经网络
# ---------------------------
class FCNet(nn.Module):
    def __init__(self, layers):
        super(FCNet, self).__init__()
        self.net = nn.Sequential()
        for i in range(len(layers) - 1):
            self.net.add_module(f"linear_{i}", nn.Linear(layers[i], layers[i + 1]))
            if i < len(layers) - 2:
                self.net.add_module(f"tanh_{i}", nn.Tanh())

    def forward(self, x):
        return self.net(x)


# ---------------------------
# 2. 定义 PDE 残差
# ---------------------------
def f(x):
    """源项：u''(x) = -π² sin(πx)，所以 f(x) = π² sin(πx)"""
    return (np.pi ** 2) * torch.sin(np.pi * x)


def pde_residual(model, x):
    """计算 PDE 残差：d²u/dx² + f(x) 应该等于 0"""
    if not x.requires_grad:
        x.requires_grad_(True)

    T = model(x)

    # 一阶导
    dT = torch.autograd.grad(
        T, x,
        grad_outputs=torch.ones_like(T),
        create_graph=True
    )[0]

    # 二阶导
    d2T = torch.autograd.grad(
        dT, x,
        grad_outputs=torch.ones_like(dT),
        create_graph=True
    )[0]

    return d2T + f(x)


# ---------------------------
# 3. 训练设置
# ---------------------------
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")

# 网络结构：1 个输入 -> 20 -> 20 -> 1 个输出
layers = [1, 20, 20, 1]
model = FCNet(layers).to(device)

# 优化器
optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)
epochs = 5000

# 配点：域内 100 个点，用于计算 PDE 残差
x_collocation = torch.linspace(0, 1, 100, requires_grad=True).view(-1, 1).to(device)

# 边界点：x=0 和 x=1，对应 u(0)=0, u(1)=0
x_bc = torch.tensor([[0.0], [1.0]], requires_grad=True).to(device)
u_bc = torch.zeros_like(x_bc)  # 边界真值都是 0


# ---------------------------
# 4. 训练循环
# ---------------------------
loss_history = []

for epoch in range(epochs):
    optimizer.zero_grad()

    # PDE 损失：残差平方均值
    res = pde_residual(model, x_collocation)
    loss_phys = torch.mean(res ** 2)

    # 边界损失：预测值 vs 真值 0
    T_bc = model(x_bc)
    loss_bc = torch.mean((T_bc - u_bc) ** 2)

    # 总损失
    loss = loss_phys + loss_bc
    loss.backward()
    optimizer.step()

    loss_history.append(loss.item())
    if epoch % 500 == 0:
        print(f"Epoch {epoch:5d}, Loss: {loss.item():.6f}")


# ---------------------------
# 5. 画图对比
# ---------------------------
x_test = torch.linspace(0, 1, 100).view(-1, 1).to(device)
T_pred = model(x_test).detach().cpu().numpy()
x_test_np = x_test.cpu().numpy()
T_exact = np.sin(np.pi * x_test_np)

# 计算误差
l2_error = np.linalg.norm(T_pred - T_exact) / np.linalg.norm(T_exact)
max_error = np.max(np.abs(T_pred - T_exact))
print(f"Relative L2 error: {l2_error:.2e}")
print(f"Max absolute error: {max_error:.2e}")

plt.figure(figsize=(10, 4))

# 左图：解对比
plt.subplot(1, 2, 1)
plt.plot(x_test_np, T_pred, label="PINN Prediction")
plt.plot(x_test_np, T_exact, '--', label="Exact Solution")
plt.xlabel("x")
plt.ylabel("T(x)")
plt.legend()
plt.title("PINN vs Exact")
plt.grid()

# 右图：损失下降
plt.subplot(1, 2, 2)
plt.semilogy(loss_history)
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.title("Loss Convergence")
plt.grid()

plt.tight_layout()
plt.show()