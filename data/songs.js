// 歌曲資料庫，與樂器無關——吉他、烏克麗麗的歌曲頁共用同一份，
// 各自頁面用自己的和弦資料庫（data/chords.js 或 data/ukulele-chords.js）畫指法圖。
//
// 新增歌曲：把歌曲物件加進下面的陣列即可，兩邊頁面會自動出現。
//
// 兩種內容格式，依歌曲版權狀況擇一：
//
// 1) chordsOnly: true —— 只列出段落與和弦進行，不含歌詞。
//    版權歌曲（絕大多數流行歌）一律用這個格式，避免在公開網站重製歌詞。
//    sections: [{ label: "段落名稱", chords: ["G","C",...], repeat: 4（選填，重複次數） }]
//
// 2) lines —— 逐行「和弦＋歌詞片段」交錯陣列，只能用在公版／原創／已取得授權的歌詞。
//    lines: [[{ chord: "C", lyric: "Twinkle " }, { chord: "G", lyric: "twinkle little " }, ...], ...]

window.SONGS_DATA = [
  {
    id: "qing-tian",
    title: "晴天",
    artist: "周杰倫",
    key: "G",
    capo: 0,
    chordsOnly: true,
    note:
      "版權原因，這裡只收錄和弦進行、不含歌詞。原曲部分段落用 D/F#（低音落在 F# 的 D 和弦），這裡簡化成一般 D 和弦方便初學者彈奏。建議邊聽原曲邊對照段落練習換和弦的時間點。",
    sections: [
      { label: "前奏", chords: ["Em7", "Cadd9", "G", "D"], repeat: 4 },
      { label: "主歌", chords: ["Em7", "Cadd9", "G", "G", "D"] },
      {
        label: "副歌",
        chords: ["G", "G", "Em", "Em", "C", "D", "G", "G", "B7", "B7", "Em", "Em", "C", "C", "Am7", "D"]
      },
      { label: "間奏", chords: ["G", "C", "Am7", "D"] },
      { label: "說唱", chords: ["G", "G", "C", "C", "Am7", "Am7", "C", "D"] }
    ]
  }
];
