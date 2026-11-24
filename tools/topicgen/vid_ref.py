# -*- coding: utf-8 -*-
"""用提示詞製作影片：參考頁。"""
from ai_common import guide, vocab
import vid_a as C

TABLE = vocab(u"速查表", u"影片提示詞速查表", u"鏡頭運動、景別、節奏、聲音、轉場與規格的常用詞彙", [
  (u"影片提示詞結構", [u"#", u"元素", u"例子"], [[u"1", u"景別", u"Medium shot"], [u"2", u"主體", u"a detective in a trench coat"], [u"3", u"動作（含順序）", u"slowly turns, then smiles"], [u"4", u"場景與光線", u"neon-lit street at night, rain"], [u"5", u"鏡頭運動", u"slow push-in"], [u"6", u"風格", u"cinematic, 35mm film look"], [u"7", u"長度與節奏", u"8 seconds, slow"], [u"8", u"聲音", u"Audio: rain, distant sirens"]]),
  (u"鏡頭運動", [u"中文", u"英文", u"效果"], [[u"固定", u"static shot, locked-off", u"讓表演說話"], [u"推", u"push in / dolly in", u"張力、意識到"], [u"拉", u"pull out / dolly out", u"揭露、孤單、結尾"], [u"左右搖", u"pan left / right", u"跟隨、掃視"], [u"上下搖", u"tilt up / down", u"介紹角色、揭示"], [u"橫移", u"truck left / right", u"視差、立體"], [u"跟拍", u"tracking / follow shot", u"跟隨角色"], [u"環繞", u"orbit / arc shot", u"英雄時刻"], [u"升降", u"crane / jib up", u"壯觀的開場"], [u"空拍", u"aerial drone shot", u"建立鏡頭"], [u"FPV", u"FPV drone shot", u"高速穿越"], [u"手持", u"handheld", u"紀實、緊張"], [u"滑動變焦", u"dolly zoom", u"震驚、暈眩"], [u"甩鏡", u"whip pan", u"快速轉場"]]),
  (u"時間與節奏", [u"詞彙", u"效果"], [[u"slow motion, 120fps", u"放大瞬間"], [u"ultra slow motion, high-speed camera", u"肉眼看不到的瞬間"], [u"time-lapse", u"壓縮時間"], [u"hyperlapse", u"移動中的縮時"], [u"reverse motion", u"超現實"], [u"freeze frame", u"時間停止"], [u"real-time", u"正常速度"]]),
  (u"聲音", [u"層次", u"寫法"], [[u"對白", u"He says in Mandarin: \"...\""], [u"語氣", u"whispers / shouts / says warmly"], [u"環境音", u"Audio: rain, crowd chatter, wind"], [u"音效", u"SFX: footsteps, door creaks"], [u"安靜", u"No music, no dialogue, only ambient sound"]]),
  (u"轉場", [u"名稱", u"英文", u"用途"], [[u"直接切", u"cut", u"最常用"], [u"動作切", u"match on action", u"順暢"], [u"溶接", u"dissolve", u"時間流逝、回憶"], [u"匹配剪接", u"match cut", u"形狀相似的畫面"], [u"跳接", u"jump cut", u"刻意的急促感"], [u"淡入淡出", u"fade in / out", u"開始與結束"]]),
  (u"平台規格", [u"平台", u"比例", u"建議"], [[u"YouTube", u"16:9", u"1080p 或 4K、24/30 fps"], [u"Shorts／Reels／TikTok", u"9:16", u"1080×1920、前 1～2 秒抓注意、字幕"], [u"IG／FB 貼文", u"1:1、4:5", u"字幕、靜音可讀"], [u"電影感", u"2.39:1", u"16:9 中加黑邊"]]),
  (u"排錯速查", [u"問題", u"對策"], [[u"手或臉變形", u"簡化動作、讓手靜止或在畫面外"], [u"鏡頭亂動", u"寫 static shot 或指定運動"], [u"動作沒發生", u"動作放前面、具體動詞"], [u"臉部漂移", u"縮短鏡頭、角色參考、切鏡頭"], [u"文字亂碼", u"後製加字"], [u"風格不一致", u"風格聖經、參考圖、統一調色"]]),
])
GUIDE = guide(u"互動實驗室", u"影片提示詞互動實驗室", [(u"影片提示詞組合器（第 3 課）", C.VBUILD), (u"景別（第 6 課）", C.SHOTSIZE), (u"鏡頭運動（第 7 課）", C.CAMOVE), (u"時長與成本估算（第 24 課）", C.COST)], u"本課程的四個互動工具")
REFERENCES = [TABLE, GUIDE]
