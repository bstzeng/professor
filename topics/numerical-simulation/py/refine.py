# 第 17 課：網格加密研究與 Richardson 外插
import numpy as np
from scipy.sparse import diags
from scipy.sparse.linalg import spsolve

def mid_value(N):
    # 解 -u'' = e^x，u(0)=u(1)=0，回傳 x=0.5 的值
    h = 1.0 / N
    x = np.linspace(0, 1, N + 1)
    A = diags([-1, 2, -1], [-1, 0, 1], shape=(N - 1, N - 1), dtype=float, format="csc") / h**2
    u = spsolve(A, np.exp(x[1:-1]))
    return u[N // 2 - 1]

exact = -np.exp(0.5) + 1 + 0.5 * (np.e - 1)               # 解析解 u = -e^x + 1 + x(e-1)
vals = {N: mid_value(N) for N in [8, 16, 32, 64]}
for N, v in vals.items():
    print(f"N={N:3d}  u(0.5)={v:.8f}  誤差={abs(v - exact):.2e}")
p = np.log2((vals[16] - vals[8]) / (vals[32] - vals[16]))
rich = vals[64] + (vals[64] - vals[32]) / (2**p - 1)
print(f"觀測階數 p ≈ {p:.3f}；Richardson 外插 {rich:.8f}（誤差 {abs(rich - exact):.1e}）")
