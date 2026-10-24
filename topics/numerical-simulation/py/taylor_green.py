# 第 18 課：把 Taylor–Green 渦流代入 Navier–Stokes，逐項算出每一項的大小
import numpy as np

nu, t, N = 0.01, 0.5, 128
L = 2 * np.pi
x = np.linspace(0, L, N, endpoint=False)
X, Y = np.meshgrid(x, x, indexing="ij")
h = L / N
F = np.exp(-2 * nu * t)                     # 解析解的衰減因子

u = np.cos(X) * np.sin(Y) * F
v = -np.sin(X) * np.cos(Y) * F
p = -0.25 * (np.cos(2 * X) + np.cos(2 * Y)) * F**2   # 密度取 1

def dx(f): return (np.roll(f, -1, 0) - np.roll(f, 1, 0)) / (2 * h)   # 週期中央差分
def dy(f): return (np.roll(f, -1, 1) - np.roll(f, 1, 1)) / (2 * h)
def lap(f):
    return (np.roll(f, -1, 0) + np.roll(f, 1, 0) + np.roll(f, -1, 1) + np.roll(f, 1, 1) - 4 * f) / h**2

dudt = -2 * nu * u                           # 解析的時間導數
conv = u * dx(u) + v * dy(u)                 # 對流項
grad = dx(p)                                 # 壓力梯度
visc = nu * lap(u)                           # 黏性項
res = dudt + conv + grad - visc              # 方程式應該等於 0

for name, f in [("∂u/∂t", dudt), ("(u·∇)u", conv), ("∂p/∂x", grad), ("ν∇²u", visc), ("殘差", res)]:
    print(f"{name:8s} 最大值 {np.abs(f).max():.3e}")
print("散度最大值", np.abs(dx(u) + dy(v)).max())
