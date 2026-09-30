# -*- coding: utf-8 -*-
"""檔案格式解剖學：MIDI 一課（樣本）。

範例檔：一個 63 位元組的 MIDI，以鋼琴依序彈 Do、Mi、Sol 各一拍（120 BPM）。
所有圖解與課文中的位元組都由這裡的 MIDI_BYTES 計算，不手打。
"""
import base64
import struct
from fmt_common import *

PPQ = 480                     # 每四分音符的 tick 數
TEMPO = 500000                # 每四分音符的微秒數（＝120 BPM）
NOTES = [(60, u"C4 Do"), (64, u"E4 Mi"), (67, u"G4 Sol")]


def _track():
    ev = []
    ev.append(b"\x00\xFF\x51\x03" + struct.pack(">I", TEMPO)[1:])        # 速度
    ev.append(b"\x00\xC0\x00")                                          # 音色：0 號鋼琴
    for n, _ in NOTES:
        ev.append(b"\x00" + bytes([0x90, n, 100]))                      # Note On
        ev.append(vlq(PPQ) + bytes([0x80, n, 64]))                      # 一拍後 Note Off
    ev.append(b"\x00\xFF\x2F\x00")                                      # 音軌結束
    return ev


EVENTS = _track()
TRACK = b"".join(EVENTS)
HEADER = b"MThd" + struct.pack(">IHHH", 6, 0, 1, PPQ)
MIDI_BYTES = HEADER + b"MTrk" + struct.pack(">I", len(TRACK)) + TRACK
assert len(HEADER) == 14 and len(TRACK) == 41 and len(MIDI_BYTES) == 63
assert vlq(480) == b"\x83\x60" and vlq(127) == b"\x7F" and vlq(128) == b"\x81\x00"
TEMPO_OFF = 22 + 4
PROG_OFF = 22 + len(EVENTS[0]) + 2
assert MIDI_BYTES[TEMPO_OFF:TEMPO_OFF + 3] == b"\x07\xA1\x20" and MIDI_BYTES[PROG_OFF - 1] == 0xC0
DATA_URI = "data:audio/midi;base64," + base64.b64encode(MIDI_BYTES).decode("ascii")


def freq(n):
    return 440.0 * 2 ** ((n - 69) / 12.0)


assert abs(freq(60) - 261.63) < 0.01

# ---------- 圖解 ----------

# 區段：位移範圍依實際位元組計算
_o = 22
_seg = []
for i, e in enumerate(EVENTS):
    _seg.append((_o, _o + len(e)))
    _o += len(e)
_REG = [
    (0, 4, GOLD, u"MThd：檔頭區塊標記"),
    (4, 14, ORANGE, u"檔頭內容：長度、格式、音軌數、解析度"),
    (14, 22, PURPLE, u"MTrk：音軌標記＋長度（41）"),
    (_seg[0][0], _seg[1][1], TEAL, u"速度 120 BPM、音色：鋼琴"),
    (_seg[2][0], _seg[7][1], GREEN, u"三個音：按下／放開"),
    (_seg[8][0], _seg[8][1], RED, u"音軌結束"),
]
_HEX, _HEX_H = hexdump(MIDI_BYTES, _REG, legend_cols=2, heading=u"一個完整的 MIDI 檔：只有 63 個位元組")
_HEXFIG = svg(_HEX)


