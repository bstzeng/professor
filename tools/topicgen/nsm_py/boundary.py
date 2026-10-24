# 第 15 課：四種邊界條件；用一個往右走的脈衝測量反射
import numpy as np

N, C, steps = 400, 0.9, 700
x = np.linspace(0, 1, N + 1)

def run(bc):
    u_prev = np.exp(-500 * (x - 0.3) ** 2)
    u = np.exp(-500 * (x - 0.3 - C / N) ** 2)            # 往右移動一步：右行波
    for _ in range(steps):
        un = np.empty_like(u)
        un[1:-1] = 2 * u[1:-1] - u_prev[1:-1] + C**2 * (u[2:] - 2 * u[1:-1] + u[:-2])
        if bc == "dirichlet":                             # 固定端：u = 0
            un[0] = un[-1] = 0.0
        elif bc == "neumann":                             # 自由端：u_x = 0（鏡像點）
            un[0] = 2 * u[0] - u_prev[0] + 2 * C**2 * (u[1] - u[0])
            un[-1] = 2 * u[-1] - u_prev[-1] + 2 * C**2 * (u[-2] - u[-1])
        elif bc == "absorbing":                           # 一階 Mur 吸收邊界
            k = (C - 1) / (C + 1)
            un[0] = u[1] + k * (un[1] - u[0])
            un[-1] = u[-2] + k * (un[-2] - u[-1])
        u_prev, u = u, un
    return np.max(np.abs(u))

for bc in ["dirichlet", "neumann", "absorbing"]:
    print(f"{bc:10s}: 脈衝撞牆後剩下的最大振幅 {run(bc):.3e}")
# 週期邊界：用 np.roll，從右邊出去就從左邊回來
u = np.exp(-500 * (x[:-1] - 0.3) ** 2)
print("週期邊界：", np.allclose(np.roll(np.roll(u, 5), -5), u))
