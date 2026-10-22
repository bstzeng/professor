# -*- coding: utf-8 -*-
"""數學公式是怎麼推導出來的：參考頁——互動工具箱與公式索引。"""
from md_common import *
from md_a import _TAGS

GUIDE = {
    "file": "guide.html", "title": u"推導工具箱", "h1": u"推導工具箱", "icon": u"🧰",
    "description": u"課程中所有圖形與數值互動：拼圖、切片、夾擠、割線、級數、機率與向量",
    "body": [
        ("raw", u"<script>%s</script>" % MDLIB),
        ("p", u"本頁集中課程中的圖形與數值互動。每一個都對應一條推導，標題後面註明出處的課。"),
        ("h", u"1. 平方差：L 形拼成長方形（" + LS(4) + u"）"), mw("sqdiff"),
        ("h", u"2. 畢氏定理拼圖（" + LS(5) + u"）"), mw("pyth"),
        ("h", u"3. 圓面積：切披薩（" + LS(6) + u"）"), mw("pizza"),
        ("h", u"4. 阿基米德夾擠 π（" + LS(7) + u"）"), mw("archi"),
        ("h", u"5. 高斯配對（" + LS(8) + u"）"), mw("gauss"),
        ("h", u"6. 等比級數（" + LS(9) + u"）"), mw("geom"),
        ("h", u"7. 配方法（" + LS(10) + u"）"), mw("compsq"),
        ("h", u"8. 拋物線的根與頂點（" + LS(10) + u"、" + LS(11) + u"）"), mw("parab"),
        ("h", u"9. 巴斯卡三角形（" + LS(12) + u"）"), mw("pascal"),
        ("h", u"10. 複利與 e（" + LS(15) + u"）"), mw("compound"),
        ("h", u"11. 和角公式（" + LS(16) + u"）"), mw("anglesum"),
        ("h", u"12. 餘弦定理（" + LS(18) + u"）"), mw("cosine"),
        ("h", u"13. sin x / x 夾擠（" + LS(20) + u"）"), mw("squeeze"),
        ("h", u"14. 割線變切線（" + LS(22) + u"）"), mw("secant"),
        ("h", u"15. 指數函數的斜率（" + LS(25) + u"）"), mw("ederiv"),
        ("h", u"16. (sin x)′ = cos x（" + LS(26) + u"）"), mw("sinderiv"),
        ("h", u"17. 黎曼和與基本定理（" + LS(27) + u"）"), mw("riemann"),
        ("h", u"18. 球的切片（" + LS(28) + u"）"), mw("sphere"),
        ("h", u"19. 泰勒多項式（" + LS(30) + u"、" + LS(31) + u"）"), mw("taylor", f="cos"),
        ("h", u"20. 巴塞爾問題（" + LS(33) + u"）"), mw("basel"),
        ("h", u"21. 斯特靈公式（" + LS(34) + u"）"), mw("stirling"),
        ("h", u"22. 貝氏定理（" + LS(36) + u"）"), mw("bayes"),
        ("h", u"23. 高斯積分（" + LS(37) + u"）"), mw("gaussint"),
        ("h", u"24. 二項分布 → 常態（" + LS(38) + u"）"), mw("binom"),
        ("h", u"25. 內積（" + LS(39) + u"）"), mw("dot"),
        ("h", u"26. 行列式（" + LS(40) + u"）"), mw("det"),
        ("h", u"27. 最小平方法（" + LS(42) + u"）"), mw("lsq"),
        ("h", u"28. 自由落體（" + LS(43) + u"）"), mw("fall"),
        ("h", u"29. 向心加速度（" + LS(44) + u"）"), mw("circular"),
        ("h", u"30. 單擺週期（" + LS(46) + u"）"), mw("pendulum"),
        ("raw", KATEX),
    ],
}

