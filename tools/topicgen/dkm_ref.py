# -*- coding: utf-8 -*-
"""暗物質與暗能量：參考頁——關鍵數字、論文清單。"""
from dkm_common import LS, M


def mono(s):
    return u'<span style="font-family:ui-monospace,Menlo,monospace;font-size:0.9em">%s</span>' % s


NUMBERS = {
    "file": "numbers.html", "title": u"關鍵數字", "h1": u"宇宙學的關鍵數字", "icon": u"🔢",
    "description": u"宇宙組成、哈伯常數與暗物質的常用數字",
    "body": [
        ("t", [u"量", u"數值（約）", u"課"], [
            [u"普通物質（重子）", u"4.9%", LS(1)],
            [u"暗物質", u"26.5%", LS(1)],
            [u"暗能量", u"68.5%", LS(1)],
            [u"太陽附近的暗物質密度", u"0.3 GeV/cm³", LS(4)],
            [u"銀河系的旋轉速度（太陽附近）", u"約 220～230 km/s", LS(3)],
            [u"MOND 加速度 a₀", M(r"1.2\times10^{-10}\ \text{m/s}^2"), LS(16)],
            [u"WIMP 奇蹟所需的湮滅截面", M(r"3\times10^{-26}\ \text{cm}^3/\text{s}"), LS(13)],
            [u"重子聲學振盪的尺度", u"約 150 Mpc", LS(36)],
            [u"哈伯常數（普朗克）", u"67.4 ± 0.5 km/s/Mpc", LS(38)],
            [u"哈伯常數（SH0ES）", u"73.0 ± 1.0 km/s/Mpc", LS(38)],
            [u"宇宙年齡", u"約 138 億年", LS(8)],
            [u"宇宙微波背景溫度", u"2.725 K", LS(8)],
        ]),
    ],
}

PAPERS = {
    "file": "papers.html", "title": u"論文清單", "h1": u"本課程引用的主要論文", "icon": u"📄",
    "description": u"暗物質與暗能量的重要原始論文",
    "body": [
        ("t", [u"論文", u"出處", u"課"], [
            [u"Zwicky：Die Rotverschiebung von extragalaktischen Nebeln", mono(u"Helv. Phys. Acta 6, 110 (1933)"), LS(2)],
            [u"Rubin, Ford：Rotation of the Andromeda Nebula from a Spectroscopic Survey of Emission Regions", mono(u"ApJ 159, 379 (1970)"), LS(3)],
            [u"Ostriker, Peebles：A Numerical Study of the Stability of Flattened Galaxies", mono(u"ApJ 186, 467 (1973)"), LS(5)],
            [u"Peccei, Quinn：CP Conservation in the Presence of Pseudoparticles", mono(u"Phys. Rev. Lett. 38, 1440 (1977)"), LS(14)],
            [u"Milgrom：A modification of the Newtonian dynamics", mono(u"ApJ 270, 365 (1983)"), LS(16)],
            [u"Clowe 等：A Direct Empirical Proof of the Existence of Dark Matter", mono(u"ApJ 648, L109 (2006)"), LS(7)],
            [u"Riess 等：Observational Evidence from Supernovae for an Accelerating Universe", mono(u"AJ 116, 1009 (1998)"), LS(30)],
            [u"Perlmutter 等：Measurements of Ω and Λ from 42 High-Redshift Supernovae", mono(u"ApJ 517, 565 (1999)"), LS(30)],
            [u"Eisenstein 等：Detection of the Baryon Acoustic Peak in the Large-Scale Correlation Function of SDSS Luminous Red Galaxies", mono(u"ApJ 633, 560 (2005)"), LS(36)],
            [u"Planck Collaboration：Planck 2018 results. VI. Cosmological parameters", mono(u"A&A 641, A6 (2020)"), LS(8)],
            [u"DESI Collaboration：DESI 2024 VI: Cosmological Constraints from the Measurements of Baryon Acoustic Oscillations", mono(u"JCAP 02 (2025) 021"), LS(39)],
        ]),
    ],
}

REFERENCES = [NUMBERS, PAPERS]
