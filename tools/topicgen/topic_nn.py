# -*- coding: utf-8 -*-
"""神經網路與深度學習主題的規格。"""
import nn_a, nn_e, nn_ref

TOPIC = {
    "id": "deep-learning",
    "category": "ai",
    "title": u"神經網路與深度學習：從一個神經元到 Transformer",
    "short": u"深度學習基礎",
    "crumb": u"深度學習基礎",
    "icon": u"🧠",
    "description": u"給沒有機器學習背景的人：從線性迴歸、損失函數、梯度下降開始，補上向量、矩陣、導數與連鎖律；感知器與 XOR、激活函數、多層網路、softmax 與 MNIST；"
                   u"反向傳播、學習率、SGD／Adam、批次、過擬合、正規化、初始化、Batch／Layer Norm；CNN 與 ResNet、遷移學習；RNN、LSTM、seq2seq 與注意力；"
                   u"Word2Vec 與上下文表示；Transformer、自注意力、BERT、GPT 與縮放定律。附十個互動工具（梯度下降、神經網路遊樂場、卷積核、詞向量、自注意力等）。",
}

MODULES = nn_a.MODULES + nn_e.MODULES

REFERENCES = nn_ref.REFERENCES
