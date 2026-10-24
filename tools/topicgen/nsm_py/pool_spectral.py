# 第 35 課：頻譜法——每個傅立葉模態照自己的 ω(k) 轉動，再乘上黏性衰減 e^{-2νk²t}
import numpy as np

g, sigma, rho, h, nu = 9.81, 0.072, 1000.0, 2.0, 1.0e-6
N, L = 512, 1.0                                 # 1 m × 1 m 的一塊水面
dx = L / N
x = (np.arange(N) - N / 2) * dx
X, Y = np.meshgrid(x, x, indexing="ij")
k1 = 2 * np.pi * np.fft.fftfreq(N, d=dx)
KX, KY = np.meshgrid(k1, k1, indexing="ij")
K = np.hypot(KX, KY)

eta0 = 1e-3 * np.exp(-(X**2 + Y**2) / 0.01**2)  # 1 cm 寬、1 mm 高的小鼓包，初速為 0
E0 = np.fft.fft2(eta0)

def evolve(omega, t):
    """完整的時間演化：η̂(k, t) = η̂(k, 0) cos(ω t) e^{-2νk²t}（初速為 0）。"""
    return np.real(np.fft.ifft2(E0 * np.cos(omega * t) * np.exp(-2 * nu * K**2 * t)))

def band_radius(omega, t, lam0):
    """只留下波長約 lam0 的成分，算它的能量集中在多遠（能量加權的平均半徑）。"""
    k0 = 2 * np.pi / lam0
    sel = np.abs(K - k0) < 0.1 * k0
    eta = np.real(np.fft.ifft2(E0 * sel * np.cos(omega * t)))
    w = eta**2
    return np.sum(np.hypot(X, Y) * w) / np.sum(w)

def cg(om_fn, k, dk=1e-4):
    return (om_fn(k * (1 + dk)) - om_fn(k * (1 - dk))) / (2 * k * dk)

full = lambda k: np.sqrt((g * k + sigma * k**3 / rho) * np.tanh(k * h))
grav = lambda k: np.sqrt(g * k)
flat = lambda k: 0.231 * k
t, lam0 = 1.0, 0.01
k0 = 2 * np.pi / lam0
print(f"t = {t} s，追蹤波長 {lam0 * 100:.0f} cm 的漣漪跑到哪裡：")
for name, fn in [("完整色散（重力＋表面張力）", full), ("只有重力（深水）", grav), ("無色散 c = 0.231 m/s", flat)]:
    rr = band_radius(fn(K), t, lam0)
    print(f"  {name:14s} 數值 {rr * 100:5.1f} cm；群速 × t = {cg(fn, k0) * t * 100:5.1f} cm；相速 × t = {fn(k0) / k0 * t * 100:5.1f} cm")

for lam in [0.005, 0.01, 0.05, 0.2]:
    k = 2 * np.pi / lam
    print(f"波長 {lam * 100:4.1f} cm 的漣漪，振幅衰減到 1/e 需要 {1 / (2 * nu * k**2):8.2f} s")
