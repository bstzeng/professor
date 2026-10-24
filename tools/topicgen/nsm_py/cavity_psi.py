# 第 22 課：渦度–流函數法解頂蓋驅動方腔流（Re = 100），和 Ghia 等人 1982 的基準比較
import numpy as np
from scipy.sparse import diags, kron, identity
from scipy.sparse.linalg import splu

Re, N = 100.0, 65                 # N×N 個格點（含邊界）
h = 1.0 / (N - 1)
n = N - 2                         # 內部點數
T = diags([1, -2, 1], [-1, 0, 1], shape=(n, n), dtype=float)
I = identity(n)
lap = splu(((kron(T, I) + kron(I, T)) / h**2).tocsc())   # 只分解一次，之後每步都很快

psi = np.zeros((N, N))            # 陣列索引 [i, j] = [x, y]
w = np.zeros((N, N))
dt = 0.2 * h * h * Re             # 擴散穩定限制 dt < h²Re/4，取保守一點
U = 1.0                           # 頂蓋速度

for it in range(20000):
    # 1) 由渦度解流函數：∇²ψ = -ω
    psi[1:-1, 1:-1] = lap.solve(-w[1:-1, 1:-1].ravel()).reshape(n, n)
    # 2) 牆上的渦度（Thom 公式）
    w[:, 0] = -2 * psi[:, 1] / h**2                  # 底
    w[:, -1] = -2 * psi[:, -2] / h**2 - 2 * U / h    # 頂（會動）
    w[0, :] = -2 * psi[1, :] / h**2                  # 左
    w[-1, :] = -2 * psi[-2, :] / h**2                # 右
    # 3) 渦度輸送：ω_t + u ω_x + v ω_y = (1/Re) ∇²ω
    u = (psi[1:-1, 2:] - psi[1:-1, :-2]) / (2 * h)   # u =  ∂ψ/∂y
    v = -(psi[2:, 1:-1] - psi[:-2, 1:-1]) / (2 * h)  # v = -∂ψ/∂x
    wx = (w[2:, 1:-1] - w[:-2, 1:-1]) / (2 * h)
    wy = (w[1:-1, 2:] - w[1:-1, :-2]) / (2 * h)
    lw = (w[2:, 1:-1] + w[:-2, 1:-1] + w[1:-1, 2:] + w[1:-1, :-2] - 4 * w[1:-1, 1:-1]) / h**2
    dw = dt * (-u * wx - v * wy + lw / Re)
    w[1:-1, 1:-1] += dw
    if np.abs(dw).max() / dt < 1e-4:          # 渦度幾乎不再變化 → 穩態
        break

c = N // 2
u_center = (psi[c, c + 1] - psi[c, c - 1]) / (2 * h)
print(f"疊代 {it} 步收斂")
print(f"中心點 u = {u_center:.4f}   （Ghia：-0.2058）")
print(f"ψ 最小值 = {psi.min():.4f}   （Ghia：-0.1034）")
i, j = np.unravel_index(psi.argmin(), psi.shape)
print(f"主渦中心 ≈ ({i * h:.3f}, {j * h:.3f})   （Ghia：(0.617, 0.734)）")
np.savez("cavity_psi.npz", psi=psi, w=w)
