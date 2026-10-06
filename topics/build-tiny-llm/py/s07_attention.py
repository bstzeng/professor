# -*- coding: utf-8 -*-
"""第 16～18 課：單頭自注意力，一步一步算。"""
import torch
import torch.nn.functional as F

torch.manual_seed(0)
B, T, C, hd = 1, 4, 8, 4                        # 1 段文字、4 個 token、每個 8 維；注意力頭 4 維
x = torch.randn(B, T, C)
Wq, Wk, Wv = (torch.randn(C, hd) * 0.4 for _ in range(3))
q, k, v = x @ Wq, x @ Wk, x @ Wv               # (1, 4, 4)

scores = q @ k.transpose(-2, -1) / hd ** 0.5    # (1, 4, 4)：每個 token 對每個 token 的分數
print("分數（未遮罩）：\n", scores[0].round(decimals=2))

mask = torch.tril(torch.ones(T, T)).bool()
scores = scores.masked_fill(~mask, float("-inf"))
print("\n因果遮罩後：\n", scores[0].round(decimals=2))

w = F.softmax(scores, dim=-1)
print("\nsoftmax 權重（每一列加起來 ＝ 1）：\n", w[0].round(decimals=2))
out = w @ v
print("\n輸出形狀：", tuple(out.shape), "  第 1 個 token 的輸出 ＝ 它自己的 v：", torch.allclose(out[0, 0], v[0, 0]))

# 多頭：把 C 維切成 H 個頭，各自做注意力
H = 2
qh = q.repeat(1, 1, H).view(B, T, H, hd).transpose(1, 2)        # (B, H, T, hd)
print("\n多頭的形狀 (B, H, T, hd)：", tuple(qh.shape))
