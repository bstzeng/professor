# 第 38 課：效能——網格加倍，成本變幾倍？float32 有幫助嗎？
import time
import numpy as np

def leapfrog_time(N, dtype, steps=50):
    eta = np.zeros((N, N), dtype); prev = np.zeros((N, N), dtype)
    eta[N // 2, N // 2] = 1
    C2 = dtype(0.25)
    t0 = time.perf_counter()
    for _ in range(steps):
        lap = np.zeros_like(eta)
        lap[1:-1, 1:-1] = eta[2:, 1:-1] + eta[:-2, 1:-1] + eta[1:-1, 2:] + eta[1:-1, :-2] - 4 * eta[1:-1, 1:-1]
        prev, eta = eta, 2 * eta - prev + C2 * lap
    return (time.perf_counter() - t0) / steps

def fft_time(N, reps=10):
    a = np.random.rand(N, N)
    t0 = time.perf_counter()
    for _ in range(reps):
        np.fft.ifft2(np.fft.fft2(a))
    return (time.perf_counter() - t0) / reps

print("    N    每步(f64)   每步(f32)   一對 FFT    1 秒動畫(60 幀×4 步)要算多久")
for N in [128, 256, 512, 1024]:
    t64 = leapfrog_time(N, np.float64)
    t32 = leapfrog_time(N, np.float32)
    tf = fft_time(N)
    print(f"{N:5d}  {t64 * 1e3:8.3f} ms  {t32 * 1e3:8.3f} ms  {tf * 1e3:8.3f} ms   {t32 * 240:6.2f} s")
print("另外：二維顯式法的 dt ∝ dx，所以模擬同樣的物理時間，N 加倍 → 格點 ×4、步數 ×2 → 總成本 ×8")
