# -*- coding: utf-8 -*-
"""親手訓練一個小 LLM：模組 E～I（第 25～42 課）。"""
from ng_common import *

lesson = nglesson

_ROPE = svg(
    title(u"RoPE：依位置把向量旋轉不同角度"),
    C(140, 110, 60, LINE), A(140, 110, 200, 110, BLUE, 2), T(214, 114, u"位置 0", 10, BLUE, "start"),
    A(140, 110, 182, 68, ORANGE, 2), T(188, 62, u"位置 1", 10, ORANGE, "start"), A(140, 110, 140, 50, GREEN, 2), T(146, 44, u"位置 2", 10, GREEN, "start"),
    T(140, 196, u"同一個向量，位置越後面轉得越多", 10, MUTED),
    box(300, 50, 320, 120, u"為什麼好用", [u"Q 和 K 都旋轉後，內積只取決於「相對距離」", u"不需要位置 embedding 表", u"每兩個維度一組、各用不同的轉速", u"Llama、Qwen、Mistral 都用它"], PURPLE),
)

_LORA = svg(
    title(u"LoRA：凍結大矩陣 W，只訓練兩個細長的小矩陣"),
    R(40, 50, 120, 120, GRAY, "rgba(140,140,140,0.15)"), T(100, 115, u"W（凍結）", 12, MUTED), T(100, 186, u"d × d", 10, MUTED),
    T(185, 115, u"＋", 18, ACC),
    R(215, 50, 26, 120, GREEN, "rgba(74,154,94,0.2)"), T(228, 186, u"B：d × r", 10, GREEN),
    R(255, 98, 120, 26, ORANGE, "rgba(217,130,43,0.2)"), T(315, 116, u"A：r × d", 10, ORANGE),
    box(420, 50, 200, 120, u"r ＝ 8、d ＝ 192 時", [u"W 有 36,864 個參數", u"A、B 合計只有 3,072 個", u"B 從 0 開始：一開始等於原模型", u"全模型 LoRA 檔約 144 KB"], ACC),
)

_PIPE = svg(
    title(u"從我們的小 GPT 到 ChatGPT"),
    flow([(u"預訓練", u"猜下一個字"), (u"SFT", u"指令與回答"), (u"偏好對齊", u"RLHF／DPO"), (u"部署", u"推論最佳化")], 50, 56, colors=[BLUE, GREEN, ORANGE, PURPLE]),
    T(110, 140, u"第 25～31 課", 10, BLUE), T(270, 140, u"第 39～41 課（LoRA 版）", 10, GREEN), T(430, 140, u"本課程未實作", 10, ORANGE), T(580, 140, u"第 33 課（KV cache）", 10, PURPLE),
)

