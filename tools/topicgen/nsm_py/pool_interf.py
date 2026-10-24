# 第 34 課：兩個波源的干涉——數值解的節線位置和「路徑差 = 半波長的奇數倍」比較
import numpy as np
from scipy.signal import argrelmin

N, L, c, f = 256, 4.0, 1.0, 2.5
lam = c / f                                    # 波長 0.4 m
dx = L / N
dt = 0.5 * dx / c
x = (np.arange(N) + 0.5) * dx
X, Y = np.meshgrid(x, x, indexing="ij")

# 池邊加一圈「海綿層」吸收外傳的波，避免反射干擾
d = np.minimum.reduce([X, L - X, Y, L - Y])
gamma = np.where(d < 0.5, 20 * (1 - d / 0.5) ** 2, 0.0)

def lap(u):
    g = np.pad(u, 1, mode="edge")
    return (g[2:, 1:-1] + g[:-2, 1:-1] + g[1:-1, 2:] + g[1:-1, :-2] - 4 * u) / dx**2

src = [(2.0 - 0.4, 1.0), (2.0 + 0.4, 1.0)]     # 兩個同相位的波源，相距 0.8 m = 2λ
mask = sum(np.exp(-((X - sx) ** 2 + (Y - sy) ** 2) / 0.03**2) for sx, sy in src)
eta = np.zeros((N, N)); prev = np.zeros((N, N)); amp = np.zeros((N, N))
steps = int(8.0 / dt)
for n in range(steps):
    t = n * dt
    forcing = mask * np.sin(2 * np.pi * f * t)
    nxt = (2 * eta - (1 - gamma * dt / 2) * prev + dt**2 * (c**2 * lap(eta) + forcing)) / (1 + gamma * dt / 2)
    prev, eta = eta, nxt
    if t > 6.0:                                # 進入穩態後記錄振幅
        amp = np.maximum(amp, np.abs(eta))

j = int(3.0 / dx)                              # 觀察線 y = 3.0 m
line = amp[:, j]
xs = x[(x > 0.6) & (x < 3.4)]
seg = line[(x > 0.6) & (x < 3.4)]
mins = xs[argrelmin(seg, order=3)[0]]
print("數值解的節點 x：", np.round(mins, 3))
r1 = np.hypot(xs - src[0][0], 3.0 - src[0][1])
r2 = np.hypot(xs - src[1][0], 3.0 - src[1][1])
m = np.round((r1 - r2) / lam)                 # 最接近的整數；它跳號的地方，路徑差正好是 (m + ½) λ
i = np.nonzero(np.diff(m) != 0)[0]
theory = 0.5 * (xs[i] + xs[i + 1])
print("理論節點 x：  ", np.round(theory, 3))
