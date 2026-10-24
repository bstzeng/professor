# 第 4 課：製造解法（MMS）驗證程式——解 -u'' = f，選定 u = sin(πx) 反推 f
import numpy as np
from scipy.sparse import diags
from scipy.sparse.linalg import spsolve

def solve(N):
    h = 1.0 / N
    x = np.linspace(0, 1, N + 1)
    f = np.pi**2 * np.sin(np.pi * x[1:-1])          # 由製造解反推的源項
    A = diags([-1, 2, -1], [-1, 0, 1], shape=(N - 1, N - 1), dtype=float) / h**2
    u = spsolve(A.tocsc(), f)
    return np.max(np.abs(u - np.sin(np.pi * x[1:-1])))

prev = None
for N in [10, 20, 40, 80, 160]:
    e = solve(N)
    order = "" if prev is None else f"  收斂階數 ≈ {np.log2(prev / e):.2f}"
    print(f"N={N:4d}  最大誤差={e:.3e}{order}")
    prev = e
