# 第 31 課：比較幾種腔體設計的晶圓均勻度（流場 LBM + 濃度對流擴散）
import numpy as np
from chamber_mask import build_mask
from chamber_lbm import solve_flow
from chamber_species import solve_species, wafer_profile, nonuniformity

designs = {
    "A 基準：寬噴淋頭＋底部雙抽氣": dict(outlet="bottom", shower=(22, 98)),
    "B 窄噴淋頭（只蓋晶圓中央）":   dict(outlet="bottom", shower=(44, 76)),
    "C 側壁雙抽氣":                 dict(outlet="side", shower=(22, 98)),
    "D 只有右邊一個抽氣口":         dict(outlet="one", shower=(22, 98)),
}
Pe, Da = 3.0, 2.0
for name, kw in designs.items():
    m = build_mask(**kw)
    ux, uy, rho, steps = solve_flow(m, verbose=False)
    c = solve_species(m, ux, uy, 0.02, Pe, Da)
    x, r = wafer_profile(m, c)
    left, right = r[: len(r) // 2].mean(), r[len(r) // 2:].mean()
    print(f"{name:18s} 平均 {r.mean():.3f}，不均勻度 ±{nonuniformity(r):4.1f}%，"
          f"左右差 {abs(left - right) / r.mean() * 100:4.1f}%（{steps} 步）")
