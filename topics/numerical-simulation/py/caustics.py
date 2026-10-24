# 第 37 課：池底的光紋（焦散）——每條光線在水面折射後打到池底，數一數每格落了幾條
import numpy as np

n_w = 1.333                                  # 水的折射率
N, L = 1000, 1.0                             # 1 m × 1 m 的水面，1000×1000 條垂直入射的光線
x = (np.arange(N) + 0.5) * L / N
X, Y = np.meshgrid(x, x, indexing="ij")
rng = np.random.default_rng(1)

# 幾個不同方向的正弦波疊成「有點亂」的水面；斜率與曲率都直接用解析微分
ex = np.zeros_like(X); ey = np.zeros_like(X)
exx = np.zeros_like(X); exy = np.zeros_like(X); eyy = np.zeros_like(X)
for _ in range(8):
    amp = 0.002 / 8**0.5                     # 總振幅約 2 mm
    while True:                              # 波數取 2π/L 的整數倍，水面才能週期地接起來
        mx, my = rng.integers(-10, 11, 2)
        if 4 <= np.hypot(mx, my) <= 10:      # 波長 10–25 cm
            break
    kx, ky = 2 * np.pi * mx / L, 2 * np.pi * my / L
    ph = kx * X + ky * Y + rng.uniform(0, 2 * np.pi)
    ex += -amp * kx * np.sin(ph);  ey += -amp * ky * np.sin(ph)
    exx += -amp * kx * kx * np.cos(ph); exy += -amp * kx * ky * np.cos(ph); eyy += -amp * ky * ky * np.cos(ph)

a = 1 - 1 / n_w                              # 小角度：折射後偏離垂直 ≈ (1 - 1/n) × 斜率，偏向水面較高的一側
kmax = np.max(-(0.5 * (exx + eyy) - np.sqrt(0.25 * (exx - eyy) ** 2 + exy**2)))   # 最凸（向上鼓）的曲率
print(f"最大斜率 {np.hypot(ex, ey).max():.3f}，第一道焦散的深度 ≈ 1/((1-1/n)·κmax) = {1 / (a * kmax):.2f} m")

for H in [0.2, 0.5, 1.0, 2.0, 4.0]:
    bx = (X + H * a * ex) % L                # 光線落在池底的位置（週期包回去）
    by = (Y + H * a * ey) % L
    img, _, _ = np.histogram2d(bx.ravel(), by.ravel(), bins=100, range=[[0, L], [0, L]])
    img /= img.mean()
    print(f"池深 {H:3.1f} m：最亮處是平均的 {img.max():5.2f} 倍，最暗 {img.min():.2f} 倍")
