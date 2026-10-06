# -*- coding: utf-8 -*-
"""第 3 課：PyTorch 速成——tensor 與自動微分。"""
import torch

a = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
b = torch.tensor([[5.0, 6.0], [7.0, 8.0]])
print("a 的形狀：", tuple(a.shape))
print("矩陣乘法 a @ b：\n", a @ b)
print("逐元素相乘 a * b：\n", a * b)

x = torch.randn(32, 80, 192)          # 一批 32 段文字、每段 80 個 token、每個 token 192 維
print("一批 token 向量的形狀：", tuple(x.shape))
print("取第 0 段的最後一個 token：", tuple(x[0, -1].shape))

# 自動微分：y = w·x + b 的梯度
w = torch.tensor(2.0, requires_grad=True)
bias = torch.tensor(1.0, requires_grad=True)
y = w * 3.0 + bias                    # x = 3
loss = (y - 10.0) ** 2                # 希望 y = 10
loss.backward()                       # 反向傳播
print("y =", y.item(), " loss =", loss.item())
print("∂loss/∂w =", w.grad.item(), "（＝ 2(y−10)·x ＝ 2×(−3)×3）")
print("∂loss/∂b =", bias.grad.item())
