# -*- coding: utf-8 -*-
"""作業系統是怎麼寫出來的：模組 A（開始之前）、B（開機）、C（中斷與例外）、D（記憶體管理）。"""
from sa_common import *

lesson = make_lesson("os")

_JOBS = svg(
    title(u"作業系統的三件事"),
    box(14, 46, 196, 130, u"抽象化", [u"把硬體變成好用的概念", u"檔案、行程、socket", u"程式不必認識磁碟型號"], BLUE),
    box(222, 46, 196, 130, u"保護", [u"程式之間互相隔離", u"使用者程式不能直接", u"碰硬體或核心記憶體"], RED),
    box(430, 46, 196, 130, u"資源管理", [u"CPU 時間、記憶體、", u"磁碟、網路頻寬", u"公平又有效率地分配"], GREEN),
    T(320, 204, u"核心（kernel）就是負責這三件事、以最高權限執行的那段程式", 9.5, ACC),
)

_KARCH = svg(
    title(u"三種核心架構"),
    R(20, 40, 180, 160, BLUE, "none", 6, 1.5), T(110, 58, u"單體式核心", 11, BLUE),
    R(30, 70, 160, 120, BLUE, BLUE, 4, 1, op=0.15), T(110, 110, u"排程・記憶體・檔案系統", 9, TXT), T(110, 126, u"驅動・網路…", 9, TXT), T(110, 146, u"全部在核心空間", 9, MUTED),
    R(230, 40, 180, 160, PURPLE, "none", 6, 1.5), T(320, 58, u"微核心", 11, PURPLE),
    R(240, 150, 160, 40, PURPLE, PURPLE, 4, 1, op=0.15), T(320, 174, u"IPC・排程・記憶體", 9, TXT),
    [R(240 + i * 55, 84, 50, 50, PURPLE, "none", 4, 1) for i in range(3)], [T(265 + i * 55, 112, s, 8.5, TXT) for i, s in enumerate([u"檔案", u"驅動", u"網路"])],
    T(320, 76, u"使用者空間的伺服器", 8.5, MUTED),
    R(440, 40, 180, 160, ORANGE, "none", 6, 1.5), T(530, 58, u"混合式", 11, ORANGE),
    R(450, 70, 160, 120, ORANGE, ORANGE, 4, 1, op=0.15), T(530, 110, u"微核心的結構", 9, TXT), T(530, 126, u"但大部分服務放回核心", 9, TXT), T(530, 146, u"兼顧效能", 9, MUTED),
    T(110, 224, u"Linux", 10, TXT), T(320, 224, u"MINIX 3、seL4、QNX", 10, TXT), T(530, 224, u"Windows NT、macOS XNU", 10, TXT),
)

_TOOLS = svg(
    title(u"開發環境"),
    flow([(u"原始碼", [u"C＋組合語言"]), (u"交叉編譯", [u"x86_64-elf-gcc"]), (u"連結", [u"→ kernel.elf"]), (u"開機映像", [u"ISO 檔"]), (u"QEMU 執行", [u"GDB 除錯"])], 70, 50, 10, 630, 8,
         [BLUE, ORANGE, PURPLE, TEAL, GREEN]),
    T(320, 150, u"核心不能用一般的 libc，也不能依賴作業系統——因為我們就是作業系統", 9.5, ACC),
)

_BOOT = [(u"按下電源", u"CPU 從固定位址開始執行主機板上的韌體。", 0),
         (u"韌體自我檢測", u"BIOS 或 UEFI 檢查記憶體、初始化基本硬體（POST）。", 0),
         (u"找到開機程式", u"BIOS：讀取磁碟第一個磁區（MBR，512 位元組，結尾 0x55AA）到 0x7C00 執行。UEFI：從 EFI 系統分割區（FAT 格式）載入 .efi 程式。", 1),
         (u"開機載入程式", u"GRUB、Limine 等讀取核心檔案到記憶體，取得記憶體地圖、畫面資訊，切換 CPU 模式。", 1),
         (u"跳進核心", u"執行核心的進入點 <code>_start</code>：設定堆疊，呼叫 <code>kmain()</code>。", 2),
         (u"初始化", u"記憶體管理、中斷表、計時器、裝置驅動依序就緒。", 3),
         (u"第一個使用者程式", u"核心建立第一個行程（Linux 的 init／systemd），由它啟動其他服務與登入畫面。", 4)]
_BOOTB = [u"韌體", u"開機程式", u"核心進入點", u"核心初始化", u"使用者空間"]

_MODES = svg(
    title(u"x86 CPU 的三種模式"),
    box(14, 46, 196, 120, u"真實模式（16 位元）", [u"開機時的模式", u"只能用 1 MB 記憶體", u"沒有保護"], GRAY),
    box(222, 46, 196, 120, u"保護模式（32 位元）", [u"GDT 定義區段", u"4 GB、特權等級", u"可開分頁"], BLUE),
    box(430, 46, 196, 120, u"長模式（64 位元）", [u"必須開啟分頁", u"48 位元虛擬位址", u"現代作業系統的模式"], GREEN),
    A(210, 106, 220, 106, MUTED), A(418, 106, 428, 106, MUTED),
    T(320, 194, u"UEFI 和現代開機程式會幫我們切好長模式，核心一開始就在 64 位元環境", 9.5, ACC),
)

_VGA = svg(
    title(u"VGA 文字模式：顯示記憶體在 0xB8000"),
    cells(40, 50, [u"H", u"07", u"i", u"07", u"!", u"4F"], 60, 30, [BLUE, ORANGE, BLUE, ORANGE, BLUE, ORANGE]),
    [T(70 + i * 120, 102, u"字元", 9, BLUE) for i in range(3)], [T(130 + i * 120, 102, u"顏色", 9, ORANGE) for i in range(3)],
    T(440, 64, u"每格 2 位元組：", 10, TXT, "start"), T(440, 80, u"字元＋前景／背景色", 10, TXT, "start"),
    T(320, 136, u"80×25 格，寫進這塊記憶體，字就出現在螢幕上；UEFI 開機則改用像素 framebuffer", 9.5, ACC),
)

