# 第 36 課：互動水池——滑鼠點一下就滴一滴水（matplotlib 動畫）
#   在沒有螢幕的環境（例如伺服器）會自動改成：自動滴 3 滴、跑 300 步、存成 pool_live.png
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

N, c, damp = 200, 1.0, 0.002              # 格點、波速（格/步）、每步的阻尼
C2 = 0.25                                  # (c dt/dx)²，二維要 ≤ 0.5
eta = np.zeros((N, N)); prev = np.zeros((N, N))
I, J = np.meshgrid(np.arange(N), np.arange(N), indexing="ij")

def drop(i, j, a=1.0, w=3.0):
    global eta, prev
    bump = -a * np.exp(-((I - i) ** 2 + (J - j) ** 2) / w**2)
    eta += bump
    prev += bump                           # 兩個時間層一起加：初速為 0

def step():
    global eta, prev
    g = np.pad(eta, 1, mode="edge")        # 反射池壁
    lap = g[2:, 1:-1] + g[:-2, 1:-1] + g[1:-1, 2:] + g[1:-1, :-2] - 4 * eta
    nxt = (2 - damp) * eta - (1 - damp) * prev + C2 * lap
    prev, eta = eta, nxt

headless = matplotlib.get_backend().lower() in ("agg", "pdf", "svg", "ps", "cairo", "template")
fig, ax = plt.subplots(figsize=(5, 5))
im = ax.imshow(eta.T, origin="lower", cmap="Blues_r", vmin=-0.15, vmax=0.15)
ax.set_title("click to drop")            # 預設字型沒有中文，標題用英文
ax.set_xticks([]); ax.set_yticks([])

if headless:
    for n in range(300):
        if n in (0, 60, 120):
            drop(*[(60, 70), (140, 120), (90, 150)][n // 60])
        step()
    im.set_data(eta.T)
    fig.savefig("pool_live.png", dpi=80)
    print("沒有螢幕：已存成 pool_live.png，最大起伏", round(float(np.abs(eta).max()), 4))
else:
    def on_click(ev):
        if ev.inaxes is ax:
            drop(ev.xdata, ev.ydata)
    fig.canvas.mpl_connect("button_press_event", on_click)
    def update(_):
        for _ in range(3):                 # 每一幀多跑幾步，畫面比較順
            step()
        im.set_data(eta.T)
        return [im]
    anim = FuncAnimation(fig, update, interval=30, blit=True, cache_frame_data=False)
    plt.show()
