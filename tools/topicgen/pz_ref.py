# -*- coding: utf-8 -*-
"""電漿物理：參考頁——互動實驗室、公式與參數速查。"""
from pz_common import LS, PZLIB, pzw

LAB = {
    "file": "lab.html", "title": u"電漿互動實驗室", "h1": u"電漿互動實驗室", "icon": u"🧪",
    "description": u"薩哈電離、德拜屏蔽、迴旋與漂移、磁鏡、電離層截止頻率、勞森判據",
    "body": [
        ("raw", u"<script>%s</script>" % PZLIB),
        ("p", u"所有模擬都在你的瀏覽器裡計算，為教學用的簡化模型。"),
        ("h", u"1. 薩哈電離（第 3 課）"), pzw({"t": "saha"}),
        ("h", u"2. 德拜屏蔽（第 4 課）"), pzw({"t": "debye"}),
        ("h", u"3. 迴旋運動與漂移（第 8～10 課）"), pzw({"t": "gyro", "mode": "gyro"}),
        ("h", u"4. 磁鏡（第 11 課）"), pzw({"t": "mirror"}),
        ("h", u"5. 電離層與截止頻率（第 5 課）"), pzw({"t": "disp"}),
        ("h", u"6. 勞森判據（第 35 課）"), pzw({"t": "lawson"}),
    ],
}

CHEATSHEET = {
    "file": "cheatsheet.html", "title": u"電漿物理速查", "h1": u"電漿物理速查", "icon": u"🗂️",
    "description": u"公式、典型參數與術語",
    "body": [
        ("h", u"1. 公式"),
        ("t", [u"量", u"公式", u"課"],
         [[u"德拜長度", u"λ_D = √(ε₀k_BT/ne²) ≈ 69 √(T[K]/n[m⁻³]) m", LS(4)], [u"電漿頻率", u"f_p ≈ 8.98 √n Hz", LS(5)],
          [u"迴旋頻率", u"ω_c = qB/m；電子 28 GHz/T、質子 15.2 MHz/T", LS(8)], [u"拉莫半徑", u"r_L = mv⊥/(qB)", LS(8)],
          [u"E×B 漂移", u"v = E×B / B²", LS(9)], [u"磁矩", u"μ = mv⊥²/2B（絕熱不變）", LS(11)], [u"損失錐", u"sin²θ = B_min / B_max", LS(11)],
          [u"阿爾芬速度", u"v_A = B/√(μ₀ρ)", LS(18)], [u"電漿 β", u"nk_BT / (B²/2μ₀)", LS(17)], [u"磁雷諾數", u"R_m = vL/η", LS(15)],
          [u"D-T 反應", u"D + T → ⁴He (3.5 MeV) + n (14.1 MeV)", LS(34)], [u"點火三重積", u"nTτ_E ≳ 3×10²¹ keV·s/m³", LS(35)]]),
        ("h", u"2. 術語"),
        ("t", [u"術語", u"英文", u"課"],
         [[u"電漿（等離子體）", u"plasma", LS(1)], [u"準中性", u"quasineutrality", LS(4)], [u"引導中心", u"guiding center", LS(9)],
          [u"磁流體力學", u"magnetohydrodynamics (MHD)", LS(15)], [u"凍結定理", u"frozen-in flux", LS(16)], [u"磁重聯", u"magnetic reconnection", LS(19)],
          [u"朗道阻尼", u"Landau damping", LS(23)], [u"日冕物質拋射", u"coronal mass ejection (CME)", LS(29)], [u"托卡馬克", u"tokamak", LS(36)],
          [u"仿星器", u"stellarator", LS(36)], [u"慣性約束", u"inertial confinement", LS(39)], [u"破裂", u"disruption", LS(37)]]),
    ],
}

REFERENCES = [LAB, CHEATSHEET]
