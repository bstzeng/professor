# -*- coding: utf-8 -*-
"""傅立葉分析：參考頁——公式表、論文與里程碑。"""
from fou_common import LS, M


def mono(s):
    return u'<span style="font-family:ui-monospace,Menlo,monospace;font-size:0.9em">%s</span>' % s


FORMULAS = {
    "file": "formulas.html", "title": u"公式表", "h1": u"傅立葉分析公式表", "icon": u"📐",
    "description": u"傅立葉級數、轉換、DFT 與主要性質的速查表",
    "body": [
        ("h", u"級數與轉換"),
        ("t", [u"名稱", u"公式", u"課"], [
            [u"傅立葉級數係數", M(r"b_n = \frac1\pi\int_{-\pi}^{\pi}f(t)\sin(nt)\,dt"), LS(3)],
            [u"傅立葉轉換", M(r"\hat f(\xi) = \int f(t)e^{-2\pi i\xi t}dt"), LS(6)],
            [u"反轉換", M(r"f(t) = \int\hat f(\xi)e^{2\pi i\xi t}d\xi"), LS(6)],
            [u"DFT", M(r"X_k = \sum_{n=0}^{N-1}x_ne^{-2\pi ikn/N}"), LS(17)],
            [u"FFT 蝴蝶", M(r"X_k = E_k + W^kO_k,\ X_{k+N/2} = E_k - W^kO_k"), LS(20)],
            [u"Z 轉換", M(r"X(z) = \sum_n x_nz^{-n}"), LS(26)],
            [u"二維轉換", M(r"\hat f(u,v) = \iint f(x,y)e^{-2\pi i(ux+vy)}dx\,dy"), LS(34)],
        ]),
        ("h", u"性質"),
        ("t", [u"性質", u"時域 ↔ 頻域", u"課"], [
            [u"卷積定理", M(r"f * g \leftrightarrow \hat f\,\hat g"), LS(9)],
            [u"延遲", M(r"f(t - t_0) \leftrightarrow e^{-2\pi i\xi t_0}\hat f"), LS(12)],
            [u"縮放", M(r"f(at) \leftrightarrow \tfrac{1}{|a|}\hat f(\xi/a)"), LS(12)],
            [u"微分", M(r"f' \leftrightarrow 2\pi i\xi\hat f"), LS(12)],
            [u"帕塞瓦爾", M(r"\int|f|^2 = \int|\hat f|^2"), LS(11)],
            [u"測不準", M(r"\Delta t\,\Delta\xi \ge 1/4\pi"), LS(10)],
            [u"取樣定理", M(r"f_s > 2B"), LS(14)],
            [u"量化訊雜比", M(r"\text{SNR} \approx 6.02b + 1.76\ \text{dB}"), LS(16)],
        ]),
        ("h", u"常見轉換對"),
        ("t", [u"時域", u"頻域", u"課"], [
            [u"矩形（寬 T）", M(r"T\,\text{sinc}(\xi T)"), LS(8)],
            [M(r"e^{-\pi t^2}"), M(r"e^{-\pi\xi^2}"), LS(8)],
            [u"δ(t)", u"1", LS(8)],
            [M(r"\cos(2\pi f_0t)"), M(r"\tfrac12[\delta(\xi - f_0) + \delta(\xi + f_0)]"), LS(8)],
        ]),
    ],
}

PAPERS = {
    "file": "papers.html", "title": u"論文與里程碑", "h1": u"傅立葉分析的重要論文與里程碑", "icon": u"📄",
    "description": u"從傅立葉到壓縮感知的原始文獻",
    "body": [
        ("t", [u"文獻", u"出處", u"課"], [
            [u"Fourier：Théorie analytique de la chaleur", mono(u"Paris, 1822"), LS(1)],
            [u"Gibbs：Fourier's Series", mono(u"Nature 59, 606 (1899)"), LS(4)],
            [u"Nyquist：Certain Topics in Telegraph Transmission Theory", mono(u"Trans. AIEE 47, 617 (1928)"), LS(14)],
            [u"Shannon：Communication in the Presence of Noise", mono(u"Proc. IRE 37, 10 (1949)"), LS(14)],
            [u"Cooley, Tukey：An Algorithm for the Machine Calculation of Complex Fourier Series", mono(u"Math. Comp. 19, 297 (1965)"), LS(20)],
            [u"Franklin, Gosling：Molecular Configuration in Sodium Thymonucleate", mono(u"Nature 171, 740 (1953)"), LS(41)],
            [u"Lauterbur：Image Formation by Induced Local Interactions", mono(u"Nature 242, 190 (1973)"), LS(39)],
            [u"Hounsfield：Computerized transverse axial scanning (tomography)", mono(u"Br. J. Radiol. 46, 1016 (1973)"), LS(40)],
            [u"Harris：On the Use of Windows for Harmonic Analysis with the DFT", mono(u"Proc. IEEE 66, 51 (1978)"), LS(21)],
            [u"Wallace：The JPEG Still Picture Compression Standard", mono(u"Commun. ACM 34, 30 (1991)"), LS(35)],
            [u"Daubechies：Orthonormal Bases of Compactly Supported Wavelets", mono(u"Commun. Pure Appl. Math. 41, 909 (1988)"), LS(45)],
            [u"Candès, Romberg, Tao：Robust Uncertainty Principles", mono(u"IEEE Trans. Inf. Theory 52, 489 (2006)"), LS(46)],
            [u"Donoho：Compressed Sensing", mono(u"IEEE Trans. Inf. Theory 52, 1289 (2006)"), LS(46)],
        ]),
    ],
}

REFERENCES = [FORMULAS, PAPERS]
