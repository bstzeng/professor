# 第 30 課：Knudsen 數——連續體假設在哪裡失效
import numpy as np

kB, T, d = 1.380649e-23, 330.0, 3.6e-10       # 氬氣分子直徑約 0.36 nm

def mfp(p_pa):
    return kB * T / (np.sqrt(2) * np.pi * d**2 * p_pa)

def regime(Kn):
    if Kn < 0.01:  return "連續體（NS 方程式）"
    if Kn < 0.1:   return "滑移流（NS + 滑移邊界）"
    if Kn < 10:    return "過渡區（DSMC / Boltzmann）"
    return "自由分子流（DSMC / 視角因子）"

scales = [("腔體高度 10 cm", 0.10), ("晶圓上方 1 cm", 0.01), ("噴淋頭孔 0.5 mm", 5e-4), ("溝槽寬 50 nm", 50e-9)]
for p_mTorr in [1, 10, 100, 1000]:
    lam = mfp(p_mTorr * 0.13332)
    print(f"\n{p_mTorr:5d} mTorr：平均自由徑 λ = {lam * 1e3:.3g} mm")
    for name, L in scales:
        Kn = lam / L
        print(f"   {name:14s} Kn = {Kn:9.3g}  {regime(Kn)}")
