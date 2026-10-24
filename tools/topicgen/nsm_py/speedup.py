# 第 9 課：加速——有 Numba 就用 JIT，沒有就退回 NumPy
import time
import numpy as np

def step_python(u, r):
    un = u.copy()
    for i in range(1, len(u) - 1):
        un[i] = u[i] + r * (u[i + 1] - 2 * u[i] + u[i - 1])
    return un

def step_numpy(u, r):
    un = u.copy()
    un[1:-1] = u[1:-1] + r * (u[2:] - 2 * u[1:-1] + u[:-2])
    return un

try:
    from numba import njit
    step_numba = njit(step_python)
    step_numba(np.zeros(10), 0.1)          # 第一次呼叫會編譯
except ImportError:
    step_numba = None

u = np.random.default_rng(0).random(200_000)
for name, f in [("Python 迴圈", step_python), ("NumPy 向量化", step_numpy), ("Numba", step_numba)]:
    if f is None:
        print(f"{name:10s}：未安裝（pip install numba）")
        continue
    t0 = time.perf_counter(); f(u, 0.2); t1 = time.perf_counter()
    print(f"{name:10s}：{(t1 - t0) * 1000:8.2f} ms")