MODULE_E = (u"模組 E｜訓練", [

lesson(u"資料載入與 batch",
  u"隨機切出一批練習題",
  [u"看懂 get_batch", u"理解 x 和 y 只差一格", u"知道 batch 與 block 的意思"],
  [("p", u"訓練資料是一長串 token id。每一步隨機挑 32 個起點，各切出 80 個字當 x，往右移一格當 y："),
   src("train", "def get_batch", "    return x.to(device), y.to(device)"),
   ("p", u"一個 batch 有 32 × 80 ＝ 2,560 個位置，每個位置都是一道「猜下一個字」的題目。因為切的位置是隨機的，一段文字可能從某首詩的中間開始、跨到下一首——換行符號會讓模型學會「詩在這裡結束，下一首從頭開始」。"),
   ("note", u"真實 LLM 怎麼做", [("p", u"大型訓練會先把所有資料 tokenize 好存成二進位檔，用記憶體映射（memmap）讀取；資料量太大，通常只會看過一遍，不會隨機重複抽。")]),
  ],
  u"get_batch 隨機挑起點切出 32 段 80 字的 x，y 是 x 往右移一格，所以一個 batch 有 2,560 道猜下一個字的題目。換行讓模型學會一首詩的結束與開始。",
  [u"x 和 y 之間是什麼關係？", u"一個 batch 有幾道題目？", u"為什麼切出來的片段可能跨越兩首詩也沒關係？"]),

lesson(u"AdamW 與學習率排程",
  u"warmup ＋ cosine",
  [u"看懂 AdamW 的設定", u"知道哪些參數要權重衰減", u"看懂學習率排程函式"],
  [src("train", "decay = [p for p", "                        lr=args.lr, betas=(0.9, 0.95))"),
   ("ul", [u"<strong>AdamW</strong>：大型 Transformer 的標準優化器。betas＝(0.9, 0.95) 是 GPT-3 論文的設定。", u"<strong>權重衰減只套用在矩陣上</strong>，偏差和 LayerNorm 的參數不衰減——這是常見的慣例。"]),
   src("train", "def lr_at", "    return args.lr * (0.1"),
   ngw({"t": "loss", "lr": 1, "q": u"上圖是實際訓練時的損失，下圖是學習率：先在 100 步內線性升到 0.001，再用餘弦曲線慢慢降到 0.0001。"}),
   ("p", u"還有一行很重要的程式：<code>clip_grad_norm_(model.parameters(), 1.0)</code>，梯度的總長度超過 1 就按比例縮小，避免偶爾一個怪 batch 讓參數爆掉。"),
  ],
  u"用 AdamW（betas 0.9、0.95），只對權重矩陣做 0.1 的權重衰減。學習率先 warmup 100 步，再以餘弦曲線衰減到 10%，並用梯度裁剪防止爆掉。",
  [u"為什麼偏差和 LayerNorm 不做權重衰減？", u"我們的學習率排程分哪兩段？", u"梯度裁剪在做什麼？"]),

lesson(u"觀察 loss 曲線",
  u"模型學到了什麼？",
  [u"讀懂訓練紀錄", u"把損失換算成困惑度", u"對照不同階段的生成結果"],
  ex("train", cmd=u"python train.py", show_src=False) + [
   ngw({"t": "loss", "q": u"實際訓練紀錄畫成曲線。"}),
   ("h", u"讀數字"),
   ("ul", [u"一開始損失約 8.85 ≈ ln(6758)：完全亂猜。", u"前幾百步下降最快：先學會常用字、標點、五七言的節奏。", u"後面越來越慢：要學的是更細的搭配和對仗，進步很難看出來。",
           u"最後驗證損失約 5.2，困惑度約 180——比 bigram 的 450 好很多，但離「真的會寫詩」還很遠。"]),
   ("p", u"整個訓練在 4 核心 CPU 上跑了約 18 分鐘。在 GPU 上，把模型放大 10 倍、訓練 10 倍久，生成品質會明顯更好。"),
  ],
  u"訓練損失從約 8.85（亂猜）開始，前幾百步下降最快，之後越來越慢，最後驗證損失約 5.2、困惑度約 180，遠優於 bigram。CPU 上約 18 分鐘。",
  [u"訓練一開始的損失為什麼約等於 ln(6758)？", u"為什麼後期損失下降越來越慢？", u"最後的困惑度大約是多少？比 bigram 好多少？"]),

lesson(u"驗證集與過擬合",
  u"它是在學，還是在背？",
  [u"比較訓練損失與驗證損失", u"知道如何判斷過擬合", u"了解我們的模型為什麼還沒過擬合"],
  [("p", u"<code>evaluate()</code> 每 200 步分別在訓練集和驗證集上抽 20 個 batch 算平均損失："),
   src("train", "def evaluate", "    return out"),
   ("p", u"注意 <code>model.eval()</code> 會關掉 dropout、<code>torch.no_grad()</code> 不記錄梯度，算完再切回 <code>model.train()</code>。"),
   ("h", u"判斷"),
   ("t", [u"現象", u"意思"], [[u"兩條線一起往下", u"還在學，可以繼續訓練"], [u"訓練往下、驗證持平或往上", u"開始過擬合（背答案）"], [u"兩條線都很高", u"模型太小或訓練不夠（欠擬合）"]]),
   ("p", u"我們的模型最後訓練損失約 4.7、驗證約 5.2，兩者還有差距但都還在下降，表示還沒嚴重過擬合。如果把同樣的資料訓練幾十個 epoch，驗證損失就會開始上升。"),
   ("note", u"驗證集的陷阱", [("p", u"我們的驗證集是整份文字的最後 5%，剛好是《全唐詩》後面的卷數，作者和風格可能和前面不同，所以驗證損失天生會高一點。更嚴謹的做法是隨機抽出 5% 的詩當驗證集。")]),
  ],
  u"每 200 步在訓練集與驗證集上評估損失，評估時用 eval() 關掉 dropout。兩者一起下降表示仍在學習；訓練降、驗證升就是過擬合。我們的模型兩條線都還在下降。",
  [u"model.eval() 和 torch.no_grad() 各做什麼？", u"怎麼從損失曲線判斷過擬合？", u"我們的驗證集切法可能有什麼問題？"]),

lesson(u"混合精度與梯度累積",
  u"用更少的記憶體、更快地訓練",
  [u"理解混合精度訓練", u"理解梯度累積", u"知道這兩招什麼時候用"],
  [("h", u"混合精度"),
   ("p", u"矩陣乘法用 16 位元（bfloat16）算，速度可以快 2 倍以上、記憶體減半；但權重和優化器狀態仍保留 32 位元，以免累積誤差。PyTorch 用 <code>torch.autocast</code> 自動處理："),
   src("train", "amp = torch.autocast", "amp = torch.autocast"),
   ("p", u"在 GPU 上加 <code>--amp</code> 就會啟用。bfloat16 的數值範圍和 FP32 一樣大，不像 FP16 需要額外做損失縮放（見〈LLM 模型全解〉第 50 課）。在 CPU 上效果有限，我們的實測沒有使用。"),
   ("h", u"梯度累積"),
   src("train", "    for _ in range(args.accum)", "        (loss / args.accum).backward()"),
   ("p", u"記憶體只夠放 8 段文字，但想要 32 段的效果？設定 <code>--batch 8 --accum 4</code>：連續算 4 次梯度（每次除以 4）累加起來，再更新一次參數，數學上等同一次 32 段的 batch。代價是一步要花 4 倍時間。"),
  ],
  u"混合精度用 bfloat16 做矩陣運算、FP32 保存權重，GPU 上更快更省記憶體。梯度累積把多個小 batch 的梯度加起來再更新，等同大 batch，用時間換記憶體。",
  [u"混合精度裡哪些部分用 16 位元、哪些用 32 位元？", u"--batch 8 --accum 4 等效於多大的 batch？", u"梯度累積的代價是什麼？"]),

lesson(u"存檔、讀檔與續訓",
  u"訓練到一半當機怎麼辦",
  [u"知道 checkpoint 要存哪些東西", u"會從存檔繼續訓練", u"看懂完整的 train.py"],
  [("p", u"每次評估時存一個 checkpoint："),
   src("train", "        torch.save(", "        torch.save("),
   ("ul", [u"<strong>model</strong>：所有權重。", u"<strong>opt</strong>：AdamW 的兩個動量狀態——不存的話，續訓時優化器要重新「暖機」。", u"<strong>cfg</strong>：模型設定，載入時才知道要建多大的模型。", u"<strong>step</strong>：學習率排程要從哪一步接著算。"]),
   ("p", u"續訓：<code>python train.py --resume</code>。真實的 LLM 訓練動輒數週、用上萬張 GPU，硬體故障是家常便飯，定期存檔與自動續訓是基本功。"),
  ] + ex("train", cmd=u"python train.py") + [],
  u"Checkpoint 要存權重、優化器狀態、模型設定與步數，才能完整續訓。用 --resume 從存檔繼續；大規模訓練必須定期存檔以應付硬體故障。",
  [u"checkpoint 為什麼要存優化器狀態？", u"為什麼要存 cfg？", u"續訓時學習率怎麼知道要從哪裡接著算？"]),

lesson(u"實驗：改層數、寬度、上下文長度",
  u"自己當研究員",
  [u"學會設計對照實驗", u"觀察模型大小對損失的影響", u"理解上下文長度的重要"],
  ex("s09_experiments") + [
   ("h", u"從結果學到"),
   ("ul", [u"在相同步數下，<strong>加深或加寬</strong>通常讓損失更低，但每一步也更慢。", u"<strong>上下文縮短到 16</strong>：模型連一句七言都看不完整，損失明顯變差——它不知道自己寫到第幾句。",
           u"只訓練 300 步的結論不一定能推廣到長時間訓練。真實的研究會用縮放定律，在小模型上做實驗、預測大模型的表現。"]),
   ("note", u"動手試試", [("ul", [u"把 dropout 改成 0，看驗證損失會不會變差。", u"把學習率改成 3e-3 或 3e-4。", u"不加 warmup（--warmup 0）會怎樣？"])]),
  ],
  u"對照實驗一次只改一個變因。加深、加寬通常降低損失但更慢；上下文太短，模型看不到整首詩的結構，損失明顯變差。短時間實驗的結論要小心推廣。",
  [u"設計對照實驗的原則是什麼？", u"上下文縮短到 16 為什麼會變差？", u"為什麼只訓練 300 步的結論可能不準？"]),
])

