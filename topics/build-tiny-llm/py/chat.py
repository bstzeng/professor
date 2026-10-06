# -*- coding: utf-8 -*-
"""第 34 課：互動寫詩。輸入開頭的字或第一句，模型接著寫；輸入空白行結束。"""
import sys
import torch
from sample import load, write
from tokenizer import CharTokenizer

tok, model = CharTokenizer.load("tokenizer.json"), load()
torch.manual_seed(7)
print("🖌️ 唐詩小模型（輸入開頭，直接按 Enter 離開）")
while True:
    try:
        s = input("> ").strip()
    except EOFError:
        break
    if not sys.stdin.isatty():                           # 從檔案或管線輸入時，把輸入也印出來
        print(s)
    if not s:
        break
    s = "".join(c for c in s if c in tok.stoi)          # 詞彙表裡沒有的字就略過
    if not s:
        print("（這些字不在詞彙表裡）")
        continue
    print(write(model, tok, s))
