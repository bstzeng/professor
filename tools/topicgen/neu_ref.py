# -*- coding: utf-8 -*-
"""微中子：參考頁——實驗總表、論文清單。"""
from neu_common import LS, M


def mono(s):
    return u'<span style="font-family:ui-monospace,Menlo,monospace;font-size:0.9em">%s</span>' % s


EXPS = {
    "file": "experiments.html", "title": u"實驗總表", "h1": u"重要的微中子實驗", "icon": u"🔭",
    "description": u"從薩凡納河到 JUNO：地點、技術與主要成果",
    "body": [
        ("t", [u"實驗", u"年代", u"地點", u"技術", u"主要成果", u"課"], [
            [u"柯溫—萊因斯", u"1956", u"美國薩凡納河", u"反應爐＋液態閃爍體", u"第一次偵測微中子", LS(6)],
            [u"布魯克黑文 AGS", u"1962", u"美國", u"加速器＋火花室", u"緲子微中子", LS(7)],
            [u"霍姆斯特克", u"1968～1994", u"美國南達科他", u"氯（放射化學）", u"太陽微中子不足", LS(11)],
            [u"Kamiokande", u"1983～1996", u"日本神岡", u"水契忍可夫", u"太陽方向、超新星 1987A", LS(13)],
            [u"GALLEX／SAGE", u"1990 年代", u"義大利／俄國", u"鎵", u"pp 微中子", LS(13)],
            [u"超級神岡", u"1996～", u"日本神岡", u"水契忍可夫（5 萬噸）", u"大氣微中子振盪", LS(16)],
            [u"SNO", u"1999～2006", u"加拿大", u"重水", u"中性流：太陽微中子問題的解答", LS(17)],
            [u"KamLAND", u"2002～", u"日本神岡", u"液態閃爍體", u"反應爐振盪、地球微中子", LS(27)],
            [u"DONUT", u"2000", u"美國費米實驗室", u"核子乳膠", u"陶子微中子", LS(8)],
            [u"Borexino", u"2007～2021", u"義大利格蘭薩索", u"液態閃爍體", u"各種太陽微中子、CNO", LS(22)],
            [u"冰立方", u"2010～", u"南極", u"冰中的契忍可夫", u"宇宙高能微中子", LS(33)],
            [u"大亞灣", u"2011～2020", u"中國廣東", u"摻釓閃爍體", u"θ₁₃", LS(27)],
            [u"T2K", u"2010～", u"日本", u"加速器→超級神岡", u"電子微中子出現、CP", LS(28)],
            [u"NOvA", u"2014～", u"美國", u"加速器→明尼蘇達", u"質量順序、CP", LS(28)],
            [u"KATRIN", u"2019～", u"德國", u"氚貝他衰變終點", u"質量上限 0.45 eV", LS(37)],
            [u"JUNO", u"2025～", u"中國廣東", u"液態閃爍體（2 萬噸）", u"質量順序、精確參數", LS(44)],
        ]),
    ],
}

PAPERS = {
    "file": "papers.html", "title": u"論文清單", "h1": u"本課程引用的主要論文", "icon": u"📄",
    "description": u"微中子物理的重要原始論文",
    "body": [
        ("t", [u"論文", u"出處", u"課"], [
            [u"Cowan, Reines 等：Detection of the Free Neutrino: a Confirmation", mono(u"Science 124, 103 (1956)"), LS(6)],
            [u"Danby 等：Observation of High-Energy Neutrino Reactions and the Existence of Two Kinds of Neutrinos", mono(u"Phys. Rev. Lett. 9, 36 (1962)"), LS(7)],
            [u"Davis 等：Search for Neutrinos from the Sun", mono(u"Phys. Rev. Lett. 20, 1205 (1968)"), LS(11)],
            [u"Super-Kamiokande：Evidence for oscillation of atmospheric neutrinos", mono(u"Phys. Rev. Lett. 81, 1562 (1998)"), LS(16)],
            [u"SNO：Direct evidence for neutrino flavor transformation from neutral-current interactions", mono(u"Phys. Rev. Lett. 89, 011301 (2002)"), LS(17)],
            [u"KamLAND：First results from KamLAND: evidence for reactor antineutrino disappearance", mono(u"Phys. Rev. Lett. 90, 021802 (2003)"), LS(27)],
            [u"Daya Bay：Observation of electron-antineutrino disappearance at Daya Bay", mono(u"Phys. Rev. Lett. 108, 171803 (2012)"), LS(27)],
            [u"T2K：Constraint on the matter–antimatter symmetry-violating phase in neutrino oscillations", mono(u"Nature 580, 339 (2020)"), LS(30)],
            [u"IceCube 等：Multimessenger observations of a flaring blazar coincident with high-energy neutrino IceCube-170922A", mono(u"Science 361, eaat1378 (2018)"), LS(34)],
            [u"Feldman, Cousins：A unified approach to the classical statistical analysis of small signals", mono(u"Phys. Rev. D 57, 3873 (1998)"), LS(25)],
            [u"KamLAND：Experimental investigation of geologically produced antineutrinos with KamLAND", mono(u"Nature 436, 499 (2005)"), LS(35)],
        ]),
    ],
}

REFERENCES = [EXPS, PAPERS]