MODULE_F = (u"模組 F｜生成", [

lesson(u"Temperature、Top-k、Top-p",
  u"控制模型的創意",
  [u"理解三種抽樣參數", u"觀察它們對生成的影響", u"看懂 generate 的抽樣程式"],
  [ngw({"t": "sample", "q": u"這是本課程模型真實的輸出分布。調整三個參數，看哪些字還有機會被抽到。"}),
   src("gpt", "            logits = logits[:, -1, :] / max", "            nxt = torch.argmax"),
  ] + ex("s10_sampling") + [
   ("t", [u"參數", u"做法", u"效果"], [[u"Temperature", u"logits 除以 T 再 softmax", u"T＜1 保守、T＞1 大膽；T＝0 等於每次選第一名"], [u"Top-k", u"只保留機率最高的 k 個", u"切掉冷門字"],
                                    [u"Top-p", u"保留累積機率剛好達到 p 的最小集合", u"候選數自動調整：有把握時少、沒把握時多"]]),
   ("p", u"貪婪解碼（T＝0）常會陷入重複，因為每次都選同樣的高頻字。實務上常用 T＝0.7～1.0 加上 top-p＝0.9。"),
  ],
  u"Temperature 調整分布的平坦程度，top-k 只留前 k 名，top-p 留累積機率達 p 的最小集合。貪婪解碼容易重複，常用 T 約 0.7～1.0 搭配 top-p 0.9。",
  [u"T＝0 時生成會怎樣？", u"top-k 和 top-p 的差別是什麼？", u"為什麼貪婪解碼容易重複？"]),

lesson(u"KV cache 實作",
  u"不要重算已經算過的東西",
  [u"理解 KV cache 的原理", u"看懂 cache 的程式", u"實測加速並驗證正確性"],
  [("p", u"沒有 KV cache 時，生成第 50 個字要把前 49 個字整個重算一次。但前面每個字的 K、V 根本沒變！KV cache 把它們存起來，每一步只算新字的 Q、K、V，再和快取接起來。"),
   src("gpt", "        if cache is not None:", "            cache[\"k\"], cache[\"v\"] = k, v"),
   ("p", u"位置也要跟著調整：新字的位置是 <code>start</code>，而不是 0。"),
  ] + ex("s11_kvcache") + [
   ("p", u"結果完全相同，速度快了一倍多，而且序列越長差距越大。代價是記憶體：每一層都要存所有字的 K、V。大型模型處理長文件時，KV cache 可能比模型本身還大（見〈一次 LLM 推論到底發生什麼〉第 12、13 課）。"),
  ],
  u"KV cache 把每層已算過的 K、V 存起來，生成時只算新 token 並接上快取，輸出完全相同但快很多。代價是記憶體，長上下文時 KV cache 可能比模型還大。",
  [u"為什麼前面字的 K、V 可以重複使用？", u"用 KV cache 時，新 token 的位置要怎麼處理？", u"KV cache 的代價是什麼？"]),

lesson(u"做一個互動寫詩介面",
  u"chat.py",
  [u"把模型包成可以互動的程式", u"處理詞彙表外的輸入", u"了解「聊天」和「續寫」的差別"],
  ex("sample", cmd=u"python sample.py --prompt 春 --n 3") + ex("chat", cmd=u"python chat.py") + [
   ("p", u"給第一句「孤帆遠影」，它就接著寫下去。這其實不是聊天，而是<strong>續寫</strong>：模型只會把你給的文字當開頭繼續寫。ChatGPT 能「對話」，是因為它在預訓練之後，又用大量「問題—回答」格式的資料微調過（第 39 課會做一個迷你版）。"),
  ],
  u"sample.py 載入模型並依參數生成，chat.py 包成互動介面，並濾掉詞彙表外的字。這是續寫而不是對話；能對話的模型還需要用問答格式的資料微調。",
  [u"chat.py 怎麼處理詞彙表裡沒有的字？", u"「續寫」和「對話」有什麼不同？", u"ChatGPT 為什麼能對話？"]),
])

