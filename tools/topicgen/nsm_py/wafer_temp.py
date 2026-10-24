# 第 28 課：晶圓溫度——薄圓盤的徑向導熱 + 背面氦氣冷卻 + 邊緣額外加熱
#   k t (1/r)(r T')' - h(r) (T - Tc) + q(r) = 0，T'(0) = 0，T'(R) = 0
import numpy as np
from scipy.sparse import diags
from scipy.sparse.linalg import spsolve

k, t, R = 130.0, 775e-6, 0.15        # 矽的導熱、晶圓厚度、半徑
Tc = 20.0                            # 靜電吸盤溫度 °C
N = 300
r = np.linspace(0, R, N + 1)
dr = R / N

def solve(h, q):
    kt = k * t
    main = np.zeros(N + 1); lo = np.zeros(N); up = np.zeros(N)
    main[0], up[0] = -4 * kt / dr**2, 4 * kt / dr**2            # r = 0 對稱
    for i in range(1, N + 1):
        rp, rm = r[i] + dr / 2, r[i] - dr / 2
        if i == N:                                               # r = R 絕熱：鏡像點
            lo[i - 1] = 2 * kt / dr**2
            main[i] = -2 * kt / dr**2
        else:
            lo[i - 1] = kt * rm / (r[i] * dr**2)
            up[i] = kt * rp / (r[i] * dr**2)
            main[i] = -kt * (rp + rm) / (r[i] * dr**2)
    A = diags([lo, main - h, up], [-1, 0, 1], format="csc")
    return Tc + spsolve(A, -q)                                   # 解的是 T - Tc

q = np.full(N + 1, 1.5e4)                    # 電漿給晶圓的熱通量 W/m²
q[r > 0.145] += 2.0e4                        # 邊緣環附近多出來的熱
cases = {
    "單區氦氣 h = 600":       np.full(N + 1, 600.0),
    "雙區：外圈 h = 900":     np.where(r > 0.12, 900.0, 600.0),
    "雙區：外圈 h = 1500":    np.where(r > 0.12, 1500.0, 600.0),
}
for name, h in cases.items():
    T = solve(h, q)
    print(f"{name:16s} 中心 {T[0]:.2f} °C，邊緣 {T[-1]:.2f} °C，全片溫差 {T.max() - T.min():.2f} K")
print(f"熱擴散長度 L = sqrt(k t / h) = {np.sqrt(k * t / 600) * 1e3:.1f} mm（溫度不均只會在邊緣這麼寬的範圍內）")
