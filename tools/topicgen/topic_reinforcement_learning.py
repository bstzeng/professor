# -*- coding: utf-8 -*-
"""強化學習主題的規格。"""
import rfl_a, rfl_c, rfl_e, rfl_g, rfl_ref

TOPIC = {
    "id": "reinforcement-learning",
    "category": "ai",
    "title": u"強化學習：從吃角子老虎到 AlphaGo 與 RLHF",
    "short": u"強化學習",
    "crumb": u"強化學習",
    "icon": u"🎰",
    "description": u"代理人、環境、獎勵與信用分配；多臂吃角子老虎：增量更新、ε-貪婪、樂觀初始值、UCB、湯普森抽樣、遺憾與萊—羅賓斯下界、A/B 測試與情境式吃角子老虎；"
                   u"馬可夫決策過程、折扣、V 與 Q、貝爾曼方程式；策略評估與改進、價值迭代、壓縮映射；蒙地卡羅、時序差分、SARSA、Q-learning、懸崖行走、資格跡；"
                   u"函數近似與致命三角、DQN、經驗回放、Double DQN 與 Rainbow；策略梯度定理、REINFORCE、基線、Actor-Critic、PPO、SAC；MCTS、AlphaGo、AlphaZero、MuZero、AlphaStar；RLHF、DPO 與推理模型；獎勵駭客與未來。附六個互動模擬。",
}

MODULES = rfl_a.MODULES + rfl_c.MODULES + rfl_e.MODULES + rfl_g.MODULES
REFERENCES = rfl_ref.REFERENCES
