# 第 26 課：用 D2Q9 晶格波茲曼法算蝕刻腔剖面的氣流
import numpy as np
from chamber_mask import build_mask, FLUID, WALL, INLET, OUTLET, WAFER

cx = np.array([0, 1, 0, -1, 0, 1, -1, -1, 1])
cy = np.array([0, 0, 1, 0, -1, 1, 1, -1, -1])
wt = np.array([4/9] + [1/9] * 4 + [1/36] * 4)
opp = [0, 3, 4, 1, 2, 7, 8, 5, 6]

def feq(rho, ux, uy):
    s = (9,) + (1,) * np.ndim(rho)               # 讓一維、二維陣列都能用
    cu = 3 * (cx.reshape(s) * ux + cy.reshape(s) * uy)
    return wt.reshape(s) * rho * (1 + cu + 0.5 * cu**2 - 1.5 * (ux**2 + uy**2))

def solve_flow(m, u_in=0.02, tau=1.0, max_steps=30000, tol=1e-7, verbose=True):
    nx, ny = m.shape
    solid = (m == WALL) | (m == WAFER)
    inlet, outlet = m == INLET, m == OUTLET
    rho = np.ones((nx, ny)); ux = np.zeros((nx, ny)); uy = np.zeros((nx, ny))
    f = feq(rho, ux, uy)
    # 進氣口當成「往下移動的牆」：反彈時多加一份動量 6 w_i ρ (c_i·u)
    kick = (6 * wt * cy * (-u_in))[:, None]
    # 抽氣口用「隔壁流體格」的速度
    ox, oy = np.nonzero(outlet)
    nbx = np.clip(ox + np.where(ox == 0, 1, np.where(ox == nx - 1, -1, 0)), 0, nx - 1)
    nby = np.clip(oy + np.where(oy == 0, 1, 0), 0, ny - 1)
    old = np.zeros((nx, ny))
    for step in range(max_steps):
        rho = f.sum(0)
        ux = (f * cx[:, None, None]).sum(0) / rho
        uy = (f * cy[:, None, None]).sum(0) / rho
        ux[solid] = uy[solid] = 0.0
        fpost = f - (f - feq(rho, ux, uy)) / tau          # 碰撞
        fpost[:, solid] = f[:, solid][opp]                # 牆與晶圓：反彈
        fpost[:, inlet] = f[:, inlet][opp] + kick         # 進氣：帶速度的反彈
        fpost[:, ox, oy] = feq(np.ones(len(ox)), ux[nbx, nby], uy[nbx, nby])   # 抽氣：ρ = 1
        for i in range(9):                                # 串流
            f[i] = np.roll(np.roll(fpost[i], cx[i], 0), cy[i], 1)
        if step % 500 == 0 and step:
            change = np.abs(uy - old)[m == FLUID].max() / u_in   # 只看氣體格
            old = uy.copy()
            if verbose:
                print(f"  第 {step:5d} 步，速度變化 {change:.1e}")
            if change < tol * 500:
                break
    ux[m != FLUID] = 0.0
    uy[m != FLUID] = 0.0
    return ux, uy, rho, step

if __name__ == "__main__":
    m = build_mask()
    ux, uy, rho, n = solve_flow(m)
    nx, ny = m.shape
    q_in = -uy[m[:, -1] == INLET, -2].sum()           # 噴淋頭下方一列往下的流量
    q_out = -uy[m[:, 0] == OUTLET, 1].sum()           # 抽氣口上方一列往下的流量
    print(f"{n} 步收斂；進氣流量 {q_in:.3f}，抽氣流量 {q_out:.3f}（晶格單位）")
    sp = np.hypot(ux, uy)
    print(f"最大速度 {sp.max():.4f}，密度範圍 {rho[m == FLUID].min():.4f}–{rho[m == FLUID].max():.4f}")
    wafer_y = np.nonzero(m == WAFER)[1][0] + 1
    print("晶圓上方 15 格處的下沖速度（左→右，取 7 點）：",
          np.round(-uy[np.linspace(33, 86, 7).astype(int), wafer_y + 15], 4))
    np.savez("chamber_flow.npz", ux=ux, uy=uy, m=m)
