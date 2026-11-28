# -*- coding: utf-8 -*-
from kx_base import table, guide
import kty_a as C
REFERENCES = [table(u"速查表", u"打字機速查表", u"年表、鍵盤與名詞", [
  (u"年表", [u"年份", u"事件"], [[u"1714", u"米爾的寫字機器專利"], [u"1865 前後", u"馬林－漢森的寫字球"], [u"1868", u"肖爾斯等人的打字機專利"], [u"1874", u"雷明頓打字機上市"], [u"1878", u"Shift 鍵（雷明頓 2 號）"], [u"1888", u"盲打比賽"], [u"1915", u"杉本京太和文打字機；周厚坤中文打字機"], [u"1920 年代", u"舒式華文打字機"], [u"1936", u"德沃夏克鍵盤專利"], [u"1947", u"林語堂明快打字機"], [u"1961", u"IBM Selectric"], [u"1964", u"IBM MT/ST：文書處理"], [u"1976", u"倉頡輸入法"]]),
  (u"鍵盤本位列", [u"配置", u"左手", u"右手"], [[u"QWERTY", u"A S D F", u"J K L ;"], [u"德沃夏克", u"A O E U", u"H T N S"], [u"Colemak", u"A R S T", u"N E I O"]]),
  (u"打字機留下的詞", [u"名詞", u"由來"], [[u"Shift", u"滾筒移位打大寫"], [u"Tab", u"表格定位器 tabulator"], [u"CR／LF", u"滑架回歸、捲紙一行"], [u"CC", u"carbon copy 複寫副本"], [u"Courier", u"1955 年 IBM 打字機字型"]]),
]), guide(u"互動實驗室", u"打字機互動實驗室", [(u"鍵盤配置比較（第 6 課）", C.LAYOUT), (u"打字速度（第 8 課）", C.SPEED), (u"複寫紙（第 10 課）", C.CARBON), (u"中文字盤（第 16 課）", C.TRAY)], C.KTYLIB, u"本課程的四個互動練習")]
