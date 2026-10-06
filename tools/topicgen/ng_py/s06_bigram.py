# -*- coding: utf-8 -*-
"""第 11～13 課：Bigram 模型——只看前一個字猜下一個字。

最直接的做法是「數次數」：統計每個字後面接什麼字，再換算成機率。
（用 nn.Embedding(V, V) 加梯度下降訓練，最後學到的也是同一張表，只是慢很多。）
"""
import math
import torch
from tokenizer import CharTokenizer

torch.manual_seed(42)
text = open("data/tang.txt", encoding="utf-8").read()
tok = CharTokenizer.load("tokenizer.json")
data = torch.tensor(tok.encode(text))
n = int(len(data) * 0.95)
train, val = data[:n], data[n:]
V = tok.vocab_size

# 1. 數次數：counts[a, b] ＝「a 後面接 b」出現幾次
counts = torch.zeros(V, V)
counts.index_put_((train[:-1], train[1:]), torch.ones(len(train) - 1), accumulate=True)
print("詞彙量 %d，表格大小 %d × %d ＝ %d 格，其中 %.2f%% 出現過" % (V, V, V, V * V, 100 * (counts > 0).float().mean()))

# 2. 換成機率（每格加 0.03 做平滑，避免沒看過的組合機率為 0，否則驗證集的損失會變成無限大）
probs = (counts + 0.03) / (counts + 0.03).sum(1, keepdim=True)

# 3. 損失與困惑度
def nll(d):
    return -torch.log(probs[d[:-1], d[1:]]).mean().item()

print("完全亂猜：損失 ln(%d) ＝ %.2f，困惑度 %d" % (V, math.log(V), V))
for name, d in [("訓練集", train), ("驗證集", val)]:
    L = nll(d)
    print("%s：損失 %.3f，困惑度 %.0f" % (name, L, math.exp(L)))

# 4. 看看「月」後面最常接什麼
row = probs[tok.stoi["月"]]
top = torch.topk(row, 8)
print("「月」的下一個字：", "  ".join("%s %.1f%%" % (tok.itos[i], v * 100) for v, i in zip(top.values.tolist(), top.indices.tolist())))

# 5. 抽樣生成（只從真的出現過的組合裡抽，否則常會抽到冷僻字）
raw = counts / counts.sum(1, keepdim=True).clamp(min=1)


def sample(start, n=60):
    idx = tok.stoi[start]
    out = start
    for _ in range(n):
        idx = torch.multinomial(raw[idx], 1).item()
        if tok.itos[idx] == "\n":
            break
        out += tok.itos[idx]
    return out

print("\n生成：")
for s in "春月山":
    print(" ", sample(s))
