# -*- coding: utf-8 -*-
"""用提示詞製作照片：參考頁。"""
from ai_common import guide, vocab
import pho_a as C

TABLE = vocab(u"速查表", u"影像提示詞速查表", u"景別、機位、鏡頭、光線、色彩、風格與參數的常用詞彙", [
  (u"提示詞結構", [u"#", u"元素", u"例子"], [[u"1", u"主體", u"an elderly tea farmer"], [u"2", u"動作與表情", u"smiling, holding a basket of tea leaves"], [u"3", u"場景", u"on a misty tea plantation in Alishan"], [u"4", u"景別", u"medium shot"], [u"5", u"機位", u"eye level"], [u"6", u"鏡頭", u"85mm, f/1.8, shallow depth of field"], [u"7", u"光線", u"soft morning light, backlit"], [u"8", u"色彩", u"muted greens, warm highlights"], [u"9", u"風格與媒材", u"documentary photography, Kodak Portra 400"]]),
  (u"景別", [u"中文", u"英文", u"用途"], [[u"大特寫", u"extreme close-up", u"眼睛、細節"], [u"特寫", u"close-up", u"臉部、情緒"], [u"近景", u"medium close-up", u"胸部以上"], [u"中景", u"medium shot", u"腰部以上、動作"], [u"全景", u"full shot", u"全身、服裝"], [u"遠景", u"wide shot", u"人物與環境"], [u"大遠景", u"extreme wide shot", u"地點、規模"]]),
  (u"機位與視角", [u"中文", u"英文", u"效果"], [[u"平視", u"eye level", u"中性、自然"], [u"仰角", u"low angle", u"強大、壯觀"], [u"俯角", u"high angle", u"弱小、全局"], [u"鳥瞰", u"bird's-eye view / top-down", u"圖案、版面"], [u"蟲視", u"worm's-eye view", u"極度誇張的高大"], [u"荷蘭角", u"Dutch angle", u"不安、緊張"], [u"過肩", u"over-the-shoulder", u"對話、關係"], [u"第一人稱", u"POV", u"沉浸感"]]),
  (u"鏡頭與景深", [u"詞彙", u"效果"], [[u"14–24mm wide angle", u"誇張的透視、空間感"], [u"35mm", u"紀實、街拍"], [u"50mm", u"接近人眼"], [u"85mm portrait lens", u"人像、壓縮背景"], [u"200mm telephoto", u"強烈壓縮、遠距"], [u"macro lens", u"微距細節"], [u"f/1.4, shallow depth of field, bokeh", u"背景模糊"], [u"f/11, deep focus", u"前後都清楚"], [u"tilt-shift", u"微縮模型感"]]),
  (u"光線", [u"詞彙", u"效果"], [[u"golden hour", u"溫暖、浪漫"], [u"blue hour", u"冷靜、都市"], [u"overcast soft light", u"柔和、無陰影"], [u"Rembrandt lighting", u"臉頰三角光、戲劇"], [u"butterfly lighting", u"美妝、明星"], [u"split lighting", u"半明半暗、神祕"], [u"rim light / backlight", u"輪廓、分離背景"], [u"low-key", u"暗調、戲劇"], [u"high-key", u"明亮、乾淨"], [u"neon lighting", u"賽博、夜晚"], [u"volumetric light, god rays", u"光束、氛圍"]]),
  (u"色彩", [u"詞彙", u"效果"], [[u"complementary colors (teal and orange)", u"強烈對比"], [u"analogous palette", u"和諧"], [u"monochromatic", u"統一、極簡"], [u"pastel colors", u"柔和、可愛"], [u"muted / desaturated", u"沉穩、文藝"], [u"vibrant / saturated", u"活潑、廣告"], [u"warm tones / cool tones", u"溫暖／冷靜"], [u"black and white", u"經典、紀實"]]),
  (u"底片與質感", [u"詞彙", u"效果"], [[u"Kodak Portra 400", u"溫暖柔和的膚色"], [u"Fujifilm Velvia", u"飽和的風景"], [u"Ilford HP5", u"黑白顆粒"], [u"Polaroid", u"復古、褪色"], [u"film grain", u"顆粒"], [u"35mm film photo", u"底片感"], [u"disposable camera, flash", u"即可拍、生活感"]]),
  (u"常見參數（以 Midjourney 為例）", [u"參數", u"作用"], [[u"--ar 3:2", u"畫面比例"], [u"--seed 1234", u"固定隨機種子"], [u"--stylize（--s）", u"風格化程度"], [u"--chaos", u"結果的多樣性"], [u"--no", u"排除元素"], [u"--sref", u"風格參考"], [u"--raw", u"較少預設美化"]]),
])
GUIDE = guide(u"互動實驗室", u"影像提示詞互動實驗室", [(u"提示詞組合器（第 1 課）", C.PBUILD), (u"構圖格線（第 11 課）", C.GRID), (u"焦距與景深（第 12 課）", C.FOCAL), (u"布光圖（第 13 課）", C.LIGHT), (u"配色盤（第 14 課）", C.PALETTE), (u"畫面比例（第 20 課）", C.ASPECT)], u"本課程的六個互動工具")
REFERENCES = [TABLE, GUIDE]
