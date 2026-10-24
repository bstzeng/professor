# 第 7 課：Matplotlib 三種常用圖——線圖、等高線、向量場
import numpy as np
import matplotlib
matplotlib.use("Agg")                      # 沒有螢幕時也能存圖
import matplotlib.pyplot as plt

x = np.linspace(-2, 2, 41)
X, Y = np.meshgrid(x, x)
psi = np.exp(-(X**2 + Y**2))               # 一個高斯函數當作「流函數」
u, v = np.gradient(psi, x, axis=0), -np.gradient(psi, x, axis=1)

fig, ax = plt.subplots(1, 3, figsize=(12, 3.6))
ax[0].plot(x, np.exp(-x**2)); ax[0].set_title("line")
cs = ax[1].contourf(X, Y, psi, 20, cmap="viridis"); fig.colorbar(cs, ax=ax[1]); ax[1].set_title("contour")
ax[2].quiver(X[::3, ::3], Y[::3, ::3], u[::3, ::3], v[::3, ::3]); ax[2].set_title("quiver")
for a in ax[1:]:
    a.set_aspect("equal")
fig.tight_layout()
fig.savefig("plots.png", dpi=100)
print("已存成 plots.png")