def _piano_roll():
    out = [title(u"同一段音樂的兩種樣子：鋼琴捲簾與事件清單")]
    x0, y0, bw = 70, 40, 90
    names = [(67, u"G4"), (64, u"E4"), (60, u"C4")]
    for i, (n, lab) in enumerate(names):
        yy = y0 + i * 30
        out.append(R(x0, yy, 3 * bw, 28, LINE, "var(--surface)", 0, 0.8))
        out.append(T(x0 - 8, yy + 18, lab, 9.5, MUTED, "end"))
    for k, (n, lab) in enumerate(NOTES):
        row = [67, 64, 60].index(n)
        out.append(R(x0 + k * bw + 3, y0 + row * 30 + 4, bw - 6, 20, GREEN, GREEN, 4, 1, op=0.6))
    for k in range(4):
        out.append(T(x0 + k * bw, y0 + 110, u"%d" % (k * PPQ), 8.5))
    out.append(T(x0 + 1.5 * bw, y0 + 126, u"時間（tick，每拍 480）", 9))
    ev_lines = [(u"0", u"速度 ＝ 500,000 µs／拍"), (u"0", u"音色 ＝ 0（鋼琴）"),
                (u"0", u"按下 60（C4），力度 100"), (u"480", u"放開 60"),
                (u"0", u"按下 64（E4）"), (u"480", u"放開 64"),
                (u"0", u"按下 67（G4）"), (u"480", u"放開 67"), (u"0", u"音軌結束")]
    out.append(T(420, y0 + 2, u"等待", 9.5, ACC, "end"))
    out.append(T(432, y0 + 2, u"事件", 9.5, ACC, "start"))
    for i, (d, s) in enumerate(ev_lines):
        yy = y0 + 20 + i * 17
        out.append(T(420, yy, d, 9.5, TXT, "end"))
        out.append(T(432, yy, s, 9.5, GREEN if u"60" in s or u"64" in s or u"67" in s else TXT, "start"))
    out.append(T(320, 230, u"MIDI 存的是右邊這張「清單」：每個事件前面寫著「距離上一個事件要等多久」", 9.5, ACC))
    return svg(out)


_ROLL = _piano_roll()


def _vlq_fig():
    out = [title(u"可變長度數量：480 怎麼變成 83 60")]
    out.append(T(320, 50, u"480（十進位）＝ 1 1110 0000（二進位，9 個位元）", 11, TXT))
    out.append(T(320, 76, u"① 從右邊每 7 個位元切一段：  0000011 │ 1100000", 10.5, MUTED))
    out.append(box(90, 96, 200, 62, u"第 1 個位元組：83", [u"1｜0000011", u"最高位 1＝後面還有"], ORANGE))
    out.append(box(350, 96, 200, 62, u"第 2 個位元組：60", [u"0｜1100000", u"最高位 0＝到此結束"], GREEN))
    out.append(T(320, 186, u"② 讀回來：3 × 128 ＋ 96 ＝ 480", 11, ACC))
    out.append(T(320, 212, u"好處：小的數字（大部分事件的間隔）只要 1 個位元組；大的數字才用更多位元組", 9.5))
    return svg(out)


_VLQ = _vlq_fig()

_SIZE = svg(
    title(u"同一首 3 分鐘的歌，存成不同格式大約多大"),
    bars(210, 40, 360, 150, [(u"WAV（CD 音質）", 31.8, BLUE), (u"MP3（128 kbps）", 2.9, ORANGE),
                             (u"MIDI（中等複雜度）", 0.05, GREEN)], 32, 10, u"約 %g MB", horizontal=True),
    T(320, 216, u"WAV：44,100 × 2 聲道 × 2 位元組 × 180 秒；MP3：128,000 ÷ 8 × 180 秒", 9.5),
    T(320, 236, u"MIDI 只記錄「彈什麼、何時彈」，所以小了幾百到上千倍——但它本身沒有聲音", 9.5, ACC),
)
assert round(44100 * 2 * 2 * 180 / 1e6, 1) == 31.8 and round(128000 / 8 * 180 / 1e6, 1) == 2.9

