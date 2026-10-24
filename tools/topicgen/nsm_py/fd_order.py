# 第 11 課：前向差分 O(h)、中央差分 O(h²)——用誤差的斜率量出收斂階數
import numpy as np

f, df, x0 = np.exp, np.exp, 0.5
print("     h      前向誤差     中央誤差")
prev = None
for k in range(1, 7):
    h = 2.0 ** (-k)
    ef = abs((f(x0 + h) - f(x0)) / h - df(x0))
    ec = abs((f(x0 + h) - f(x0 - h)) / (2 * h) - df(x0))
    s = "" if prev is None else f"   階數 {np.log2(prev[0] / ef):.2f} / {np.log2(prev[1] / ec):.2f}"
    print(f"{h:8.5f}  {ef:.3e}  {ec:.3e}{s}")
    prev = (ef, ec)
