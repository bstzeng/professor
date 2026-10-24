# 第 21 課：Chorin 投影法（原始變數 u, v, p）解頂蓋驅動方腔流 Re = 100
import numpy as np
from scipy.sparse import diags, kron, identity, csc_matrix
from scipy.sparse.linalg import splu

def cavity(N, Re=100.0):
    h = 1.0 / (N - 1)
    dt = 0.08 * h                                  # 跟著網格縮小時間步
    nu = 1.0 / Re
    # 壓力 Poisson 方程式（Neumann 邊界）：∇²p = (ρ/dt) ∇·u*
    def neumann_1d(n):
        T = diags([1, -2, 1], [-1, 0, 1], shape=(n, n), dtype=float).tolil()
        T[0, 1] = 2.0                                  # 鏡像點：∂p/∂n = 0
        T[-1, -2] = 2.0
        return T.tocsc()
    T = neumann_1d(N)
    I = identity(N)
    A = ((kron(T, I) + kron(I, T)) / h**2).tolil()
    A[0, :] = 0.0                                      # 釘住一點 p = 0，消除常數不定性
    A[0, 0] = 1.0
    P = splu(csc_matrix(A))

    u = np.zeros((N, N)); v = np.zeros((N, N)); p = np.zeros((N, N))
    def ddx(f): return (f[2:, 1:-1] - f[:-2, 1:-1]) / (2 * h)
    def ddy(f): return (f[1:-1, 2:] - f[1:-1, :-2]) / (2 * h)
    def lap(f): return (f[2:, 1:-1] + f[:-2, 1:-1] + f[1:-1, 2:] + f[1:-1, :-2] - 4 * f[1:-1, 1:-1]) / h**2

    for it in range(20000):
        un = u.copy()
        # 1) 預測：先不管壓力
        us, vs = u.copy(), v.copy()
        ui, vi = u[1:-1, 1:-1], v[1:-1, 1:-1]
        us[1:-1, 1:-1] = ui + dt * (-ui * ddx(u) - vi * ddy(u) + nu * lap(u))
        vs[1:-1, 1:-1] = vi + dt * (-ui * ddx(v) - vi * ddy(v) + nu * lap(v))
        # 2) 解壓力
        b = np.zeros((N, N))
        b[1:-1, 1:-1] = (ddx(us) + ddy(vs)) / dt
        b.flat[0] = 0.0
        p = P.solve(b.ravel()).reshape(N, N)
        # 3) 修正：減掉壓力梯度
        u[1:-1, 1:-1] = us[1:-1, 1:-1] - dt * ddx(p)
        v[1:-1, 1:-1] = vs[1:-1, 1:-1] - dt * ddy(p)
        u[:, -1] = 1.0                                 # 頂蓋 u = 1，其他牆 u = v = 0 不變
        if it > 100 and np.abs(u - un).max() / dt < 1e-4:
            break

    c = N // 2
    div = ddx(u) + ddy(v)
    return it, u[c, c], np.abs(div).mean()

for N in [21, 41, 81]:
    it, uc, dv = cavity(N)
    print(f"N = {N:3d}：{it:6d} 步，中心點 u = {uc:.4f}（Ghia：-0.2058），平均 |散度| {dv:.1e}")
