# 第 2 課：最小的模擬流程——放射性衰變 dN/dt = -λN，用尤拉法與解析解比較
import numpy as np

lam, N0, T = 0.5, 1000.0, 10.0          # 衰變常數、初始數量、總時間
for dt in [1.0, 0.5, 0.1, 0.01]:
    n = int(round(T / dt))
    N = N0
    for _ in range(n):                    # 尤拉法：N(t+dt) = N(t) + dt * f(N)
        N = N + dt * (-lam * N)
    exact = N0 * np.exp(-lam * T)
    print(f"dt={dt:5.2f}  數值={N:10.4f}  解析={exact:10.4f}  相對誤差={abs(N-exact)/exact:.2e}")
