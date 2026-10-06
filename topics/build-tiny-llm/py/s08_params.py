# -*- coding: utf-8 -*-
"""第 23 課：數一數模型有多少參數。"""
from gpt import GPT, GPTConfig
from tokenizer import CharTokenizer

tok = CharTokenizer.load("tokenizer.json")
cfg = GPTConfig(vocab_size=tok.vocab_size, block_size=80)
m = GPT(cfg)
parts = {}
for name, p in m.named_parameters():
    key = "embedding（字）" if name.startswith("tok_emb") else "embedding（位置）" if name.startswith("pos_emb") else \
          "注意力" if ".attn." in name else "MLP" if ".mlp." in name else "LayerNorm"
    parts[key] = parts.get(key, 0) + p.numel()
for k, v in parts.items():
    print("%-16s %9d" % (k, v))
print("%-16s %9d  （輸出層和字 embedding 共用權重，所以不另外計算）" % ("合計", m.num_params()))
d, L, V = cfg.n_embd, cfg.n_layer, cfg.vocab_size
est = V * d + cfg.block_size * d + L * (12 * d * d + 13 * d) + 2 * d
print("公式 V·d ＋ T·d ＋ L·(12d² ＋ 13d) ＋ 2d ＝", est)
