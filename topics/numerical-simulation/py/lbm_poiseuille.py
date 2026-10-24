# 第 23 課：D2Q9 晶格波茲曼法（BGK），用體積力推動的平板流驗證拋物線解
import numpy as np

# D2Q9 的 9 個速度方向與權重
cx = np.array([0, 1, 0, -1, 0, 1, -1, -1, 1])
cy = np.array([0, 0, 1, 0, -1, 1, 1, -1, -1])
wt = np.array([4/9] + [1/9] * 4 + [1/36] * 4)
opp = [0, 3, 4, 1, 2, 7, 8, 5, 6]            # 反方向，用來做反彈

def feq(rho, ux, uy):
    cu = 3 * (cx[:, None, None] * ux + cy[:, None, None] * uy)
    usq = 1.5 * (ux**2 + uy**2)
    return wt[:, None, None] * rho * (1 + cu + 0.5 * cu**2 - usq)

nx, ny = 4, 33                                # x 方向週期；y = 0 與 y = ny-1 是牆
tau = 0.8
nu = (tau - 0.5) / 3                          # 晶格單位的運動黏度
g = 1e-5                                      # x 方向體積力（像壓力梯度）
solid = np.zeros((nx, ny), bool)
solid[:, 0] = solid[:, -1] = True

rho = np.ones((nx, ny)); ux = np.zeros((nx, ny)); uy = np.zeros((nx, ny))
f = feq(rho, ux, uy)
for step in range(20000):
    rho = f.sum(0)
    ux = (f * cx[:, None, None]).sum(0) / rho + 0.5 * g / rho   # 加力的半步修正
    uy = (f * cy[:, None, None]).sum(0) / rho
    # 碰撞（BGK）＋ Guo 體積力項
    cu = cx[:, None, None] * ux + cy[:, None, None] * uy
    Fi = (1 - 0.5 / tau) * wt[:, None, None] * (3 * (cx[:, None, None] - ux) + 9 * cu * cx[:, None, None]) * g
    fpost = f - (f - feq(rho, ux, uy)) / tau + Fi
    fpost[:, solid] = f[:, solid][opp]        # 牆：反彈
    # 串流
    for i in range(9):
        f[i] = np.roll(np.roll(fpost[i], cx[i], 0), cy[i], 1)

u = ux[0, 1:-1]
H = ny - 2                                    # 反彈牆位在牆格點與流體之間的半格處
y = np.arange(1, ny - 1) - 0.5
exact = g / (2 * nu) * y * (H - y)
print(f"中心速度 LBM = {u.max():.6e}，解析 = {exact.max():.6e}")
print(f"最大相對誤差 {np.abs(u - exact).max() / exact.max():.2e}")
