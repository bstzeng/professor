# -*- coding: utf-8 -*-
"""重力波：參考頁——事件表、論文清單。"""
from gwv_common import LS, M


def mono(s):
    return u'<span style="font-family:ui-monospace,Menlo,monospace;font-size:0.9em">%s</span>' % s


EVENTS = {
    "file": "events.html", "title": u"重要事件表", "h1": u"重要的重力波事件", "icon": u"🌌",
    "description": u"從 GW150914 到 GW250114 的代表性事件",
    "body": [
        ("t", [u"事件", u"類型", u"質量（太陽質量，約）", u"距離（約）", u"意義", u"課"], [
            [u"GW150914", u"雙黑洞", u"36 + 29 → 62", u"410 Mpc", u"第一次直接偵測", LS(37)],
            [u"GW151226", u"雙黑洞", u"14 + 8", u"440 Mpc", u"第二個事件；較輕的黑洞", LS(41)],
            [u"GW170814", u"雙黑洞", u"31 + 25", u"540 Mpc", u"第一次三站偵測", LS(33)],
            [u"GW170817", u"雙中子星", u"1.46 + 1.27", u"40 Mpc", u"多信使天文學、千新星、重力波速度", LS(40)],
            [u"GW190521", u"雙黑洞", u"85 + 66 → 142", u"約 5 Gpc", u"質量缺口、中等質量黑洞", LS(42)],
            [u"GW200105、GW200115", u"黑洞—中子星", u"約 9 + 1.9、6 + 1.5", u"約 300 Mpc", u"第一批黑洞—中子星合併", LS(41)],
            [u"GW250114", u"雙黑洞", u"約 33 + 32", u"約 440 Mpc", u"高訊雜比；檢驗面積定理", LS(43)],
        ]),
        ("p", u"數值為論文中的中位數，四捨五入；詳細的誤差範圍請見原始論文與 GWOSC 事件目錄。"),
    ],
}

PAPERS = {
    "file": "papers.html", "title": u"論文清單", "h1": u"本課程引用的主要論文", "icon": u"📄",
    "description": u"重力波的發現論文與經典理論、方法論文",
    "body": [
        ("t", [u"論文", u"出處", u"課"], [
            [u"Hulse, Taylor：Discovery of a pulsar in a binary system", mono(u"ApJ 195, L51 (1975)"), LS(12)],
            [u"Weisberg, Taylor 等：脈衝星雙星的軌道衰減測量（系列論文）", mono(u"ApJ（1981～2016）"), LS(13)],
            [u"Pretorius：Evolution of binary black-hole spacetimes", mono(u"Phys. Rev. Lett. 95, 121101 (2005)"), LS(30)],
            [u"Allen：A χ² time-frequency discriminator for gravitational wave detection", mono(u"Phys. Rev. D 71, 062001 (2005)"), LS(31)],
            [u"LIGO–Virgo：Observation of Gravitational Waves from a Binary Black Hole Merger", mono(u"Phys. Rev. Lett. 116, 061102 (2016)；arXiv:1602.03837"), LS(38)],
            [u"LIGO–Virgo：GW170817: Observation of Gravitational Waves from a Binary Neutron Star Inspiral", mono(u"Phys. Rev. Lett. 119, 161101 (2017)"), LS(40)],
            [u"LIGO–Virgo 等：Multi-messenger Observations of a Binary Neutron Star Merger", mono(u"ApJL 848, L12 (2017)"), LS(40)],
            [u"LIGO–Virgo 等：A gravitational-wave standard siren measurement of the Hubble constant", mono(u"Nature 551, 85 (2017)"), LS(44)],
            [u"LIGO–Virgo：GW190521: A Binary Black Hole Merger with a Total Mass of 150 M⊙", mono(u"Phys. Rev. Lett. 125, 101102 (2020)"), LS(42)],
            [u"NANOGrav：The NANOGrav 15 yr Data Set: Evidence for a Gravitational-wave Background", mono(u"ApJL 951, L8 (2023)"), LS(45)],
            [u"Schutz：Determining the Hubble constant from gravitational wave observations", mono(u"Nature 323, 310 (1986)"), LS(44)],
        ]),
        ("p", u"LIGO 的資料與教學：重力波開放科學中心（gwosc.org）。"),
    ],
}

REFERENCES = [EVENTS, PAPERS]
