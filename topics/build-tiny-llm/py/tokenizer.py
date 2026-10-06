# -*- coding: utf-8 -*-
"""兩種 tokenizer：字元級（CharTokenizer）與從零實作的 BPE（BPETokenizer）。"""
import json
from collections import Counter

SPECIAL = ["\n", "〔", "〕", " "]        # 換行＝一首詩結束；〔〕與空白給第 39 課的指令格式用


class CharTokenizer:
    """每個字一個 token。"""

    def __init__(self, chars):
        self.itos = list(chars)
        self.stoi = {c: i for i, c in enumerate(self.itos)}

    @classmethod
    def train(cls, text):
        chars = sorted(set(text) | set(SPECIAL))
        return cls(chars)

    def encode(self, s):
        return [self.stoi[c] for c in s]

    def decode(self, ids):
        return "".join(self.itos[i] for i in ids)

    @property
    def vocab_size(self):
        return len(self.itos)

    def save(self, path):
        with open(path, "w", encoding="utf-8") as f:
            json.dump({"type": "char", "itos": self.itos}, f, ensure_ascii=False)

    @classmethod
    def load(cls, path):
        with open(path, encoding="utf-8") as f:
            return cls(json.load(f)["itos"])


def show(b):
    """把一段位元組顯示出來：是完整的 UTF-8 字就顯示字，否則顯示十六進位。"""
    try:
        return b.decode("utf-8").replace("\n", "⏎")
    except UnicodeDecodeError:
        return "‹" + b.hex(" ") + "›"


class BPETokenizer:
    """位元組層級的 BPE：從 256 個位元組開始，反覆合併最常一起出現的一對。"""

    def __init__(self, merges=None):
        self.merges = merges or []                 # [(a, b), ...]，依合併順序
        self.vocab = {i: bytes([i]) for i in range(256)}
        for k, (a, b) in enumerate(self.merges):
            self.vocab[256 + k] = self.vocab[a] + self.vocab[b]

    @staticmethod
    def _pairs(ids):
        return Counter(zip(ids, ids[1:]))

    @staticmethod
    def _merge(ids, pair, new):
        out, i = [], 0
        while i < len(ids):
            if i < len(ids) - 1 and (ids[i], ids[i + 1]) == pair:
                out.append(new)
                i += 2
            else:
                out.append(ids[i])
                i += 1
        return out

    @classmethod
    def train(cls, text, n_merges, verbose=0):
        ids = list(text.encode("utf-8"))
        tok = cls()
        for k in range(n_merges):
            stats = cls._pairs(ids)
            if not stats:
                break
            pair, cnt = stats.most_common(1)[0]
            new = 256 + k
            ids = cls._merge(ids, pair, new)
            tok.merges.append(pair)
            tok.vocab[new] = tok.vocab[pair[0]] + tok.vocab[pair[1]]
            if verbose and (k < verbose or k == n_merges - 1):
                print("合併 #%d：%s ＋ %s → %s（出現 %d 次）" % (k + 1, show(tok.vocab[pair[0]]), show(tok.vocab[pair[1]]),
                                                             show(tok.vocab[new]), cnt))
        return tok

    def encode(self, s):
        ids = list(s.encode("utf-8"))
        rank = {p: k for k, p in enumerate(self.merges)}
        while len(ids) > 1:
            pair = min(self._pairs(ids), key=lambda p: rank.get(p, 1e18))
            if pair not in rank:
                break
            ids = self._merge(ids, pair, 256 + rank[pair])
        return ids

    def decode(self, ids):
        return b"".join(self.vocab[i] for i in ids).decode("utf-8", errors="replace")

    @property
    def vocab_size(self):
        return 256 + len(self.merges)
