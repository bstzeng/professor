# 第 8 課：SciPy——稀疏矩陣求解與常微分方程
import numpy as np
from scipy.sparse import diags
from scipy.sparse.linalg import spsolve
from scipy.integrate import solve_ivp

# 1) 稀疏矩陣：一維 -u'' = 1、u(0)=u(1)=0，解析解 u = x(1-x)/2
N = 100
h = 1.0 / N
A = diags([-1, 2, -1], [-1, 0, 1], shape=(N - 1, N - 1), dtype=float, format="csc") / h**2
u = spsolve(A, np.ones(N - 1))
x = np.linspace(h, 1 - h, N - 1)
print("矩陣非零元素", A.nnz, "／總元素", (N - 1) ** 2, "；最大誤差", np.max(np.abs(u - x * (1 - x) / 2)))

# 2) 常微分方程：阻尼彈簧 x'' + 0.2x' + x = 0
sol = solve_ivp(lambda t, y: [y[1], -0.2 * y[1] - y[0]], [0, 20], [1.0, 0.0], rtol=1e-9, atol=1e-12, dense_output=True)
t = 20.0
wd = np.sqrt(1 - 0.01)
exact = np.exp(-0.1 * t) * (np.cos(wd * t) + 0.1 / wd * np.sin(wd * t))
print("t=20 時數值解", sol.sol(t)[0], "解析解", exact)
