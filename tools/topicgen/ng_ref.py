# -*- coding: utf-8 -*-
"""親手訓練一個小 LLM：參考頁——互動工具箱、範例下載與指令速查。"""
from ng_common import LS, NGLIB, ngw, PUBLISH

GUIDE = {
    "file": "guide.html", "title": u"小 LLM 互動工具箱", "h1": u"小 LLM 互動工具箱", "icon": u"🧮",
    "description": u"BPE 合併、Bigram 機率表、因果遮罩、參數計算、真實訓練曲線、真實模型的抽樣",
    "body": [
        ("raw", u"<script>%s</script>" % NGLIB),
        ("h", u"1. BPE 合併步驟（第 7 課）"), ngw({"t": "bpe"}),
        ("h", u"2. Bigram 機率表（第 11 課）"), ngw({"t": "bigram"}),
        ("h", u"3. 因果遮罩（第 17 課）"), ngw({"t": "mask"}),
        ("h", u"4. 參數與記憶體計算器（第 23 課）"), ngw({"t": "params"}),
        ("h", u"5. 實際的訓練曲線（第 27、37 課）"), ngw({"t": "loss", "modern": 1}),
        ("h", u"6. 真實模型的抽樣（第 32 課）"), ngw({"t": "sample"}),
    ],
}

_DESC = {"prepare_data": (u"下載並整理《全唐詩》", 2), "tokenizer": (u"字元級與 BPE tokenizer", 10), "gpt": (u"完整的 GPT 模型", 24), "train": (u"訓練程式", 30),
         "sample": (u"寫詩", 34), "chat": (u"互動寫詩", 34), "lora": (u"從零實作 LoRA 微調", 40), "hf_qwen_lora": (u"用 peft 微調開源模型（延伸）", 40),
         "s01_tensor": (u"tensor 與 autograd", 3), "s02_module": (u"nn.Module 與訓練迴圈", 4), "s03_data": (u"語料統計", 5), "s04_char_tok": (u"字元級 tokenizer", 6),
         "s05_bpe": (u"BPE 實驗", 8), "s06_bigram": (u"Bigram 模型", 11), "s07_attention": (u"單頭自注意力", 16), "s08_params": (u"數參數", 23),
         "s09_experiments": (u"對照實驗", 31), "s10_sampling": (u"抽樣參數", 32), "s11_kvcache": (u"KV cache 測速", 33), "s12_modern": (u"兩種架構比較", 37),
         "s13_instruct_data": (u"產生指令資料", 39), "s14_eval": (u"評估微調", 41)}

FILES = {
    "file": "files.html", "title": u"範例下載與指令速查", "h1": u"範例下載與指令速查", "icon": u"📦",
    "description": u"所有 Python 範例、建議執行順序與常用指令",
    "body": [
        ("p", u"<a href=\"py/build-tiny-llm-examples.zip\" download>⬇️ 下載全部範例（zip）</a>。需要 Python 3.9 以上與 PyTorch。"),
        ("h", u"建議執行順序"),
        ("code", u"python prepare_data.py          # 下載語料（約 30 MB），產生 data/tang.txt\npython train.py                 # 訓練（4 核心 CPU 約 20 分鐘，GPU 幾分鐘）\npython sample.py --prompt 春     # 寫詩\npython chat.py                  # 互動\npython train.py --modern --out ckpt_modern.pt   # Llama 風格\npython s13_instruct_data.py     # 產生指令資料\npython lora.py                  # LoRA 微調\npython s14_eval.py              # 評估"),
        ("h", u"檔案一覽"),
        ("t", [u"檔案", u"內容", u"課"], [[u'<a href="py/%s.py" download>%s.py</a>' % (n, n), _DESC[n][0], LS(_DESC[n][1])] for n in PUBLISH]),
        ("h", u"train.py 常用參數"),
        ("t", [u"參數", u"預設", u"說明"], [[u"--steps", u"2000", u"訓練步數"], [u"--batch／--accum", u"32／1", u"批次大小與梯度累積"], [u"--block", u"80", u"上下文長度"],
                                      [u"--n_layer／--n_head／--n_embd", u"4／4／192", u"模型大小"], [u"--lr／--warmup", u"1e-3／100", u"學習率與 warmup 步數"],
                                      [u"--modern", u"關", u"Llama 風格"], [u"--resume", u"關", u"從存檔繼續"], [u"--amp", u"關", u"混合精度（GPU）"]]),
    ],
}

REFERENCES = [GUIDE, FILES]
