# -*- coding: utf-8 -*-
"""第 38～40 課（延伸）：用 Hugging Face 的 transformers ＋ peft 對開源小模型做 LoRA 微調。

需要：pip install transformers peft accelerate
第一次執行會從 Hugging Face 下載約 1 GB 的模型。建議有 GPU；CPU 也能跑，但很慢。
本課程頁面沒有附上這支程式的執行結果。
"""
import torch
from peft import LoraConfig, get_peft_model
from transformers import AutoModelForCausalLM, AutoTokenizer

NAME = "Qwen/Qwen2.5-0.5B-Instruct"
tok = AutoTokenizer.from_pretrained(NAME)
model = AutoModelForCausalLM.from_pretrained(NAME, torch_dtype=torch.bfloat16)

# 1. 指令資料：用模型自己的 chat template 排成對話格式
pairs = [("寫一首關於春天的七言絕句", "春風吹綠江南岸，……"),        # ← 換成你自己的資料
         ("用一句話介紹台北", "台北是台灣的首都，……")]
def encode(q, a):
    msgs = [{"role": "user", "content": q}, {"role": "assistant", "content": a}]
    ids = tok.apply_chat_template(msgs, tokenize=True)
    n_prompt = len(tok.apply_chat_template(msgs[:1], tokenize=True, add_generation_prompt=True))
    labels = [-100] * n_prompt + ids[n_prompt:]          # 只對回答的部分算損失
    return torch.tensor([ids]), torch.tensor([labels])

# 2. 掛上 LoRA：只訓練注意力層的小矩陣
cfg = LoraConfig(r=8, lora_alpha=16, lora_dropout=0.05, task_type="CAUSAL_LM",
                 target_modules=["q_proj", "k_proj", "v_proj", "o_proj"])
model = get_peft_model(model, cfg)
model.print_trainable_parameters()

# 3. 和我們自己的訓練迴圈一模一樣
opt = torch.optim.AdamW([p for p in model.parameters() if p.requires_grad], lr=2e-4)
model.train()
for epoch in range(3):
    for q, a in pairs:
        x, y = encode(q, a)
        loss = model(input_ids=x, labels=y).loss
        opt.zero_grad()
        loss.backward()
        opt.step()
    print("epoch", epoch, "loss", loss.item())

model.save_pretrained("qwen-lora")                      # 只存 LoRA 權重，通常只有幾 MB
