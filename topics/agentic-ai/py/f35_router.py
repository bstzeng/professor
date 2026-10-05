# -*- coding: utf-8 -*-
"""第 35 課：路由（routing）與交接（handoff）。
路由器先判斷問題類型，交給專門的代理；專門代理處理不了時，可以把對話「交接」給另一個代理。"""
from mockllm import MockClient, text

def classify(q):
    r = MockClient(lambda ctx: text("billing" if any(w in q for w in ("扣款", "發票", "退費")) else
                                    "tech" if any(w in q for w in ("當機", "錯誤", "登入")) else "general"))
    return r.messages.create(model="mock", max_tokens=10, system="只輸出 billing / tech / general 其中之一",
                             messages=[{"role": "user", "content": q}]).content[0].text

AGENTS = {
    "billing": lambda q: "【帳務代理】已查到重複扣款，3 個工作天內退回。" if "扣款" in q else "HANDOFF:tech",
    "tech": lambda q: "【技術代理】請清除快取後重新登入；若仍失敗，我幫你重設密碼。",
    "general": lambda q: "【一般客服】我們的營業時間是 9:00～18:00。",
}

def handle(q):
    route = classify(q)
    print("問題：%s\n  路由 → %s" % (q, route))
    ans = AGENTS[route](q)
    if ans.startswith("HANDOFF:"):                     # 交接：把原問題與已知資訊轉給另一個代理
        to = ans.split(":")[1]
        print("  帳務代理判斷不是帳務問題 → 交接給 %s" % to)
        ans = AGENTS[to](q)
    print("  " + ans)

for q in ["這個月被扣款兩次！", "App 一直顯示登入錯誤", "你們幾點開門？", "發票上的登入帳號錯誤"]:
    handle(q)
print("\n好處：每個代理的提示與工具都很聚焦；路由本身可以用小而快的模型。")