_INTR = svg(
    title(u"中斷：CPU 被打斷，跳去處理，再回來"),
    P("M40 80 H260", BLUE, sw=3), P("M260 80 L300 140", MUTED, sw=1.5, dash="4 3"),
    R(300, 120, 200, 40, ORANGE, ORANGE, 6, 1, op=0.2), T(400, 145, u"中斷處理程式", 10, ORANGE),
    P("M500 140 L540 80", MUTED, sw=1.5, dash="4 3"), P("M540 80 H620", BLUE, sw=3),
    T(150, 70, u"正在執行的程式", 10, BLUE), T(270, 110, u"事件發生", 9, RED, "end"), T(580, 70, u"繼續", 10, BLUE),
    T(400, 112, u"保存暫存器 → 處理 → 還原 → iretq", 9, MUTED),
    box(20, 180, 190, 56, u"硬體中斷", [u"計時器、鍵盤、網卡"], GREEN), box(225, 180, 190, 56, u"例外", [u"除以零、分頁錯誤"], RED),
    box(430, 180, 190, 56, u"軟體觸發", [u"系統呼叫"], PURPLE),
)

_IDT = svg(
    title(u"中斷描述表（IDT）：256 個入口"),
    cells(30, 50, [u"0", u"1", u"…", u"13", u"14", u"…", u"32", u"33", u"…", u"255"], 58, 28,
          [RED, RED, None, RED, RED, None, GREEN, GREEN, None, PURPLE]),
    T(118, 100, u"0～31：CPU 例外", 9.5, RED), T(400, 100, u"32 以後：硬體中斷（重新對應後）", 9.5, GREEN),
    T(320, 130, u"每個入口記錄：處理程式的位址、程式碼區段、權限等級、類型", 9.5, ACC),
    T(320, 148, u"用 lidt 指令把整張表的位址交給 CPU", 9.5, MUTED),
)

_MMAP = svg(
    title(u"開機時的實體記憶體地圖（示意）"),
    R(30, 50, 580, 40, MUTED, "none", 0, 1),
    R(30, 50, 40, 40, GRAY, GRAY, 0, 1, op=0.5), R(70, 50, 30, 40, ORANGE, ORANGE, 0, 1, op=0.5), R(100, 50, 320, 40, GREEN, GREEN, 0, 1, op=0.4),
    R(420, 50, 50, 40, RED, RED, 0, 1, op=0.4), R(470, 50, 140, 40, GREEN, GREEN, 0, 1, op=0.4),
    T(50, 110, u"低位保留", 8.5, TXT), T(85, 128, u"BIOS/ACPI", 8.5, TXT), T(260, 110, u"可用（核心也在這）", 9, GREEN), T(445, 128, u"裝置映射", 8.5, RED), T(540, 110, u"可用", 9, GREEN),
    T(320, 160, u"開機程式從韌體取得這張表（E820 或 UEFI 記憶體地圖），核心只能使用標示「可用」的區域", 9.5, ACC),
)

_PT = svg(
    title(u"x86-64 的四層頁表：48 位元虛擬位址怎麼拆"),
    cells(20, 50, [u"PML4", u"PDPT", u"PD", u"PT", u"偏移"], 118, 30, [BLUE, TEAL, GREEN, ORANGE, PURPLE], size=11),
    [T(79 + i * 118, 98, s, 9.5, MUTED) for i, s in enumerate([u"9 位元", u"9 位元", u"9 位元", u"9 位元", u"12 位元"])],
    flow([u"CR3", u"PML4 表", u"PDPT 表", u"PD 表", u"PT 表", (u"實體頁框", [u"＋偏移"])], 120, 40, 10, 630, 6, [GRAY, BLUE, TEAL, GREEN, ORANGE, PURPLE]),
    T(320, 190, u"每層 512 個入口（2⁹）；一頁 4 KB（2¹²）；TLB 快取最近的轉換，避免每次都查四層", 9.5, ACC),
)

_KSPACE = svg(
    title(u"64 位元位址空間的典型配置（類 Linux）"),
    R(200, 40, 240, 200, MUTED, "none", 4, 1.5),
    R(200, 40, 240, 70, PURPLE, PURPLE, 0, 1, op=0.2), T(320, 70, u"核心空間（上半部）", 10, PURPLE), T(320, 88, u"所有行程共用", 9, MUTED),
    R(200, 110, 240, 40, GRAY, GRAY, 0, 1, op=0.15), T(320, 134, u"非正規位址（不能用）", 9, MUTED),
    R(200, 150, 240, 90, BLUE, BLUE, 0, 1, op=0.15), T(320, 186, u"使用者空間（下半部）", 10, BLUE), T(320, 204, u"每個行程各自不同", 9, MUTED),
    T(460, 46, u"0xFFFF…", 9, TXT, "start"), T(460, 236, u"0x0000…", 9, TXT, "start"),
    T(180, 70, u"核心程式碼、直接映射", 9, TXT, "end"), T(180, 86, u"所有實體記憶體", 9, TXT, "end"),
    T(180, 170, u"程式碼、堆積", 9, TXT, "end"), T(180, 186, u"共用函式庫、堆疊", 9, TXT, "end"),
)

_SLAB = svg(
    title(u"slab 配置器：同樣大小的物件放在一起"),
    box(20, 46, 180, 140, u"kmalloc(48)", [u"從 64 位元組", u"的快取拿一格"], BLUE),
    R(240, 50, 380, 40, MUTED, "none", 4, 1), [R(244 + i * 46, 54, 42, 32, GREEN if i in (0, 1, 3) else MUTED, GREEN if i in (0, 1, 3) else "none", 3, 1, op=0.3) for i in range(8)],
    T(430, 104, u"64 位元組物件的 slab（一頁切成 64 格）", 9, MUTED),
    R(240, 120, 380, 40, MUTED, "none", 4, 1), [R(244 + i * 92, 124, 88, 32, ORANGE if i in (1,) else MUTED, ORANGE if i == 1 else "none", 3, 1, op=0.3) for i in range(4)],
    T(430, 174, u"task_struct 專用的 slab", 9, MUTED),
    T(320, 210, u"頁框配置器只會給整頁；slab 把頁切成小格，配置與釋放都只要 O(1)", 9.5, ACC),
)

