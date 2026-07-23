#!/usr/bin/env python3
"""
從課程 HTML 檔案掃描 data-ko="..." 屬性，為每個獨特的韓文字串
生成真實語音檔（macOS `say` 命令 + ffmpeg 轉檔），存進 audio/ko/。

檔名規則：對韓文文字做 URL 百分比編碼（percent-encoding），與
js/korean-audio.js 裡的 encodeURIComponent() 完全一致，兩邊各自
獨立算出同一個檔名，不需要維護額外的對照表。

用法：
    python3 tools/gen-korean-audio.py topics/korean/lesson-02.html
    python3 tools/gen-korean-audio.py topics/korean/lesson-*.html
    python3 tools/gen-korean-audio.py --voice Yuna --rate 150 topics/korean/lesson-02.html

需求：僅能在裝有 macOS `say` 指令與韓文語音（例如 Yuna）的機器上執行，
以及系統已安裝 ffmpeg（用於將 say 產生的 AIFF 轉成 mp3）。
"""

import argparse
import glob
import os
import re
import subprocess
import sys

AUDIO_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "audio", "ko")


def extract_ko_texts(html_path):
    with open(html_path, encoding="utf-8") as f:
        content = f.read()
    return sorted(set(re.findall(r'data-ko="([^"]+)"', content)))


def audio_filename(text):
    # 檔名直接用原始韓文文字（不是百分比編碼字串）——網頁瀏覽器請求
    # 的 URL 會是百分比編碼過的（例如 %EC%95%84.mp3），但 HTTP 伺服器
    # 在對應到檔案系統路徑之前，會自動把 URL 解碼回原始文字，所以磁碟
    # 上實際存放的檔名必須是解碼後的原始文字，兩邊才會對上。
    return text + ".mp3"


def generate_one(text, voice, rate, force):
    fname = audio_filename(text)
    out_path = os.path.join(AUDIO_DIR, fname)
    if os.path.exists(out_path) and not force:
        return fname, "skip (exists)"

    aiff_path = out_path.replace(".mp3", ".aiff")
    try:
        subprocess.run(
            ["say", "-v", voice, "-r", str(rate), "-o", aiff_path, text],
            check=True, capture_output=True, text=True,
        )
        subprocess.run(
            ["ffmpeg", "-y", "-i", aiff_path, "-codec:a", "libmp3lame",
             "-qscale:a", "4", "-ar", "22050", out_path],
            check=True, capture_output=True, text=True,
        )
    finally:
        if os.path.exists(aiff_path):
            os.remove(aiff_path)

    if not os.path.exists(out_path) or os.path.getsize(out_path) == 0:
        return fname, "FAILED (empty output)"
    return fname, "generated"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("html_files", nargs="+", help="課程 HTML 檔案（支援 shell 萬用字元）")
    ap.add_argument("--voice", default="Yuna", help="macOS 語音名稱（預設 Yuna）")
    ap.add_argument("--rate", type=int, default=150, help="語速，字詞/分鐘（預設 150，略慢於預設值方便學習）")
    ap.add_argument("--force", action="store_true", help="即使音檔已存在也重新生成")
    args = ap.parse_args()

    os.makedirs(AUDIO_DIR, exist_ok=True)

    all_texts = set()
    for pattern in args.html_files:
        for path in sorted(glob.glob(pattern)):
            texts = extract_ko_texts(path)
            print(f"{path}: {len(texts)} 個獨特韓文字串")
            all_texts.update(texts)

    print(f"\n總共 {len(all_texts)} 個獨特字串，開始生成音檔...\n")

    generated = skipped = failed = 0
    for text in sorted(all_texts):
        fname, status = generate_one(text, args.voice, args.rate, args.force)
        print(f"  {status:20s} {fname}  ({text})")
        if status == "generated":
            generated += 1
        elif status.startswith("skip"):
            skipped += 1
        else:
            failed += 1

    print(f"\n完成：{generated} 個新生成、{skipped} 個略過（已存在）、{failed} 個失敗")
    if failed:
        sys.exit(1)


if __name__ == "__main__":
    main()
