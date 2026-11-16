# -*- coding: utf-8 -*-
"""黑洞：參考頁——關鍵數字、論文。"""
from bhl_common import LS, M


def mono(s):
    return u'<span style="font-family:ui-monospace,Menlo,monospace;font-size:0.9em">%s</span>' % s


NUMBERS = {
    "file": "numbers.html", "title": u"公式與數字", "h1": u"黑洞的公式與關鍵數字", "icon": u"🔢",
    "description": u"史瓦西半徑、ISCO、霍金溫度等常用公式與數字",
    "body": [
        ("t", [u"量", u"公式／數值", u"課"], [
            [u"史瓦西半徑", M(r"r_s = 2GM/c^2\approx 2.95\ \text{km}\times M/M_\odot"), LS(1)],
            [u"時間膨脹", M(r"d\tau = \sqrt{1 - r_s/r}\,dt"), LS(7)],
            [u"光子球", M(r"r = 1.5\,r_s"), LS(8)],
            [u"陰影（衝擊參數）", M(r"b_c = 3\sqrt3\,GM/c^2\approx 2.6\,r_s"), LS(8)],
            [u"ISCO（不旋轉）", M(r"r = 3\,r_s"), LS(8)],
            [u"錢德拉塞卡極限", u"約 1.4 倍太陽質量", LS(10)],
            [u"中子星最大質量", u"約 2.2～2.3 倍太陽質量", LS(11)],
            [u"吸積效率", u"5.7%（不旋轉）～42%（最大自旋）", LS(20)],
            [u"愛丁頓光度", M(r"L_{\text{Edd}}\approx 1.3\times10^{31}\ \text{W}\times M/M_\odot"), LS(20)],
            [u"人馬座 A*", u"約 430 萬倍太陽質量，距離約 2.7 萬光年", LS(23)],
            [u"M87*", u"約 65 億倍太陽質量，距離約 5500 萬光年，環約 42 微角秒", LS(29)],
            [u"霍金溫度", M(r"T_H = \hbar c^3/(8\pi GMk_B)\approx 6\times10^{-8}\ \text{K}\times M_\odot/M"), LS(36)],
            [u"貝肯斯坦—霍金熵", M(r"S = k_BA/4\ell_P^2"), LS(38)],
        ]),
    ],
}

PAPERS = {
    "file": "papers.html", "title": u"論文清單", "h1": u"黑洞研究的重要論文", "icon": u"📄",
    "description": u"從米歇爾到事件視界望遠鏡",
    "body": [
        ("t", [u"論文", u"出處", u"課"], [
            [u"Michell：On the Means of Discovering the Distance, Magnitude, &c. of the Fixed Stars", mono(u"Phil. Trans. R. Soc. 74, 35 (1784)"), LS(2)],
            [u"Schwarzschild：Über das Gravitationsfeld eines Massenpunktes nach der Einsteinschen Theorie", mono(u"Sitzungsber. Preuss. Akad. Wiss. (1916)"), LS(5)],
            [u"Chandrasekhar：The Maximum Mass of Ideal White Dwarfs", mono(u"ApJ 74, 81 (1931)"), LS(10)],
            [u"Oppenheimer, Volkoff：On Massive Neutron Cores", mono(u"Phys. Rev. 55, 374 (1939)"), LS(11)],
            [u"Oppenheimer, Snyder：On Continued Gravitational Contraction", mono(u"Phys. Rev. 56, 455 (1939)"), LS(13)],
            [u"Kerr：Gravitational Field of a Spinning Mass as an Example of Algebraically Special Metrics", mono(u"Phys. Rev. Lett. 11, 237 (1963)"), LS(15)],
            [u"Schmidt：3C 273: A Star-Like Object with Large Red-Shift", mono(u"Nature 197, 1040 (1963)"), LS(21)],
            [u"Penrose：Gravitational Collapse and Space-Time Singularities", mono(u"Phys. Rev. Lett. 14, 57 (1965)"), LS(6)],
            [u"Hewish, Bell 等：Observation of a Rapidly Pulsating Radio Source", mono(u"Nature 217, 709 (1968)"), LS(11)],
            [u"Bekenstein：Black Holes and Entropy", mono(u"Phys. Rev. D 7, 2333 (1973)"), LS(38)],
            [u"Bardeen, Carter, Hawking：The Four Laws of Black Hole Mechanics", mono(u"Commun. Math. Phys. 31, 161 (1973)"), LS(37)],
            [u"Hawking：Black hole explosions?", mono(u"Nature 248, 30 (1974)"), LS(36)],
            [u"Blandford, Znajek：Electromagnetic extraction of energy from Kerr black holes", mono(u"MNRAS 179, 433 (1977)"), LS(16)],
            [u"Page：Information in Black Hole Radiation", mono(u"Phys. Rev. Lett. 71, 3743 (1993)"), LS(39)],
            [u"Maldacena：The Large N Limit of Superconformal Field Theories and Supergravity", mono(u"Adv. Theor. Math. Phys. 2, 231 (1998)"), LS(40)],
            [u"LIGO/Virgo：Observation of Gravitational Waves from a Binary Black Hole Merger", mono(u"Phys. Rev. Lett. 116, 061102 (2016)"), LS(32)],
            [u"James, von Tunzelmann, Franklin, Thorne：Gravitational lensing by spinning black holes in astrophysics, and in the movie Interstellar", mono(u"Class. Quantum Grav. 32, 065001 (2015)"), LS(44)],
            [u"EHT Collaboration：First M87 Event Horizon Telescope Results. I.", mono(u"ApJL 875, L1 (2019)"), LS(29)],
            [u"Penington：Entanglement Wedge Reconstruction and the Information Paradox", mono(u"JHEP 09 (2020) 002"), LS(39)],
            [u"GRAVITY Collaboration：Detection of the Schwarzschild precession in the orbit of the star S2", mono(u"A&A 636, L5 (2020)"), LS(23)],
            [u"EHT Collaboration：First Sagittarius A* Event Horizon Telescope Results. I.", mono(u"ApJL 930, L12 (2022)"), LS(30)],
            [u"Bogdán 等：Evidence for heavy-seed origin of early supermassive black holes from a z ≈ 10 X-ray quasar", mono(u"Nat. Astron. 8, 126 (2024)"), LS(45)],
            [u"Häberle 等：Fast-moving stars around an intermediate-mass black hole in ω Centauri", mono(u"Nature 631, 285 (2024)"), LS(34)],
        ]),
    ],
}

REFERENCES = [NUMBERS, PAPERS]
