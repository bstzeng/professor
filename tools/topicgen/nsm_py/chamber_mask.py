# 第 25 課：用一張整數陣列描述蝕刻腔剖面——哪裡是氣體、牆、進氣、抽氣、晶圓
import numpy as np

FLUID, WALL, INLET, OUTLET, WAFER = 0, 1, 2, 3, 4

def build_mask(nx=120, ny=60, outlet="bottom", shower=(22, 98), pedestal=(32, 88), ph=18):
    """回傳 m[x, y]；y = 0 在腔底。"""
    m = np.full((nx, ny), FLUID, dtype=np.int8)
    m[0, :] = m[-1, :] = WALL
    m[:, 0] = m[:, -1] = WALL
    m[shower[0]:shower[1], -1] = INLET              # 頂部噴淋頭
    a, b = pedestal
    m[a:b, :ph] = WALL                              # 晶圓座（實心）
    m[a:b, ph - 1] = WAFER                          # 座的頂面就是晶圓
    if outlet == "bottom":                          # 底部兩側抽氣口
        m[2:22, 0] = OUTLET
        m[nx - 22:nx - 2, 0] = OUTLET
    elif outlet == "side":                          # 側壁低處抽氣口
        m[0, 2:16] = OUTLET
        m[-1, 2:16] = OUTLET
    elif outlet == "one":                           # 只有右邊一個抽氣口（不對稱）
        m[nx - 30:nx - 2, 0] = OUTLET
    return m

if __name__ == "__main__":
    m = build_mask()
    names = ["氣體", "牆", "進氣", "抽氣", "晶圓"]
    for code, name in enumerate(names):
        print(f"{name}：{(m == code).sum()} 格")
    sym = ".#vOW"
    xs = np.linspace(0, m.shape[0] - 1, 40).astype(int)     # 縮小成 40×20 的文字圖
    for y in np.linspace(m.shape[1] - 1, 0, 20).astype(int):
        print("".join(sym[c] for c in m[xs, y]))
