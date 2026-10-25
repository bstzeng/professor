# -*- coding: utf-8 -*-
"""材料老化與結構安全檢查：參考頁——互動工具箱、公式速查。"""
from ins_common import *

GUIDE = {
    "file": "guide.html", "title": u"老化與檢查互動工具箱", "h1": u"老化與檢查互動工具箱", "icon": u"🔩",
    "description": u"疲勞、裂紋成長與檢查間隔、超音波、POD、氯離子、橋樑評等、裂縫判讀、振動監測、FRP 補強、檢查最佳化",
    "body": [
        ("raw", u"<script>%s</script>" % INLIB),
        ("p", u"所有工具都是教學用的簡化模型，數值為代表性的量級。"),
        ("h", u"1. S-N 曲線與 Miner 累積損傷（" + LS(2) + u"、" + LS(8) + u"）"), iw("sn"),
        ("h", u"2. 裂紋成長與檢查間隔（" + LS(10) + u"、" + LS(25) + u"）"), iw("crack"),
        ("h", u"3. 超音波 A 掃描（" + LS(17) + u"）"), iw("ut"),
        ("h", u"4. 偵測機率 POD（" + LS(20) + u"）"), iw("pod"),
        ("h", u"5. 氯離子擴散與碳化（" + LS(6) + u"、" + LS(32) + u"）"), iw("chloride"),
        ("h", u"6. 橋樑狀況評等（" + LS(31) + u"）"), iw("nbi"),
        ("h", u"7. 裂縫型態判讀（" + LS(41) + u"）"), iw("crackid"),
        ("h", u"8. 振動頻率與損傷（" + LS(62) + u"）"), iw("modal"),
        ("h", u"9. FRP 貼梁補強（" + LS(57) + u"）"), iw("frp"),
        ("h", u"10. 檢查間隔最佳化（" + LS(66) + u"）"), iw("risk"),
    ],
}

