# -*- coding: utf-8 -*-
"""第 49 課（Claude API 版）：上線時的錯誤處理。
SDK 會自動重試連線錯誤、408/409/429/5xx（預設 2 次，可調 max_retries）。
另外示範：伺服器端備援（fallbacks，beta）——遇到安全分類器拒答時由伺服器自動改用合適模型；以及 refusal 停止原因。"""
import anthropic

client = anthropic.Anthropic(max_retries=4, timeout=120.0)

try:
    r = client.beta.messages.create(
        model="claude-opus-5-5",
        max_tokens=16000,
        betas=["server-side-fallback-2026-07-01"],
        fallbacks="default",
        messages=[{"role": "user", "content": "用一句話介紹代理迴圈。"}],
    )
    if r.stop_reason == "refusal":
        print("被拒絕：", r.stop_details)
    else:
        print(next(b.text for b in r.content if b.type == "text"))
    print("request id（回報問題時附上）：", r._request_id)
except anthropic.BadRequestError as e:          # 400：請求本身有錯，重試沒用
    print("請求錯誤：", e.message)
except anthropic.RateLimitError as e:           # 429：SDK 已重試過仍失敗
    print("被限流，請稍後再試；retry-after =", e.response.headers.get("retry-after"))
except anthropic.APIStatusError as e:
    print("API 錯誤 %d：%s" % (e.status_code, e.message))
except anthropic.APIConnectionError:
    print("網路連線失敗")
