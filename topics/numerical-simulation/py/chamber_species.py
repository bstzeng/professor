# 第 29 課：自由基濃度——穩態對流擴散，晶圓表面是會吃掉粒子的「匯」
import os
import numpy as np
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import spsolve
from chamber_mask import FLUID, WALL, INLET, OUTLET, WAFER

def solve_species(m, ux, uy, u_in, Pe=1.0, Da=1.0, gap=None):
    """Pe = U·G/D，Da = k·G/D，G 是噴淋頭到晶圓的距離（格數）。回傳濃度場 c。"""
    nx, ny = m.shape
    if gap is None:
        gap = ny - 1 - (np.nonzero(m == WAFER)[1][0] + 1)
    D = 1.0                                    # 以 D 為單位，速度與反應速率跟著縮放
    s = Pe * D / (u_in * gap)                  # 把晶格速度換成 Pe 指定的大小
    vx, vy, k = ux * s, uy * s, Da * D / gap
    idx = -np.ones((nx, ny), int)
    fl = np.argwhere(m == FLUID)
    idx[fl[:, 0], fl[:, 1]] = np.arange(len(fl))
    rows, cols, vals = [], [], []
    b = np.zeros(len(fl))
    for n, (i, j) in enumerate(fl):
        diag = 0.0
        for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            a, c = i + di, j + dj
            t = m[a, c]
            if t == FLUID:                         # 一般內部面
                F = 0.5 * (vx[i, j] + vx[a, c]) * di + 0.5 * (vy[i, j] + vy[a, c]) * dj   # 往外為正
                diag += D + max(F, 0.0)            # 擴散 + 往外流（迎風取自己）
                rows.append(n); cols.append(idx[a, c]); vals.append(-(D + max(-F, 0.0)))
            elif t == INLET:                       # 進氣（只在頂部）：c = 1，牆面距格心半格
                diag += 2 * D
                b[n] += 2 * D * 1.0 + s * u_in * 1.0   # 擴散進來 + 氣流帶進來
            elif t == OUTLET:                      # 抽氣：零梯度，只有往外的對流
                F = vx[i, j] * di + vy[i, j] * dj
                diag += max(F, 0.0)
            elif t == WAFER:                       # 晶圓：表面反應通量 k·c
                diag += k
            # WALL：不吃粒子、也不讓粒子穿過 → 什麼都不加
        rows.append(n); cols.append(n); vals.append(diag)
    A = coo_matrix((vals, (rows, cols)), shape=(len(fl), len(fl))).tocsr()
    c = np.zeros((nx, ny))
    c[fl[:, 0], fl[:, 1]] = spsolve(A, b)
    return c

def wafer_profile(m, c):
    wx, wy = np.nonzero(m == WAFER)
    return wx, c[wx, wy + 1]                   # 晶圓正上方那一格的濃度 ∝ 蝕刻速率

def nonuniformity(r):
    return (r.max() - r.min()) / (r.max() + r.min()) * 100   # ±%

if __name__ == "__main__":
    if not os.path.exists("chamber_flow.npz"):
        raise SystemExit("請先執行 chamber_lbm.py 產生流場")
    d = np.load("chamber_flow.npz")
    m, ux, uy = d["m"], d["ux"], d["uy"]
    for Pe, Da in [(0.3, 1.0), (3.0, 1.0), (30.0, 1.0), (3.0, 10.0)]:
        c = solve_species(m, ux, uy, 0.02, Pe, Da)
        x, r = wafer_profile(m, c)
        mid = len(r) // 2
        print(f"Pe={Pe:5.1f} Da={Da:5.1f}：中心 {r[mid]:.3f}、邊緣 {r[0]:.3f}，不均勻度 ±{nonuniformity(r):.1f}%")
    # 質量守恆檢查（Pe = 3, Da = 1）：進來的 = 晶圓吃掉的 + 抽走的
    c = solve_species(m, ux, uy, 0.02, 3.0, 1.0)
    gap = m.shape[1] - 1 - (np.nonzero(m == WAFER)[1][0] + 1)
    s = 3.0 / (0.02 * gap)
    ix, iy = np.nonzero(m == INLET)
    inflow = (2 * (1 - c[ix, iy - 1]) + s * 0.02).sum()
    wx, wy = np.nonzero(m == WAFER)
    eaten = (1.0 / gap * c[wx, wy + 1]).sum()
    ox, oy = np.nonzero(m == OUTLET)
    pumped = (np.maximum(-uy[ox, oy + 1] * s, 0) * c[ox, oy + 1]).sum()
    print(f"進 {inflow:.4f} ＝ 晶圓 {eaten:.4f} ＋ 抽走 {pumped:.4f}（差 {inflow - eaten - pumped:+.1e}）")
