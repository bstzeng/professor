# 第 32 課：水波的色散關係 ω² = (g k + σ k³/ρ) tanh(k h)
import numpy as np
from scipy.optimize import minimize_scalar

g, sigma, rho, h = 9.81, 0.072, 1000.0, 2.0     # 重力、表面張力、密度、池深

def omega(k):
    return np.sqrt((g * k + sigma * k**3 / rho) * np.tanh(k * h))

def group_speed(k, dk=1e-6):
    return (omega(k * (1 + dk)) - omega(k * (1 - dk))) / (2 * k * dk)

print("   波長       相速 c=ω/k   群速 cg=dω/dk   cg/c")
for lam in [0.005, 0.017, 0.05, 0.2, 1.0, 5.0, 20.0, 100.0]:
    k = 2 * np.pi / lam
    c, cg = omega(k) / k, group_speed(k)
    print(f"{lam:8.3f} m   {c:8.3f} m/s   {cg:8.3f} m/s     {cg / c:.2f}")

res = minimize_scalar(lambda k: omega(k) / k, bounds=(10, 2000), method="bounded")
print(f"\n最慢的波：波長 {2 * np.pi / res.x * 100:.2f} cm，相速 {res.fun:.3f} m/s")
print(f"淺水極限 sqrt(g h) = {np.sqrt(g * h):.2f} m/s")
