# 第 12 課：一維熱傳導 u_t = α u_xx，顯式 FTCS，與解析解 e^{-απ²t} sin(πx) 比較
import numpy as np

alpha, L, N = 1.0, 1.0, 50
dx = L / N
r = 0.4                                     # r = α dt / dx²
dt = r * dx**2 / alpha
x = np.linspace(0, L, N + 1)
u = np.sin(np.pi * x)                       # 初始條件；兩端 u = 0
t, T = 0.0, 0.1
while t < T - 1e-12:
    u[1:-1] = u[1:-1] + r * (u[2:] - 2 * u[1:-1] + u[:-2])
    t += dt
exact = np.exp(-alpha * np.pi**2 * t) * np.sin(np.pi * x)
print(f"步數 {int(round(t/dt))}，t = {t:.4f}，最大誤差 {np.max(np.abs(u - exact)):.2e}")
print(f"中點溫度 數值 {u[N//2]:.6f}  解析 {exact[N//2]:.6f}")
