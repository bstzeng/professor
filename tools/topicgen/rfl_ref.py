# -*- coding: utf-8 -*-
"""強化學習：參考頁——公式速查表、年表。"""
from rfl_common import LS, M

CHEATSHEET = {
    "file": "cheatsheet.html", "title": u"強化學習公式速查表", "h1": u"強化學習公式速查表", "icon": u"📐",
    "description": u"吃角子老虎、貝爾曼方程式、TD、Q-learning、策略梯度、PPO、RLHF 的核心公式",
    "body": [
        ("h", u"吃角子老虎"),
        ("t", [u"公式", u"說明", u"課"], [
            [M(r"Q_{n+1} = Q_n + \alpha(R_n - Q_n)"), u"增量更新", LS(7)],
            [M(r"Q_t(a) + c\sqrt{\ln t/N_t(a)}"), u"UCB", LS(10)],
            [M(r"\theta_a \sim \text{Beta}(\alpha_a, \beta_a)"), u"湯普森抽樣", LS(11)],
            [M(r"L_T = \sum_a\mathbb{E}[N_T(a)]\Delta_a"), u"累積遺憾", LS(12)],
        ]),
        ("h", u"MDP 與貝爾曼方程式"),
        ("t", [u"公式", u"說明", u"課"], [
            [M(r"G_t = R_{t+1} + \gamma G_{t+1}"), u"回報的遞迴", LS(17)],
            [M(r"v_\pi(s) = \sum_a\pi(a|s)\sum_{s'}p(s'|s,a)[r + \gamma v_\pi(s')]"), u"貝爾曼期望方程式", LS(19)],
            [M(r"q_*(s,a) = \sum_{s'}p(s'|s,a)[r + \gamma\max_{a'}q_*(s',a')]"), u"貝爾曼最優方程式", LS(20)],
            [M(r"\|\mathcal Tu - \mathcal Tv\|_\infty \le \gamma\|u - v\|_\infty"), u"壓縮映射", LS(25)],
        ]),
        ("h", u"無模型學習"),
        ("t", [u"公式", u"說明", u"課"], [
            [M(r"V(S) \leftarrow V(S) + \alpha[G_t - V(S)]"), u"蒙地卡羅", LS(27)],
            [M(r"\delta = R + \gamma V(S') - V(S)"), u"TD 誤差", LS(28)],
            [M(r"Q(S,A) \leftarrow Q(S,A) + \alpha[R + \gamma Q(S',A') - Q(S,A)]"), u"SARSA", LS(29)],
            [M(r"Q(S,A) \leftarrow Q(S,A) + \alpha[R + \gamma\max_aQ(S',a) - Q(S,A)]"), u"Q-learning", LS(30)],
            [M(r"y = r + \gamma Q(s', \arg\max_{a'}Q(s',a';\mathbf w);\mathbf w^-)"), u"Double DQN", LS(38)],
        ]),
        ("h", u"策略梯度"),
        ("t", [u"公式", u"說明", u"課"], [
            [M(r"\nabla J = \mathbb{E}[\sum_t\nabla\ln\pi(A_t|S_t)\,G_t]"), u"策略梯度定理", LS(41)],
            [M(r"A(s,a) = q(s,a) - v(s)"), u"優勢函數", LS(42)],
            [M(r"\min(r_tA_t,\ \mathrm{clip}(r_t, 1-\epsilon, 1+\epsilon)A_t)"), u"PPO", LS(44)],
            [M(r"\ell = (z - v)^2 - \boldsymbol\pi^\top\ln\mathbf p"), u"AlphaGo Zero 損失", LS(50)],
            [M(r"P(y_A \succ y_B) = \sigma(r_A - r_B)"), u"布拉德利—特里", LS(52)],
            [M(r"-\ln\sigma(\beta\ln\frac{\pi(y_w)}{\pi_{\text{ref}}(y_w)} - \beta\ln\frac{\pi(y_l)}{\pi_{\text{ref}}(y_l)})"), u"DPO", LS(53)],
        ]),
    ],
}

TIMELINE = {
    "file": "timeline.html", "title": u"強化學習年表", "h1": u"強化學習年表", "icon": u"⏳",
    "description": u"從桑代克的迷籠到推理模型",
    "body": [
        ("t", [u"年份", u"事件", u"課"], [
            [u"1898", u"桑代克的迷籠實驗與效果律", LS(4)],
            [u"1933", u"湯普森抽樣", LS(11)],
            [u"1957", u"貝爾曼：動態規劃與貝爾曼方程式", LS(19)],
            [u"1959", u"山謬的西洋跳棋程式", LS(4)],
            [u"1961", u"米奇的火柴盒井字遊戲機 MENACE", LS(4)],
            [u"1985", u"萊與羅賓斯的遺憾下界", LS(12)],
            [u"1988", u"薩頓：時序差分學習", LS(28)],
            [u"1989", u"華金斯：Q-learning", LS(30)],
            [u"1990", u"薩頓：Dyna", LS(47)],
            [u"1992", u"TD-Gammon；威廉斯：REINFORCE", LS(28)],
            [u"1998", u"薩頓與巴托《強化學習：導論》", LS(4)],
            [u"2002", u"UCB1", LS(10)],
            [u"2006", u"UCT 與蒙地卡羅樹搜尋", LS(48)],
            [u"2013／2015", u"DQN 玩 Atari", LS(36)],
            [u"2015", u"TRPO、DDPG、Double DQN", LS(44)],
            [u"2016", u"AlphaGo 擊敗李世乭；A3C", LS(49)],
            [u"2017", u"PPO、Rainbow、AlphaGo Zero、AlphaZero", LS(50)],
            [u"2018", u"SAC、TD3", LS(45)],
            [u"2019", u"OpenAI Five、AlphaStar、MuZero", LS(51)],
            [u"2022", u"InstructGPT 與 ChatGPT（RLHF）", LS(52)],
            [u"2023", u"DPO", LS(53)],
            [u"2024～2025", u"推理模型 o1、DeepSeek-R1；薩頓與巴托獲 2024 年度圖靈獎", LS(53)],
        ]),
    ],
}

REFERENCES = [CHEATSHEET, TIMELINE]
