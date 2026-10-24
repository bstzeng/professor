# -*- coding: utf-8 -*-
"""用 Python 做數值模擬：參考頁——互動工具箱、程式下載、公式速查。"""
from nsm_common import *

_DESC = {
    "decay": (u"尤拉法與解析解（放射性衰變）", 2), "roundoff": (u"截斷與捨入誤差", 3), "mms": (u"製造解法與收斂階數", 4),
    "envcheck": (u"確認環境", 5), "vectorize": (u"迴圈與向量化", 6), "plotting": (u"三種常用圖", 7), "scipy_demo": (u"稀疏矩陣與 solve_ivp", 8),
    "speedup": (u"NumPy 與 Numba", 9), "fd_order": (u"差分公式的收斂階數", 11), "heat1d": (u"一維熱傳導 FTCS", 12), "stability": (u"顯式與隱式的穩定性", 13),
    "wave1d": (u"跳蛙法與 CFL", 14), "boundary": (u"四種邊界條件", 15), "poisson2d": (u"二維 Poisson 與 Kronecker 積", 16), "refine": (u"網格加密與 Richardson 外插", 17),
    "taylor_green": (u"NS 方程式逐項檢查", 18), "reynolds": (u"雷諾數", 19), "projection": (u"FFT 投影", 20), "cavity_chorin": (u"方腔流：Chorin 投影法", 21),
    "cavity_psi": (u"方腔流：渦度–流函數法", 22), "lbm_poiseuille": (u"LBM 與 Poiseuille 流", 23), "chamber_params": (u"蝕刻腔的無因次數", 24),
    "chamber_mask": (u"蝕刻腔幾何遮罩", 25), "chamber_lbm": (u"蝕刻腔 LBM 流場", 26), "axisym": (u"軸對稱導熱", 27), "wafer_temp": (u"晶圓溫度與雙區冷卻", 28),
    "chamber_species": (u"自由基對流擴散與均勻度", 29), "knudsen": (u"平均自由徑與 Kn", 30), "chamber_design": (u"四種腔體設計比較", 31),
    "pool_dispersion": (u"水波色散關係", 32), "pool_drop": (u"二維波動與水滴", 33), "pool_interf": (u"干涉與海綿層", 34), "pool_spectral": (u"頻譜法、群速與黏性衰減", 35),
    "pool_live": (u"互動水池（Matplotlib 動畫）", 36), "caustics": (u"池底焦散", 37), "pool_perf": (u"效能量測", 38),
}

GUIDE = {
    "file": "guide.html", "title": u"數值模擬互動工具箱", "h1": u"數值模擬互動工具箱", "icon": u"🌊",
    "description": u"熱傳導穩定性、波動 CFL、網格收斂、LBM 方腔流、蝕刻腔、水波色散、互動水池",
    "body": [
        ("raw", u"<script>%s</script>" % NMLIB),
        ("p", u"所有工具都在瀏覽器裡即時計算；模型是教學用的簡化版本。"),
        ("h", u"1. 一維熱傳導：顯式與隱式（" + LS(12) + u"、" + LS(13) + u"）"), nw("heat"),
        ("h", u"2. 一維波動方程式與 CFL（" + LS(14) + u"）"), nw("wave"),
        ("h", u"3. 差分公式的網格收斂（" + LS(3) + u"、" + LS(11) + u"）"), nw("conv"),
        ("h", u"4. LBM 頂蓋驅動方腔流（" + LS(21) + u"～" + LS(23) + u"）"), nw("cavity"),
        ("h", u"5. 蝕刻腔：氣流與自由基（" + LS(26) + u"、" + LS(29) + u"、" + LS(31) + u"）"), nw("chamber"),
        ("h", u"6. 水波色散關係（" + LS(32) + u"、" + LS(35) + u"）"), nw("disp"),
        ("h", u"7. 互動水池與焦散（" + LS(33) + u"、" + LS(36) + u"、" + LS(37) + u"）"), nw("pool"),
    ],
}

CODE = {
    "file": "code.html", "title": u"Python 範例下載", "h1": u"Python 範例下載", "icon": u"🐍",
    "description": u"課程中所有實際執行過的 Python 程式",
    "body": [
        ("p", u"需要 Python 3.9 以上與 NumPy、SciPy、Matplotlib（<code>pip install numpy scipy matplotlib</code>；Numba 可選）。"
              u"蝕刻腔的程式彼此引用：chamber_species.py 需要先執行 chamber_lbm.py 產生 chamber_flow.npz，chamber_design.py 會用到 chamber_mask、chamber_lbm、chamber_species 三個檔案。"),
        ("raw", u'<p><a href="py/numerical-simulation-examples.zip" download><strong>⬇ 全部打包下載（zip）</strong></a></p>'),
        ("t", [u"檔案", u"內容", u"課"], [[u'<a href="py/%s.py" download>%s.py</a>' % (n, n), _DESC[n][0], LS(_DESC[n][1])] for n in PUBLISH]),
    ],
}