_HDR_ROWS = [
    [u"00–03", hexbytes(MIDI_BYTES[0:4]), u"「MThd」", u"這是 MIDI 檔頭區塊（魔術數字）"],
    [u"04–07", hexbytes(MIDI_BYTES[4:8]), u"6", u"接下來的檔頭內容有 6 個位元組"],
    [u"08–09", hexbytes(MIDI_BYTES[8:10]), u"0", u"格式 0：所有聲部放在同一條音軌"],
    [u"0A–0B", hexbytes(MIDI_BYTES[10:12]), u"1", u"共有 1 條音軌"],
    [u"0C–0D", hexbytes(MIDI_BYTES[12:14]), u"480", u"每個四分音符切成 480 個 tick"],
    [u"0E–11", hexbytes(MIDI_BYTES[14:18]), u"「MTrk」", u"音軌區塊開始"],
    [u"12–15", hexbytes(MIDI_BYTES[18:22]), u"%d" % len(TRACK), u"音軌內容有 41 個位元組"],
]

LESSON = lesson(u"MIDI：不存聲音，只存「誰在何時彈了哪個音」",
  u"一首三分鐘的歌，MP3 要 3 MB，MIDI 可能只要幾十 KB——因為它存的根本不是聲音",
  [u"說出 MIDI 和 WAV、MP3 在本質上的差別",
   u"逐位元組讀懂一個 MIDI 檔的檔頭與音軌",
   u"理解可變長度數量（VLQ）與 tick 時間的換算",
   u"解釋為什麼同一個 MIDI 在不同裝置上聽起來不一樣"],
  [("p", u"前幾課的 WAV、MP3 都在想辦法記錄<strong>聲波</strong>：每秒取樣幾萬次，再想辦法壓縮。"
        u"MIDI 走的是完全不同的路——它不記錄聲音，而是記錄<strong>演奏的動作</strong>："
        u"第幾拍按下哪個琴鍵、按多用力、什麼時候放開。它比較像一張給電腦看的樂譜。"),
   ("h", u"1. 樂譜 vs. 錄音"),
   ("t", [u"", u"WAV／MP3", u"MIDI"],
    [[u"存的是什麼", u"聲波的樣本（錄音）", u"演奏事件（樂譜）"],
     [u"聲音從哪來", u"檔案本身", u"播放端的音源（合成器、音色庫）"],
     [u"檔案大小", u"大（MB 等級）", u"極小（KB 等級）"],
     [u"能不能改一個音", u"很難", u"很容易：改一個數字"],
     [u"能不能存人聲", u"可以", u"不行"]]),
   ("FIGX", _SIZE, "0 0 640 250", u"MIDI 小得驚人，因為它只存指令，不存波形。"),
   ("h", u"2. 拆開一個真正的 MIDI 檔"),
   ("p", u"下面是一個完整、可以播放的 MIDI 檔，全部只有 <strong>63 個位元組</strong>，"
        u"內容是用鋼琴依序彈 Do、Mi、Sol 各一拍。"
        u"<a download=\"do-mi-sol.mid\" href=\"" + DATA_URI + u"\">下載這個檔案</a>，"
        u"用播放器打開聽聽看，再用 Hex 檢視器打開對照下圖。"),
   ("FIGX", _HEXFIG, "0 0 640 %d" % _HEX_H, u"整個檔案分成一個檔頭區塊（MThd）和一個音軌區塊（MTrk）。"),
   ("p", u"MIDI 和 PNG 一樣採用<strong>區塊</strong>結構（" + LS(5) + u"）：每個區塊開頭是 4 個字母的名稱，"
        u"接著 4 個位元組寫出內容長度。讀取程式遇到不認識的區塊，只要依長度跳過即可。"
        u"注意 MIDI 的整數是<strong>大端序</strong>（高位在前，" + LS(3) + u"），所以 <code>00 00 00 06</code> 就是 6。"),
   ("h", u"3. 檔頭逐位元組"),
   ("t", [u"位移", u"位元組", u"值", u"意思"], _HDR_ROWS),
   ("h", u"4. 音軌：一連串「等待＋事件」"),
   ("FIGX", _ROLL, "0 0 640 245", u"左邊是我們熟悉的鋼琴捲簾，右邊是檔案實際存的事件清單。"),
   ("p", u"音軌裡的每個事件都是「<strong>先等多久（delta time）</strong>，再做什麼」。"
        u"最常見的事件只有三個位元組："),
   ("t", [u"事件", u"第 1 個位元組", u"第 2 個", u"第 3 個", u"範例"],
    [[u"按下琴鍵（Note On）", u"9n（n＝聲道 0～15）", u"音高 0～127", u"力度 0～127",
      hexbytes(EVENTS[2][1:])],
     [u"放開琴鍵（Note Off）", u"8n", u"音高", u"放開力度", hexbytes(EVENTS[3][2:])],
     [u"換音色（Program Change）", u"Cn", u"音色編號 0～127", u"—", hexbytes(EVENTS[1][1:])],
     [u"設定速度（Meta）", u"FF 51 03", u"每拍微秒數（3 個位元組）", u"", hexbytes(EVENTS[0][1:])],
     [u"音軌結束（Meta）", u"FF 2F 00", u"—", u"—", hexbytes(EVENTS[-1][1:])]]),
   ("p", u"音高用 0～127 的整數表示，<strong>60 是中央 C（C4）</strong>，每加 1 就高半音。"
        u"要換算成頻率，用公式 <code>f ＝ 440 × 2^((n − 69) ÷ 12)</code>：69 是 A4＝440 Hz，"
        u"60 算出來約 %.2f Hz。" % freq(60)),
   ("h", u"5. 等待時間怎麼存：可變長度數量"),
   ("FIGX", _VLQ, "0 0 640 230", u"每個位元組只用 7 個位元存數字，最高位元當作「後面還有」的旗標。"),
   ("p", u"等待時間的單位是 <strong>tick</strong>。檔頭寫著每拍 480 tick，速度事件寫著每拍 500,000 微秒，"
        u"所以 480 tick ＝ 0.5 秒，也就是每分鐘 120 拍。同一個檔案只要改掉速度事件的 3 個位元組，整首歌就會變快或變慢，"
        u"音高完全不受影響——這在 MP3 裡是很難做到的。"),
   ("h", u"6. 為什麼同一個 MIDI 聽起來不一樣"),
   ("p", u"檔案裡只寫著「音色 0 號」，並沒有附上鋼琴的聲音。真正發出聲音的是播放端的<strong>音源</strong>："
        u"作業系統內建的合成器、電子琴，或是專業的音色庫。"
        u"<strong>General MIDI</strong> 標準規定了 128 種音色的編號（例如 0 是大鋼琴、40 是小提琴），"
        u"並規定第 10 聲道專門給鼓組使用，所以不同裝置至少「樂器種類」會一致，但音質可以天差地遠。"),
   ("h", u"7. 省位元組的小技巧：執行狀態"),
   ("p", u"如果連續好幾個事件的類型和聲道都相同，後面的事件可以省略第一個位元組，直接寫音高和力度，"
        u"稱為<strong>執行狀態</strong>（running status）。很多 MIDI 檔還會用「力度 0 的 Note On」來代替 Note Off，"
        u"好讓整串事件都能共用同一個狀態位元組。讀取程式判斷的方法是：資料位元組的最高位元一定是 0，"
        u"狀態位元組的最高位元一定是 1。")],
  u"下載上面的 do-mi-sol.mid，用 Hex 編輯器把位移 0x%02X 的 <code>00</code>（音色）改成 <code>28</code>（十進位 40，小提琴），"
  u"或把位移 0x%02X～0x%02X 的速度 <code>07 A1 20</code> 改成 <code>0F 42 40</code>（1,000,000 微秒＝60 BPM），"
  u"存檔後再播放，聽聽看有什麼不同。" % (PROG_OFF, TEMPO_OFF, TEMPO_OFF + 2),
  [u"為什麼 MIDI 檔比 MP3 小那麼多？它缺少了什麼？",
   u"<code>90 40 64</code> 代表什麼意思？",
   u"可變長度數量 <code>81 00</code> 代表多少？",
   u"每拍 480 tick、速度 500,000 微秒，960 tick 是幾秒？"])
