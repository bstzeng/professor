# -*- coding: utf-8 -*-
"""氣象學：參考頁——互動實驗室、公式總表、名詞對照。"""
from wx_common import WXLIB, LS, ww, KATEX, M

LAB = {
    "file": "lab.html", "title": u"氣象互動實驗室", "h1": u"氣象互動實驗室", "icon": u"🧪",
    "description": u"氣壓與高度、空氣塊抬升與雲底、科氏力、地轉風、颱風風場、颱風路徑、勞倫茲吸子與系集預報",
    "body": [
        ("raw", u"<script>%s</script>" % WXLIB),
        ("p", u"把課程中的互動工具集中在這裡。所有工具都是簡化模型，用來建立直覺。"),
        ("h", u"1. 氣壓與高度（第 5 課）"), ww("hyp"),
        ("h", u"2. 空氣塊抬升、雲底與大氣穩定度（第 9 課）"), ww("parcel"),
        ("h", u"3. 科氏力（第 12 課）"), ww("coriolis"),
        ("h", u"4. 地轉風與摩擦（第 13 課）"), ww("geo"),
        ("h", u"5. 颱風風場（第 28 課）"), ww("tywind"),
        ("h", u"6. 颱風路徑與太平洋高壓（第 30 課）"), ww("track"),
        ("h", u"7. 勞倫茲吸子與系集預報（第 39 課）"), ww("lorenz"),
    ],
}

FORMULAS = {
    "file": "formulas.html", "title": u"氣象公式總表", "h1": u"氣象公式總表", "icon": u"📋",
    "description": u"輻射、熱力學、動力學、颱風與數值預報的常用公式",
    "body": [
        ("raw", KATEX),
        ("t", [u"主題", u"公式", u"課"], [
            [u"史蒂芬－波茲曼", M(r"E = \sigma T^4"), LS(4)],
            [u"維恩位移", M(r"\lambda_{max} \approx 2898 / T\ \mu m"), LS(4)],
            [u"地球平衡溫度", M(r"S_0(1-\alpha)/4 = \sigma T_e^4"), LS(4)],
            [u"理想氣體", M(r"p = \rho R_d T"), LS(5)],
            [u"靜力平衡", M(r"\partial p / \partial z = -\rho g"), LS(5)],
            [u"壓高公式", M(r"z_2 - z_1 = (R_d \bar{T}/g) \ln(p_1/p_2)"), LS(5)],
            [u"飽和水氣壓", M(r"e_s \approx 6.112 \exp(17.67T/(T+243.5))"), LS(7)],
            [u"乾絕熱遞減率", M(r"\Gamma_d = g / c_p \approx 9.8\ \text{K/km}"), LS(8)],
            [u"雲底高度", M(r"z_{LCL} \approx 125 (T - T_d)\ \text{m}"), LS(8)],
            [u"位溫", M(r"\theta = T (1000/p)^{R_d/c_p}"), LS(8)],
            [u"對流可用位能", M(r"\text{CAPE} = g \int (T_p - T_e)/T_e\, dz"), LS(9)],
            [u"氣壓梯度力", M(r"-\frac{1}{\rho}\nabla p"), LS(11)],
            [u"科氏參數", M(r"f = 2\Omega \sin\varphi"), LS(12)],
            [u"羅士比數", M(r"Ro = U / (f L)"), LS(12)],
            [u"地轉風", M(r"V_g = \frac{1}{\rho f}\frac{\Delta p}{\Delta n}"), LS(13)],
            [u"梯度風", M(r"V^2/R + fV = \frac{1}{\rho}\partial p/\partial n"), LS(13)],
            [u"熱力風", M(r"\partial \vec{V}_g / \partial \ln p = -(R_d/f)\, \vec{k} \times \nabla_p T"), LS(14)],
            [u"相對渦度", M(r"\zeta = \partial v/\partial x - \partial u/\partial y"), LS(15)],
            [u"位渦守恆", M(r"\frac{d}{dt}\frac{\zeta + f}{H} = 0"), LS(15)],
            [u"羅士比波相速", M(r"c = U - \beta / k^2"), LS(15)],
            [u"焚風增溫", M(r"\Delta T \approx (\Gamma_d - \Gamma_m) H"), LS(24)],
            [u"最大潛在強度", M(r"V_{max}^2 = \frac{C_k}{C_D}\frac{T_s - T_o}{T_o}(k_s^* - k)"), LS(29)],
            [u"CFL 條件", M(r"c\, \Delta t / \Delta x \le 1"), LS(36)],
            [u"資料同化", M(r"x_a = x_b + K(y - x_b)"), LS(38)],
            [u"勞倫茲方程", M(r"\dot{x} = \sigma(y-x),\ \dot{y} = x(\rho - z) - y,\ \dot{z} = xy - \beta z"), LS(39)],
            [u"可預報時間", M(r"t \approx \lambda^{-1} \ln(\Delta / \delta_0)"), LS(39)],
            [u"布萊爾分數", M(r"BS = \frac{1}{N}\sum (p_i - o_i)^2"), LS(40)],
        ]),
    ],
}