_COW = svg(
    title(u"寫入時複製（Copy-on-Write）"),
    box(20, 46, 150, 50, u"父行程", [u"頁表"], BLUE), box(20, 140, 150, 50, u"子行程（fork 後）", [u"頁表"], GREEN),
    R(260, 90, 120, 50, PURPLE, PURPLE, 4, 1, op=0.2), T(320, 112, u"同一個實體頁", 10, PURPLE), T(320, 128, u"標記為唯讀", 9, MUTED),
    A(170, 72, 258, 104, MUTED), A(170, 164, 258, 128, MUTED),
    R(470, 120, 140, 50, ORANGE, ORANGE, 4, 1, op=0.2), T(540, 142, u"子行程寫入時", 10, ORANGE), T(540, 158, u"才複製一份", 9, MUTED),
    P("M380 128 L468 140", ORANGE, sw=1.5, dash="4 3"),
    T(320, 218, u"fork 幾乎是瞬間完成；大部分頁面從來沒有被寫過，也就永遠不必複製", 9.5, ACC),
)

MODULES = [
(u"模組 A｜開始之前", [

lesson(u"作業系統要做哪些事",
  u"抽象化、保護、資源管理",
  [u"理解作業系統的三大職責",
   u"區分核心與使用者程式",
   u"認識本主題的學習地圖"],
  [fig(_JOBS, 214, u"作業系統的三大職責。"),
   ("p", u"本主題用「寫一個極簡的教學用核心」當主線：從開機印出第一行字開始，一路做到能執行使用者程式、讀檔案、跑一個簡單的 Shell。每一步都對照 Linux、Windows、macOS 的真實做法。"),
   ("t", [u"模組", u"做出什麼"],
         [[u"B 開機", u"從開機到 <code>kmain()</code> 印出 Hello"], [u"C 中斷", u"處理例外、計時器、鍵盤"],
          [u"D 記憶體", u"實體頁框、分頁、核心堆積"], [u"E 行程", u"情境切換、排程、系統呼叫、使用者程式"],
          [u"F 檔案與裝置", u"驅動模型、磁碟、檔案系統"], [u"G 讓它能用", u"終端機、Shell、管線、libc"]]),
   ("p", u"概念性的作業系統介紹（行程、排程、虛擬記憶體）可以先看 " + XL("cs") + u"；本主題著重「實際怎麼寫」。"),
  ],
  u"作業系統負責抽象化、保護與資源管理；核心是以最高權限執行、實現這些功能的程式。",
  [u"作業系統的三大職責是什麼？",
   u"核心和一般程式有什麼不同？",
   u"本主題的主線是什麼？"]),

lesson(u"核心架構：單體式、微核心、混合式",
  u"東西要放在核心裡，還是外面",
  [u"比較三種核心架構",
   u"理解效能與穩定的取捨",
   u"知道主流作業系統的選擇"],
  [fig(_KARCH, 236, u"三種核心架構。"),
   ("t", [u"架構", u"優點", u"缺點"],
         [[u"單體式", u"服務之間直接呼叫，效能好", u"一個驅動出錯可能讓整個系統當掉"],
          [u"微核心", u"服務在使用者空間，彼此隔離，可單獨重啟", u"服務之間靠訊息傳遞（IPC），開銷較大"],
          [u"混合式", u"保留模組化設計，效能關鍵部分放核心", u"實際上更接近單體式"]]),
   ("p", u"Linux 雖然是單體式，但支援<strong>可載入核心模組</strong>，驅動可以在執行時載入卸載。本主題的教學核心採單體式，最容易理解。"),
  ],
  u"單體式效能好、微核心隔離好；主流系統多半是單體式或混合式。",
  [u"單體式核心的主要缺點是什麼？",
   u"微核心的服務之間怎麼溝通？",
   u"Linux 是哪一種架構？"]),

lesson(u"開發環境",
  u"交叉編譯器、QEMU、GDB",
  [u"理解為什麼需要交叉編譯",
   u"認識核心專用的編譯選項",
   u"學會用 QEMU 執行與除錯"],
  [fig(_TOOLS, 170, u"核心的開發流程。"),
   code(u"""# 核心專用的編譯選項（重點）
CFLAGS = -ffreestanding        # 沒有標準函式庫，main 不是進入點
         -fno-stack-protector  # 沒有 libc 提供的堆疊保護函式
         -mno-red-zone         # 中斷會覆蓋紅區，核心不能用
         -mcmodel=kernel       # 核心放在位址空間的最上方
         -mno-sse -mno-mmx     # 避免在中斷中使用浮點暫存器

qemu-system-x86_64 -cdrom os.iso -serial stdio -s -S   # -s -S：等待 GDB 連線"""),
   ("ul", [u"<strong>交叉編譯器</strong>：產生「沒有作業系統」的目標檔，避免意外連結到主機的 libc。",
           u"<strong>QEMU</strong>：模擬整台電腦，當掉只要重開模擬器；可以印出 CPU 狀態。",
           u"<strong>GDB</strong>：連上 QEMU，在核心程式碼設中斷點、逐步執行。"]),
  ],
  u"核心要用獨立（freestanding）的方式編譯，並在 QEMU 中執行、用 GDB 除錯。",
  [u"為什麼需要交叉編譯器？",
   u"-ffreestanding 的意義是什麼？",
   u"為什麼核心要關閉紅區？"]),

lesson(u"專案結構",
  u"開機程式、核心、函式庫、使用者程式",
  [u"認識教學核心的專案結構",
   u"理解連結器腳本",
   u"知道核心映像的組成"],
  [code(u"""myos/
├── boot/          # 開機設定（使用 Limine 開機程式）
├── kernel/
│   ├── arch/x86_64/   # 與 CPU 相關：進入點、GDT、IDT、情境切換（組合語言）
│   ├── mm/            # 記憶體管理
│   ├── sched/         # 行程與排程
│   ├── fs/            # 檔案系統
│   ├── drivers/       # 序列埠、鍵盤、磁碟
│   └── main.c         # kmain()
├── libc/          # 給使用者程式用的迷你 C 函式庫
├── user/          # 使用者程式：init、sh
└── linker.ld"""),
   code(u"""/* linker.ld：告訴連結器核心要放在記憶體的哪裡 */
ENTRY(_start)
SECTIONS {
    . = 0xffffffff80000000;          /* 核心位於位址空間最上方 2 GB */
    .text   : { *(.text*) }
    .rodata : { *(.rodata*) }
    .data   : { *(.data*) }
    .bss    : { *(COMMON) *(.bss*) }
}"""),
   ("p", u"注意 <code>arch/</code> 資料夾：和 CPU 架構有關的程式集中在這裡，其他部分用 C 寫成與架構無關，Linux 也是這樣組織的（" + LS(44) + u"）。"),
  ],
  u"核心專案依子系統分資料夾，把架構相關程式碼集中；連結器腳本決定核心在記憶體中的位置。",
  [u"arch 資料夾放什麼？",
   u"連結器腳本的 ENTRY 是什麼？",
   u"為什麼核心放在位址空間最上方？"]),
]),

(u"模組 B｜開機", [

lesson(u"按下電源之後：BIOS 與 UEFI",
  u"從韌體到開機程式",
  [u"理解開機的完整流程",
   u"比較 BIOS 與 UEFI",
   u"知道 MBR 與 EFI 系統分割區"],
  [steps(_BOOT, u"<b>開機流程</b>：一步一步看", _BOOTB),
   ("t", [u"", u"傳統 BIOS", u"UEFI"],
         [[u"開機程式位置", u"磁碟第一個磁區（MBR）", u"EFI 系統分割區中的 .efi 檔"], [u"大小限制", u"512 位元組（需分段載入）", u"一般檔案，沒有特別限制"],
          [u"開始時的 CPU 模式", u"16 位元真實模式", u"64 位元（多數平台）"], [u"分割表", u"MBR（最大 2 TB）", u"GPT"],
          [u"安全開機", u"無", u"可驗證開機程式的簽章"]]),
  ],
  u"韌體初始化硬體後載入開機程式；UEFI 比傳統 BIOS 更現代、直接在 64 位元環境載入。",
  [u"BIOS 從哪裡找開機程式？",
   u"UEFI 的開機程式是什麼格式？",
   u"安全開機做什麼？"]),

lesson(u"開機載入程式",
  u"GRUB、Limine 與開機協定",
  [u"理解開機程式的工作",
   u"認識開機協定",
   u"知道核心從開機程式得到什麼"],
  [("p", u"開機程式負責：讀取核心檔案、放到正確位置、準備好 CPU 模式，最後跳進核心。核心和開機程式之間需要一份「約定」（開機協定），說明交接時的狀態與資訊。"),
   ("t", [u"協定", u"使用者", u"交給核心的資訊"],
         [[u"Multiboot2", u"GRUB", u"記憶體地圖、framebuffer、模組、命令列"],
          [u"Limine 協定", u"Limine", u"同上，並直接進入 64 位元、已映射上半部核心"],
          [u"Linux boot protocol", u"Linux 核心", u"boot_params 結構"]]),
   code(u"""// 用 Limine 協定向開機程式「要」資訊：在核心裡放一個請求結構
__attribute__((section(".requests")))
static volatile struct limine_memmap_request memmap_req = {
    .id = LIMINE_MEMMAP_REQUEST, .revision = 0
};
// 開機後，memmap_req.response 就指向記憶體地圖"""),
   ("p", u"教學核心選用 Limine，因為它直接把我們帶進 64 位元長模式，省去大量組合語言。"),
  ],
  u"開機程式依開機協定載入核心並提供記憶體地圖等資訊；選好協定能省去許多底層工作。",
  [u"開機協定規定了什麼？",
   u"核心需要從開機程式得到哪些資訊？",
   u"為什麼教學核心選擇 Limine？"]),

lesson(u"CPU 模式：真實、保護、長模式",
  u"x86 的歷史包袱",
  [u"認識 x86 的三種模式",
   u"理解 GDT 的角色",
   u"知道進入長模式的條件"],
  [fig(_MODES, 206, u"x86 的三種模式。"),
   ("p", u"為了相容 1978 年的 8086，今天的 x86 CPU 開機時仍處於 16 位元真實模式。進入 64 位元長模式需要："),
   ("ol", [u"建立 GDT（全域描述表），定義程式碼與資料區段。",
           u"建立頁表（長模式強制要求分頁）。",
           u"開啟 CR4.PAE、設定 EFER.LME，最後開啟 CR0.PG 分頁。",
           u"遠跳躍到 64 位元的程式碼區段。"]),
   code(u"""; 64 位元下仍然需要一個極簡的 GDT
gdt:
    dq 0                      ; 空描述子
    dq 0x00AF9A000000FFFF     ; 核心程式碼（64 位元）
    dq 0x00AF92000000FFFF     ; 核心資料
    dq 0x00AFFA000000FFFF     ; 使用者程式碼（權限 3）
    dq 0x00AFF2000000FFFF     ; 使用者資料"""),
   ("p", u"即使開機程式已經切好模式，核心仍會載入自己的 GDT，因為之後要加入使用者模式的區段與 TSS（" + LS(26) + u"）。"),
  ],
  u"x86 從 16 位元真實模式一路切到 64 位元長模式；長模式需要 GDT 與分頁。",
  [u"為什麼 x86 開機時是 16 位元？",
   u"進入長模式需要哪些步驟？",
   u"核心為什麼還要自己載入 GDT？"]),

lesson(u"第一行核心程式碼",
  u"從組合語言跳到 C",
  [u"寫出核心進入點",
   u"理解堆疊的設定",
   u"知道核心停機的方式"],
  [code(u"""; arch/x86_64/entry.asm
section .bss
align 16
stack_bottom: resb 16384         ; 16 KB 的核心堆疊
stack_top:

section .text
global _start
extern kmain
_start:
    cli                          ; 先關中斷：還沒有中斷表
    mov rsp, stack_top           ; 設定堆疊——C 函式需要它
    call kmain
.hang:
    hlt                          ; 讓 CPU 休眠
    jmp .hang"""),
   code(u"""// kernel/main.c
void kmain(void) {
    serial_init();
    kprintf("Hello from myos!\\n");
    for (;;) asm volatile("hlt");
}"""),
   ("ul", [u"C 語言需要堆疊才能呼叫函式、存區域變數；在設定 <code>rsp</code> 之前不能呼叫任何 C 函式。",
           u"<code>.bss</code> 區段不佔核心檔案的空間，開機程式會把它清成 0。",
           u"<code>kmain</code> 永遠不應該回傳——回到哪裡呢？所以最後停在 <code>hlt</code> 迴圈。"]),
  ],
  u"進入點用組合語言設定堆疊後呼叫 kmain；核心的主函式永遠不回傳。",
  [u"為什麼要先 cli？",
   u"為什麼 C 函式之前必須設定堆疊？",
   u"kmain 回傳會發生什麼事？"]),

lesson(u"在螢幕上印字",
  u"VGA 文字模式與 framebuffer",
  [u"理解記憶體映射 I/O",
   u"寫出 VGA 文字輸出",
   u"知道 framebuffer 的做法"],
  [fig(_VGA, 148, u"VGA 文字模式的記憶體配置。"),
   code(u"""// 傳統 BIOS 開機：寫入 0xB8000 就會出現在螢幕上
static volatile uint16_t* const vga = (uint16_t*)0xB8000;
static int col = 0, row = 0;

void vga_putc(char c) {
    if (c == '\\n') { col = 0; row++; return; }
    vga[row * 80 + col] = (uint16_t)c | (0x07 << 8);   // 0x07：黑底灰字
    if (++col == 80) { col = 0; row++; }
}"""),
   ("p", u"這叫<strong>記憶體映射 I/O</strong>：某段實體位址其實不是 RAM，而是連到顯示卡。UEFI 開機時沒有文字模式，開機程式會給我們一塊像素 framebuffer（位址、寬、高、每列位元組數），核心需要自己畫字型點陣。"),
  ],
  u"寫入特定的記憶體位址就能控制硬體（記憶體映射 I/O）；文字模式最簡單，framebuffer 更通用。",
  [u"什麼是記憶體映射 I/O？",
   u"VGA 文字模式每格幾個位元組？",
   u"UEFI 開機時要怎麼顯示文字？"]),

lesson(u"序列埠與 kprintf",
  u"核心的除錯工具",
  [u"理解連接埠 I/O",
   u"寫出序列埠輸出",
   u"實作簡化的 kprintf"],
  [code(u"""// 連接埠 I/O：x86 另一種和裝置溝通的方式
static inline void outb(uint16_t port, uint8_t v) {
    asm volatile("outb %0, %1" :: "a"(v), "Nd"(port));
}
static inline uint8_t inb(uint16_t port) {
    uint8_t v; asm volatile("inb %1, %0" : "=a"(v) : "Nd"(port)); return v;
}

#define COM1 0x3F8
void serial_putc(char c) {
    while (!(inb(COM1 + 5) & 0x20)) ;   // 等待傳送緩衝區空出來
    outb(COM1, c);
}"""),
   code(u"""void kprintf(const char* fmt, ...) {      // 只支援 %s %d %x 的迷你版
    va_list ap; va_start(ap, fmt);
    for (; *fmt; fmt++) {
        if (*fmt != '%') { serial_putc(*fmt); continue; }
        switch (*++fmt) {
            case 's': puts(va_arg(ap, char*)); break;
            case 'd': print_dec(va_arg(ap, int)); break;
            case 'x': print_hex(va_arg(ap, uint64_t)); break;
        }
    }
    va_end(ap);
}"""),
   ("p", u"用 QEMU 的 <code>-serial stdio</code>，核心的輸出會直接出現在主機的終端機裡，可以複製、搜尋，當機前的最後訊息也不會消失。"),
  ],
  u"序列埠用連接埠 I/O 輸出文字，是核心開發最可靠的除錯管道；kprintf 是自己實作的 printf。",
  [u"連接埠 I/O 和記憶體映射 I/O 有什麼不同？",
   u"為什麼要等待傳送緩衝區？",
   u"為什麼核心不能直接用 printf？"]),
]),

(u"模組 C｜中斷與例外", [

lesson(u"中斷是什麼",
  u"硬體中斷、例外、軟體中斷",
  [u"理解中斷的概念",
   u"區分三種中斷來源",
   u"知道中斷時 CPU 做了什麼"],
  [fig(_INTR, 248, u"中斷的流程。"),
   ("p", u"沒有中斷，CPU 只能不停地問「鍵盤有按鍵嗎？」（輪詢）。有了中斷，裝置有事時主動「打斷」CPU。中斷發生時，CPU 會自動："),
   ("ol", [u"把目前的指令位址、旗標、堆疊指標推到堆疊上。",
           u"從中斷描述表找到對應的處理程式並跳過去。",
           u"處理完成後，處理程式以 <code>iretq</code> 指令回到原本的地方。"]),
   ("p", u"中斷也是作業系統能「搶回」CPU 的手段：計時器中斷讓核心定期取得控制權，才能切換行程（" + LS(25) + u"）。"),
  ],
  u"中斷讓裝置與錯誤能主動打斷 CPU；它也是核心定期取回控制權的基礎。",
  [u"中斷和輪詢有什麼不同？",
   u"中斷有哪三種來源？",
   u"為什麼計時器中斷對多工很重要？"]),

lesson(u"中斷描述表（IDT）",
  u"告訴 CPU 每種中斷該跳去哪",
  [u"理解 IDT 的結構",
   u"寫出 IDT 入口",
   u"知道中斷處理程式的骨架"],
  [fig(_IDT, 160, u"中斷描述表。"),
   code(u"""struct idt_entry {               // 長模式下每個入口 16 位元組
    uint16_t offset_lo;
    uint16_t selector;          // 核心程式碼區段
    uint8_t  ist;               // 中斷堆疊表索引（雙重錯誤用）
    uint8_t  type_attr;         // 0x8E：存在、權限 0、中斷閘
    uint16_t offset_mid;
    uint32_t offset_hi;
    uint32_t zero;
} __attribute__((packed));

static struct idt_entry idt[256];

void idt_set(int n, void* handler) {
    uint64_t a = (uint64_t)handler;
    idt[n] = (struct idt_entry){ a & 0xFFFF, KERNEL_CS, 0, 0x8E, (a >> 16) & 0xFFFF, a >> 32, 0 };
}"""),
   code(u"""; 每個向量一小段組合語言：保存暫存器後呼叫共同的 C 處理函式
isr_stub_14:
    ; 分頁錯誤：CPU 已經推了錯誤碼
    push 14                     ; 向量編號
    jmp isr_common
isr_common:
    push rax
    push rcx                    ; ……保存所有通用暫存器
    mov rdi, rsp                ; 第一個參數：指向保存的暫存器
    call interrupt_dispatch
    ; ……還原暫存器
    add rsp, 16                 ; 丟掉向量編號與錯誤碼
    iretq"""),
  ],
  u"IDT 有 256 個入口，每個指向一段處理程式；組合語言樁保存暫存器後交給 C 處理。",
  [u"IDT 有幾個入口？",
   u"為什麼需要組合語言樁？",
   u"iretq 做什麼？"]),

lesson(u"例外處理與核心恐慌",
  u"除以零、分頁錯誤、雙重錯誤",
  [u"認識常見的 CPU 例外",
   u"理解分頁錯誤的資訊",
   u"知道核心恐慌的處理"],
  [("t", [u"向量", u"例外", u"常見原因"],
         [[u"0", u"除以零（#DE）", u"整數除以 0"], [u"6", u"無效指令（#UD）", u"跳到錯誤位址執行"],
          [u"13", u"一般保護錯誤（#GP）", u"權限不足、非正規位址"], [u"14", u"分頁錯誤（#PF）", u"存取沒有映射或權限不符的頁；CR2 存著出錯位址"],
          [u"8", u"雙重錯誤（#DF）", u"處理例外時又發生例外"], [u"—", u"三重錯誤", u"連雙重錯誤都處理不了 → CPU 直接重新開機"]]),
   code(u"""void interrupt_dispatch(struct regs* r) {
    if (r->vector == 14) {
        uint64_t addr; asm volatile("mov %%cr2, %0" : "=r"(addr));
        if (handle_page_fault(addr, r->error_code)) return;   // 可處理的情況（第 22 課）
    }
    if (r->vector < 32) {
        if (from_user_mode(r)) { kill_current_process(); return; }   // 使用者程式的錯：只殺它
        panic("exception %d at %p", r->vector, r->rip);              // 核心的錯：停機
    }
    // ……硬體中斷
}"""),
   ("p", u"同樣是除以零：發生在使用者程式，核心只要終止那個程式；發生在核心裡，代表核心本身有錯，只能停機並印出資訊——Linux 的 kernel panic、Windows 的藍色畫面就是這個。"),
  ],
  u"CPU 例外會跳到核心；使用者程式的錯誤就終止該程式，核心自己的錯誤只能恐慌停機。",
  [u"分頁錯誤時 CR2 存了什麼？",
   u"什麼是三重錯誤？",
   u"使用者程式和核心發生例外時的處理有什麼不同？"]),

lesson(u"計時器中斷",
  u"作業系統的心跳",
  [u"認識計時器硬體",
   u"理解中斷控制器",
   u"實作系統時鐘"],
  [code(u"""// 舊式 PIT（8254）：輸入頻率約 1.193182 MHz，除以 N 得到中斷頻率
void pit_init(int hz) {
    uint16_t div = 1193182 / hz;
    outb(0x43, 0x36);              // 通道 0，方波模式
    outb(0x40, div & 0xFF);
    outb(0x40, div >> 8);
}

volatile uint64_t ticks;
void timer_irq(struct regs* r) {
    ticks++;
    send_eoi(0);                   // 通知中斷控制器：處理完了
    schedule_tick();               // 讓排程器決定要不要換行程（第 25 課）
}"""),
   ("ul", [u"<strong>中斷控制器</strong>：舊的 8259 PIC 預設把 IRQ 0～7 對應到向量 8～15，正好和 CPU 例外重疊，所以第一件事是把它<strong>重新對應</strong>到 32 以後。現代系統改用 APIC。",
           u"<strong>EOI</strong>：每次處理完都要告訴中斷控制器，否則不會再收到同一條線的中斷。",
           u"<strong>現代做法</strong>：每顆 CPU 有自己的 Local APIC 計時器；Linux 也支援「無滴答」模式，閒置時不產生定時中斷以省電。"]),
  ],
  u"計時器中斷提供時間來源並讓核心定期取回控制權；記得重新對應 PIC 並送出 EOI。",
  [u"為什麼要重新對應 PIC？",
   u"EOI 是什麼？",
   u"無滴答模式有什麼好處？"]),

lesson(u"鍵盤驅動",
  u"從按鍵到字元",
  [u"理解掃描碼",
   u"寫出鍵盤中斷處理",
   u"認識環形緩衝區"],
  [code(u"""// PS/2 鍵盤：IRQ1；從連接埠 0x60 讀掃描碼
static const char keymap[128] = { 0, 27, '1','2','3','4','5','6','7','8','9','0','-','=','\\b',
                                  '\\t','q','w','e','r','t','y','u','i','o','p','[',']','\\n', /* … */ };

static char buf[256]; static uint8_t head, tail;     // 環形緩衝區

void keyboard_irq(struct regs* r) {
    uint8_t sc = inb(0x60);
    if (!(sc & 0x80)) {                 // 最高位元 1 表示放開，0 表示按下
        char c = keymap[sc];
        if (c) buf[head++] = c;          // uint8_t 自動在 256 繞回
    }
    send_eoi(1);
}

int kbd_getc(void) {                     // 給終端機用（第 39 課）
    while (head == tail) asm volatile("hlt");   // 沒有字就睡到下一次中斷
    return buf[tail++];
}"""),
   ("p", u"中斷處理程式要<strong>越短越好</strong>：只把資料放進緩衝區就返回，真正的處理留給之後的程式。這個「上半部／下半部」的分工在 Linux 驅動中非常普遍。"),
  ],
  u"鍵盤中斷讀取掃描碼放進環形緩衝區；中斷處理程式只做最少的事。",
  [u"掃描碼和字元有什麼不同？",
   u"環形緩衝區的優點是什麼？",
   u"為什麼中斷處理程式要越短越好？"]),
]),

(u"模組 D｜記憶體管理", [

lesson(u"實體記憶體地圖",
  u"哪些記憶體可以用",
  [u"理解記憶體地圖",
   u"知道保留區域的來源",
   u"讀取開機程式提供的地圖"],
  [fig(_MMAP, 172, u"實體記憶體地圖（示意）。"),
   code(u"""struct limine_memmap_response* mm = memmap_req.response;
for (uint64_t i = 0; i < mm->entry_count; i++) {
    struct limine_memmap_entry* e = mm->entries[i];
    kprintf("%x - %x  %s\\n", e->base, e->base + e->length, type_name(e->type));
    if (e->type == LIMINE_MEMMAP_USABLE) pmm_add_region(e->base, e->length);
}"""),
   ("p", u"實體位址空間裡有很多「洞」：韌體資料、ACPI 表、裝置的記憶體映射 I/O（" + LS(9) + u"）。核心絕不能把這些地方當成一般記憶體使用，否則會覆蓋韌體資料或寫進裝置暫存器。"),
  ],
  u"核心從開機程式取得記憶體地圖，只把「可用」區域交給實體記憶體配置器。",
  [u"實體位址空間為什麼有「洞」？",
   u"記憶體地圖從哪裡來？",
   u"核心誤用保留區域會發生什麼事？"]),

lesson(u"實體頁框配置器",
  u"以 4 KB 為單位管理記憶體",
  [u"理解頁框的概念",
   u"實作點陣圖配置器",
   u"體驗外部碎片"],
  [widget({"t": "frames", "q": u"<b>頁框配置器</b>：配置與釋放不同大小，觀察點陣圖與碎片。"}),
   code(u"""#define PAGE 4096
static uint8_t* bitmap;           // 每個位元代表一個 4 KB 頁框：1＝使用中
static uint64_t total_frames;

uint64_t pmm_alloc(void) {
    for (uint64_t i = 0; i < total_frames; i++)
        if (!(bitmap[i / 8] & (1 << (i % 8)))) {
            bitmap[i / 8] |= 1 << (i % 8);
            return i * PAGE;          // 回傳實體位址
        }
    panic("out of memory");
}
void pmm_free(uint64_t addr) { uint64_t i = addr / PAGE; bitmap[i / 8] &= ~(1 << (i % 8)); }"""),
   ("t", [u"做法", u"特點"],
         [[u"點陣圖", u"簡單、省空間，找空位要掃描"], [u"空閒串列", u"O(1) 配置，把空閒頁串起來"],
          [u"夥伴系統（Linux）", u"以 2 的次方大小管理，合併相鄰空閒塊，減少碎片"]]),
  ],
  u"實體配置器以頁框為單位管理記憶體；連續大塊容易因碎片而失敗，所以核心多依賴分頁。",
  [u"一個頁框多大？",
   u"點陣圖配置器怎麼記錄使用狀態？",
   u"什麼是外部碎片？"]),

lesson(u"分頁與頁表",
  u"虛擬位址怎麼變成實體位址",
  [u"理解虛擬記憶體的意義",
   u"認識 x86-64 四層頁表",
   u"親手做位址轉換"],
  [fig(_PT, 202, u"x86-64 的四層頁表。"),
   widget({"t": "xlate", "q": u"<b>位址轉換練習</b>（簡化成 16 位元、一層頁表）：輸入虛擬位址。"}),
   code(u"""// 頁表項的重要位元
#define PTE_PRESENT  (1ull << 0)    // 存在：0 時存取會觸發分頁錯誤
#define PTE_WRITE    (1ull << 1)    // 可寫入
#define PTE_USER     (1ull << 2)    // 使用者模式可存取
#define PTE_NX       (1ull << 63)   // 不可執行

void map_page(uint64_t* pml4, uint64_t virt, uint64_t phys, uint64_t flags) {
    uint64_t* t = pml4;
    for (int level = 3; level > 0; level--) {          // PML4 → PDPT → PD
        int idx = (virt >> (12 + 9 * level)) & 0x1FF;
        if (!(t[idx] & PTE_PRESENT)) t[idx] = pmm_alloc() | PTE_PRESENT | PTE_WRITE | PTE_USER;
        t = phys_to_virt(t[idx] & ~0xFFFull);
    }
    t[(virt >> 12) & 0x1FF] = phys | flags | PTE_PRESENT;   // PT
    asm volatile("invlpg (%0)" :: "r"(virt) : "memory");   // 清掉 TLB 中的舊轉換
}"""),
  ],
  u"分頁把虛擬位址經四層頁表轉成實體位址；頁表項的位元控制存在、可寫、使用者與可執行權限。",
  [u"48 位元虛擬位址怎麼拆成五段？",
   u"存在位元為 0 時會發生什麼？",
   u"為什麼修改頁表後要 invlpg？"]),

lesson(u"核心的位址空間",
  u"上半部核心與直接映射",
  [u"理解位址空間的分配",
   u"認識上半部核心",
   u"知道直接映射的用途"],
  [fig(_KSPACE, 252, u"64 位元位址空間的典型配置。"),
   ("ul", [u"<strong>上半部核心</strong>：核心放在位址空間最上方，使用者程式用下半部；這樣每個行程的位址空間都可以「共用」同一份核心映射。",
           u"<strong>直接映射</strong>：把所有實體記憶體連續映射到核心空間的某一段（Linux 稱為 direct map），核心要存取某個實體位址時，只要加上固定偏移。",
           u"<strong>非正規位址</strong>：48 位元虛擬位址的高 16 位必須和第 47 位相同，中間的巨大空洞不能使用（存取會觸發 #GP）。"]),
   code(u"""#define HHDM_OFFSET 0xffff800000000000ull     // 直接映射的起點（由開機程式提供）
static inline void* phys_to_virt(uint64_t p) { return (void*)(p + HHDM_OFFSET); }"""),
  ],
  u"核心在上半部、使用者在下半部；直接映射讓核心能方便地存取任何實體記憶體。",
  [u"為什麼核心要放在上半部？",
   u"直接映射有什麼用？",
   u"什麼是非正規位址？"]),

lesson(u"核心堆積：kmalloc 與 slab",
  u"配置小塊記憶體",
  [u"理解核心堆積的需求",
   u"認識 slab 配置器",
   u"實作簡單的 kmalloc"],
  [fig(_SLAB, 222, u"slab 配置器。"),
   code(u"""// 依大小分級：8、16、32、64……2048 位元組各一個快取
struct cache { size_t obj_size; void* free_list; };
static struct cache caches[9];

void* kmalloc(size_t n) {
    struct cache* c = pick_cache(n);              // 找到 >= n 的最小級距
    if (!c->free_list) refill(c);                 // 從頁框配置器拿一頁，切成小格串起來
    void* obj = c->free_list;
    c->free_list = *(void**)obj;                  // 空閒格的開頭存著下一個空閒格
    return obj;
}
void kfree(void* p) { struct cache* c = cache_of(p); *(void**)p = c->free_list; c->free_list = p; }"""),
   ("p", u"Linux 為常用的核心物件（行程描述、inode、網路封包）各建專用快取，配置與釋放都非常快，也減少碎片。這個想法最早由 Sun 的 Solaris 提出。"),
  ],
  u"頁框配置器只給整頁；slab 把頁切成固定大小的格子，提供快速的 kmalloc／kfree。",
  [u"為什麼需要 kmalloc？",
   u"slab 的空閒串列存在哪裡？",
   u"為什麼要為常用物件建專用快取？"]),

lesson(u"每個行程獨立的位址空間",
  u"同一個位址，不同的記憶體",
  [u"理解行程隔離的實現",
   u"知道切換位址空間的方式",
   u"認識 TLB 與 PCID"],
  [("p", u"兩個程式都可以使用位址 <code>0x400000</code>，卻看到不同的內容——因為它們有<strong>各自的頁表</strong>。核心只要在切換行程時更換 CR3 暫存器（指向 PML4），整個位址空間就換掉了。"),
   code(u"""uint64_t* create_address_space(void) {
    uint64_t* pml4 = phys_to_virt(pmm_alloc());
    memset(pml4, 0, 4096);
    memcpy(pml4 + 256, kernel_pml4 + 256, 256 * 8);   // 上半部：共用核心映射
    return pml4;                                     // 下半部：空的，之後載入程式時填
}

void switch_address_space(uint64_t* pml4) {
    asm volatile("mov %0, %%cr3" :: "r"(virt_to_phys(pml4)) : "memory");
}"""),
   ("ul", [u"使用者頁面設定 <code>PTE_USER</code>；核心頁面不設，使用者模式存取就會觸發分頁錯誤。",
           u"換 CR3 會清空 TLB，代價不小；PCID 功能讓 TLB 項目帶著「位址空間編號」，切換時不必全部清空。",
           u"2018 年的 Meltdown 漏洞讓許多系統改成使用者模式時連核心映射都拿掉（KPTI），PCID 因此變得更重要。"]),
  ],
  u"每個行程有自己的頁表，切換 CR3 就切換整個位址空間；核心映射在每個行程中共用。",
  [u"兩個程式為什麼可以用同一個位址？",
   u"切換位址空間要改哪個暫存器？",
   u"PCID 解決什麼問題？"]),

lesson(u"分頁錯誤的妙用",
  u"延遲配置、寫入時複製、記憶體映射檔",
  [u"理解需求分頁",
   u"認識寫入時複製",
   u"知道記憶體映射檔與置換"],
  [fig(_COW, 230, u"寫入時複製。"),
   ("t", [u"技巧", u"做法", u"好處"],
         [[u"需求分頁", u"程式要 1 GB，先只登記不配置；真的存取某頁時才在分頁錯誤中配置", u"沒用到的記憶體不佔空間"],
          [u"寫入時複製", u"fork 時共用頁面並設唯讀，寫入時才複製（" + LS(29) + u"）", u"fork 很快"],
          [u"記憶體映射檔", u"把檔案映射到位址空間，存取時才從磁碟讀入", u"大檔案、共用函式庫"],
          [u"置換（swap）", u"把不常用的頁寫到磁碟，存在位元清 0；再存取時讀回", u"可用記憶體看起來比實體多"]]),
   code(u"""bool handle_page_fault(uint64_t addr, uint64_t err) {
    struct vma* v = find_vma(current->mm, addr);       // 這個位址屬於程式登記過的區域嗎？
    if (!v) return false;                              // 沒有 → 真正的錯誤（segmentation fault）
    if ((err & PF_WRITE) && is_cow(addr)) return cow_copy(addr);
    map_page(current->pml4, page_align(addr), pmm_alloc(), v->flags);   // 需求分頁
    return true;
}"""),
  ],
  u"分頁錯誤不只是錯誤：需求分頁、寫入時複製、記憶體映射檔、置換都建立在它之上。",
  [u"什麼是需求分頁？",
   u"寫入時複製怎麼讓 fork 變快？",
   u"什麼時候分頁錯誤會變成 segmentation fault？"]),
]),
]