MODULE_G = (u"模組 G｜升級成現代架構", [

lesson(u"RoPE：旋轉位置編碼",
  u"Llama 的位置編碼",
  [u"理解 RoPE 的想法", u"看懂 rope 函式", u"知道 RoPE 的優點"],
  [("fig", _ROPE, "0 0 640 210", u"RoPE 把 Q、K 依位置旋轉，內積只取決於兩個字的相對距離。"),
   ("p", u"2021 年蘇劍林等人提出 RoPE。做法：把向量每兩個維度當成平面上的一個點，依照 token 的位置旋轉一個角度。不同的維度組用不同的轉速（從快到慢）。"),
   src("gpt", "def rope(x, pos)", "    return out.flatten(-2)"),
   ("p", u"關鍵性質：位置 m 的 Q 和位置 n 的 K 都旋轉之後，它們的內積只跟 <strong>m − n</strong> 有關。模型自然學到「相對位置」，而且不需要位置 embedding 表。"),
   ("p", u"在 <code>CausalSelfAttention.forward</code> 裡，只對 Q、K 套用 RoPE（V 不用）："),
   src("gpt", "            pos = torch.arange(start", "            q, k = rope(q, pos), rope(k, pos)"),
   ("p", u"搭配 YaRN 等方法調整轉速，RoPE 模型可以延伸到比訓練時更長的上下文（見〈LLM 模型全解〉第 69 課）。"),
  ],
  u"RoPE 把 Q、K 每兩個維度依位置旋轉不同角度，旋轉後的內積只取決於相對距離，不需要位置 embedding 表，還能延伸上下文。Llama、Qwen 等都使用。",
  [u"RoPE 為什麼只轉 Q、K，不轉 V？", u"RoPE 的內積只取決於什麼？", u"用 RoPE 的模型還需要位置 embedding 表嗎？"]),

lesson(u"RMSNorm 與 SwiGLU",
  u"更省、更好的兩個零件",
  [u"看懂 RMSNorm", u"看懂 SwiGLU", u"知道它們取代了什麼"],
  [("h", u"RMSNorm"),
   src("gpt", "class RMSNorm", "        return x * torch.rsqrt"),
   ("p", u"LayerNorm 要減平均、除標準差；RMSNorm 只除以均方根，省掉減平均的步驟，也沒有偏差。效果幾乎一樣，計算更快。"),
   ("h", u"SwiGLU"),
   src("gpt", "        if cfg.modern:                              # SwiGLU", "            self.w2 = nn.Linear(h, cfg.n_embd, bias=False)"),
   ("p", u"一般 FFN 是 <code>W₂ · GELU(W₁x)</code>；SwiGLU 是 <code>W₂ · (SiLU(W₁x) ⊙ W₃x)</code>：多一個矩陣 W₃ 當「閘門」，逐元素相乘。為了讓參數量和原本差不多，中間層從 4d 縮成約 8d/3。2020 年 Noam Shazeer 的論文顯示它效果更好，之後被 PaLM、Llama 採用。"),
   ("p", u"另外，modern 版的線性層都拿掉了偏差（<code>bias=False</code>），這也是 Llama 的做法。"),
  ],
  u"RMSNorm 只除以均方根、不減平均也沒有偏差，更快且效果相當。SwiGLU 用 SiLU 閘門乘上另一路線性變換，中間層約 8d/3 以維持參數量，效果比 GELU FFN 好。",
  [u"RMSNorm 比 LayerNorm 省了哪一步？", u"SwiGLU 比一般 FFN 多了哪個矩陣？", u"為什麼 SwiGLU 的中間層是 8d/3 而不是 4d？"]),

lesson(u"對照 Llama 的程式碼",
  u"我們的模型和 Llama 差在哪？",
  [u"比較兩種風格的訓練結果", u"列出我們的模型和 Llama 的差異", u"知道還差了哪些元件"],
  [("p", u"用 <code>python train.py --modern --out ckpt_modern.pt</code> 訓練同樣步數的 Llama 風格模型，比較兩者："),
   ngw({"t": "loss", "modern": 1, "q": u"兩種模型的驗證損失。"}),
  ] + ex("s12_modern") + [
   ("t", [u"元件", u"我們的 modern 版", u"Llama 3"], [[u"位置編碼", u"RoPE", u"RoPE（base 50 萬）"], [u"正規化", u"RMSNorm", u"RMSNorm"], [u"FFN", u"SwiGLU", u"SwiGLU"],
                                                [u"注意力", u"多頭（MHA）", u"GQA：多個 Q 頭共用 KV"], [u"Tokenizer", u"字元級 6,758", u"BPE 128,256"], [u"規模", u"4 層、192 維", u"8B：32 層、4096 維"],
                                                [u"權重綁定", u"有", u"8B 沒有"]]),
   ("p", u"結構上我們只差 GQA，其他都是規模和工程的差異。看懂了這份 200 行的程式，就看得懂 Llama 的官方實作。"),
  ],
  u"Llama 風格模型在同樣步數與參數量下訓練並比較驗證損失。與 Llama 3 相比，結構上只差 GQA，其餘差異在 tokenizer、規模與工程細節。",
  [u"我們的 modern 版和 Llama 3 結構上差了哪個元件？", u"Llama 3 的詞彙量大約多少？", u"兩種風格的驗證損失哪個比較低？"]),
])

