# -*- coding: utf-8 -*-
"""微積分：參考頁——公式速查、名詞表。"""
from clc_common import LS, D

FORMULAS = {
    "file": "formulas.html", "title": u"公式速查", "h1": u"微積分公式速查", "icon": u"🧮",
    "description": u"常用的導數、積分與級數",
    "body": [
        ("h", u"導數"),
        ("t", [u"f(x)", u"f′(x)", u"課"], [
            [u"c", u"0", LS(7)], [u"xⁿ", u"nxⁿ⁻¹", LS(7)], [u"eˣ", u"eˣ", LS(9)], [u"aˣ", u"aˣ ln a", LS(9)], [u"ln x", u"1/x", LS(9)],
            [u"sin x", u"cos x", LS(10)], [u"cos x", u"−sin x", LS(10)], [u"tan x", u"sec² x", LS(10)],
        ]),
        ("h", u"規則"),
        D(r"(fg)'=f'g+fg',\qquad \left(\frac fg\right)'=\frac{f'g-fg'}{g^2},\qquad \frac{dy}{dx}=\frac{dy}{du}\frac{du}{dx}"),
        ("h", u"積分"),
        ("t", [u"f(x)", u"∫ f(x) dx", u"課"], [
            [u"xⁿ（n ≠ −1）", u"xⁿ⁺¹/(n+1) + C", LS(19)], [u"1/x", u"ln|x| + C", LS(20)], [u"eˣ", u"eˣ + C", LS(20)], [u"sin x", u"−cos x + C", LS(20)], [u"cos x", u"sin x + C", LS(20)],
        ]),
        D(r"\int_a^b f(x)\,dx=F(b)-F(a),\qquad \int u\,dv=uv-\int v\,du"),
        ("h", u"級數"),
        D(r"e^x=\sum_{n=0}^\infty\frac{x^n}{n!},\quad \sin x=\sum_{n=0}^\infty\frac{(-1)^nx^{2n+1}}{(2n+1)!},\quad \frac1{1-x}=\sum_{n=0}^\infty x^n\ (|x|<1)"),
    ],
}

GLOSSARY = {
    "file": "glossary.html", "title": u"名詞表", "h1": u"微積分名詞表", "icon": u"📖",
    "description": u"本課程用到的微積分名詞",
    "body": [
        ("t", [u"名詞", u"意思", u"課"], [
            [u"極限", u"無限接近的值", LS(3)], [u"平均變化率", u"割線斜率", LS(4)], [u"導數", u"瞬間變化率；切線斜率", LS(6)], [u"二階導數", u"導數的導數；彎曲", LS(6)],
            [u"連鎖律", u"合成函數的導數：變化率相乘", LS(8)], [u"臨界點", u"導數為零的點", LS(12)], [u"牛頓法", u"沿切線找根", LS(14)], [u"線性近似", u"用切線代替曲線", LS(15)],
            [u"邊際", u"經濟學中的導數", LS(16)], [u"黎曼和", u"用長方形逼近面積", LS(18)], [u"定積分", u"黎曼和的極限", LS(18)], [u"反導數", u"導數是 f 的函數", LS(19)],
            [u"機率密度", u"面積代表機率的函數", LS(22)], [u"微分方程", u"包含導數的方程式", LS(24)], [u"斜率場", u"微分方程在每點的斜率", LS(24)], [u"半衰期", u"減半所需的時間", LS(25)],
            [u"共振", u"以自然頻率推動時振幅變大", LS(27)], [u"泰勒展開", u"用多項式模仿函數", LS(29)], [u"梯度", u"偏導數組成的向量，指向上升最快的方向", LS(30)],
        ]),
    ],
}

REFERENCES = [FORMULAS, GLOSSARY]
