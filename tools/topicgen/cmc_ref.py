# -*- coding: utf-8 -*-
"""古典力學：參考頁——公式速查表、人物年表。"""
from cmc_common import LS, M, D

CHEATSHEET = {
    "file": "cheatsheet.html", "title": u"古典力學公式速查表", "h1": u"古典力學公式速查表", "icon": u"📐",
    "description": u"運動學、守恆律、振動、軌道、剛體、拉格朗日與哈密頓的核心公式",
    "body": [
        ("h", u"運動學與牛頓定律"),
        ("t", [u"公式", u"說明", u"課"], [
            [M(r"v = v_0 + at,\ x = x_0 + v_0t + \tfrac12at^2,\ v^2 = v_0^2 + 2a\Delta x"), u"等加速度", LS(6)],
            [M(r"R = v_0^2\sin2\theta/g"), u"真空拋體射程", LS(7)],
            [M(r"v_T = mg/b,\quad v_T = \sqrt{mg/c}"), u"線性／二次阻力的終端速度", LS(7)],
            [M(r"\vec F = d\vec p/dt"), u"牛頓第二定律", LS(4)],
            [M(r"-2m\vec\omega\times\vec v,\quad -m\vec\omega\times(\vec\omega\times\vec r)"), u"科氏力、離心力", LS(9)],
        ]),
        ("h", u"守恆律"),
        ("t", [u"公式", u"說明", u"課"], [
            [M(r"W = \int\vec F\cdot d\vec r = \Delta K"), u"動能定理", LS(12)],
            [M(r"\vec F = -\nabla U,\quad E = K + U"), u"保守力與力學能", LS(13)],
            [M(r"v_1 = \frac{m_1-m_2}{m_1+m_2}u_1,\ v_2 = \frac{2m_1}{m_1+m_2}u_1"), u"一維彈性碰撞", LS(14)],
            [M(r"\Delta v = u\ln(m_0/m_f)"), u"火箭方程式", LS(15)],
            [M(r"d\vec L/dt = \vec\tau"), u"角動量定理", LS(16)],
        ]),
        ("h", u"振動與波"),
        ("t", [u"公式", u"說明", u"課"], [
            [M(r"T = 2\pi\sqrt{m/k},\quad T = 2\pi\sqrt{L/g}"), u"彈簧、單擺", LS(18)],
            [M(r"\lambda = -\zeta\omega_0\pm\omega_0\sqrt{\zeta^2-1}"), u"阻尼振動特徵根", LS(19)],
            [M(r"A = \frac{F_0/m}{\sqrt{(\omega_0^2-\Omega^2)^2+(2\zeta\omega_0\Omega)^2}}"), u"受迫振動振幅", LS(20)],
            [M(r"\partial_t^2y = v^2\partial_x^2y,\ v = \sqrt{T/\mu},\ f_n = nv/2L"), u"波動方程式與駐波", LS(22)],
        ]),
        ("h", u"重力與軌道"),
        ("t", [u"公式", u"說明", u"課"], [
            [M(r"U_{\text{eff}} = \frac{L^2}{2\mu r^2} + U(r)"), u"有效位能", LS(25)],
            [M(r"r = \frac{p}{1+e\cos\theta},\quad p = \frac{L^2}{\mu k}"), u"克卜勒軌道", LS(26)],
            [M(r"T^2 = \frac{4\pi^2}{G(m_1+m_2)}a^3"), u"克卜勒第三定律", LS(26)],
            [M(r"v_c = \sqrt{GM/r},\ v_{\text{esc}} = \sqrt{2GM/r}"), u"圓軌道與逃逸速度", LS(27)],
            [M(r"v^2 = GM(2/r - 1/a)"), u"活力公式", LS(27)],
            [M(r"\Delta a = 2GMR/d^3"), u"潮汐加速度", LS(28)],
            [M(r"r_{L1}\approx R(m/3M)^{1/3}"), u"L1／希爾球半徑", LS(29)],
        ]),
        ("h", u"剛體"),
        ("t", [u"公式", u"說明", u"課"], [
            [M(r"I = \int r^2dm,\ I = I_{\text{cm}} + Md^2"), u"轉動慣量、平行軸定理", LS(32)],
            [M(r"I_1\dot\omega_1 - (I_2-I_3)\omega_2\omega_3 = \tau_1"), u"歐拉方程式（循環排列）", LS(34)],
            [M(r"\Omega_p = mgr/I\omega"), u"陀螺進動", LS(35)],
        ]),
        ("h", u"拉格朗日與哈密頓"),
        ("t", [u"公式", u"說明", u"課"], [
            [M(r"\frac{d}{dt}\frac{\partial\mathcal L}{\partial\dot q} - \frac{\partial\mathcal L}{\partial q} = 0"), u"歐拉—拉格朗日方程式", LS(38)],
            [M(r"S = \int(T - V)\,dt,\ \delta S = 0"), u"最小作用量原理", LS(39)],
            [M(r"Q = \sum p_iK_i"), u"諾特守恆量", LS(41)],
            [M(r"H = \sum p\dot q - \mathcal L"), u"哈密頓量", LS(43)],
            [M(r"\dot q = \partial H/\partial p,\ \dot p = -\partial H/\partial q"), u"哈密頓方程式", LS(44)],
            [M(r"df/dt = \{f, H\},\ \{q,p\} = 1"), u"泊松括號", LS(46)],
            [M(r"J = \frac{1}{2\pi}\oint p\,dq"), u"作用量變數", LS(47)],
            [M(r"\delta(t)\approx\delta_0e^{\lambda t}"), u"李亞普諾夫指數", LS(49)],
        ]),
    ],
}

