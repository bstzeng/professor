# -*- coding: utf-8 -*-
"""第 31 課：Computer use——沒有 API 可呼叫時，讓代理「看螢幕、動滑鼠、打字」。
迴圈：截圖 → 模型看圖決定動作（點哪個座標、輸入什麼）→ 執行 → 再截圖。
這裡用文字畫面模擬一個登入表單，模型「看到」的是畫面描述。"""
from mockllm import MockClient, text, tool_use

class Screen(object):
    def __init__(self):
        self.fields = {"帳號": "", "密碼": ""}
        self.focus = None
        self.page = "login"
        self.layout = {"帳號": (100, 80), "密碼": (100, 120), "登入": (100, 170)}   # 元件中心座標

    def screenshot(self):
        if self.page == "home":
            return "[畫面] 歡迎回來，xiaoan！（首頁）"
        return "[畫面] 登入頁｜帳號框@(100,80)=「%s」｜密碼框@(100,120)=「%s」｜[登入]按鈕@(100,170)" % (
            self.fields["帳號"], "•" * len(self.fields["密碼"]))

    def left_click(self, x, y):
        for name, (cx, cy) in self.layout.items():
            if abs(x - cx) < 60 and abs(y - cy) < 15:
                if name == "登入":
                    self.page = "home" if self.fields["帳號"] and self.fields["密碼"] else "login"
                else:
                    self.focus = name
                return "OK"
        return "OK（點到空白處）"

    def type(self, text):
        if self.focus:
            self.fields[self.focus] += text
        return "OK"

scr = Screen()
PLAN = [("screenshot", {}), ("left_click", {"x": 100, "y": 80}), ("type", {"text": "xiaoan"}),
        ("left_click", {"x": 100, "y": 120}), ("type", {"text": "s3cret"}), ("left_click", {"x": 100, "y": 170}), ("screenshot", {})]

def policy(ctx):
    if ctx.turn < len(PLAN):
        return tool_use(*PLAN[ctx.turn])
    return text("已登入成功。")

tools = [{"name": n, "description": n, "input_schema": {"type": "object"}} for n in ("screenshot", "left_click", "type")]
client, msgs = MockClient(policy), [{"role": "user", "content": "幫我用帳號 xiaoan 登入"}]
while True:
    r = client.messages.create(model="mock", max_tokens=500, tools=tools, messages=msgs)
    msgs.append({"role": "assistant", "content": r.content})
    if r.stop_reason != "tool_use":
        break
    b = r.content[0]
    out = getattr(scr, b.name)(**b.input)
    print("%-11s %-28s → %s" % (b.name, b.input, out))
    msgs.append({"role": "user", "content": [{"type": "tool_result", "tool_use_id": b.id, "content": out}]})
print(r.content[0].text, "（共 %d 個動作；比呼叫 API 慢得多，也更容易出錯——能用 API 就用 API）" % len(PLAN))