GLOSSARY = {
    "file": "glossary.html", "title": u"數值模擬公式速查", "h1": u"數值模擬公式速查", "icon": u"📖",
    "description": u"本課程的關鍵公式與名詞",
    "body": [
        ("raw", KATEX),
        ("h", u"1. 關鍵公式"),
        ("t", [u"公式", u"意思", u"課"],
         [[M(r"\text{cost}\propto N^{d+1}"), u"顯式模擬的成本", LS(1)], [M(r"N_{n+1}=N_n+\Delta t\,f(N_n)"), u"尤拉法（一階）", LS(2)],
          [M(r"h^*=2\sqrt{\varepsilon|f|/M}"), u"前向差分的最佳步長", LS(3)], [M(r"p=\log_2\frac{E(h)}{E(h/2)}"), u"觀測收斂階數", LS(4)],
          [M(r"\frac{u_{i+1}-2u_i+u_{i-1}}{h^2}=u''+\frac{h^2}{12}u''''"), u"二階差分", LS(11)], [M(r"r=\frac{\alpha\Delta t}{\Delta x^2}\le\frac12"), u"顯式熱傳導穩定條件", LS(13)],
          [M(r"C=\frac{c\Delta t}{\Delta x}\le\frac{1}{\sqrt d}"), u"CFL 條件", LS(14)], [M(r"u_0^{n+1}=u_1^n+\frac{C-1}{C+1}(u_1^{n+1}-u_0^n)"), u"Mur 吸收邊界", LS(15)],
          [M(r"\text{nnz}=5n^2-4n"), u"二維五點矩陣", LS(16)], [M(r"u\approx u_h+\frac{u_h-u_{2h}}{2^p-1}"), u"Richardson 外插", LS(17)],
          [M(r"Re=\frac{UL}{\nu}"), u"雷諾數", LS(19)], [M(r"\nabla^2p=\frac{\rho}{\Delta t}\nabla\cdot\mathbf u^*"), u"壓力 Poisson 方程式", LS(20)],
          [M(r"\omega_w=-\frac{2\psi_1}{h^2}-\frac{2U}{h}"), u"Thom 牆面渦度", LS(22)], [M(r"\nu=\frac13\left(\tau-\frac12\right)"), u"LBM 黏度", LS(23)],
          [M(r"\tau_{res}=\frac{pV}{Q_{pV}}"), u"停留時間", LS(24)], [M(r"L_{th}=\sqrt{kt/h}"), u"晶圓熱擴散長度", LS(28)],
          [M(r"k=\frac{\gamma\bar v/4}{1-\gamma/2}"), u"表面反應速率", LS(29)], [M(r"\lambda=\frac{k_BT}{\sqrt2\pi d^2p}"), u"平均自由徑", LS(30)],
          [M(r"\omega^2=(gk+\sigma k^3/\rho)\tanh kh"), u"水波色散", LS(32)], [M(r"a\propto e^{-2\nu k^2t}"), u"黏性衰減", LS(35)],
          [M(r"H_c=\frac{1}{(1-1/n)\kappa}"), u"焦散深度", LS(37)]]),
        ("h", u"2. 名詞"),
        ("t", [u"名詞", u"說明", u"課"],
         [[u"截斷誤差", u"差分丟掉的泰勒高次項", LS(3)], [u"Verification／Validation", u"方程式解對了沒／方程式選對了沒", LS(4)], [u"MMS", u"製造解法", LS(4)],
          [u"FTCS", u"時間前向、空間中央的顯式格式", LS(12)], [u"von Neumann 分析", u"用傅立葉模態的放大因子判斷穩定性", LS(13)], [u"CFL 條件", u"數值傳播速度不能比物理慢", LS(14)],
          [u"跳蛙法", u"時間用中央差分的二階格式", LS(14)], [u"海綿層", u"邊緣逐漸加大阻尼、吸收外傳的波", LS(34)], [u"投影法", u"先預測速度再用壓力消去散度", LS(20)],
          [u"Ghia 基準", u"方腔流的標準比較資料（1982）", LS(21)], [u"LBM", u"晶格波茲曼法：碰撞＋串流", LS(23)], [u"噴淋頭", u"蝕刻腔頂部的均勻進氣板", LS(24)],
          [u"黏附係數 γ", u"粒子撞到表面後反應的比例", LS(29)], [u"Damköhler 數", u"表面反應速率與擴散補充的比", LS(29)], [u"Knudsen 數", u"平均自由徑與幾何尺寸的比", LS(30)],
          [u"DSMC", u"直接模擬蒙地卡羅，稀薄氣體的方法", LS(30)], [u"群速", u"波包（能量）傳播的速度", LS(35)], [u"焦散", u"折射光線聚焦形成的亮紋", LS(37)]]),
    ],
}

REFERENCES = [GUIDE, CODE, GLOSSARY]
