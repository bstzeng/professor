# -*- coding: utf-8 -*-
"""半導體元件物理：參考頁——互動工具箱、公式與常數速查。"""
from dp_common import LS, DPLIB, dpw

GUIDE = {
    "file": "guide.html", "title": u"元件物理工具箱", "h1": u"元件物理工具箱", "icon": u"🧪",
    "description": u"能帶圖、費米分布、載子對溫度、PN 接面、二極體、MOS 電容、MOSFET、CMOS 反相器、太陽能電池",
    "body": [
        ("raw", u"<script>%s</script>" % DPLIB),
        ("p", u"所有工具都在瀏覽器中即時計算，使用教科書等級的解析模型。"),
        ("h", u"1. 能帶圖與費米能階（第 12、13 課）"), dpw({"t": "band"}),
        ("h", u"2. 費米—狄拉克分布（第 11 課）"), dpw({"t": "fd"}),
        ("h", u"3. 載子濃度對溫度（第 14 課）"), dpw({"t": "cart"}),
        ("h", u"4. PN 接面（第 19～21 課）"), dpw({"t": "pn"}),
        ("h", u"5. 二極體 I–V（第 22、23 課）"), dpw({"t": "diode"}),
        ("h", u"6. MOS 電容與 C–V（第 33～35 課）"), dpw({"t": "mos"}),
        ("h", u"7. MOSFET（第 36～38 課）"), dpw({"t": "fet"}),
        ("h", u"8. CMOS 反相器（第 41 課）"), dpw({"t": "inv"}),
        ("h", u"9. 太陽能電池（第 46 課）"), dpw({"t": "solar"}),
    ],
}

GLOSSARY = {
    "file": "glossary.html", "title": u"公式與常數速查", "h1": u"公式與常數速查", "icon": u"📖",
    "description": u"常用常數、矽的參數與主要公式",
    "body": [
        ("h", u"常數與矽的參數（300 K）"),
        ("t", [u"量", u"數值"],
         [[u"kT/q", u"25.9 mV"], [u"能隙 E_g", u"1.12 eV"], [u"本質濃度 n_i", u"約 1.0×10¹⁰ cm⁻³"], [u"N_c／N_v", u"約 2.9×10¹⁹／2.7×10¹⁹ cm⁻³"],
          [u"介電常數 ε_Si／ε_SiO₂", u"11.7 ε₀／3.9 ε₀"], [u"電子親和力 χ", u"4.05 eV"], [u"μ_n／μ_p（輕摻雜）", u"約 1400／450 cm²/V·s"], [u"飽和速度", u"約 10⁷ cm/s"], [u"臨界電場", u"約 3×10⁵ V/cm"]]),
        ("h", u"主要公式"),
        ("t", [u"名稱", u"公式", u"課"],
         [[u"質量作用定律", u"np = n_i²", LS(12)], [u"載子濃度", u"n = n_i e^{(E_F−E_i)/kT}", LS(12)], [u"導電率", u"σ = q(nμ_n + pμ_p)", LS(1)], [u"愛因斯坦關係", u"D/μ = kT/q", LS(16)],
          [u"擴散長度", u"L = √(Dτ)", LS(18)], [u"內建電位", u"V_bi = (kT/q) ln(N_aN_d/n_i²)", LS(19)], [u"空乏寬度", u"W = √[2ε(V_bi−V)/q · (1/N_a+1/N_d)]", LS(21)],
          [u"二極體", u"J = J_s(e^{qV/kT} − 1)", LS(22)], [u"雪崩崩潰", u"V_BR ≈ εE_crit²/2qN_B", LS(24)], [u"熱離子發射", u"J = A**T² e^{−qφ_B/kT}(e^{qV/nkT} − 1)", LS(26)],
          [u"BJT 集極電流", u"I_C = qAD_nn_i²/(N_BW_B) · e^{qV_BE/kT}", LS(29)], [u"臨界電壓", u"V_T = V_FB + 2φ_F + √(2εqN_a2φ_F)/C_ox", LS(35)],
          [u"MOSFET 飽和", u"I_D = (μC_ox/2)(W/L)(V_GS−V_T)²", LS(36)], [u"次臨界擺幅", u"S = n(kT/q) ln10", LS(37)], [u"動態功耗", u"P = αCV²f", LS(41)],
          [u"開路電壓", u"V_oc = (kT/q) ln(J_sc/J_0 + 1)", LS(46)], [u"功率元件極限", u"R_on,sp = 4V_BR²/(εμE_crit³)", LS(50)]]),
    ],
}

REFERENCES = [GUIDE, GLOSSARY]
