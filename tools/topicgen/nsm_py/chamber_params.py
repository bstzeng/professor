# 第 24 課：先把蝕刻腔的數字算清楚——停留時間、速度、Re、Pe、Kn
import numpy as np

kB, R = 1.380649e-23, 8.314
T = 330.0                      # 氣體溫度 K
p_mTorr = 20.0
p = p_mTorr * 0.13332          # Pa
Q_sccm = 200.0                 # 進氣流量
r_ch, H = 0.25, 0.10           # 腔體半徑、高度（m）
r_sh = 0.16                    # 噴淋頭半徑
M, mu, d = 0.040, 2.4e-5, 3.6e-10   # 氬氣：分子量、黏度、分子直徑

# 1 sccm = 每分鐘 1 cm³ 的標準狀態（0°C, 1 atm）氣體
Q_pV = Q_sccm * 1e-6 / 60 * 101325 * (T / 273.15)   # Pa·m³/s，換到腔內溫度
Q_vol = Q_pV / p                                     # 腔內的體積流率 m³/s
V = np.pi * r_ch**2 * H
tau_res = V / Q_vol
U = Q_vol / (np.pi * r_sh**2)                        # 噴淋頭出口的平均速度
rho = p * M / (R * T)
nu = mu / rho
D = 1.0 / (p / 101325) * 2.0e-5                      # 擴散係數約與壓力成反比
lam = kB * T / (np.sqrt(2) * np.pi * d**2 * p)

print(f"壓力 {p:.2f} Pa，體積流率 {Q_vol:.3f} m³/s，停留時間 {tau_res * 1e3:.0f} ms")
print(f"噴淋頭出口速度 U = {U:.2f} m/s")
print(f"Re = U H / ν = {U * H / nu:.2f}   （ν = {nu:.2f} m²/s）")
print(f"Pe = U H / D = {U * H / D:.2f}   （D = {D:.2f} m²/s）")
print(f"平均自由徑 λ = {lam * 1e3:.2f} mm，Kn = λ/H = {lam / H:.3f}")
