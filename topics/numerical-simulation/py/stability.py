# 第 13 課：顯式在 r > 1/2 會爆掉；隱式（後向尤拉）無條件穩定
import numpy as np
from scipy.sparse import identity, diags
from scipy.sparse.linalg import splu

N = 50
dx = 1.0 / N
x = np.linspace(0, 1, N + 1)

def explicit(r, steps=200):
    u = np.sin(np.pi * x) + 0.01 * np.sin(40 * np.pi * x)   # 加一點高頻擾動
    for _ in range(steps):
        u[1:-1] = u[1:-1] + r * (u[2:] - 2 * u[1:-1] + u[:-2])
    return np.max(np.abs(u))

def implicit(r, steps=200):
    u = np.sin(np.pi * x) + 0.01 * np.sin(40 * np.pi * x)
    A = (identity(N - 1) - r * diags([1, -2, 1], [-1, 0, 1], shape=(N - 1, N - 1), dtype=float)).tocsc()
    lu = splu(A)                                              # 矩陣固定，先分解一次
    for _ in range(steps):
        u[1:-1] = lu.solve(u[1:-1])
    return np.max(np.abs(u))

for r in [0.4, 0.5, 0.6]:
    print(f"顯式 r={r}: max|u| = {explicit(r):.3e}")
for r in [0.6, 5.0]:
    print(f"隱式 r={r}: max|u| = {implicit(r):.3e}")
