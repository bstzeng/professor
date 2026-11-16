# -*- coding: utf-8 -*-
"""資訊理論：參考頁——公式表、論文。"""
from inf_common import LS, M


def mono(s):
    return u'<span style="font-family:ui-monospace,Menlo,monospace;font-size:0.9em">%s</span>' % s


FORMULAS = {
    "file": "formulas.html", "title": u"公式表", "h1": u"資訊理論公式表", "icon": u"📐",
    "description": u"熵、互資訊、容量、KL 散度等主要公式",
    "body": [
        ("t", [u"名稱", u"公式", u"課"], [
            [u"資訊量", M(r"I(p) = -\log_2 p"), LS(2)],
            [u"熵", M(r"H(X) = -\sum_x p(x)\log_2 p(x)"), LS(3)],
            [u"二元熵", M(r"H_2(p) = -p\log_2 p - (1-p)\log_2(1-p)"), LS(3)],
            [u"克拉夫特不等式", M(r"\sum_i 2^{-\ell_i} \le 1"), LS(7)],
            [u"信源編碼定理", M(r"H \le L < H + 1"), LS(7)],
            [u"高斯率—失真", M(r"R(D) = \tfrac12\log_2(\sigma^2/D)"), LS(12)],
            [u"條件熵", M(r"H(X|Y) = -\sum p(x,y)\log_2 p(x|y)"), LS(15)],
            [u"互資訊", M(r"I(X;Y) = H(X) - H(X|Y)"), LS(15)],
            [u"通道容量", M(r"C = \max_{p(x)} I(X;Y)"), LS(16)],
            [u"二元對稱通道", M(r"C = 1 - H_2(p)"), LS(16)],
            [u"夏農—哈特利", M(r"C = B\log_2(1 + S/N)"), LS(17)],
            [u"交叉熵", M(r"H(P,Q) = -\sum p\log_2 q"), LS(25)],
            [u"KL 散度", M(r"D_{\text{KL}}(P\|Q) = \sum p\log_2(p/q)"), LS(26)],
            [u"最大熵分布", M(r"p_i = e^{-\beta E_i}/Z"), LS(27)],
            [u"困惑度", M(r"\text{PPL} = 2^{H}"), LS(31)],
            [u"西拉德引擎／蘭道爾", M(r"kT\ln 2"), LS(37)],
            [u"黑洞熵", M(r"S = kA/4\ell_P^2"), LS(38)],
        ]),
    ],
}

PAPERS = {
    "file": "papers.html", "title": u"論文清單", "h1": u"資訊理論的重要論文", "icon": u"📄",
    "description": u"從夏農到極化碼的原始文獻",
    "body": [
        ("t", [u"論文", u"出處", u"課"], [
            [u"Szilard：Über die Entropieverminderung in einem thermodynamischen System bei Eingriffen intelligenter Wesen", mono(u"Z. Physik 53, 840 (1929)"), LS(36)],
            [u"Shannon：A Mathematical Theory of Communication", mono(u"Bell Syst. Tech. J. 27, 379 & 623 (1948)"), LS(1)],
            [u"Shannon：Communication Theory of Secrecy Systems", mono(u"Bell Syst. Tech. J. 28, 656 (1949)"), LS(41)],
            [u"Hamming：Error Detecting and Error Correcting Codes", mono(u"Bell Syst. Tech. J. 29, 147 (1950)"), LS(20)],
            [u"Shannon：Prediction and Entropy of Printed English", mono(u"Bell Syst. Tech. J. 30, 50 (1951)"), LS(5)],
            [u"Kullback, Leibler：On Information and Sufficiency", mono(u"Ann. Math. Stat. 22, 79 (1951)"), LS(26)],
            [u"Huffman：A Method for the Construction of Minimum-Redundancy Codes", mono(u"Proc. IRE 40, 1098 (1952)"), LS(8)],
            [u"Jaynes：Information Theory and Statistical Mechanics", mono(u"Phys. Rev. 106, 620 (1957)"), LS(27)],
            [u"Reed, Solomon：Polynomial Codes over Certain Finite Fields", mono(u"J. SIAM 8, 300 (1960)"), LS(21)],
            [u"Landauer：Irreversibility and Heat Generation in the Computing Process", mono(u"IBM J. Res. Dev. 5, 183 (1961)"), LS(37)],
            [u"Gallager：Low-Density Parity-Check Codes", mono(u"IRE Trans. Inf. Theory 8, 21 (1962)"), LS(22)],
            [u"Bekenstein：Black Holes and Entropy", mono(u"Phys. Rev. D 7, 2333 (1973)"), LS(38)],
            [u"Hawking：Particle Creation by Black Holes", mono(u"Commun. Math. Phys. 43, 199 (1975)"), LS(38)],
            [u"Ziv, Lempel：A Universal Algorithm for Sequential Data Compression", mono(u"IEEE Trans. Inf. Theory 23, 337 (1977)"), LS(10)],
            [u"Bennett：The Thermodynamics of Computation—a Review", mono(u"Int. J. Theor. Phys. 21, 905 (1982)"), LS(37)],
            [u"Berrou, Glavieux, Thitimajshima：Near Shannon Limit Error-Correcting Coding and Decoding: Turbo-Codes", mono(u"Proc. ICC 1993"), LS(22)],
            [u"Arıkan：Channel Polarization", mono(u"IEEE Trans. Inf. Theory 55, 3051 (2009)"), LS(23)],
            [u"Bérut 等：Experimental verification of Landauer's principle linking information and thermodynamics", mono(u"Nature 483, 187 (2012)"), LS(37)],
            [u"Kingma, Welling：Auto-Encoding Variational Bayes", mono(u"arXiv:1312.6114 (2013)"), LS(33)],
            [u"Delétang 等：Language Modeling Is Compression", mono(u"arXiv:2309.10668 (2023)"), LS(30)],
        ]),
    ],
}

REFERENCES = [FORMULAS, PAPERS]
