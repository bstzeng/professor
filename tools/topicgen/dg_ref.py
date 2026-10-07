# -*- coding: utf-8 -*-
"""數位邏輯設計：參考頁——互動工具箱、Verilog 範例下載與速查。"""
from dg_common import LS, DGLIB, dgw, PUBLISH

GUIDE = {
    "file": "guide.html", "title": u"數位邏輯工具箱", "h1": u"數位邏輯工具箱", "icon": u"🧪",
    "description": u"邏輯閘沙盒、卡諾圖化簡、毛刺波形、加法器延遲、正反器時序、亞穩態、狀態機、時序預算、RISC-V CPU 模擬器，以及 Verilog 範例下載",
    "body": [
        ("raw", u"<script>%s</script>" % DGLIB),
        ("p", u"所有工具都在瀏覽器中即時計算。Verilog 範例的原始碼與模擬輸出分散在各課，也可以在本頁最下方整包下載。"),
        ("h", u"1. 邏輯閘沙盒（第 5、18、19、21、28 課）"), dgw({"t": "logic"}),
        ("h", u"2. 卡諾圖化簡（第 9、10 課）"), dgw({"t": "kmap", "n": 4}),
        ("h", u"3. 延遲與毛刺（第 15、16 課）"), dgw({"t": "glitch"}),
        ("h", u"4. 加法器延遲比較（第 22 課）"), dgw({"t": "adder"}),
        ("h", u"5. 閂鎖器、正反器與 setup／hold（第 30、32 課）"), dgw({"t": "ff"}),
        ("h", u"6. 亞穩態與 MTBF（第 33、42 課）"), dgw({"t": "meta"}),
        ("h", u"7. 有限狀態機（第 38、40 課）"), dgw({"t": "fsm"}),
        ("h", u"8. 時序預算與最高頻率（第 17、41 課）"), dgw({"t": "timing"}),
        ("h", u"9. RISC-V 單週期 CPU（第 51 課）"), dgw({"t": "cpu"}),
        ("h", u"Verilog 範例下載"),
        ("raw", u'<p><a href="v/digital-logic-verilog.zip" download><strong>⬇ 下載全部範例（zip）</strong></a></p>'),
        ("p", u"需要 Icarus Verilog（Linux：<code>apt install iverilog</code>；macOS：<code>brew install icarus-verilog</code>；Windows 有安裝程式）與 Python 3（組譯器用）。解壓後執行 <code>sh run_all.sh</code>，所有模擬輸出會寫到 <code>_out/</code>。"),
        ("t", [u"檔案", u"內容", u"課"],
         [[u"gates.v", u"內建閘原語與真值表", LS(5)], [u"mux.v", u"4 選 1 多工器三種寫法", LS(18)], [u"decoder.v", u"3 對 8 解碼器、優先權編碼器", LS(19)],
          [u"adders.v", u"半加器、全加器、N 位元漣波、4 位元超前進位", LS(21)], [u"timing.v", u"時脈太快時加法器出錯的實驗", LS(14)], [u"glitch.v", u"靜態危障與共識項", LS(15)],
          [u"alu.v", u"RV32I 用 32 位元 ALU、桶式移位器", LS(23)], [u"latches.v", u"SR、D 閂鎖器、主從式正反器", LS(28)], [u"counter.v", u"計數器、移位暫存器、LFSR", LS(37)],
          [u"fsm_seq.v", u"1011 序列偵測器（Moore／Mealy）", LS(39)], [u"traffic.v", u"紅綠燈控制器", LS(40)], [u"regfile.v", u"RISC-V 暫存器檔", LS(35)],
          [u"sync.v", u"兩級同步器", LS(42)], [u"rv_single.v、asm.py、prog.s", u"單週期 RISC-V CPU、組譯器、測試程式", LS(51)]]),
        ("raw", u"<p>" + u"　".join(u'<a href="v/%s" download>%s</a>' % (n, n) for n in PUBLISH) + u"</p>"),
    ],
}

GLOSSARY = {
    "file": "glossary.html", "title": u"公式與術語速查", "h1": u"公式與術語速查", "icon": u"📖",
    "description": u"布林代數、算術、時序公式與常用術語",
    "body": [
        ("h", u"布林代數"),
        ("t", [u"名稱", u"式子", u"課"],
         [[u"笛摩根", u"(AB)′ = A′ + B′，(A + B)′ = A′B′", LS(7)], [u"合併", u"AB + AB′ = A", LS(6)], [u"吸收", u"A + AB = A", LS(6)],
          [u"共識", u"AB + A′C + BC = AB + A′C", LS(6)], [u"夏農展開", u"F = x′F|ₓ₌₀ + xF|ₓ₌₁", LS(18)], [u"n 變數函數個數", u"2^(2ⁿ)", LS(8)]]),
        ("h", u"算術"),
        ("t", [u"名稱", u"式子", u"課"],
         [[u"二補數值", u"−b_{N−1}2^{N−1} + Σ bᵢ2ⁱ", LS(2)], [u"取負", u"−x = x̄ + 1", LS(2)], [u"全加器", u"s = a ⊕ b ⊕ c，c_out = ab + c(a ⊕ b)", LS(21)],
          [u"產生／傳遞", u"g = ab，p = a ⊕ b，c_{i+1} = gᵢ + pᵢcᵢ", LS(22)], [u"有號溢位", u"V = c_N ⊕ c_{N−1}", LS(23)], [u"有號小於", u"N ⊕ V", LS(20)]]),
        ("h", u"延遲與時序"),
        ("t", [u"名稱", u"式子", u"課"],
         [[u"RC 延遲", u"t ≈ 0.69 RC", LS(12)], [u"邏輯努力", u"d = gh + p", LS(13)], [u"動態功耗", u"P = αCV²f", LS(4)],
          [u"setup", u"t_cq + t_pd + t_setup ≤ T + t_skew", LS(41)], [u"hold", u"t_ccq + t_cd ≥ t_hold + t_skew", LS(41)],
          [u"亞穩態 MTBF", u"e^{t_r/τ} ／ (T₀ f_clk f_data)", LS(33)], [u"環形振盪器", u"T = 2N t_pd", LS(27)], [u"執行時間", u"指令數 × CPI × T", LS(53)]]),
        ("h", u"術語"),
        ("t", [u"術語", u"意義", u"課"],
         [[u"雜訊邊限", u"NM_H = V_OH − V_IH，NM_L = V_IL − V_OL", LS(1)], [u"質蘊涵項", u"卡諾圖上無法再擴大的圈", LS(9)], [u"關鍵路徑", u"延遲最長的路徑", LS(14)],
          [u"危障／毛刺", u"不同路徑延遲造成的短暫錯誤輸出", LS(15)], [u"閂鎖器", u"準位觸發、透明", LS(29)], [u"正反器", u"邊緣觸發", LS(30)],
          [u"亞穩態", u"雙穩態電路停在不穩定平衡點附近", LS(33)], [u"Moore／Mealy", u"輸出只看狀態／看狀態與輸入", LS(38)], [u"one-hot", u"每個狀態一個正反器", LS(39)],
          [u"同步器", u"兩級正反器，給亞穩態恢復時間", LS(42)], [u"非阻塞賦值", u"<=：循序邏輯用", LS(45)], [u"LUT", u"FPGA 的查表", LS(49)],
          [u"CPI", u"每條指令平均週期數", LS(53)], [u"轉送", u"把未寫回的結果直接送給下一條指令", LS(54)]]),
    ],
}

REFERENCES = [GUIDE, GLOSSARY]
