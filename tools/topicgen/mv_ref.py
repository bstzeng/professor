# -*- coding: utf-8 -*-
"""多模態 LLM 與影片生成的內部運作：參考頁——互動工具箱與名詞、公式速查。"""
from mv_common import *
import mv_a, mv_b, mv_e

GUIDE = {
    "file": "guide.html", "title": u"多模態與影片工具箱", "h1": u"多模態與影片工具箱", "icon": u"🧰",
    "description": u"token 計算、注意力成本、flow matching、噪音排程、對比學習、抽幀、VRAM 估算",
    "body": [
        ("raw", u"<script>%s</script><script>%s</script>" % (NVLIB, MVLIB)),
        ("p", u"本頁集中課程中的互動工具。數值為教學用的約略估算，實際以論文與官方模型卡為準。"),
        ("h", u"1. 四種多模態接法（第 6 課）"), mv_a._ARCH,
        ("h", u"2. 圖片 token 計算器（第 3、10 課）"), mv_a._TOK_IMG,
        ("h", u"3. 對比學習相似度矩陣（第 4 課）"), mv_a._CLIP,
        ("h", u"4. 影片抽幀與 token 預算（第 21 課）"), mv_b._FRAMES,
        ("h", u"5. Flow matching 精確速度場（第 25、38 課）"), mv_b._FLOW,
        ("h", u"6. 噪音排程與時間步平移（第 26 課）"), mv_b._SCHED,
        ("h", u"7. 影片 token 計算器（第 28 課）"), mv_b._TOK_VID,
        ("h", u"8. 注意力成本計算器（第 37 課）"), mv_e._ATTN,
        ("h", u"9. VRAM 估算（第 40 課）"), mv_e._VRAM,
        ("h", u"10. 影片生成大事記（第 36、45 課）"), mv_e._TL,
    ],
}

GLOSSARY = {
    "file": "glossary.html", "title": u"名詞與公式速查", "h1": u"名詞與公式速查", "icon": u"📖",
    "description": u"多模態 LLM 與影片生成的關鍵名詞、數字與公式",
    "body": [
        ("h", u"關鍵數字"),
        ("t", [u"項目", u"數字", u"課"],
         [[u"LLaVA 視覺 token", u"336×336、patch 14 → 576 個", LS(7)], [u"BLIP-2 Q-Former", u"32 個 query", LS(8)], [u"Whisper 編碼器", u"30 秒 → 1,500 個位置", LS(19)],
          [u"Mimi codec", u"12.5 Hz × 8 層 × 11 位元 ≈ 1.1 kbps", LS(19)], [u"5 秒 720p 影片", u"81 幀 → 潛空間 21 幀 → 75,600 個 token", LS(28)], [u"注意力主導的臨界點", u"N > 6d", LS(37)],
          [u"Wan 2.2 A14B", u"兩個專家、總約 27B、每步啟用 14B", LS(36)], [u"即時 24 fps", u"每幀約 41.7 毫秒", LS(42)]]),
        ("h", u"名詞"),
        ("t", [u"名詞", u"說明", u"課"],
         [[u"patch", u"圖片或影片切出的小塊，一塊一個 token", LS(3)], [u"RoPE", u"旋轉位置編碼，注意力只依賴相對位置", LS(3)], [u"InfoNCE", u"CLIP 的對比損失", LS(4)], [u"SigLIP", u"把每對圖文當成獨立二元分類的對比損失", LS(4)],
          [u"VQ-VAE", u"把連續特徵量化成 codebook 編號", LS(5)], [u"直通估計", u"前向用量化值、反向假裝導數為 1", LS(5)], [u"投影層", u"把視覺特徵映射到 LLM 嵌入空間的 MLP", LS(7)], [u"Q-Former", u"用可學習 query 壓縮視覺特徵", LS(8)],
          [u"門控交叉注意力", u"Flamingo 以 tanh(α) 門控、從恆等開始", LS(9)], [u"早期融合", u"所有模態 token 化後放進同一個 Transformer", LS(11)], [u"QK-Norm", u"先正規化 q、k 再算注意力分數", LS(11)],
          [u"DPO", u"不需獎勵模型的偏好對齊", LS(17)], [u"KV 快取", u"推論時存下每層的鍵與值", LS(22)], [u"Flow matching", u"回歸「資料減噪音」的速度場來學生成", LS(25)], [u"log-SNR", u"訊噪比的對數", LS(26)],
          [u"時間步平移", u"把取樣步數移向高噪音區", LS(26)], [u"因果 3D 卷積", u"只看過去的時間卷積，第一幀單獨編碼", LS(27)], [u"adaLN-Zero", u"條件產生縮放偏移與門控、門控初始為 0", LS(28)],
          [u"MMDiT", u"文字與影像 token 串接做聯合注意力", LS(29)], [u"CFG", u"有條件與無條件預測的外插", LS(29)], [u"Plücker 座標", u"用 6 維向量表示一條射線", LS(33)], [u"Diffusion forcing", u"每幀獨立噪音程度的訓練", LS(35)],
          [u"FlashAttention", u"分塊計算、線上 softmax，記憶體 O(N)", LS(37)], [u"一致性模型", u"同一軌跡上的點映射到同一終點", LS(38)], [u"FVD", u"影片特徵的 Fréchet 距離", LS(43)], [u"C2PA", u"經數位簽章的內容來源憑證", LS(44)]]),
    ],
}

REFERENCES = [GUIDE, GLOSSARY]
