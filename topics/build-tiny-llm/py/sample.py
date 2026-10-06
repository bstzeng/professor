# -*- coding: utf-8 -*-
"""用訓練好的模型寫詩。

  python sample.py --prompt 春 --n 3
  python sample.py --prompt 床前明月光， --temperature 0.8 --top_p 0.9
"""
import argparse
import torch
from gpt import GPT, GPTConfig
from tokenizer import CharTokenizer


def load(path="ckpt.pt", device="cpu"):
    ck = torch.load(path, map_location=device)
    model = GPT(GPTConfig(**ck["cfg"])).to(device)
    model.load_state_dict(ck["model"])
    model.eval()
    return model


def write(model, tok, prompt, temperature=0.8, top_k=None, top_p=0.9, max_new=80):
    """前面加一個換行：在訓練資料裡，換行後面就是「一首詩的開頭」。"""
    idx = torch.tensor([tok.encode("\n" + prompt)])
    out = model.generate(idx, max_new, temperature=temperature, top_k=top_k, top_p=top_p, stop=tok.stoi["\n"])
    return tok.decode(out[0, 1:].tolist()).strip()


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--ckpt", default="ckpt.pt")
    ap.add_argument("--prompt", default="春")
    ap.add_argument("--n", type=int, default=3)
    ap.add_argument("--temperature", type=float, default=0.8)
    ap.add_argument("--top_k", type=int, default=None)
    ap.add_argument("--top_p", type=float, default=0.9)
    ap.add_argument("--seed", type=int, default=0)
    a = ap.parse_args()
    torch.manual_seed(a.seed)
    tok, model = CharTokenizer.load("tokenizer.json"), load(a.ckpt)
    for _ in range(a.n):
        print(write(model, tok, a.prompt, a.temperature, a.top_k, a.top_p))