MODULE_H = (u"模組 H｜微調", [

lesson(u"載入開源小模型",
  u"站在別人訓練好的模型上",
  [u"知道 Hugging Face 的角色", u"看懂載入模型與 tokenizer 的程式", u"了解微調開源模型需要的資源"],
  [("p", u"我們的唐詩模型只看過 162 萬字。開源模型（Llama、Qwen、Gemma、Mistral 等）用數兆 token 預訓練過，懂得多得多。實務上幾乎都是<strong>拿開源模型來微調</strong>，而不是從零訓練。"),
   ("p", u"Hugging Face 是最大的開源模型平台，用 <code>transformers</code> 套件兩行就能載入："),
   ("code", u"from transformers import AutoModelForCausalLM, AutoTokenizer\ntok = AutoTokenizer.from_pretrained(\"Qwen/Qwen2.5-0.5B-Instruct\")\nmodel = AutoModelForCausalLM.from_pretrained(\"Qwen/Qwen2.5-0.5B-Instruct\")"),
   ("p", u"載入的模型和我們的 GPT 本質相同：<code>model(input_ids)</code> 輸出 logits，<code>.generate()</code> 逐字生成。0.5B 的模型約 1 GB，筆電也跑得動；7B 以上的模型通常需要 GPU 或量化。"),
   ("t", [u"模型大小", u"推論（16 位元）", u"LoRA 微調（約略）"], [[u"0.5B", u"約 1 GB", u"CPU 可行但慢；任何 GPU"], [u"7B～8B", u"約 16 GB", u"24 GB GPU，或用 QLoRA 壓到約 10 GB"], [u"70B", u"約 140 GB", u"多張 GPU，或 QLoRA 約 48 GB"]]),
   ("note", u"本課程的實測範圍", [("p", u"本課程的測試環境無法連線到 Hugging Face，所以下面第 40 課附的 <code>hf_qwen_lora.py</code> 沒有附上執行結果。我們改在自己的唐詩模型上，從零實作 LoRA 並完整跑過——原理完全相同。")]),
  ],
  u"實務上多半拿開源模型微調而非從零訓練。transformers 套件兩行就能從 Hugging Face 載入模型與 tokenizer，用法和我們的 GPT 相同；模型越大需要的 GPU 記憶體越多。",
  [u"為什麼實務上很少從零訓練 LLM？", u"0.5B 的模型用 16 位元大約佔多少記憶體？", u"AutoModelForCausalLM 載入的模型輸出什麼？"]),

lesson(u"指令微調的資料格式",
  u"教模型「聽話」",
  [u"理解指令資料的格式", u"知道 chat template", u"自己做一份指令資料"],
  [("p", u"預訓練模型只會續寫。要讓它聽懂指令，就要用「指令 → 回答」格式的資料再訓練，叫<strong>指令微調（SFT）</strong>。常見格式是 JSONL，每行一筆："),
   ("code", u"{\"messages\": [{\"role\": \"user\", \"content\": \"寫一首關於春天的七言絕句\"},\n              {\"role\": \"assistant\", \"content\": \"春風……\"}]}"),
   ("p", u"每個模型有自己的 <strong>chat template</strong>，把對話轉成一串文字，例如 Qwen 用 <code>&lt;|im_start|&gt;user … &lt;|im_end|&gt;</code>。微調和使用時必須用同一種格式。"),
   ("h", u"我們的迷你版"),
   ("p", u"我們發明一個簡單格式：<code>〔體裁 主題字〕詩</code>。從語料自動產生：判斷每首詩的體裁，再從詩中挑一個常見的主題字。"),
  ] + ex("s13_instruct_data") + [
   ("p", u"現在看看<strong>微調前</strong>的模型，給它「〔七言絕句 春〕」會發生什麼——第 41 課有完整評估，結果是它幾乎完全不理會指令，因為它從沒看過「〔」。"),
  ],
  u"指令微調用「指令→回答」格式的資料讓模型學會聽話，資料常以 JSONL 儲存，並套用模型專屬的 chat template。我們從唐詩自動產生〔體裁 主題字〕＋詩的迷你指令資料。",
  [u"什麼是 SFT？", u"為什麼微調和使用時要用同一種 chat template？", u"我們的指令資料是怎麼自動產生的？"]),

lesson(u"用 LoRA 微調",
  u"只訓練 1% 的參數",
  [u"理解 LoRA 的原理", u"從零實作 LoRALinear", u"只對回答的部分計算損失"],
  [("fig", _LORA, "0 0 640 200", u"LoRA 在原本的權重旁邊加上兩個低秩小矩陣。"),
   ("p", u"全參數微調要存一整份新模型，也要很多記憶體。<strong>LoRA</strong>（2021，微軟）凍結原本的權重 W，只在旁邊加兩個細長的小矩陣：\\(y = Wx + BAx \\cdot \\frac{\\alpha}{r}\\)。r 通常是 8～64，遠小於 d。"),
  ] + ex("lora") + [
   ("h", u"三個重點"),
   ("ul", [u"<strong>B 初始化為 0</strong>：訓練開始時 BA ＝ 0，模型和原本一模一樣，不會一開始就被破壞。",
           u"<strong>只對詩算損失</strong>：<code>y</code> 裡指令部分設成 −100（PyTorch 的 ignore_index），模型只學「看到指令後怎麼寫」，不用學怎麼寫指令。",
           u"<strong>檔案很小</strong>：只要存 A、B，本課程約 144 KB（原模型約 12 MB）；可以為不同任務各訓練一份，隨時切換。"]),
   ("p", u"用 Hugging Face 的 <code>peft</code> 套件對開源模型做 LoRA，概念完全一樣："),
  ] + ex("hf_qwen_lora", cmd=u"python hf_qwen_lora.py（需安裝 transformers、peft，並可連線 Hugging Face）") + [],
  u"LoRA 凍結原權重，只訓練兩個低秩矩陣 A、B（y = Wx + BAx·α/r），B 從 0 開始所以初始等於原模型。只對回答部分算損失，訓練參數約 1%，存檔約 144 KB。",
  [u"LoRA 為什麼把 B 初始化為 0？", u"ignore_index＝−100 的作用是什麼？", u"LoRA 的檔案為什麼這麼小？"]),

lesson(u"評估微調前後的差異",
  u"用數字說話",
  [u"設計可自動檢查的評估", u"比較微調前後", u"理解評估的限制"],
  [("p", u"「感覺變好了」不算數。我們設計兩個可以用程式自動檢查的指標："),
   ("ul", [u"<strong>體裁正確</strong>：句數（4 或 8）和每句字數（5 或 7）都對。", u"<strong>包含主題字</strong>：詩裡有出現指定的字。"]),
  ] + ex("s14_eval") + [
   ("p", u"只訓練約 1% 的參數、600 步，<strong>體裁正確率從 4/60 提升到 48/60</strong>：模型學會了看指令決定寫五言還是七言、絕句還是律詩。這就是 SFT 的威力——也是 ChatGPT 從 GPT-3 變得「聽話」的關鍵一步。"),
   ("p", u"但<strong>包含主題字只從 3/60 變成 6/60</strong>，幾乎沒有進步。格式是很強、很一致的訊號（每首詩都有），容易學；「詩裡要出現某個字」對這個 300 萬參數的小模型來說難得多，而且我們的訓練資料裡，主題字可能出現在詩的任何位置，訊號比較弱。這是很真實的一課：微調前後一定要分項目量，不能只憑幾個好例子就說「成功了」。"),
   ("note", u"動手試試", [("ul", [u"把 lora.py 的訓練步數從 600 加到 3000，看主題字的比例會不會上升。", u"把 r 從 8 加到 32，或把 LoRA 也加到 MLP 層。", u"改用 Llama 風格的模型（ckpt_modern.pt）當基礎。"])]),
   ("h", u"評估的限制"),
   ("ul", [u"這兩個指標只檢查<strong>格式</strong>，不檢查<strong>好不好</strong>。詩寫得好不好，需要人來評，或用更強的模型當評審（LLM-as-a-judge）。",
           u"評估用的提示要和訓練資料分開，否則可能只是背下來。我們留了最後 500 筆不參與訓練。",
           u"建立自己的評估集，是任何微調專案最重要的一步（見〈LLM 模型全解〉第 76 課、〈提示工程〉第 40、41 課）。"]),
  ],
  u"用可自動檢查的指標（體裁正確、包含主題字）比較微調前後：LoRA 只訓練約 1% 參數，體裁正確率從 4/60 升到 48/60，但主題字只從 3/60 到 6/60——格式易學、內容控制難。格式指標不代表品質，評估資料也要與訓練資料分開。",
  [u"我們用了哪兩個自動評估指標？結果各是多少？", u"為什麼體裁容易學、主題字比較難？", u"這兩個指標沒辦法評估什麼？"]),
])

