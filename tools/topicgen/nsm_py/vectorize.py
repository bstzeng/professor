# 第 6 課：迴圈 vs 向量化——同一個差分運算，速度差一個數量級以上
import time
import numpy as np

n = 1_000_000
x = np.linspace(0, 2 * np.pi, n)
y = np.sin(x)
dx = x[1] - x[0]

t0 = time.perf_counter()
d1 = np.empty(n - 2)
for i in range(1, n - 1):                 # 純 Python 迴圈
    d1[i - 1] = (y[i + 1] - y[i - 1]) / (2 * dx)
t1 = time.perf_counter()
d2 = (y[2:] - y[:-2]) / (2 * dx)          # 向量化：一次對整個陣列運算
t2 = time.perf_counter()

print(f"迴圈 {t1 - t0:.3f} s，向量化 {t2 - t1:.4f} s，快 {(t1 - t0) / (t2 - t1):.0f} 倍")
print("兩者最大差異：", np.max(np.abs(d1 - d2)))
print("與 cos(x) 的最大誤差：", np.max(np.abs(d2 - np.cos(x[1:-1]))))
