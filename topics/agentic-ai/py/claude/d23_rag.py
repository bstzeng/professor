# -*- coding: utf-8 -*-
"""第 23 課（Claude API 版）：檢索到的段落用 document 區塊送進去，並開啟 citations，
Claude 的回答會附上精確的引用位置（cited_text）。"""
import anthropic

client = anthropic.Anthropic()
hits = ["退貨：商品到貨 7 天內可申請退貨，需保持包裝完整。",
        "退款：退貨審核通過後，款項於 5 個工作天內退回原付款方式。"]   # 由你的檢索器取得
content = [{"type": "document", "source": {"type": "text", "media_type": "text/plain", "data": h},
            "title": "客服手冊段落 %d" % i, "citations": {"enabled": True}} for i, h in enumerate(hits, 1)]
content.append({"type": "text", "text": "退貨之後錢多久會退回來？只根據文件回答。"})

r = client.messages.create(model="claude-opus-5-5", max_tokens=16000, messages=[{"role": "user", "content": content}])
for b in r.content:
    if b.type == "text":
        print(b.text, end="")
        for c in (b.citations or []):
            print("  ⟨引用：%s｜%s⟩" % (c.document_title, c.cited_text), end="")
print()
