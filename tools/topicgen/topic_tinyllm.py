# -*- coding: utf-8 -*-
"""親手訓練一個小 LLM 主題的規格。產生頁面時會把 Python 範例複製到 topics/build-tiny-llm/py/ 並打包成 zip。"""
import io
import os
import shutil
import zipfile
import ng_a, ng_e, ng_ref
from ng_common import PYDIR, PUBLISH

TOPIC = {
    "id": "build-tiny-llm",
    "category": "ai",
    "title": u"親手訓練一個小 LLM：從零寫出你的 GPT",
    "short": u"親手訓練小 LLM",
    "crumb": u"親手訓練小 LLM",
    "icon": u"🛠️",
    "description": u"用 Python 和 PyTorch 從零寫一個約 300 萬參數的 GPT，拿 3.6 萬首唐詩在一般電腦的 CPU 上訓練，讓它學會寫五言、七言詩。"
                   u"字元級與 BPE tokenizer、bigram 模型、一行一行寫出注意力、因果遮罩、多頭、FFN、殘差與 LayerNorm；AdamW、warmup 與 cosine、"
                   u"驗證與過擬合、混合精度、梯度累積、存檔續訓與對照實驗；temperature／top-k／top-p 與 KV cache；RoPE、RMSNorm、SwiGLU；"
                   u"指令資料與從零實作 LoRA 微調、評估。每支程式都實際執行過並附上輸出，可整包下載。",
}

MODULES = ng_a.MODULES + ng_e.MODULES

REFERENCES = ng_ref.REFERENCES


def _publish():
    out = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "topics", TOPIC["id"], "py")
    if os.path.isdir(out):
        shutil.rmtree(out)
    os.makedirs(out)
    for n in PUBLISH:
        shutil.copyfile(os.path.join(PYDIR, n + ".py"), os.path.join(out, n + ".py"))
    readme = (u"親手訓練一個小 LLM：Python 範例\n\n"
              u"需要 Python 3.9 以上與 PyTorch（pip install torch）。\n\n"
              u"1. python prepare_data.py   下載《全唐詩》（chinese-poetry 專案，MIT 授權），產生 data/tang.txt\n"
              u"2. python train.py          訓練，產生 ckpt.pt 與 tokenizer.json\n"
              u"3. python sample.py --prompt 春\n"
              u"4. python chat.py\n"
              u"5. python s13_instruct_data.py && python lora.py && python s14_eval.py   LoRA 指令微調與評估\n\n"
              u"hf_qwen_lora.py 另外需要 pip install transformers peft，並可連線 Hugging Face。\n")
    with zipfile.ZipFile(os.path.join(out, "build-tiny-llm-examples.zip"), "w", zipfile.ZIP_DEFLATED) as z:
        def add(name, data):
            info = zipfile.ZipInfo("build-tiny-llm/" + name, date_time=(2026, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            z.writestr(info, data)
        add("README.txt", readme.encode("utf-8"))
        for n in PUBLISH:
            add(n + ".py", io.open(os.path.join(PYDIR, n + ".py"), "rb").read())


_publish()
