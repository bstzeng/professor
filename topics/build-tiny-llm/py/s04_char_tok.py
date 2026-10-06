# -*- coding: utf-8 -*-
"""第 6 課：字元級 tokenizer。"""
from tokenizer import CharTokenizer

text = open("data/tang.txt", encoding="utf-8").read()
tok = CharTokenizer.train(text)
print("詞彙量：", tok.vocab_size)
s = "床前明月光，疑是地上霜。"
ids = tok.encode(s)
print("編碼：", ids)
print("解碼：", tok.decode(ids))
print("換行符號的 id：", tok.encode("\n"))
print("詞彙表最前面 10 個：", repr("".join(tok.itos[:10])))
