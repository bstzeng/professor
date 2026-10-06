# -*- coding: utf-8 -*-
"""多模態與生成式 AI：參考頁——互動工具箱、名詞速查。"""
from mm_common import LS, MMLIB, mmw

GUIDE = {
    "file": "guide.html", "title": u"多模態互動工具箱", "h1": u"多模態互動工具箱", "icon": u"🧮",
    "description": u"擴散加噪、CFG 引導、ViT 切 patch、CLIP 相似度、頻譜圖、潛空間壓縮",
    "body": [
        ("raw", u"<script>%s</script>" % MMLIB),
        ("h", u"1. 擴散：加噪與去噪（第 13、14 課）"), mmw({"t": "noise"}),
        ("h", u"2. Classifier-free guidance（第 17 課）"), mmw({"t": "cfg"}),
        ("h", u"3. 潛空間壓縮（第 18 課）"), mmw({"t": "latent"}),
        ("h", u"4. ViT 切 patch 與圖片 token 數（第 6、30 課）"), mmw({"t": "patch"}),
        ("h", u"5. CLIP 圖文相似度（第 7 課）"), mmw({"t": "clip"}),
        ("h", u"6. 頻譜圖（第 33 課）"), mmw({"t": "spec"}),
    ],
}

GLOSSARY = {
    "file": "glossary.html", "title": u"多模態名詞速查", "h1": u"多模態名詞速查", "icon": u"📖",
    "description": u"本課程用到的名詞與對應課次",
    "body": [
        ("t", [u"名詞", u"說明", u"課"],
         [[u"模態", u"資訊的形式：文字、圖片、聲音、影片…", LS(1)], [u"GAN", u"生成器與判別器對抗訓練", LS(10)], [u"VAE", u"把資料壓縮到可抽樣的潛空間", LS(9)],
          [u"模式崩潰", u"GAN 只生成少數幾種結果", LS(12)], [u"Deepfake", u"以深度學習偽造的影音", LS(11)], [u"ViT", u"把圖切成 patch 當 token 的 Transformer", LS(6)],
          [u"CLIP", u"以對比學習讓圖文向量對齊", LS(7)], [u"零樣本分類", u"不重新訓練、用文字描述分類", LS(7)], [u"擴散模型", u"學會逐步去除雜訊", LS(13)],
          [u"雜訊排程 β／ᾱ", u"每一步加多少雜訊／還剩多少原圖", LS(14)], [u"U-Net", u"下採樣＋上採樣＋跳接的去噪網路", LS(15)], [u"取樣器", u"DDPM、DDIM、Euler、DPM++…", LS(16)],
          [u"種子", u"決定起點雜訊的亂數", LS(16)], [u"CFG", u"無條件 ＋ w ×（有條件 − 無條件）", LS(17)], [u"負面提示詞", u"讓生成遠離的描述", LS(21)],
          [u"Latent Diffusion", u"在 VAE 潛空間中擴散", LS(18)], [u"交叉注意力", u"Q 來自圖、K/V 來自文字", LS(19)], [u"DiT", u"以 Transformer 為骨幹的擴散模型", LS(20)],
          [u"Flow matching", u"學從雜訊到資料的近直線路徑", LS(20)], [u"Img2img／Inpainting", u"從現有圖片加噪重畫／局部重畫", LS(23)], [u"ControlNet", u"以姿勢、邊緣等控制構圖", LS(24)],
          [u"LoRA（圖像）", u"小型微調檔，學特定主體或畫風", LS(25)], [u"ComfyUI", u"節點式生成工作流工具", LS(26)], [u"視覺語言模型", u"視覺編碼器＋投影層＋LLM", LS(28)],
          [u"LLaVA", u"2023 年的開源視覺語言模型範本", LS(29)], [u"頻譜圖／Mel", u"時間×頻率的聲音表示", LS(33)], [u"Whisper", u"68 萬小時訓練的語音辨識模型", LS(35)],
          [u"TTS／聲碼器", u"語音合成／頻譜轉波形", LS(36)], [u"Neural codec／RVQ", u"把聲音變成離散 token", LS(38)], [u"端到端語音", u"聲音 token 進、聲音 token 出", LS(39)],
          [u"時空 patch", u"影片切成的 token", LS(42)], [u"世界模型", u"預測世界接下來會如何的模型", LS(43)], [u"NeRF／Gaussian Splatting", u"從照片重建 3D 場景", LS(44)],
          [u"C2PA／SynthID", u"內容來源標記／隱形浮水印", LS(47)]]),
    ],
}

REFERENCES = [GUIDE, GLOSSARY]