MODULE_I = (u"模組 I｜總結", [

lesson(u"從你的小 GPT 到 GPT-4：差了什麼",
  u"規模、資料、對齊與工程",
  [u"比較本課程模型與大型 LLM", u"知道還沒做的步驟", u"規劃接下來的學習"],
  [("fig", _PIPE, "0 0 640 160", u"一個聊天模型的完整流程，以及本課程做到哪裡。"),
   ("t", [u"", u"本課程", u"大型 LLM（約略）"],
    [[u"參數", u"300 萬", u"數十億到數兆"], [u"訓練資料", u"162 萬字", u"數兆到數十兆 token"], [u"訓練算力", u"一台 CPU、約 20 分鐘", u"上萬張 GPU、數週到數月"],
     [u"Tokenizer", u"字元級", u"BPE，10 萬以上"], [u"上下文", u"80", u"數萬到百萬"], [u"對齊", u"LoRA 指令微調", u"SFT ＋ RLHF／DPO ＋ 安全訓練"],
     [u"推論", u"KV cache", u"量化、批次、推測解碼、分散式部署"]]),
   ("p", u"但<strong>核心的程式碼和原理是一樣的</strong>：tokenizer、embedding、注意力、殘差、預測下一個 token、交叉熵、AdamW、抽樣。你已經親手寫過每一個零件了。"),
   ("h", u"接下來"),
   ("ul", [u"把模型放大、在 GPU 上訓練更久，看品質怎麼變。", u"把語料換成你自己的（例如金庸小說、宋詞、你的部落格），注意長度和清理。", u"改用 BPE tokenizer 訓練一般中文文章。",
           u"讀 nanoGPT、Llama 的原始碼。", u"〈LLM 模型全解〉：RLHF、DPO、量化、MoE。", u"〈一次 LLM 推論到底發生什麼〉：推論系統的工程。"]),
   ("h", u"下載全部範例"),
   ("p", u"<a href=\"py/build-tiny-llm-examples.zip\" download>build-tiny-llm-examples.zip</a>：所有程式碼（不含資料與訓練好的模型）。先執行 <code>python prepare_data.py</code>，再 <code>python train.py</code>。"),
  ],
  u"本課程的模型與大型 LLM 在參數、資料、算力、tokenizer、上下文、對齊與推論工程上差了好幾個數量級，但核心原理與程式碼相同。接下來可以放大模型、換語料、改用 BPE、閱讀 nanoGPT 與 Llama。",
  [u"本課程的模型和大型 LLM 在哪些方面差距最大？", u"本課程沒有實作的對齊步驟是什麼？", u"想讓模型寫宋詞，需要改哪些地方？"]),
])

MODULES = [MODULE_E, MODULE_F, MODULE_G, MODULE_H, MODULE_I]
