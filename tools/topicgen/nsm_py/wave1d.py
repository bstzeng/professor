# 第 14 課：一維波動方程式 u_tt = c² u_xx，跳蛙法；CFL 數 C = c dt/dx
import numpy as np

def run(C, N=200, T=0.6):
    steps = round(T / (C / N))                          # dt = C·dx/c，c = 1；固定模擬到 t = T
    x = np.linspace(0, 1, N + 1)
    u0 = np.exp(-200 * (x - 0.5) ** 2)                   # 一個鼓起的脈衝
    u_prev = u0.copy()
    u = u0.copy()
    u[1:-1] = u0[1:-1] + 0.5 * C**2 * (u0[2:] - 2 * u0[1:-1] + u0[:-2])   # 初速為 0 的第一步
    for _ in range(steps):
        un = np.zeros_like(u)
        un[1:-1] = 2 * u[1:-1] - u_prev[1:-1] + C**2 * (u[2:] - 2 * u[1:-1] + u[:-2])
        u_prev, u = u, un
    return np.max(np.abs(u))

for C in [0.5, 0.9, 1.0, 1.02, 1.1]:
    print(f"C = {C:4.2f}  ->  t = 0.6 時 max|u| = {run(C):.3e}")
