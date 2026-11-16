# -*- coding: utf-8 -*-
"""系外行星：參考頁——公式與著名行星、論文。"""
from exo_common import LS, M


def mono(s):
    return u'<span style="font-family:ui-monospace,Menlo,monospace;font-size:0.9em">%s</span>' % s


PLANETS = {
    "file": "planets.html", "title": u"公式與著名行星", "h1": u"系外行星的公式與著名行星", "icon": u"🪐",
    "description": u"常用公式，以及本課程提到的著名行星",
    "body": [
        ("h", u"公式"),
        ("t", [u"名稱", u"公式", u"課"], [
            [u"徑向速度振幅", M(r"K = (2\pi G/P)^{1/3}\,m_p\sin i\,/\,M_*^{2/3}"), LS(4)],
            [u"都卜勒位移", M(r"\Delta\lambda/\lambda = v/c"), LS(4)],
            [u"凌日深度", M(r"\delta\approx(R_p/R_*)^2"), LS(10)],
            [u"凌日機率", M(r"\approx R_*/a"), LS(10)],
            [u"大氣標高", M(r"H = k_BT/(\mu m_Hg)"), LS(27)],
            [u"平衡溫度", M(r"T_{\text{eq}} = [(1-A)L_*/(16\pi\sigma a^2)]^{1/4}"), LS(32)],
            [u"德雷克方程式", M(r"N = R_*f_pn_ef_lf_if_cL"), LS(43)],
        ]),
        ("h", u"著名行星"),
        ("t", [u"行星", u"特色", u"課"], [
            [u"PSR B1257+12 b、c、d", u"第一批確認的系外行星，繞脈衝星（1992）", LS(16)],
            [u"飛馬座 51 b", u"第一顆類太陽恆星的行星、第一顆熱木星（1995）", LS(6)],
            [u"HD 209458 b", u"第一次凌日（1999）、第一次大氣偵測（2001）", LS(10)],
            [u"HR 8799 b～e", u"直接拍到的四顆巨行星（2008）", LS(18)],
            [u"克卜勒 16b", u"環繞雙星的行星", LS(11)],
            [u"克卜勒 186f", u"第一顆可居住帶中的地球大小行星（2014）", LS(11)],
            [u"克卜勒 90i", u"機器學習發現，讓克卜勒 90 有八顆行星", LS(38)],
            [u"比鄰星 b", u"最近的系外行星，約 4.24 光年", LS(24)],
            [u"TRAPPIST-1 b～h", u"七顆地球大小的行星", LS(23)],
            [u"WASP-39b", u"韋伯偵測到二氧化碳與二氧化硫", LS(28)],
            [u"K2-18b", u"甲烷、二氧化碳與二甲基硫的爭議", LS(29)],
            [u"HD 189733 b", u"第一張系外行星溫度地圖", LS(30)],
        ]),
    ],
}

PAPERS = {
    "file": "papers.html", "title": u"論文清單", "h1": u"系外行星的重要論文", "icon": u"📄",
    "description": u"從脈衝星行星到韋伯望遠鏡",
    "body": [
        ("t", [u"論文", u"出處", u"課"], [
            [u"Wolszczan, Frail：A planetary system around the millisecond pulsar PSR1257 + 12", mono(u"Nature 355, 145 (1992)"), LS(16)],
            [u"Mayor, Queloz：A Jupiter-mass companion to a solar-type star", mono(u"Nature 378, 355 (1995)"), LS(6)],
            [u"Charbonneau 等：Detection of Planetary Transits Across a Sun-like Star", mono(u"ApJ 529, L45 (2000)"), LS(10)],
            [u"Charbonneau 等：Detection of an Extrasolar Planet Atmosphere", mono(u"ApJ 568, 377 (2002)"), LS(27)],
            [u"Kovács, Zucker, Mazeh：A box-fitting algorithm in the search for periodic transits", mono(u"A&A 391, 369 (2002)"), LS(36)],
            [u"Knutson 等：A map of the day–night contrast of the extrasolar planet HD 189733b", mono(u"Nature 447, 183 (2007)"), LS(30)],
            [u"Marois 等：Direct Imaging of Multiple Planets Orbiting the Star HR 8799", mono(u"Science 322, 1348 (2008)"), LS(18)],
            [u"Borucki 等：Kepler Planet-Detection Mission: Introduction and First Results", mono(u"Science 327, 977 (2010)"), LS(11)],
            [u"Kopparapu 等：Habitable Zones around Main-sequence Stars: Dependence on Planetary Mass", mono(u"ApJL 787, L29 (2014)"), LS(32)],
            [u"Anglada-Escudé 等：A terrestrial planet candidate in a temperate orbit around Proxima Centauri", mono(u"Nature 536, 437 (2016)"), LS(24)],
            [u"Gillon 等：Seven temperate terrestrial planets around the nearby ultracool dwarf star TRAPPIST-1", mono(u"Nature 542, 456 (2017)"), LS(23)],
            [u"Fulton 等：The California-Kepler Survey. III. A Gap in the Radius Distribution of Small Planets", mono(u"AJ 154, 109 (2017)"), LS(22)],
            [u"Shallue, Vanderburg：Identifying Exoplanets with Deep Learning", mono(u"AJ 155, 94 (2018)"), LS(38)],
            [u"JWST Transiting Exoplanet Community ERS Team：Identification of carbon dioxide in an exoplanet atmosphere", mono(u"Nature 614, 649 (2023)"), LS(28)],
            [u"Tsai 等：Photochemically produced SO2 in the atmosphere of WASP-39b", mono(u"Nature 617, 483 (2023)"), LS(28)],
            [u"Madhusudhan 等：Carbon-bearing Molecules in a Possible Hycean Atmosphere", mono(u"ApJL 956, L13 (2023)"), LS(29)],
        ]),
    ],
}

REFERENCES = [PLANETS, PAPERS]
