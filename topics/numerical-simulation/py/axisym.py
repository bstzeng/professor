# 第 27 課：軸對稱座標——圓柱內均勻發熱的溫度 (1/r) d/dr (r dT/dr) = -q/k
import numpy as np
from scipy.sparse import diags
from scipy.sparse.linalg import spsolve

q, k, R = 1.0e6, 20.0, 0.01          # W/m³、W/(m·K)、m

def solve(N, src=None):
    r = np.linspace(0, R, N + 1)
    h = R / N
    main = np.zeros(N); lo = np.zeros(N - 1); up = np.zeros(N - 1)
    # r = 0：對稱，(1/r)(rT')' → 2T''，再用鏡像點 T(-h) = T(h) 得 4(T1 - T0)/h²
    main[0], up[0] = -4 / h**2, 4 / h**2
    for i in range(1, N):
        rp, rm = r[i] + h / 2, r[i] - h / 2       # 半格位置的 r
        main[i] = -(rp + rm) / (r[i] * h**2)
        if i + 1 < N:
            up[i] = rp / (r[i] * h**2)
        lo[i - 1] = rm / (r[i] * h**2)
    A = diags([lo, main, up], [-1, 0, 1], format="csc")
    T = np.zeros(N + 1)                            # T(R) = 0
    rhs = np.full(N, -q / k) if src is None else -src(r[:N])
    T[:N] = spsolve(A, rhs)
    return r, T

for N in [10, 20, 40, 80]:
    r, T = solve(N)
    exact = q * (R**2 - r**2) / (4 * k)
    print(f"N={N:3d}  中心溫升 {T[0]:.4f} K（解析 {exact[0]:.4f}），最大誤差 {np.abs(T - exact).max():.2e}")

# 拋物線剛好被二階差分「完全吃下」，誤差只剩捨入。換一個非多項式的製造解看收斂階數：
a = np.pi / (2 * R)                                # T = cos(a r)，T(R) = 0
def src(r):                                        # src = -(1/r)(r T')'
    out = a**2 * np.cos(a * r)
    out[1:] += a * np.sin(a * r[1:]) / r[1:]
    out[0] += a**2                                 # r → 0 時 sin(ar)/r → a
    return out
prev = None
for N in [10, 20, 40, 80]:
    r, T = solve(N, src)
    e = np.abs(T - np.cos(a * r)).max()
    print(f"製造解 N={N:3d} 最大誤差 {e:.2e}" + (f"  階數 {np.log2(prev / e):.2f}" if prev else ""))
    prev = e
