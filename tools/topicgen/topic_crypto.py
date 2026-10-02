# -*- coding: utf-8 -*-
"""加密貨幣主題的規格。"""
import cc_a, cc_k, cc_ref

TOPIC = {
    "id": "crypto-currency",
    "category": "finance",
    "title": "加密貨幣：從密碼學原理到比特幣、以太坊與穩定幣",
    "short": "加密貨幣",
    "crumb": "加密貨幣",
    "icon": "₿",
    "description": "錢是什麼、數位支付為什麼有雙重支付難題；比特幣之前的 eCash、Hashcash、b-money；雜湊、公私鑰、數位簽章與地址；"
                   "比特幣的交易、區塊鏈、默克爾樹、挖礦、難度、最長鏈、減半與 51% 攻擊；從創世區塊到 ETF 的歷史；以太坊、智慧合約、"
                   "The DAO、權益證明與 Rollup；穩定幣、DeFi、NFT、交易所與錢包；FTX、Terra 等事件、詐騙防範、監管與 CBDC。"
                   "附 SHA-256、簽章、區塊鏈竄改、挖礦等互動實驗。教育用途，不構成投資建議。",
}

MODULES = cc_a.MODULES + cc_k.MODULES

REFERENCES = cc_ref.REFERENCES
