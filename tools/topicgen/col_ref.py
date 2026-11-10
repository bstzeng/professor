# -*- coding: utf-8 -*-
"""大型對撞機：參考頁——論文清單、關鍵數字。"""
from col_common import LS, M


def R(title, ref, note, ls):
    return [title, u'<span style="font-family:ui-monospace,Menlo,monospace;font-size:0.9em">%s</span>' % ref, note, ls]


PAPERS = {
    "file": "papers.html", "title": u"論文清單", "h1": u"本課程引用的主要論文", "icon": u"📄",
    "description": u"希格斯發現、統計方法、重建演算法與歷史發現的原始論文",
    "body": [
        ("p", u"論文編號可以在 arXiv（arxiv.org）或 INSPIRE-HEP（inspirehep.net）搜尋；大部分 LHC 的論文都可以免費閱讀。"),
        ("h", u"希格斯玻色子"),
        ("t", [u"論文", u"出處", u"重點", u"課"], [
            R(u"ATLAS：Observation of a new particle in the search for the Standard Model Higgs boson", u"Phys. Lett. B 716, 1 (2012)；arXiv:1207.7214", u"126.0 GeV，5.9σ", LS(56)),
            R(u"CMS：Observation of a new boson at a mass of 125 GeV", u"Phys. Lett. B 716, 30 (2012)；arXiv:1207.7235", u"125.3 GeV，5.0σ（預期 5.8σ）", LS(56)),
            R(u"ATLAS 與 CMS：Combined measurement of the Higgs boson mass", u"Phys. Rev. Lett. 114, 191803 (2015)", u"125.09 ± 0.24 GeV", LS(57)),
            R(u"ATLAS：A detailed map of Higgs boson interactions … ten years after the discovery", u"Nature 607, 52 (2022)", u"十週年耦合總結", LS(57)),
            R(u"CMS：A portrait of the Higgs boson … ten years after the discovery", u"Nature 607, 60 (2022)", u"十週年耦合總結", LS(57)),
        ]),
        ("h", u"統計方法"),
        ("t", [u"論文", u"出處", u"重點", u"課"], [
            R(u"Cowan, Cranmer, Gross, Vitells：Asymptotic formulae for likelihood-based tests of new physics", u"Eur. Phys. J. C 71, 1554 (2011)；arXiv:1007.1727", u"Z = √q₀、阿西莫夫資料集", LS(43)),
            R(u"Read：Presentation of search results: the CLs technique", u"J. Phys. G 28, 2693 (2002)", u"CLs 方法", LS(46)),
            R(u"Gross, Vitells：Trial factors for the look elsewhere effect in high energy physics", u"Eur. Phys. J. C 70, 525 (2010)", u"全域顯著性的估計", LS(45)),
        ]),
        ("h", u"重建與機器學習"),
        ("t", [u"論文", u"出處", u"重點", u"課"], [
            R(u"Cacciari, Salam, Soyez：The anti-kt jet clustering algorithm", u"JHEP 04 (2008) 063；arXiv:0802.1189", u"LHC 的標準噴流演算法", LS(34)),
            R(u"CMS：Particle-flow reconstruction and global event description with the CMS detector", u"JINST 12, P10003 (2017)", u"粒子流", LS(33)),
            R(u"Metodiev, Nachman, Thaler：Classification without labels", u"JHEP 10 (2017) 174", u"CWoLa 弱監督學習", LS(52)),
        ]),
        ("h", u"歷史發現"),
        ("t", [u"論文", u"出處", u"重點", u"課"], [
            R(u"Aubert et al.（丁肇中團隊）：Experimental observation of a heavy particle J", u"Phys. Rev. Lett. 33, 1404 (1974)", u"J/ψ（BNL）", LS(9)),
            R(u"Augustin et al.（里克特團隊）：Discovery of a narrow resonance in e⁺e⁻ annihilation", u"Phys. Rev. Lett. 33, 1406 (1974)", u"J/ψ（SLAC）", LS(9)),
            R(u"UA1：Experimental observation of isolated large transverse energy electrons with associated missing energy", u"Phys. Lett. B 122, 103 (1983)", u"W 玻色子", LS(10)),
            R(u"CDF：Observation of top quark production in p̄p collisions", u"Phys. Rev. Lett. 74, 2626 (1995)", u"頂夸克", LS(11)),
            R(u"D0：Observation of the top quark", u"Phys. Rev. Lett. 74, 2632 (1995)", u"頂夸克", LS(11)),
            R(u"ALEPH、DELPHI、L3、OPAL、SLD：Precision electroweak measurements on the Z resonance", u"Phys. Rept. 427, 257 (2006)", u"N_ν = 2.984 ± 0.008", LS(12)),
        ]),
        ("h", u"其他"),
        ("t", [u"論文", u"出處", u"重點", u"課"], [
            R(u"LHCb：Test of lepton universality in b → sℓ⁺ℓ⁻ decays", u"arXiv:2212.09152、2212.09153", u"R_K 與標準模型一致", LS(59)),
        ]),
    ],
}