GLOSSARY = {
    "file": "glossary.html", "title": u"老化與檢查公式速查", "h1": u"老化與檢查公式速查", "icon": u"📖",
    "description": u"本課程的關鍵公式與名詞",
    "body": [
        ("raw", KATEX),
        ("h", u"1. 關鍵公式"),
        ("t", [u"公式", u"意思", u"課"],
         [[M(r"\sigma_f=\sqrt{2E\gamma_s/(\pi a)}"), u"Griffith 破裂應力", LS(1)], [M(r"S_a=\sigma_f'(2N)^b"), u"Basquin S-N 曲線", LS(2)],
          [M(r"CR=\frac{iM}{nF\rho}"), u"腐蝕速率", LS(3)], [M(r"\mathrm{LMP}=T(C+\log t_r)"), u"Larson–Miller 參數", LS(5)],
          [M(r"x_c=k\sqrt t"), u"碳化深度", LS(6)], [M(r"D=\sum n_i/N_i"), u"Miner 法則", LS(8)],
          [M(r"K=Y\sigma\sqrt{\pi a}"), u"應力強度因子", LS(9)], [M(r"da/dN=C(\Delta K)^m"), u"Paris 定律", LS(10)],
          [M(r"AF=e^{\frac{E_a}{R}(\frac1{T_u}-\frac1{T_t})}"), u"Arrhenius 加速因子", LS(11)], [M(r"F=1-e^{-(N/\eta)^\beta}"), u"Weibull 分佈", LS(13)],
          [M(r"\delta=1/\sqrt{\pi f\mu\sigma}"), u"渦電流集膚深度", LS(16)], [M(r"R=(\frac{Z_2-Z_1}{Z_2+Z_1})^2"), u"超音波反射率", LS(17)],
          [M(r"I=I_0e^{-\mu x}"), u"射線衰減", LS(18)], [M(r"a_{90}=a_{50}9^\sigma"), u"POD", LS(20)],
          [M(r"\sigma_\theta=pr/t"), u"薄壁環向應力", LS(23)], [M(r"\Delta N=N(a_d\to a_c)/k"), u"檢查間隔", LS(25)],
          [M(r"C=C_s[1-\mathrm{erf}(\frac{x}{2\sqrt{Dt}})]"), u"氯離子擴散", LS(32)], [M(r"N=A/\Delta\sigma^3"), u"銲接細節疲勞", LS(33)],
          [M(r"i_{corr}=B/R_p"), u"Stern–Geary", LS(36)], [M(r"RF=\frac{C-\gamma_DD}{\gamma_L(L+I)}"), u"載重評級因子", LS(37)],
          [M(r"\beta=\delta/L"), u"角變位", LS(42)], [M(r"\Delta RT_{NDT}=CF\,f^{0.28-0.1\log f}"), u"中子脆化", LS(46)],
          [M(r"\sigma_{max}=2K/\sqrt{\pi\rho}"), u"止裂孔", LS(52)], [M(r"f_{cc}'=f_c'+3.3\psi_f f_l"), u"FRP 圍束", LS(58)],
          [M(r"\Delta f_n/f_n\approx-\delta\frac{\ell}{L}\sin^2\frac{n\pi x}{L}"), u"頻率與損傷", LS(62)], [M(r"\beta=\frac{\mu_R-\mu_S}{\sqrt{\sigma_R^2+\sigma_S^2}}"), u"可靠度指標", LS(65)],
          [M(r"T^*=\eta[\frac{C_i}{(\beta-1)C_f}]^{1/\beta}"), u"最佳檢查間隔", LS(66)]]),
        ("h", u"2. 名詞"),
        ("t", [u"名詞", u"說明", u"課"],
         [[u"疲勞", u"反覆受力下裂紋萌生與成長", LS(2)], [u"應力腐蝕（SCC）", u"敏感材料＋環境＋拉應力", LS(4)], [u"潛變", u"高溫下隨時間的變形", LS(5)],
          [u"破壞韌性 K_IC", u"裂紋失穩的應力強度因子", LS(9)], [u"疲勞條紋", u"斷口上每次循環留下的細紋", LS(12)], [u"NDT", u"非破壞檢測", LS(14)],
          [u"POD", u"偵測機率", LS(20)], [u"損傷容限", u"假設有缺陷，用檢查在臨界前發現", LS(22)], [u"MSD／WFD", u"多處損傷／廣泛疲勞損傷", LS(27)],
          [u"LOV", u"有效壽命上限", LS(27)], [u"BVID", u"幾乎看不見的衝擊損傷", LS(28)], [u"壽命限制件", u"引擎碟片等依循環數更換的零件", LS(29)],
          [u"D.E.R.&U.", u"劣化程度、範圍、影響、急迫性評估法", LS(31)], [u"斷裂關鍵構件", u"沒有冗餘的受拉構件", LS(33)], [u"沖刷", u"基礎周圍河床被水掏空", LS(34)],
          [u"半電池電位", u"判斷鋼筋鏽蝕機率的電位量測", LS(36)], [u"軟弱層", u"勁度明顯較低、變形集中的樓層", LS(43)], [u"洩漏先於破裂", u"裂紋穿透時仍遠小於臨界長度", LS(45)],
          [u"RBI", u"風險基礎檢查", LS(48)], [u"SRM", u"結構修理手冊", LS(51)], [u"斜接修補", u"複材磨成緩斜面逐層修補", LS(53)], [u"陰極防蝕", u"讓鋼筋成為陰極以停止腐蝕", LS(54)],
          [u"外加預力", u"梁外加鋼腱施加壓力", LS(56)], [u"圍束", u"包覆限制側向膨脹，提升強度與韌性", LS(58)], [u"隔震", u"拉長週期降低地震力", LS(59)],
          [u"數位孿生", u"隨資料更新的結構模型", LS(64)], [u"ALARP", u"風險在合理可行範圍內盡量低", LS(67)]]),
    ],
}

REFERENCES = [GUIDE, GLOSSARY]
