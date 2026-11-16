# -*- coding: utf-8 -*-
"""從哈伯到韋伯：參考頁——太空望遠鏡一覽、文獻。"""
from tel_common import LS, M


def mono(s):
    return u'<span style="font-family:ui-monospace,Menlo,monospace;font-size:0.9em">%s</span>' % s


SCOPES = {
    "file": "telescopes.html", "title": u"太空望遠鏡一覽", "h1": u"重要的太空望遠鏡", "icon": u"🛰️",
    "description": u"本課程提到的太空望遠鏡與規格",
    "body": [
        ("t", [u"望遠鏡", u"機構", u"運作", u"口徑", u"波段", u"課"], [
            [u"哈伯", u"NASA／ESA", u"1990～", u"2.4 m", u"紫外線～近紅外線", LS(7)],
            [u"康普頓伽瑪射線天文台", u"NASA", u"1991～2000", u"—", u"伽瑪射線", LS(19)],
            [u"錢德拉", u"NASA", u"1999～", u"1.2 m（掠射）", u"X 射線", LS(19)],
            [u"史匹哲", u"NASA", u"2003～2020", u"0.85 m", u"紅外線", LS(19)],
            [u"普朗克", u"ESA", u"2009～2013", u"1.5 m", u"微波", LS(20)],
            [u"克卜勒", u"NASA", u"2009～2018", u"0.95 m", u"可見光", LS(20)],
            [u"蓋亞", u"ESA", u"2013～2025", u"1.45×0.5 m", u"可見光", LS(20)],
            [u"TESS", u"NASA", u"2018～", u"4 × 0.1 m", u"可見光～近紅外線", LS(20)],
            [u"韋伯", u"NASA／ESA／CSA", u"2021～", u"6.5 m", u"0.6～28 μm", LS(22)],
            [u"歐幾里得", u"ESA", u"2023～", u"1.2 m", u"可見光～近紅外線", LS(38)],
            [u"羅曼", u"NASA", u"預計 2026～2027", u"2.4 m", u"近紅外線", LS(38)],
            [u"宜居世界天文台", u"NASA", u"規劃中（2040 年代）", u"約 6 m 以上", u"紫外線～近紅外線", LS(39)],
        ]),
        ("h", u"常用公式"),
        ("t", [u"名稱", u"公式", u"課"], [
            [u"繞射極限", M(r"\theta\approx 1.22\lambda/D"), LS(2)],
            [u"維恩定律", M(r"\lambda_{\max}T\approx 2900\ \mu\text{m}\,\text{K}"), LS(4)],
            [u"哈伯定律", M(r"v = H_0d"), LS(12)],
            [u"宇宙紅移", M(r"\lambda_{\text{obs}} = (1+z)\lambda_{\text{emit}}"), LS(22)],
        ]),
    ],
}

PAPERS = {
    "file": "papers.html", "title": u"文獻", "h1": u"太空望遠鏡的重要文獻", "icon": u"📄",
    "description": u"從史匹哲的報告到韋伯的發現",
    "body": [
        ("t", [u"文獻", u"出處", u"課"], [
            [u"Spitzer：Astronomical Advantages of an Extra-Terrestrial Observatory", mono(u"RAND 報告 (1946)"), LS(6)],
            [u"Hubble：A Relation between Distance and Radial Velocity among Extra-Galactic Nebulae", mono(u"PNAS 15, 168 (1929)"), LS(12)],
            [u"Allen 等：The Hubble Space Telescope Optical Systems Failure Report", mono(u"NASA (1990)"), LS(8)],
            [u"Williams 等：The Hubble Deep Field", mono(u"AJ 112, 1335 (1996)"), LS(13)],
            [u"Riess 等：Observational Evidence from Supernovae for an Accelerating Universe", mono(u"AJ 116, 1009 (1998)"), LS(14)],
            [u"Perlmutter 等：Measurements of Ω and Λ from 42 High-Redshift Supernovae", mono(u"ApJ 517, 565 (1999)"), LS(14)],
            [u"Ferrarese, Merritt：A Fundamental Relation between Supermassive Black Holes and Their Host Galaxies", mono(u"ApJ 539, L9 (2000)"), LS(17)],
            [u"Freedman 等：Final Results from the Hubble Space Telescope Key Project", mono(u"ApJ 553, 47 (2001)"), LS(12)],
            [u"Gardner 等：The James Webb Space Telescope Mission", mono(u"PASP 135, 068001 (2023)"), LS(22)],
            [u"Rigby 等：The Science Performance of JWST as Characterized in Commissioning", mono(u"PASP 135, 048001 (2023)"), LS(30)],
            [u"Labbé 等：A population of red candidate massive galaxies ~600 Myr after the Big Bang", mono(u"Nature 616, 266 (2023)"), LS(33)],
            [u"Carniani 等：Spectroscopic confirmation of two luminous galaxies at a redshift of 14", mono(u"Nature 633, 318 (2024)"), LS(33)],
            [u"Riess 等：JWST Observations Reject Unrecognized Crowding of Cepheid Photometry as an Explanation for the Hubble Tension", mono(u"ApJL 962, L17 (2024)"), LS(35)],
            [u"Matthee 等：Little Red Dots: An Abundant Population of Faint Active Galactic Nuclei at z ~ 5 Revealed by the EIGER and FRESCO JWST Surveys", mono(u"ApJ 963, 129 (2024)"), LS(36)],
        ]),
    ],
}

REFERENCES = [SCOPES, PAPERS]
