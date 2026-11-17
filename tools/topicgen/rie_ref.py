# -*- coding: utf-8 -*-
"""質數與黎曼猜想：參考頁——公式表、文獻。"""
from rie_common import LS, M


def mono(s):
    return u'<span style="font-family:ui-monospace,Menlo,monospace;font-size:0.9em">%s</span>' % s


FORMULAS = {
    "file": "formulas.html", "title": u"公式表", "h1": u"質數與 ζ 函數公式表", "icon": u"📐",
    "description": u"質數定理、ζ 函數、顯式公式等主要公式",
    "body": [
        ("t", [u"名稱", u"公式", u"課"], [
            [u"質數定理", M(r"\pi(x)\sim x/\ln x"), LS(5)],
            [u"對數積分", M(r"\text{Li}(x) = \int_2^x dt/\ln t"), LS(6)],
            [u"切比雪夫函數", M(r"\psi(x) = \sum_{p^k\le x}\ln p"), LS(7)],
            [u"巴塞爾問題", M(r"\zeta(2) = \pi^2/6"), LS(10)],
            [u"ζ 函數", M(r"\zeta(s) = \sum_{n\ge1}n^{-s}"), LS(10)],
            [u"歐拉乘積", M(r"\zeta(s) = \prod_p(1 - p^{-s})^{-1}"), LS(11)],
            [u"函數方程", M(r"\xi(s) = \xi(1 - s)"), LS(13)],
            [u"顯式公式", M(r"\psi(x) = x - \sum_\rho x^\rho/\rho - \ln 2\pi - \tfrac12\ln(1 - x^{-2})"), LS(17)],
            [u"零點個數", M(r"N(T)\approx\tfrac{T}{2\pi}\ln\tfrac{T}{2\pi} - \tfrac{T}{2\pi} + \tfrac78"), LS(18)],
            [u"黎曼猜想的等價形式", M(r"\pi(x) = \text{Li}(x) + O(\sqrt x\ln x)"), LS(23)],
            [u"羅賓不等式", M(r"\sigma(n) < e^\gamma n\ln\ln n\ (n > 5040)"), LS(24)],
            [u"蒙哥馬利對相關", M(r"1 - (\sin\pi u/\pi u)^2"), LS(27)],
        ]),
        ("h", u"最初的幾個非平凡零點（虛部）"),
        ("p", u"14.1347、21.0220、25.0109、30.4249、32.9351、37.5862、40.9187、43.3271、48.0052、49.7738……（實部都是 ½）"),
    ],
}

PAPERS = {
    "file": "papers.html", "title": u"文獻", "h1": u"質數與黎曼猜想的重要文獻", "icon": u"📄",
    "description": u"從歐拉到張益唐",
    "body": [
        ("t", [u"文獻", u"出處", u"課"], [
            [u"Euler：Variae observationes circa series infinitas（歐拉乘積）", mono(u"1737"), LS(11)],
            [u"Dirichlet：等差數列中的質數", mono(u"1837"), LS(34)],
            [u"Riemann：Ueber die Anzahl der Primzahlen unter einer gegebenen Grösse", mono(u"Monatsber. Berlin Akad. (1859)"), LS(16)],
            [u"Hadamard：Sur la distribution des zéros de la fonction ζ(s)", mono(u"Bull. SMF 24, 199 (1896)"), LS(8)],
            [u"de la Vallée Poussin：Recherches analytiques sur la théorie des nombres premiers", mono(u"1896"), LS(8)],
            [u"Hardy：Sur les zéros de la fonction ζ(s) de Riemann", mono(u"C. R. Acad. Sci. 158, 1012 (1914)"), LS(22)],
            [u"Turing：Some Calculations of the Riemann Zeta-Function", mono(u"Proc. LMS 3, 99 (1953)"), LS(21)],
            [u"Montgomery：The pair correlation of zeros of the zeta function", mono(u"Proc. Symp. Pure Math. 24, 181 (1973)"), LS(27)],
            [u"Deligne：La conjecture de Weil. I", mono(u"Publ. Math. IHÉS 43, 273 (1974)"), LS(34)],
            [u"Rivest, Shamir, Adleman：A Method for Obtaining Digital Signatures and Public-Key Cryptosystems", mono(u"Commun. ACM 21, 120 (1978)"), LS(31)],
            [u"Robin：Grandes valeurs de la fonction somme des diviseurs et hypothèse de Riemann", mono(u"J. Math. Pures Appl. 63, 187 (1984)"), LS(24)],
            [u"Odlyzko：On the distribution of spacings between zeros of the zeta function", mono(u"Math. Comp. 48, 273 (1987)"), LS(27)],
            [u"Berry, Keating：The Riemann Zeros and Eigenvalue Asymptotics", mono(u"SIAM Review 41, 236 (1999)"), LS(29)],
            [u"Zhang：Bounded gaps between primes", mono(u"Ann. Math. 179, 1121 (2014)"), LS(32)],
            [u"Maynard：Small gaps between primes", mono(u"Ann. Math. 181, 383 (2015)"), LS(32)],
            [u"Platt, Trudgian：The Riemann hypothesis is true up to 3·10¹²", mono(u"Bull. LMS 53, 792 (2021)"), LS(21)],
            [u"du Sautoy：The Music of the Primes（《質數的音樂》）", mono(u"2003"), LS(19)],
        ]),
    ],
}

REFERENCES = [FORMULAS, PAPERS]
