# -*- coding: utf-8 -*-
"""第 3 課：呼叫 LLM API 的基本形狀——system、messages、角色交替。
API 是「無狀態」的：每次呼叫都要把整段對話重新送過去。"""
from mockllm import MockClient, text

def policy(ctx):
    # 假模型：能「記得」名字，只因為整段歷史每次都被送進來
    for m in ctx.messages:
        if m["role"] == "user" and "我叫" in m["content"]:
            name = m["content"].split("我叫")[1].strip("。 ")
            if "名字" in ctx.user_text():
                return text("你叫%s。（我是從你送來的對話歷史裡讀到的）" % name)
    if "名字" in ctx.user_text():
        return text("我不知道你的名字——這次送來的訊息裡沒有提到。")
    return text("你好！（system 要我：%s）" % ctx.system)

client = MockClient(policy)
system = "用繁體中文、一句話回答。"
history = []

def send(msg):
    history.append({"role": "user", "content": msg})
    r = client.messages.create(model="mock", max_tokens=300, system=system, messages=history)
    history.append({"role": "assistant", "content": r.content})
    print("使用者：%s\n模型　：%s   (送出 %d tokens)" % (msg, r.content[0].text, r.usage.input_tokens))

send("嗨，我叫小安。")
send("我的名字是什麼？")
print("\n歷史共有 %d 則訊息，角色依序：%s" % (len(history), [m["role"] for m in history]))

# 如果「忘了」把歷史送回去，模型就真的不知道：
r = client.messages.create(model="mock", max_tokens=300, system=system,
                           messages=[{"role": "user", "content": "我的名字是什麼？"}])
print("不送歷史 →", r.content[0].text)
