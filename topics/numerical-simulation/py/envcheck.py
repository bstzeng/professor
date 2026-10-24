# 第 5 課：確認環境——印出版本並做一次簡單的向量運算
import sys
import numpy as np
import scipy
import matplotlib

print("Python", sys.version.split()[0])
print("NumPy", np.__version__, "SciPy", scipy.__version__, "Matplotlib", matplotlib.__version__)
a = np.arange(5)
print("a =", a, " a**2 =", a**2, " sum =", a.sum())
