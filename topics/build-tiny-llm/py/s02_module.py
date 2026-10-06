# -*- coding: utf-8 -*-
"""第 4 課：nn.Module 與訓練迴圈——用梯度下降找出 y = 2x + 1。"""
import torch
import torch.nn as nn

torch.manual_seed(0)
x = torch.linspace(-3, 3, 100).unsqueeze(1)          # 100 個點，形狀 (100, 1)
y = 2 * x + 1 + 0.3 * torch.randn_like(x)            # 加一點雜訊


class Line(nn.Module):
    def __init__(self):
        super().__init__()
        self.lin = nn.Linear(1, 1)                   # 裡面有 weight 和 bias 兩個參數

    def forward(self, x):
        return self.lin(x)


model = Line()
opt = torch.optim.SGD(model.parameters(), lr=0.1)
for step in range(101):
    pred = model(x)                                  # 1. 前向
    loss = ((pred - y) ** 2).mean()                  # 2. 算損失（MSE）
    opt.zero_grad()                                  # 3. 清掉舊梯度
    loss.backward()                                  # 4. 反向傳播
    opt.step()                                       # 5. 更新參數
    if step % 20 == 0:
        print("step %3d  loss %.4f  w=%.3f  b=%.3f" % (step, loss.item(), model.lin.weight.item(), model.lin.bias.item()))
