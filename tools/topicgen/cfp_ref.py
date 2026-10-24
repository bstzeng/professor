# -*- coding: utf-8 -*-
"""晶片的分區規劃：參考頁——互動工具箱、公式速查。"""
from cfp_common import *

GUIDE = {
    "file": "guide.html", "title": u"分區規劃互動工具箱", "h1": u"分區規劃互動工具箱", "icon": u"🧩",
    "description": u"floorplan 拼圖、互連拓樸、長線延遲、電源壓降、良率與 chiplet 成本",
    "body": [
        ("raw", u"<script>%s</script>" % CFLIB),
        ("p", u"所有工具都是教學用的簡化模型，數值為代表性的數量級。"),
        ("h", u"1. Floorplan 拼圖（" + LS(2) + u"、" + LS(39) + u"）"), cw("floor"),
        ("h", u"2. 互連拓樸比較（" + LS(25) + u"）"), cw("noc"),
        ("h", u"3. 長線延遲與中繼器（" + LS(27) + u"）"), cw("wire"),
        ("h", u"4. 電源網格壓降（" + LS(32) + u"）"), cw("ir"),
        ("h", u"5. 良率、成本與 chiplet（" + LS(38) + u"、" + LS(41) + u"）"), cw("yield"),
    ],
}

GLOSSARY = {
    "file": "glossary.html", "title": u"分區規劃公式速查", "h1": u"分區規劃公式速查", "icon": u"📖",
    "description": u"本課程的關鍵公式與名詞",
    "body": [
        ("raw", KATEX),
        ("h", u"1. 關鍵公式"),
        ("t", [u"公式", u"意思", u"課"],
         [[M(r"W=\sum w_n\,\mathrm{HPWL}_n"), u"加權線長；單一區塊最佳位置是加權中位數", LS(2)],
          [M(r"\mathrm{DPW}\approx\frac{\pi d^2}{4A}-\frac{\pi d}{\sqrt{2A}}"), u"每片晶圓晶片數", LS(5)],
          [M(r"t\approx t_0+\kappa\sqrt C"), u"快取延遲與容量", LS(6)], [M(r"I=\frac{2n}{3b},\ P=\min(P_{peak},I\cdot BW)"), u"算術強度與 roofline", LS(8)],
          [M(r"A=\frac{N_{bit}A_{cell}}{\eta}"), u"SRAM 巨集面積", LS(12)], [M(r"\mathrm{AMAT}=t_1+m_1(t_2+m_2(\dots))"), u"平均記憶體存取時間", LS(13)],
          [M(r"N=\lambda T"), u"Little 定律", LS(14)], [M(r"L\ge Np/4"), u"焊墊受限", LS(17)], [M(r"\Delta V_{BE}=\frac{kT}{q}\ln N"), u"溫度感測", LS(21)],
          [M(r"W=\frac{1/\mu}{1-\rho}"), u"共用匯流排延遲", LS(23)], [M(r"\bar h\approx\frac{2k}{3}"), u"網格 NoC 平均跳數", LS(25)],
          [M(r"T^*=(2+\sqrt2)L\sqrt{R_0C_0rc}"), u"最佳中繼器延遲", LS(27)], [M(r"\Delta V=\frac{ri\ell^2}{8}"), u"電源條最大壓降", LS(32)],
          [M(r"\mathrm{MTBF}=\frac{e^{t_r/\tau}}{T_0f_{clk}f_{data}}"), u"同步器失效間隔", LS(33)], [M(r"P\propto V^3,\ E\propto V^2"), u"DVFS", LS(34)],
          [M(r"T=tg^p"), u"Rent 定律", LS(37)], [M(r"Y=e^{-AD_0}"), u"Poisson 良率", LS(38)], [M(r"n=1/p^2"), u"接點密度", LS(42)]]),
        ("h", u"2. 名詞"),
        ("t", [u"名詞", u"說明", u"課"],
         [[u"Floorplan", u"大區塊的位置、形狀與通道規劃", LS(2)], [u"硬核／軟核", u"形狀固定的版圖 IP／可調整的邏輯 IP", LS(3)], [u"利用率", u"標準元件占區塊面積的比例", LS(4)],
          [u"SLC", u"系統層級快取，各區塊共享", LS(6)], [u"PHY", u"高速介面的實體層電路", LS(14)], [u"HBM", u"堆疊式高頻寬記憶體", LS(15)], [u"SerDes", u"串列器／解串器", LS(18)],
          [u"LDO", u"低壓差線性穩壓器", LS(19)], [u"保護環", u"吸收基板雜訊的接地擴散環", LS(20)], [u"NoC", u"晶片內網路", LS(25)], [u"中繼器", u"長線中的緩衝器", LS(27)],
          [u"電源域／電壓島", u"可整體開關／使用不同電壓的區域", LS(30)], [u"IR drop", u"電源網格的電阻壓降", LS(32)], [u"CDC", u"跨時脈域", LS(33)], [u"DVFS", u"動態調壓調頻", LS(34)],
          [u"Chiplet", u"拆分後在同一封裝內互連的小晶片", LS(41)], [u"UCIe", u"chiplet 互連開放標準", LS(42)]]),
    ],
}

REFERENCES = [GUIDE, GLOSSARY]
