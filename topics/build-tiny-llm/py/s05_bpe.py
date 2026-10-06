# -*- coding: utf-8 -*-
"""第 7、8 課：從零實作 BPE，看它在中文上學到什麼。"""
import time
from tokenizer import BPETokenizer, show

poems = open("data/tang.txt", encoding="utf-8").read().split("\n")[:1500]
sample = "\n".join(poems)
t = time.time()
tok = BPETokenizer.train(sample, 400, verbose=12)
print("訓練 400 次合併花了 %.0f 秒" % (time.time() - t))

s = "白日依山盡，黃河入海流。欲窮千里目，更上一層樓。"
ids = tok.encode(s)
print("\n「%s」" % s)
print("UTF-8 位元組數：", len(s.encode("utf-8")), "  字數：", len(s), "  BPE token 數：", len(ids))
print("切法：", " | ".join(show(tok.vocab[i]) for i in ids))

test = "\n".join(open("data/tang.txt", encoding="utf-8").read().split("\n")[30000:30200])
n_ids = len(tok.encode(test))
print("\n在沒看過的 200 首詩上：位元組 %d → BPE token %d（字數 %d）" % (len(test.encode("utf-8")), n_ids, len(test)))