_F = [[r"(n-2)\times180^\circ", u"多邊形內角和", u"拆開重組", 1], [r"(a+b)^2 = a^2+2ab+b^2", u"完全平方", u"展開化簡、圖形", 4],
      [r"a^2+b^2=c^2", u"畢氏定理", u"拆開重組、相似", 5], [r"A=\pi r^2", u"圓面積", u"極限", 6], [r"n\sin\frac\pi n\lt\pi\lt n\tan\frac\pi n", u"阿基米德夾擠", u"圖形、極限", 7],
      [r"\frac{n(n+1)}{2}", u"等差級數", u"對稱", 8], [r"\frac{a(1-r^n)}{1-r}", u"等比級數", u"錯位相減", 9], [r"\frac{-b\pm\sqrt{b^2-4ac}}{2a}", u"一元二次公式", u"配方", 10],
      [r"\alpha+\beta=-\frac ba,\ \alpha\beta=\frac ca", u"根與係數", u"比較係數", 11], [r"\sum\binom nk a^{n-k}b^k", u"二項式定理", u"計數", 12],
      [r"\frac{n!}{k!(n-k)!}", u"組合數", u"乘法原理", 13], [r"\log xy=\log x+\log y", u"對數律", u"定義、代換", 14], [r"e=\sum\frac1{k!}", u"e", u"二項式、極限", 15],
      [r"\sin(\alpha+\beta)", u"和角公式", u"圖形、旋轉", 16], [r"\sin^2\frac\theta2=\frac{1-\cos\theta}2", u"半角公式", u"代換", 17],
      [r"c^2=a^2+b^2-2ab\cos C", u"餘弦定理", u"座標", 18], [r"\sqrt{s(s-a)(s-b)(s-c)}", u"海龍公式", u"平方差", 19], [r"\lim\frac{\sin x}{x}=1", u"重要極限", u"夾擠", 20],
      [r"(x^n)'=nx^{n-1}", u"冪次法則", u"二項式", 23], [r"(fg)'=f'g+fg'", u"乘積律", u"加一項減一項", 24], [r"(e^x)'=e^x", u"指數的導數", u"定義 e", 25],
      [r"(\sin x)'=\cos x", u"三角的導數", u"和角公式、極限", 26], [r"\int_a^bf=F(b)-F(a)", u"微積分基本定理", u"夾擠", 27], [r"\frac43\pi r^3", u"球體積", u"切片", 28],
      [r"\int u\,dv=uv-\int v\,du", u"分部積分", u"乘積律", 29], [r"\sum\frac{f^{(k)}(0)}{k!}x^k", u"泰勒展開", u"比較係數", 30], [r"e^{i\theta}=\cos\theta+i\sin\theta", u"尤拉公式", u"代換", 32],
      [r"\sum\frac1{k^2}=\frac{\pi^2}6", u"巴塞爾問題", u"無窮乘積", 33], [r"\sqrt{2\pi n}(n/e)^n", u"斯特靈公式", u"拉普拉斯方法", 34],
      [r"E[X^2]-\mu^2", u"變異數", u"線性", 35], [r"\frac{P(B|A)P(A)}{P(B)}", u"貝氏定理", u"對稱", 36], [r"\int e^{-x^2}=\sqrt\pi", u"高斯積分", u"極座標", 37],
      [r"\frac{1}{\sqrt{2\pi npq}}e^{-x^2/2npq}", u"棣美弗–拉普拉斯", u"近似", 38], [r"|\mathbf a||\mathbf b|\cos\theta", u"內積", u"餘弦定理", 39],
      [r"ad-bc", u"行列式", u"拆開重組", 40], [r"x=\frac{ed-bf}{ad-bc}", u"克拉瑪公式", u"消去", 41], [r"A^{\mathsf T}A\beta=A^{\mathsf T}y", u"法線方程", u"偏導、投影", 42],
      [r"\tfrac12gt^2", u"自由落體", u"積分、面積", 43], [r"\frac{v^2}{r}", u"向心加速度", u"相似、微分", 44], [r"T^2=\frac{4\pi^2}{GM}r^3", u"克卜勒第三定律", u"代換", 45],
      [r"2\pi\sqrt{L/g}", u"單擺週期", u"近似", 46], [r"\frac{n(n+1)(2n+1)}6", u"平方和", u"歸納", 48]]

GLOSSARY = {
    "file": "glossary.html", "title": u"公式與招式速查", "h1": u"公式與招式速查", "icon": u"📖",
    "description": u"十二種推導招式，以及課程中每條公式的出處與主要招式",
    "body": [
        ("h", u"推導的十二種招式"), _TAGS,
        ("h", u"公式索引"),
        ("t", [u"公式", u"名稱", u"主要招式", u"課"], [[u"\\(%s\\)" % f, n, t, LS(k)] for f, n, t, k in _F]),
        ("raw", KATEX),
    ],
}

REFERENCES = [GUIDE, GLOSSARY]
