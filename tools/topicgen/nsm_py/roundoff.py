# 第 3 課：截斷誤差與捨入誤差——前向差分的誤差先降後升
import numpy as np

x = 1.0
exact = np.cos(x)                          # d/dx sin(x)
for k in range(1, 16, 2):
    h = 10.0 ** (-k)
    approx = (np.sin(x + h) - np.sin(x)) / h
    print(f"h=1e-{k:02d}  誤差={abs(approx - exact):.3e}")
# 最小誤差出現在 h ≈ sqrt(機器精度) ≈ 1e-8 附近
print("機器精度 eps =", np.finfo(float).eps)
