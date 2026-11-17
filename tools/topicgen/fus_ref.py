# -*- coding: utf-8 -*-
"""核融合：參考頁——公式與數字、設施與文獻。"""
from fus_common import LS, M


def mono(s):
    return u'<span style="font-family:ui-monospace,Menlo,monospace;font-size:0.9em">%s</span>' % s


NUMBERS = {
    "file": "numbers.html", "title": u"公式與設施", "h1": u"核融合的公式、數字與主要設施", "icon": u"🔢",
    "description": u"反應、點火條件與主要的融合裝置",
    "body": [
        ("h", u"公式與數字"),
        ("t", [u"名稱", u"公式／數值", u"課"], [
            [u"D-T 反應", M(r"\text{D} + \text{T}\to{}^4\text{He}\,(3.5) + n\,(14.1)") + u"（MeV）", LS(2)],
            [u"庫侖位能", M(r"U\approx 1.44\ \text{MeV\,fm}\cdot Z_1Z_2/r"), LS(3)],
            [u"穿隧機率", M(r"P\approx\exp(-\sqrt{E_G/E})"), LS(3)],
            [u"太陽 p-p 鏈", M(r"4p\to{}^4\text{He} + 2e^+ + 2\nu_e") + u"，26.7 MeV", LS(6)],
            [u"勞森判據", M(r"n\tau_E\ge 12T/(\langle\sigma v\rangle E_\alpha - 4C_B\sqrt T)"), LS(10)],
            [u"三重積", M(r"nT\tau_E\gtrsim 3\times10^{21}\ \text{keV\,s/m}^3"), LS(10)],
            [u"融合功率密度", M(r"\propto\beta^2B^4"), LS(30)],
            [u"氚增殖", M(r"{}^6\text{Li} + n\to\text{T} + {}^4\text{He} + 4.8\ \text{MeV}"), LS(28)],
        ]),
        ("h", u"主要設施"),
        ("t", [u"設施", u"地點", u"類型", u"重點", u"課"], [
            [u"T-3", u"蘇聯", u"托卡馬克", u"1968 年的突破", LS(16)],
            [u"TFTR", u"美國", u"托卡馬克", u"1994 年 10.7 MW", LS(17)],
            [u"JET", u"英國（歐洲）", u"托卡馬克", u"1997 年 Q≈0.67；2023 年 69 MJ", LS(17)],
            [u"ITER", u"法國", u"托卡馬克", u"目標 Q=10；2034 年研究運轉、2039 年 D-T", LS(19)],
            [u"W7-X", u"德國", u"仿星器", u"最佳化的磁場", LS(20)],
            [u"NIF", u"美國", u"雷射慣性約束", u"2022 年點火；2025 年 8.6 MJ", LS(24)],
            [u"EAST", u"中國", u"超導托卡馬克", u"2025 年 1066 秒 H 模式", LS(33)],
            [u"KSTAR", u"韓國", u"超導托卡馬克", u"約 1 億度 48 秒", LS(33)],
            [u"JT-60SA", u"日本", u"超導托卡馬克", u"2023 年第一個電漿", LS(33)],
            [u"SPARC", u"美國（CFS）", u"高溫超導托卡馬克", u"建造中，目標 Q>1", LS(30)],
        ]),
    ],
}

PAPERS = {
    "file": "papers.html", "title": u"文獻", "h1": u"核融合的重要文獻", "icon": u"📄",
    "description": u"從恆星能源到點火",
    "body": [
        ("t", [u"文獻", u"出處", u"課"], [
            [u"Gamow：Zur Quantentheorie des Atomkernes", mono(u"Z. Physik 51, 204 (1928)"), LS(3)],
            [u"Bethe：Energy Production in Stars", mono(u"Phys. Rev. 55, 434 (1939)"), LS(7)],
            [u"Lawson：Some Criteria for a Power Producing Thermonuclear Reactor", mono(u"Proc. Phys. Soc. B 70, 6 (1957)"), LS(10)],
            [u"Peacock 等：Measurement of the Electron Temperature by Thomson Scattering in Tokamak T3", mono(u"Nature 224, 488 (1969)"), LS(16)],
            [u"Nuckolls 等：Laser Compression of Matter to Super-High Densities", mono(u"Nature 239, 139 (1972)"), LS(22)],
            [u"Wagner 等：Regime of Improved Confinement and High Beta in Neutral-Beam-Heated Divertor Discharges of the ASDEX Tokamak", mono(u"Phys. Rev. Lett. 49, 1408 (1982)"), LS(18)],
            [u"Fleischmann, Pons：Electrochemically induced nuclear fusion of deuterium", mono(u"J. Electroanal. Chem. 261, 301 (1989)"), LS(35)],
            [u"Keilhacker 等：High fusion performance from deuterium-tritium plasmas in JET", mono(u"Nucl. Fusion 39, 209 (1999)"), LS(17)],
            [u"Klinger 等：Performance and properties of the first plasmas of Wendelstein 7-X", mono(u"Plasma Phys. Control. Fusion 59, 014018 (2017)"), LS(20)],
            [u"Creely 等：Overview of the SPARC tokamak", mono(u"J. Plasma Phys. 86, 865860502 (2020)"), LS(30)],
            [u"Abu-Shawareb 等（Indirect Drive ICF Collaboration）：Achievement of Target Gain Larger than Unity in an Inertial Fusion Experiment", mono(u"Phys. Rev. Lett. 132, 065102 (2024)"), LS(24)],
        ]),
    ],
}

REFERENCES = [NUMBERS, PAPERS]
