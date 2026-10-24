# 第 20 課：投影法的核心——用 FFT 把任意速度場的散度去掉
import numpy as np

N = 64
L = 2 * np.pi
x = np.linspace(0, L, N, endpoint=False)
X, Y = np.meshgrid(x, x, indexing="ij")

# 一個「有散度」的速度場：旋轉部分 + 梯度部分
u = np.sin(Y) + np.cos(X) * 0.7
v = np.sin(X) + np.cos(Y) * 0.7

k = np.fft.fftfreq(N, d=L / N) * 2 * np.pi
KX, KY = np.meshgrid(k, k, indexing="ij")
K2 = KX**2 + KY**2
K2[0, 0] = 1.0                               # 避免除以 0（平均值不影響）

def div(u, v):
    return np.real(np.fft.ifft2(1j * KX * np.fft.fft2(u) + 1j * KY * np.fft.fft2(v)))

uh, vh = np.fft.fft2(u), np.fft.fft2(v)
phi_h = (1j * KX * uh + 1j * KY * vh) / (-K2)   # ∇²φ = ∇·u
u2 = np.real(np.fft.ifft2(uh - 1j * KX * phi_h))  # u - ∇φ
v2 = np.real(np.fft.ifft2(vh - 1j * KY * phi_h))

print("投影前 最大散度", np.abs(div(u, v)).max())
print("投影後 最大散度", np.abs(div(u2, v2)).max())
print("留下來的應該是旋轉部分 sin(y), sin(x)：誤差",
      max(np.abs(u2 - np.sin(Y)).max(), np.abs(v2 - np.sin(X)).max()))
