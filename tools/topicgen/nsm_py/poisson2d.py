# 第 16 課：二維 Poisson 方程式 -∇²u = f，用 Kronecker 積組出稀疏矩陣
import numpy as np
from scipy.sparse import diags, kron, identity
from scipy.sparse.linalg import spsolve

N = 64
h = 1.0 / N
n = N - 1
T = diags([-1, 2, -1], [-1, 0, 1], shape=(n, n), dtype=float)
A = (kron(identity(n), T) + kron(T, identity(n))).tocsc() / h**2   # 五點差分的拉普拉斯
xs = np.linspace(h, 1 - h, n)
X, Y = np.meshgrid(xs, xs, indexing="ij")
f = 2 * np.pi**2 * np.sin(np.pi * X) * np.sin(np.pi * Y)
u = spsolve(A, f.ravel()).reshape(n, n)
print("未知數", n * n, "，非零元素", A.nnz, "，最大誤差", np.max(np.abs(u - np.sin(np.pi * X) * np.sin(np.pi * Y))))