PEOPLE = {
    "file": "timeline.html", "title": u"古典力學年表", "h1": u"古典力學年表", "icon": u"⏳",
    "description": u"從亞里斯多德到 KAM 定理：人物與關鍵發現",
    "body": [
        ("t", [u"年代", u"人物", u"貢獻", u"課"], [
            [u"約前 350", u"亞里斯多德", u"自然運動與強迫運動", LS(1)],
            [u"約 1340", u"布里丹", u"衝力理論", LS(1)],
            [u"1609、1619", u"克卜勒", u"行星運動三大定律", LS(3)],
            [u"1638", u"伽利略", u"《兩種新科學》：等加速度、慣性", LS(2)],
            [u"1656、1673", u"惠更斯", u"擺鐘、等時曲線、向心力", LS(18)],
            [u"1662", u"費馬", u"光學最短時間原理", LS(39)],
            [u"1687", u"牛頓", u"《原理》：三大定律與萬有引力", LS(4)],
            [u"1696", u"約翰・白努利", u"最速降線問題", LS(38)],
            [u"1744", u"歐拉、莫佩爾蒂", u"變分法、最小作用量", LS(38)],
            [u"1747", u"達朗貝爾", u"波動方程式", LS(22)],
            [u"1765", u"歐拉", u"剛體運動方程式", LS(34)],
            [u"1772", u"拉格朗日", u"拉格朗日點", LS(29)],
            [u"1788", u"拉格朗日", u"《分析力學》", LS(37)],
            [u"1798", u"卡文迪許", u"測量 G", LS(4)],
            [u"1807", u"傅立葉", u"傅立葉級數", LS(22)],
            [u"1809", u"泊松", u"泊松括號", LS(46)],
            [u"1833～1834", u"哈密頓", u"哈密頓力學、哈密頓原理", LS(43)],
            [u"1835", u"科氏", u"旋轉座標系中的假想力", LS(9)],
            [u"1838", u"劉維爾", u"相空間體積守恆", LS(45)],
            [u"1846", u"勒維耶、加勒", u"發現海王星", LS(30)],
            [u"1851", u"傅科", u"傅科擺", LS(10)],
            [u"1890", u"龐加萊", u"三體問題不可積、混沌的發現", LS(29)],
            [u"1903", u"齊奧爾科夫斯基", u"火箭方程式", LS(15)],
            [u"1915", u"愛因斯坦", u"水星進動的 43 角秒", LS(30)],
            [u"1918", u"諾特", u"諾特定理", LS(41)],
            [u"1925", u"狄拉克", u"泊松括號 → 量子對易子", LS(46)],
            [u"1961", u"勞倫茲", u"蝴蝶效應", LS(49)],
            [u"1954～1963", u"柯爾莫哥洛夫、阿諾德、莫瑟", u"KAM 定理", LS(50)],
            [u"1985", u"賈尼別科夫", u"太空中的中間軸翻轉", LS(34)],
            [u"1989", u"拉斯卡爾", u"內太陽系是混沌的", LS(50)],
        ]),
    ],
}

REFERENCES = [CHEATSHEET, PEOPLE]