G = [
    (u"對流層", u"troposphere", 2), (u"對流層頂", u"tropopause", 2), (u"地球同步衛星", u"geostationary satellite", 3), (u"雷達回波", u"radar reflectivity (dBZ)", 3),
    (u"反照率", u"albedo", 4), (u"溫室效應", u"greenhouse effect", 4), (u"靜力平衡", u"hydrostatic balance", 5), (u"尺度高度", u"scale height", 5),
    (u"潛熱", u"latent heat", 6), (u"露點", u"dew point", 7), (u"相對濕度", u"relative humidity", 7), (u"乾絕熱遞減率", u"dry adiabatic lapse rate", 8),
    (u"舉升凝結高度", u"lifting condensation level (LCL)", 8), (u"位溫", u"potential temperature", 8), (u"條件性不穩定", u"conditional instability", 9), (u"對流可用位能", u"CAPE", 9),
    (u"逆溫", u"temperature inversion", 9), (u"凝結核", u"condensation nuclei", 10), (u"氣壓梯度力", u"pressure gradient force", 11), (u"科氏力", u"Coriolis force", 12),
    (u"地轉風", u"geostrophic wind", 13), (u"白貝羅定律", u"Buys Ballot's law", 13), (u"邊界層", u"boundary layer", 14), (u"熱力風", u"thermal wind", 14),
    (u"噴流", u"jet stream", 14), (u"垂直風切", u"vertical wind shear", 14), (u"渦度", u"vorticity", 15), (u"羅士比波", u"Rossby wave", 15),
    (u"哈德里胞", u"Hadley cell", 16), (u"熱帶輻合帶", u"ITCZ", 16), (u"副熱帶高壓", u"subtropical high", 16), (u"季風", u"monsoon", 17),
    (u"冷鋒／暖鋒", u"cold / warm front", 18), (u"滯留鋒", u"stationary front", 18), (u"溫帶氣旋", u"extratropical cyclone", 19), (u"斜壓不穩定", u"baroclinic instability", 19),
    (u"梅雨", u"Meiyu (plum rain)", 21), (u"中尺度對流系統", u"mesoscale convective system", 21), (u"超大胞", u"supercell", 23), (u"焚風", u"foehn wind", 24),
    (u"熱帶氣旋", u"tropical cyclone", 26), (u"暖心", u"warm core", 28), (u"眼牆", u"eyewall", 28), (u"眼牆置換", u"eyewall replacement cycle", 28),
    (u"最大潛在強度", u"maximum potential intensity", 29), (u"快速增強", u"rapid intensification", 29), (u"駛流", u"steering flow", 30), (u"藤原效應", u"Fujiwhara effect", 30),
    (u"β 漂移", u"beta drift", 30), (u"副低壓", u"secondary low", 31), (u"共伴效應", u"typhoon–monsoon interaction", 32), (u"原始方程", u"primitive equations", 35),
    (u"參數化", u"parameterization", 37), (u"資料同化", u"data assimilation", 38), (u"四維變分", u"4D-Var", 38), (u"蝴蝶效應", u"butterfly effect", 39),
    (u"系集預報", u"ensemble forecast", 40), (u"再分析", u"reanalysis (ERA5)", 42), (u"聖嬰—南方振盪", u"ENSO", 44), (u"混合層", u"mixed layer", 45),
]

GLOSSARY = {
    "file": "glossary.html", "title": u"氣象名詞對照", "h1": u"氣象名詞對照", "icon": u"📖",
    "description": u"氣象學與颱風常用名詞的中英對照",
    "body": [("t", [u"中文", u"英文", u"課"], [[a, b, LS(n)] for a, b, n in G])],
}

REFERENCES = [LAB, FORMULAS, GLOSSARY]
