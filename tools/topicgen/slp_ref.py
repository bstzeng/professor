# -*- coding: utf-8 -*-
"""睡眠的科學：參考頁——睡眠實驗室、公式總表、名詞對照。"""
from slp_common import SLLIB, LS, sw, KATEX, M

LAB = {
    "file": "lab.html", "title": u"睡眠實驗室", "h1": u"睡眠實驗室", "icon": u"🧪",
    "description": u"睡眠週期圖、兩歷程模型、咖啡因殘留、睡眠負債與社交時差、時差調整計畫",
    "body": [
        ("raw", u"<script>%s</script>" % SLLIB),
        ("p", u"把課程中的互動工具集中在這裡。所有工具都是簡化模型，用來建立直覺，不能取代醫療評估。"),
        ("h", u"1. 睡眠週期圖（第 4 課）"), sw("hypno"),
        ("h", u"2. 兩歷程模型（第 5 課）"), sw("twoproc"),
        ("h", u"3. 咖啡因殘留計算（第 8 課）"), sw("caff"),
        ("h", u"4. 睡眠負債與社交時差（第 18 課）"), sw("debt"),
        ("h", u"5. 時差調整計畫（第 27 課）"), sw("jetlag"),
    ],
}

FORMULAS = {
    "file": "formulas.html", "title": u"睡眠公式總表", "h1": u"睡眠公式總表", "icon": u"📋",
    "description": u"睡眠效率、兩歷程模型、咖啡因代謝、社交時差、睡眠負債、呼吸中止指數",
    "body": [
        ("raw", KATEX),
        ("t", [u"主題", u"公式", u"說明", u"課"], [
            [u"睡眠效率", M(r"\text{SE} = \text{TST} / \text{TIB} \times 100\%"), u"總睡眠時間除以躺床時間，85% 以上通常正常", LS(3)],
            [u"睡眠壓力上升", M(r"S(t) = 1 - (1 - S_0) e^{-t/\tau_r}"), u"清醒時，τ<sub>r</sub> 約 18 小時", LS(5)],
            [u"睡眠壓力下降", M(r"S(t) = S_0 e^{-t/\tau_d}"), u"睡眠時，τ<sub>d</sub> 約 4 小時", LS(5)],
            [u"社交時差", M(r"|\text{MSF} - \text{MSW}|"), u"休息日與工作日睡眠中點的差", LS(7)],
            [u"咖啡因代謝", M(r"C(t) = C_0 (1/2)^{t / t_{1/2}}"), u"半衰期平均約 5 小時", LS(8)],
            [u"睡眠負債", M(r"\sum (\text{need} - \text{actual})"), u"每日睡眠需求與實際睡眠差的累積", LS(18)],
            [u"呼吸中止指數", M(r"\text{AHI} = (\text{apneas} + \text{hypopneas}) / \text{hours}"), u"5～15 輕度、15～30 中度、30 以上重度", LS(21)],
        ]),
    ],
}

G = [(u"非快速動眼期", u"NREM sleep", 4), (u"快速動眼期", u"REM sleep", 4), (u"深睡（慢波睡眠）", u"N3 / slow-wave sleep", 4), (u"睡眠紡錘波", u"sleep spindle", 12), (u"睡眠麻痺（鬼壓床）", u"sleep paralysis", 4),
     (u"多項睡眠生理檢查", u"polysomnography (PSG)", 3), (u"睡眠效率", u"sleep efficiency", 3), (u"入睡潛伏期", u"sleep onset latency", 3), (u"兩歷程模型", u"two-process model", 5), (u"睡眠壓力", u"sleep pressure (Process S)", 5),
     (u"生理時鐘", u"circadian rhythm (Process C)", 6), (u"視交叉上核", u"suprachiasmatic nucleus (SCN)", 6), (u"褪黑激素", u"melatonin", 6), (u"黑視素", u"melanopsin", 6), (u"時型", u"chronotype", 7),
     (u"社交時差", u"social jetlag", 7), (u"腺苷", u"adenosine", 8), (u"半衰期", u"half-life", 8), (u"清醒夢", u"lucid dream", 10), (u"記憶鞏固", u"memory consolidation", 12),
     (u"瘦素／飢餓素", u"leptin / ghrelin", 15), (u"類淋巴系統", u"glymphatic system", 17), (u"睡眠負債", u"sleep debt", 18), (u"微睡眠", u"microsleep", 18), (u"失眠的認知行為治療", u"CBT-I", 20),
     (u"睡眠限制", u"sleep restriction therapy", 20), (u"阻塞型睡眠呼吸中止症", u"obstructive sleep apnea (OSA)", 21), (u"連續正壓呼吸器", u"CPAP", 21), (u"猝睡症", u"narcolepsy", 22), (u"猝倒", u"cataplexy", 22),
     (u"下視丘泌素", u"orexin / hypocretin", 22), (u"不寧腿症候群", u"restless legs syndrome", 23), (u"異睡症", u"parasomnia", 24), (u"快速動眼期睡眠行為障礙", u"REM sleep behavior disorder (RBD)", 24), (u"睡眠相位後移", u"delayed sleep phase", 25),
     (u"輪班工作睡眠障礙", u"shift work disorder", 26), (u"時差", u"jet lag", 27), (u"睡眠慣性", u"sleep inertia", 33), (u"睡眠完美主義", u"orthosomnia", 34), (u"嬰兒猝死症候群", u"SIDS", 36)]

GLOSSARY = {
    "file": "glossary.html", "title": u"睡眠名詞對照", "h1": u"睡眠名詞對照", "icon": u"📖",
    "description": u"睡眠科學常用名詞的中英對照",
    "body": [("t", [u"中文", u"英文", u"課"], [[a, b, LS(n)] for a, b, n in G])],
}

REFERENCES = [LAB, FORMULAS, GLOSSARY]
