# -*- coding: utf-8 -*-
"""一次 LLM 推論：參考頁——互動工具箱、名詞與數字速查。"""
from lf_common import LS, LFLIB, lfw

GUIDE = {
    "file": "guide.html", "title": u"LLM 推論互動工具箱", "h1": u"LLM 推論互動工具箱", "icon": u"🧮",
    "description": u"Tokenizer、注意力、KV Cache 計算器、roofline、速度估算、時間軸、抽樣、batching、推測解碼",
    "body": [
        ("raw", u"<script>%s</script>" % LFLIB),
        ("p", u"所有數字都是依公開規格做的理論估算，實際效能會因軟體、kernel 與工作負載而不同。"),
        ("h", u"1. TTFT／TPOT 時間軸（第 1 課）"), lfw({"t": "timeline"}),
        ("h", u"2. 簡化 tokenizer（第 5 課）"), lfw({"t": "tok"}),
        ("h", u"3. 因果注意力熱圖（第 10、11 課）"), lfw({"t": "attn"}),
        ("h", u"4. KV Cache 計算器（第 13 課）"), lfw({"t": "kv"}),
        ("h", u"5. Roofline 模型（第 23 課）"), lfw({"t": "roof", "ai": 1}),
        ("h", u"6. Prefill／Decode 速度估算（第 17、24 課）"), lfw({"t": "speed"}),
        ("h", u"7. 抽樣：溫度、top-k、top-p（第 25 課）"), lfw({"t": "sample"}),
        ("h", u"8. Batching 的吞吐量與延遲（第 27 課）"), lfw({"t": "batch"}),
        ("h", u"9. 推測解碼加速比（第 32 課）"), lfw({"t": "spec"}),
    ],
}

GLOSSARY = {
    "file": "glossary.html", "title": u"LLM 推論速查", "h1": u"LLM 推論速查", "icon": u"📖",
    "description": u"名詞、公式與硬體數字",
    "body": [
        ("h", u"1. 名詞"),
        ("t", [u"名詞", u"說明", u"課"],
         [[u"Token", u"tokenizer 切出的單位，對應詞彙表中的整數 ID", LS(5)], [u"Prefill", u"一次平行處理整段輸入、建立 KV Cache", LS(16)],
          [u"Decode", u"自回歸地一次生成一個 token", LS(21)], [u"TTFT", u"到第一個 token 的時間", LS(4)], [u"TPOT／ITL", u"每個輸出 token 之間的時間", LS(4)],
          [u"KV Cache", u"存放每層每個 token 的 Key、Value", LS(12)], [u"GQA", u"多個 Query 頭共用一組 KV", LS(14)], [u"MLA", u"把 KV 壓縮成潛在向量", LS(14)],
          [u"算術強度", u"運算次數 ÷ 讀寫位元組數", LS(18)], [u"Roofline", u"算力與頻寬限制的對數圖", LS(23)], [u"MFU", u"實際算力 ÷ 峰值算力", LS(17)],
          [u"FlashAttention", u"分塊計算注意力，不寫回 N×N 矩陣", LS(19)], [u"Chunked prefill", u"長輸入切段並和 decode 混合", LS(20)],
          [u"Continuous batching", u"每一步 decode 都可以加入或移除請求", LS(28)], [u"PagedAttention", u"以分頁區塊管理 KV Cache", LS(29)],
          [u"Prefix caching", u"重用相同前綴的 KV Cache", LS(30)], [u"量化", u"以較少位元存權重或 KV", LS(31)],
          [u"推測解碼", u"草稿模型猜、大模型一次驗證", LS(32)], [u"分離部署", u"prefill 與 decode 在不同機器", LS(33)], [u"MoE", u"每個 token 只啟用少數專家", LS(34)],
          [u"TP／PP／EP／DP", u"張量／管線／專家／資料平行", LS(37)], [u"Goodput", u"滿足 SLO 前提下的吞吐量", LS(40)]]),
        ("h", u"2. 公式"),
        ("t", [u"量", u"估算", u"課"],
         [[u"Prefill FLOPs", u"≈ 2 × 參數量 × 輸入 token 數（＋注意力項）", LS(17)],
          [u"每 token KV Cache", u"2 × 層數 × KV 頭數 × 頭維度 × 位元組數", LS(13)],
          [u"Decode 單請求上限", u"≈ 總頻寬 ÷（權重位元組＋KV 位元組）", LS(24)],
          [u"算術強度", u"prefill ≈ 輸入 token 數；decode ≈ batch 大小", LS(22)],
          [u"轉折點", u"峰值算力 ÷ 記憶體頻寬", LS(23)],
          [u"推測解碼加速比", u"(1−α^(γ+1)) ÷ ((1−α)(γc+1))", LS(32)]]),
        ("h", u"3. 硬體數字（BF16 稠密）"),
        ("t", [u"GPU", u"算力", u"頻寬", u"記憶體"],
         [[u"A100 80GB", u"312 TFLOPS", u"2.04 TB/s", u"80 GB"], [u"H100 SXM", u"989 TFLOPS", u"3.35 TB/s", u"80 GB"],
          [u"H200", u"989 TFLOPS", u"4.8 TB/s", u"141 GB"], [u"B200", u"2,250 TFLOPS", u"8 TB/s", u"192 GB"],
          [u"MI300X", u"1,307 TFLOPS", u"5.3 TB/s", u"192 GB"], [u"RTX 4090", u"165 TFLOPS", u"1.01 TB/s", u"24 GB"]]),
        ("h", u"4. 模型 KV Cache（BF16，每 token）"),
        ("t", [u"模型", u"層數 × KV 頭 × 頭維度", u"每 token"],
         [[u"Llama 3 8B", u"32 × 8 × 128", u"128 KiB"], [u"Llama 3 70B", u"80 × 8 × 128", u"320 KiB"], [u"DeepSeek-V3（MLA）", u"61 層 × 576 維", u"約 69 KiB"]]),
    ],
}

REFERENCES = [GUIDE, GLOSSARY]
