# -*- coding: utf-8 -*-
# LeetCode 題解主題的題目清單。
# 新增一題：在 PROBLEMS 裡加一筆，並在 bodies/ 放對應的 NNNN.html。

PROBLEMS = [
    {
        "num": 1,
        "en": "Two Sum",
        "zh": "兩數之和",
        "difficulty": "Easy",
        "tags": ["陣列", "雜湊表"],
        "desc": "從暴力法到一趟雜湊表：四種解法、複雜度對照與常見陷阱。",
    },
    {
        "num": 2,
        "en": "Add Two Numbers",
        "zh": "兩數相加",
        "difficulty": "Medium",
        "tags": ["鏈結串列", "數學", "遞迴"],
        "desc": "鏈結串列上的直式加法：虛擬頭節點、進位處理、遞迴版本，以及「轉成整數再加」為何是陷阱。",
    },
    {
        "num": 3,
        "en": "Longest Substring Without Repeating Characters",
        "zh": "無重複字元的最長子字串",
        "difficulty": "Medium",
        "tags": ["雜湊表", "字串", "滑動視窗"],
        "desc": "滑動視窗的標準範本：從 O(n³) 暴力法一路優化到一趟掃描的 O(n)。",
    },
]

DIFFICULTY_ZH = {"Easy": "簡單", "Medium": "中等", "Hard": "困難"}

# 側邊欄與主題頁的分組：每 25 題一組，題目變多時自動延伸。
GROUP_SIZE = 25


def group_label(num):
    start = ((num - 1) // GROUP_SIZE) * GROUP_SIZE + 1
    return u"第 %03d–%03d 題" % (start, start + GROUP_SIZE - 1)


def grouped():
    """回傳 [(group_label, [problem, ...]), ...]，依題號排序。"""
    out = []
    for p in sorted(PROBLEMS, key=lambda x: x["num"]):
        label = group_label(p["num"])
        if not out or out[-1][0] != label:
            out.append((label, []))
        out[-1][1].append(p)
    return out


def course_title(p):
    return u"%d. %s %s" % (p["num"], p["en"], p["zh"])


def slug(p):
    return u"problem-%04d" % p["num"]
