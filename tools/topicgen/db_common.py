# -*- coding: utf-8 -*-
"""扯鈴主題共用小工具：YouTube 搜尋連結產生器。"""
from urllib.parse import quote


def yt(keyword, label=None):
    label = label or keyword
    url = "https://www.youtube.com/results?search_query=" + quote(keyword)
    return ('<a href="%s" target="_blank" rel="noopener">YouTube 搜尋「%s」</a>'
            % (url, label))


def video_note(keyword, extra=""):
    text = ("這個動作靠純文字很難傳達手感與節奏，建議先看示範影片：" + yt(keyword) + "。")
    if extra:
        text += extra
    return ("note", "影片輔助", [("p", text)])
