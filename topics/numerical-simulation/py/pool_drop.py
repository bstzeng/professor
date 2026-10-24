# 第 33 課：一滴水掉進池子——二維波動方程式 η_tt = c² ∇²η，跳蛙法
import numpy as np

N, L, c = 256, 4.0, 1.0                 # 4 m × 4 m 的池面，波速 1 m/s（先不管色散）
dx = L / N
dt = 0.5 * dx / c                       # 二維 CFL：c dt/dx ≤ 1/√2
x = (np.arange(N) + 0.5) * dx
X, Y = np.meshgrid(x, x, indexing="ij")

def lap(f):                             # 牆是反射邊界（∂η/∂n = 0）：用邊緣值補一圈
    g = np.pad(f, 1, mode="edge")
    return (g[2:, 1:-1] + g[:-2, 1:-1] + g[1:-1, 2:] + g[1:-1, :-2] - 4 * f) / dx**2

def energy(eta, eta_prev):
    # 跳蛙法真正守恆的「離散能量」：動能用前後兩步之差，位能用兩步的交叉乘積
    v = (eta - eta_prev) / dt
    return 0.5 * np.sum(v**2 - c**2 * eta * lap(eta_prev)) * dx * dx

eta = 0.01 * np.exp(-((X - 2) ** 2 + (Y - 2) ** 2) / 0.05**2)   # 水滴造成的小凹陷（1 cm）
eta_prev = eta.copy()
E0 = None
r = np.hypot(X - 2, Y - 2)
for n in range(1, 1201):
    eta_next = 2 * eta - eta_prev + (c * dt) ** 2 * lap(eta)
    eta_prev, eta = eta, eta_next
    if n == 2:
        E0 = energy(eta, eta_prev)
    t = n * dt
    if n in (64, 128, 192):                          # 還沒撞到牆（半徑 < 2 m）
        front = r[np.abs(eta) > 1e-4].max()          # 波前：最外面還看得到起伏的地方
        print(f"t = {t:.2f} s：波前半徑 {front:.3f} m（c t = {c * t:.3f}），能量 {energy(eta, eta_prev) / E0:.6f} E0")
    if n in (600, 1200):                             # 撞牆反彈很多次之後
        print(f"t = {t:.2f} s：已在池壁間來回反射，能量 {energy(eta, eta_prev) / E0:.6f} E0")