NUMBERS = {
    "file": "numbers.html", "title": u"LHC 關鍵數字", "h1": u"LHC 關鍵數字", "icon": u"🔢",
    "description": u"加速器、偵測器、資料與統計的常用數字",
    "body": [
        ("t", [u"項目", u"數值（約）", u"課"], [
            [u"周長", u"26.7 公里", LS(14)],
            [u"每束能量（Run 3）", u"6.8 TeV（質心 13.6 TeV）", LS(14)],
            [u"偶極磁鐵", u"1232 個，約 8 T，1.9 K", LS(17)],
            [u"繞行頻率", u"11,245 圈／秒", LS(4)],
            [u"粒子團間隔", u"25 奈秒（40 MHz）", LS(16)],
            [u"每團質子數", u"約 1～1.8 × 10¹¹", LS(4)],
            [u"對撞點的束流寬度", u"約 10～17 微米", LS(18)],
            [u"設計亮度", M(r"10^{34}\ \text{cm}^{-2}\text{s}^{-1}") + u"（Run 3 約兩倍）", LS(4)],
            [u"平均堆疊", u"Run 3 約 50～60", LS(20)],
            [u"非彈性截面（13 TeV）", u"約 80 mb", LS(4)],
            [u"希格斯產生截面（13 TeV）", u"約 55 pb", LS(4)],
            [u"觸發輸出", u"第一級約 10 萬次／秒；高階約 1000～數千次／秒", LS(28)],
            [u"CMS 磁場", u"3.8 T", LS(26)],
            [u"ATLAS 內部磁場", u"2 T", LS(26)],
            [u"希格斯質量", u"約 125.1 GeV", LS(57)],
            [u"H → γγ 分支比", u"約 0.23%", LS(54)],
            [u"H → ZZ* → 4ℓ 分支比", u"約 1.25 × 10⁻⁴", LS(55)],
        ]),
        ("h", u"統計"),
        ("t", [u"顯著性", u"單尾 p 值", u"意義"], [
            [u"3σ", u"1.35 × 10⁻³", u"證據"],
            [u"5σ", u"2.87 × 10⁻⁷", u"發現"],
        ]),
        ("h", u"單位"),
        ("t", [u"單位", u"換算"], [
            [u"1 b（邦）", M(r"10^{-24}\ \text{cm}^2")],
            [u"1 pb", M(r"10^{-36}\ \text{cm}^2")],
            [u"1 fb", M(r"10^{-39}\ \text{cm}^2")],
            [u"1 " + M(r"\text{fb}^{-1}"), M(r"10^{39}\ \text{cm}^{-2}")],
            [u"1 GeV", M(r"1.6\times10^{-10}") + u" 焦耳"],
        ]),
    ],
}

REFERENCES = [PAPERS, NUMBERS]
