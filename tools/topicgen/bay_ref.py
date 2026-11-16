# -*- coding: utf-8 -*-
"""貝氏統計：參考頁——公式表、論文。"""
from bay_common import LS, M


def mono(s):
    return u'<span style="font-family:ui-monospace,Menlo,monospace;font-size:0.9em">%s</span>' % s


FORMULAS = {
    "file": "formulas.html", "title": u"公式表", "h1": u"貝氏統計公式表", "icon": u"📐",
    "description": u"貝氏定理、共軛模型、貝氏因子與 MCMC 的速查表",
    "body": [
        ("t", [u"名稱", u"公式", u"課"], [
            [u"貝氏定理", M(r"P(A|B) = P(B|A)P(A)/P(B)"), LS(2)],
            [u"勝算形式", M(r"\text{後驗勝算} = BF\times\text{先驗勝算}"), LS(15)],
            [u"Beta—二項式", M(r"\text{Beta}(a,b)\to\text{Beta}(a+k,\,b+n-k)"), LS(7)],
            [u"繼承法則", M(r"(k+1)/(n+2)"), LS(13)],
            [u"常態—常態", M(r"1/\tau_1^2 = 1/\tau_0^2 + 1/\sigma^2"), LS(8)],
            [u"卜瓦松—伽瑪", M(r"\text{Gamma}(\alpha,\beta)\to\text{Gamma}(\alpha+K,\,\beta+n)"), LS(9)],
            [u"梅特羅波利斯接受率", M(r"\min(1,\,\pi(\theta')/\pi(\theta))"), LS(19)],
            [u"ELBO", M(r"\log p(D) = \text{ELBO} + D_{\text{KL}}(q\|p)"), LS(23)],
            [u"脊迴歸 = 常態先驗", M(r"\lambda = \sigma^2/\tau^2"), LS(25)],
            [u"邊際似然", M(r"p(D|M) = \int p(D|\theta)p(\theta)d\theta"), LS(27)],
            [u"布萊爾分數", M(r"\frac1N\sum(p_i - o_i)^2"), LS(36)],
        ]),
        ("h", u"傑佛瑞斯的貝氏因子尺度"),
        ("t", [u"BF", u"證據"], [[u"1～3", u"幾乎不值一提"], [u"3～10", u"中等"], [u"10～30", u"強"], [u"30～100", u"非常強"], [u"> 100", u"決定性"]]),
    ],
}

PAPERS = {
    "file": "papers.html", "title": u"論文與書籍", "h1": u"貝氏統計的重要文獻", "icon": u"📄",
    "description": u"從貝葉斯到 NUTS 的原始文獻",
    "body": [
        ("t", [u"文獻", u"出處", u"課"], [
            [u"Bayes, Price：An Essay towards solving a Problem in the Doctrine of Chances", mono(u"Phil. Trans. R. Soc. 53, 370 (1763)"), LS(13)],
            [u"Laplace：Mémoire sur la probabilité des causes par les événements", mono(u"1774"), LS(13)],
            [u"Jeffreys：Theory of Probability", mono(u"Oxford, 1939"), LS(14)],
            [u"Metropolis 等：Equation of State Calculations by Fast Computing Machines", mono(u"J. Chem. Phys. 21, 1087 (1953)"), LS(19)],
            [u"Lindley：A Statistical Paradox", mono(u"Biometrika 44, 187 (1957)"), LS(31)],
            [u"Kalman：A New Approach to Linear Filtering and Prediction Problems", mono(u"J. Basic Eng. 82, 35 (1960)"), LS(8)],
            [u"Hastings：Monte Carlo sampling methods using Markov chains and their applications", mono(u"Biometrika 57, 97 (1970)"), LS(19)],
            [u"Rubin：Estimation in Parallel Randomized Experiments", mono(u"J. Educ. Stat. 6, 377 (1981)"), LS(26)],
            [u"Geman, Geman：Stochastic Relaxation, Gibbs Distributions, and the Bayesian Restoration of Images", mono(u"IEEE TPAMI 6, 721 (1984)"), LS(20)],
            [u"Duane 等：Hybrid Monte Carlo", mono(u"Phys. Lett. B 195, 216 (1987)"), LS(21)],
            [u"Gelfand, Smith：Sampling-Based Approaches to Calculating Marginal Densities", mono(u"JASA 85, 398 (1990)"), LS(20)],
            [u"Gelman, Rubin：Inference from Iterative Simulation Using Multiple Sequences", mono(u"Stat. Sci. 7, 457 (1992)"), LS(22)],
            [u"Kass, Raftery：Bayes Factors", mono(u"JASA 90, 773 (1995)"), LS(27)],
            [u"Ernst, Banks：Humans integrate visual and haptic information in a statistically optimal fashion", mono(u"Nature 415, 429 (2002)"), LS(43)],
            [u"Ioannidis：Why Most Published Research Findings Are False", mono(u"PLoS Med. 2, e124 (2005)"), LS(30)],
            [u"Hoffman, Gelman：The No-U-Turn Sampler", mono(u"JMLR 15, 1593 (2014)"), LS(21)],
            [u"Open Science Collaboration：Estimating the reproducibility of psychological science", mono(u"Science 349, aac4716 (2015)"), LS(30)],
            [u"Gal, Ghahramani：Dropout as a Bayesian Approximation", mono(u"ICML 2016"), LS(41)],
            [u"Wasserstein, Lazar：The ASA Statement on p-Values", mono(u"Am. Stat. 70, 129 (2016)"), LS(30)],
            [u"Polack 等：Safety and Efficacy of the BNT162b2 mRNA Covid-19 Vaccine", mono(u"N. Engl. J. Med. 383, 2603 (2020)"), LS(38)],
            [u"Gelman 等：Bayesian Data Analysis（第三版）", mono(u"CRC Press, 2013"), LS(26)],
        ]),
    ],
}

REFERENCES = [FORMULAS, PAPERS]
