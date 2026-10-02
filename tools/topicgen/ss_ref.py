# -*- coding: utf-8 -*-
"""統計物理與相變：參考頁——互動實驗室、公式速查。"""
from ss_common import LS, SSLIB, ssw

LAB = {
    "file": "lab.html", "title": u"統計物理互動實驗室", "h1": u"統計物理互動實驗室", "icon": u"🧪",
    "description": u"隨機漫步、自由膨脹、速度分布、負溫度、量子統計、伊辛模型、區塊自旋、滲流",
    "body": [
        ("raw", u"<script>%s</script>" % SSLIB),
        ("p", u"所有模擬都在你的瀏覽器裡即時執行。"),
        ("h", u"1. 隨機漫步（第 4 課）"), ssw({"t": "walk"}),
        ("h", u"2. 自由膨脹與熵（第 10 課）"), ssw({"t": "expand"}),
        ("h", u"3. 馬克士威速度分布（第 20 課）"), ssw({"t": "mb"}),
        ("h", u"4. 二能階系統與負溫度（第 18 課）"), ssw({"t": "two"}),
        ("h", u"5. 量子統計（第 24 課）"), ssw({"t": "qs"}),
        ("h", u"6. 伊辛模型（第 33 課）"), ssw({"t": "ising"}),
        ("h", u"7. 區塊自旋粗粒化（第 39 課）"), ssw({"t": "block"}),
        ("h", u"8. 滲流（第 42 課）"), ssw({"t": "perc"}),
    ],
}

CHEATSHEET = {
    "file": "cheatsheet.html", "title": u"統計物理公式速查", "h1": u"統計物理公式速查", "icon": u"🗂️",
    "description": u"常數、核心公式與臨界指數",
    "body": [
        ("h", u"1. 常數"),
        ("t", [u"常數", u"數值"],
         [[u"波茲曼常數 k_B", u"1.380649×10⁻²³ J/K"], [u"室溫 k_BT", u"約 0.0259 eV（300 K）"], [u"亞佛加厥數", u"6.022×10²³ /mol"], [u"氣體常數 R", u"8.314 J/(mol·K)"]]),
        ("h", u"2. 核心公式"),
        ("t", [u"公式", u"意義", u"課"],
         [[u"S = k_B ln W", u"波茲曼熵", LS(9)], [u"1/T = ∂S/∂E", u"溫度的定義", LS(12)], [u"F = U − TS", u"亥姆霍茲自由能", LS(14)],
          [u"P ∝ e^(−E/k_BT)", u"波茲曼因子", LS(16)], [u"Z = Σ e^(−Eᵢ/k_BT)，F = −k_BT ln Z", u"配分函數", LS(17)],
          [u"⟨½mv²⟩ = (3/2)k_BT", u"能量均分", LS(19)], [u"⟨n⟩ = 1/(e^((E−μ)/k_BT) ± 1)", u"費米—狄拉克（+）／玻色—愛因斯坦（−）", LS(24)],
          [u"⟨r²⟩ ∝ N", u"隨機漫步", LS(4)], [u"D = k_BT / (6πηa)", u"愛因斯坦—斯托克斯", LS(5)], [u"Q ≥ k_BT ln 2", u"蘭道爾原理", LS(13)],
          [u"η = 1 − T_c/T_h", u"卡諾效率", LS(7)], [u"k_BT_c/J = 2/ln(1+√2) ≈ 2.269", u"二維伊辛臨界溫度", LS(35)]]),
        ("h", u"3. 臨界指數"),
        ("t", [u"指數", u"平均場", u"二維伊辛", u"三維伊辛"],
         [[u"β", u"1/2", u"1/8", u"0.326"], [u"γ", u"1", u"7/4", u"1.237"], [u"ν", u"1/2", u"1", u"0.630"], [u"α", u"0", u"0（對數）", u"0.110"]]),
        ("h", u"4. 術語"),
        ("t", [u"術語", u"英文", u"課"],
         [[u"系綜", u"ensemble", LS(15)], [u"配分函數", u"partition function", LS(17)], [u"化學勢", u"chemical potential", LS(22)],
          [u"序參量", u"order parameter", LS(32)], [u"關聯長度", u"correlation length", LS(36)], [u"普適性", u"universality", LS(37)],
          [u"重整化群", u"renormalization group", LS(40)], [u"滲流", u"percolation", LS(42)], [u"湧現", u"emergence", LS(47)]]),
    ],
}

REFERENCES = [LAB, CHEATSHEET]
