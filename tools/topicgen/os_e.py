# -*- coding: utf-8 -*-
"""作業系統是怎麼寫出來的：模組 E（行程與排程）、F（檔案系統與裝置）、G（讓它能用）、H（真實世界）。"""
from sa_common import *

lesson = make_lesson("os")

_PCB = svg(
    title(u"行程控制區塊（PCB）"),
    box(20, 40, 280, 190, u"struct process", [u"pid、名稱、狀態", u"保存的暫存器（情境）", u"頁表（位址空間）", u"核心堆疊", u"開啟的檔案表", u"父行程、子行程", u"排程資訊（優先權、時間）"], BLUE),
    box(340, 40, 280, 190, u"行程狀態", [u"就緒：等 CPU", u"執行中：正在 CPU 上", u"阻塞：等 I/O 或事件", u"殭屍：結束了，等父行程收屍"], GREEN),
)

_CTX = svg(
    title(u"情境切換：換掉堆疊，就換掉了執行緒"),
    box(20, 46, 180, 140, u"行程 A 的核心堆疊", [u"……", u"rbx rbp r12-r15", u"返回位址"], BLUE),
    box(440, 46, 180, 140, u"行程 B 的核心堆疊", [u"……", u"rbx rbp r12-r15", u"返回位址"], GREEN),
    box(230, 76, 180, 80, u"switch_to(A, B)", [u"1. 推入 A 的暫存器", u"2. 存 A 的 rsp", u"3. 載入 B 的 rsp", u"4. 彈出 B 的暫存器"], ORANGE),
    T(320, 214, u"ret 回到的是 B 上次被切走的地方——對 B 來說，就像 switch_to 剛剛回傳", 9.5, ACC),
)

_RINGS = svg(
    title(u"特權等級：Ring 0 與 Ring 3"),
    C(320, 130, 90, BLUE, "none", 2), C(320, 130, 40, RED, RED, 2, 0.2),
    T(320, 134, u"Ring 0", 11, RED), T(320, 150, u"核心", 9, RED), T(320, 200, u"Ring 3：使用者程式", 10, BLUE),
    box(450, 60, 180, 140, u"Ring 3 不能做的事", [u"執行 cli、hlt、lidt", u"修改 CR3", u"直接 in／out 連接埠", u"存取沒有 USER 位元的頁"], ORANGE),
    T(320, 240, u"x86 有 4 個等級，但主流作業系統只用 0（核心）和 3（使用者）", 9.5, ACC),
)

_SYS = [(u"程式呼叫 write()", u"使用者程式呼叫 libc 的 <code>write(1, “hi”, 2)</code>。", 0),
        (u"libc 準備參數", u"系統呼叫編號放 <code>rax</code>（Linux x86-64 的 write 是 1），參數依序放 <code>rdi、rsi、rdx</code>。", 1),
        (u"執行 syscall 指令", u"CPU 切到 Ring 0，跳到核心事先登錄在 MSR（LSTAR）中的進入點。", 2),
        (u"核心進入點", u"切換到核心堆疊、保存使用者暫存器。", 2),
        (u"查表分派", u"用 <code>rax</code> 查系統呼叫表，呼叫 <code>sys_write</code>。", 3),
        (u"執行功能", u"檢查使用者給的指標是否合法，找到檔案描述元 1（終端機），寫出資料。", 4),
        (u"返回", u"結果放進 <code>rax</code>，執行 <code>sysretq</code> 回到 Ring 3。", [2, 1]),
        (u"回到程式", u"libc 檢查回傳值，錯誤時設定 <code>errno</code>，再回傳給呼叫者。", 0)]
_SYSB = [u"使用者程式", u"libc", u"syscall 進入點", u"系統呼叫表", u"核心功能"]

_ELF = svg(
    title(u"載入 ELF：把程式標頭描述的區段放進位址空間"),
    box(20, 40, 200, 180, u"ELF 檔案", [u"ELF 標頭（進入點）", u"程式標頭表", u"PT_LOAD #1：程式碼", u"PT_LOAD #2：資料", u"區段（除錯用）"], BLUE),
    box(420, 40, 200, 180, u"行程的位址空間", [u"堆疊（argv、環境變數）", u"↓", u"堆積 ↑", u"資料（可讀寫）", u"程式碼（可讀可執行）"], GREEN),
    A(220, 150, 418, 196, MUTED), A(220, 168, 418, 172, MUTED),
    T(320, 246, u"核心只看程式標頭；區段表是給連結器和除錯器用的", 9.5, ACC),
)

_FORK = svg(
    title(u"fork、exec、wait、exit"),
    box(20, 80, 140, 50, u"shell（父）", [], BLUE),
    box(200, 30, 140, 50, u"fork()", [u"複製出子行程"], ORANGE),
    box(380, 30, 140, 50, u"exec(“ls”)", [u"子行程換成 ls"], PURPLE),
    box(540, 30, 90, 50, u"exit(0)", [], RED),
    box(200, 120, 320, 50, u"wait()：父行程等待子行程結束、取得結束碼", [], GREEN),
    A(160, 96, 198, 60, MUTED), A(340, 55, 378, 55, MUTED), A(520, 55, 538, 55, MUTED), A(160, 116, 198, 142, MUTED), P("M585 80 V145 H522", RED, sw=1.2, dash="4 3"),
    T(320, 206, u"「先複製、再替換」看似浪費，但配合寫入時複製，fork 幾乎沒有成本", 9.5, ACC),
)

_DEAD = svg(
    title(u"死結：互相等待對方手上的鎖"),
    C(180, 110, 34, BLUE, "#e8f0fa", 1.5), T(180, 114, u"執行緒 1", 10, BLUE),
    C(460, 110, 34, GREEN, "#eaf5ec", 1.5), T(460, 114, u"執行緒 2", 10, GREEN),
    R(290, 40, 60, 30, ORANGE, "#fdf1e3", 4, 1.5), T(320, 60, u"鎖 A", 10, ORANGE),
    R(290, 150, 60, 30, PURPLE, "#f3eefa", 4, 1.5), T(320, 170, u"鎖 B", 10, PURPLE),
    A(290, 55, 212, 96, ORANGE), T(230, 66, u"持有", 9, ORANGE), A(214, 124, 288, 162, PURPLE), T(230, 160, u"等待", 9, PURPLE),
    A(350, 165, 428, 124, PURPLE), T(410, 160, u"持有", 9, PURPLE), A(428, 96, 352, 58, ORANGE), T(410, 66, u"等待", 9, ORANGE),
    T(320, 214, u"解法之一：所有人都依固定順序取鎖（永遠先 A 後 B）", 9.5, ACC),
)

_DRV = svg(
    title(u"驅動程式模型"),
    layers([(u"子系統介面：區塊裝置、字元裝置、網路裝置", u"上層只認識介面", BLUE),
            (u"驅動程式：NVMe、AHCI、e1000、virtio", u"把介面翻譯成硬體操作", ORANGE),
            (u"匯流排：PCI Express、USB", u"列舉裝置、配對驅動", TEAL),
            (u"硬體", u"暫存器、DMA、中斷", GRAY)], y=44),
    T(320, 222, u"匯流排發現裝置 → 依廠商／裝置 ID 找到驅動 → 驅動向子系統登錄", 9.5, ACC),
)

_VFS = svg(
    title(u"虛擬檔案系統（VFS）"),
    box(220, 36, 200, 36, u"open／read／write", [], BLUE),
    box(220, 92, 200, 40, u"VFS：inode、dentry、file", [], PURPLE),
    box(20, 160, 130, 36, u"ext4", [], GREEN), box(170, 160, 130, 36, u"FAT32（USB 隨身碟）", [], GREEN),
    box(320, 160, 130, 36, u"procfs（/proc）", [], ORANGE), box(470, 160, 150, 36, u"tmpfs、裝置檔", [], ORANGE),
    A(320, 72, 320, 90, MUTED), P("M320 132 V146 H85 V160 M320 146 H235 V160 M320 146 H385 V160 M320 146 H545 V160", MUTED, sw=1.2),
    T(320, 224, u"系統呼叫只跟 VFS 打交道；每種檔案系統實作同一組函式指標", 9.5, ACC),
)

_FS = svg(
    title(u"一個簡單檔案系統的磁碟配置"),
    cells(20, 60, [u"超級區塊", u"inode 點陣圖", u"資料點陣圖", u"inode 表", u"資料區塊……"], 120, 34, [PURPLE, ORANGE, ORANGE, BLUE, GREEN], size=10),
    T(80, 116, u"大小、數量", 9, MUTED), T(200, 116, u"哪些 inode 已用", 9, MUTED), T(320, 116, u"哪些區塊已用", 9, MUTED), T(440, 116, u"檔案的中繼資料", 9, MUTED), T(560, 116, u"檔案內容、目錄", 9, MUTED),
    box(120, 140, 400, 80, u"inode #12", [u"大小 5000 位元組、權限、時間", u"區塊指標：[38, 39]（直接）＋ 間接區塊"], BLUE),
    T(320, 246, u"目錄也是檔案：內容是一串「名稱 → inode 編號」", 9.5, ACC),
)

_CACHE = svg(
    title(u"頁快取：讀寫先經過記憶體"),
    box(20, 70, 150, 70, u"程式 write()", [], BLUE), box(245, 50, 150, 110, u"頁快取（RAM）", [u"髒頁", u"稍後寫回"], ORANGE),
    box(470, 70, 150, 70, u"磁碟", [], GRAY),
    A(170, 105, 243, 105, MUTED), P("M395 105 H468", MUTED, sw=1.5, dash="5 3"), T(432, 96, u"背景寫回", 9, MUTED),
    T(320, 190, u"write() 回傳時資料可能還在記憶體；fsync() 才保證寫到磁碟", 9.5, ACC),
)

_JOURNAL = svg(
    title(u"日誌式檔案系統：先記下要做什麼"),
    flow([(u"寫入日誌", [u"要改的中繼資料"]), u"寫入「提交」記錄", u"實際修改檔案系統", u"清除日誌項目"], 60, 50, 20, 620, 12, [ORANGE, RED, BLUE, GREEN]),
    T(320, 140, u"斷電發生在提交前：當作沒發生；提交後：重播日誌補完——不再需要漫長的全碟檢查", 9.5, ACC),
)

_TTY = svg(
    title(u"終端機的層次"),
    flow([u"鍵盤驅動", (u"TTY 行規", [u"line discipline"]), u"前景行程 read()"], 60, 50, 20, 620, 14, [GRAY, ORANGE, BLUE]),
    T(320, 140, u"行規負責：回顯、退格、整行緩衝，以及把 Ctrl+C 變成 SIGINT 訊號", 9.5, ACC),
    T(320, 158, u"終端機模擬器（Terminal、iTerm）則透過虛擬終端（pty）扮演鍵盤與螢幕", 9.5, MUTED),
)

_PIPE = svg(
    title(u"管線：ls | grep txt"),
    box(20, 60, 160, 70, u"ls", [u"stdout → 管線寫端"], BLUE),
    R(230, 80, 180, 30, ORANGE, ORANGE, 15, 1.5, op=0.2), T(320, 100, u"核心中的管線緩衝區", 10, ORANGE),
    box(460, 60, 160, 70, u"grep txt", [u"stdin ← 管線讀端"], GREEN),
    A(180, 95, 228, 95, MUTED), A(410, 95, 458, 95, MUTED),
    T(320, 166, u"shell 用 pipe() 建立管線，fork 兩次，各自用 dup2() 把 0 或 1 號描述元換成管線的一端", 9.5, ACC),
)

_NETSTK = svg(
    title(u"網路堆疊"),
    layers([(u"socket API：socket、connect、send、recv", u"使用者程式", BLUE),
            (u"傳輸層：TCP、UDP", u"連線、重傳、壅塞控制", TEAL),
            (u"網路層：IP、路由", u"位址與轉送", GREEN),
            (u"鏈結層：乙太網路、ARP", u"同一網段內的傳送", ORANGE),
            (u"網卡驅動：DMA 環形緩衝區、中斷", u"硬體", GRAY)], y=44),
    T(320, 262, u"收到封包時由下往上一層層拆封，送出時由上往下一層層包裝", 9.5, ACC),
)

_LINUX = svg(
    title(u"Linux 原始碼樹（主要資料夾）"),
    [box(20 + (i % 4) * 155, 40 + (i // 4) * 70, 145, 58, n, [d], c) for i, (n, d, c) in enumerate([
        (u"arch/", u"各 CPU 架構", ORANGE), (u"init/", u"start_kernel()", RED), (u"kernel/", u"排程、訊號、時間", BLUE), (u"mm/", u"記憶體管理", BLUE),
        (u"fs/", u"VFS 與檔案系統", GREEN), (u"drivers/", u"驅動（佔一大半）", PURPLE), (u"net/", u"網路堆疊", TEAL), (u"include/", u"標頭檔", GRAY)])],
    T(320, 200, u"init/main.c 的 start_kernel() 是架構無關的起點，相當於我們的 kmain()", 9.5, ACC),
)

_NTXNU = svg(
    title(u"Windows NT 與 macOS XNU"),
    box(20, 40, 290, 170, u"Windows NT", [u"使用者模式：Win32 子系統、服務", u"────────────", u"執行體：I/O、記憶體、行程、安全", u"核心：排程、中斷、同步", u"HAL：硬體抽象層", u"驅動：WDM／WDF"], BLUE),
    box(330, 40, 290, 170, u"macOS XNU", [u"使用者模式：launchd、框架", u"────────────", u"BSD 層：POSIX、檔案系統、網路", u"Mach：行程、記憶體、IPC", u"IOKit：物件導向的驅動框架", u"（三者都在核心空間）"], GREEN),
    T(320, 234, u"兩者都源自微核心思想，最後為了效能把主要服務放回核心——混合式", 9.5, ACC),
)

MODULES = [
(u"模組 E｜行程與排程", [

lesson(u"行程與執行緒的資料結構",
  u"核心怎麼記住每個程式",
  [u"認識行程控制區塊",
   u"理解行程狀態",
   u"區分行程與執行緒"],
  [fig(_PCB, 244, u"行程控制區塊與狀態。"),
   code(u"""enum state { READY, RUNNING, BLOCKED, ZOMBIE };

struct process {
    int pid;
    enum state state;
    struct context* ctx;          // 被切走時保存的暫存器（在核心堆疊上）
    uint64_t* pml4;               // 位址空間（第 21 課）
    void* kstack;                 // 每個執行緒自己的核心堆疊
    struct file* files[64];       // 檔案描述元表（第 34 課）
    struct process* parent;
    uint64_t vruntime;            // 排程資訊（第 25 課）
    struct process* next;         // 串在就緒佇列裡
};"""),
   ("p", u"<strong>執行緒</strong>是 CPU 排程的單位；<strong>行程</strong>是資源（位址空間、檔案）的容器。同一個行程的多條執行緒共用位址空間，各有自己的暫存器與堆疊。Linux 把兩者統一成 <code>task_struct</code>，差別只在共用了哪些資源。"),
  ],
  u"PCB 記錄行程的一切：狀態、暫存器、位址空間、檔案；執行緒共用行程的資源但有自己的堆疊。",
  [u"PCB 裡有哪些主要欄位？",
   u"行程有哪些狀態？",
   u"行程和執行緒的差別是什麼？"]),

lesson(u"情境切換",
  u"保存與還原暫存器",
  [u"理解情境切換的原理",
   u"讀懂 switch_to 的組合語言",
   u"知道情境切換的成本"],
  [fig(_CTX, 226, u"情境切換。"),
   code(u"""; void switch_to(struct context** old, struct context* new)
; 依呼叫慣例，rbx rbp r12-r15 由被呼叫者保存——只需要存這些
switch_to:
    push rbx
    push rbp
    push r12
    push r13
    push r14
    push r15
    mov [rdi], rsp        ; *old = 目前的堆疊指標
    mov rsp, rsi          ; 換成新執行緒的堆疊
    pop r15
    pop r14
    pop r13
    pop r12
    pop rbp
    pop rbx
    ret                   ; 回到新執行緒上次呼叫 switch_to 的地方"""),
   ("ul", [u"若兩個行程的位址空間不同，還要換 CR3（" + LS(21) + u"）。",
           u"浮點與 SIMD 暫存器很大，通常延遲到真的被使用時才保存。",
           u"成本不只是幾十條指令：快取與 TLB 的內容也失效了，這才是主要開銷。"]),
  ],
  u"情境切換＝保存舊執行緒的暫存器、換堆疊指標、還原新執行緒的暫存器。",
  [u"為什麼只要保存 rbx、rbp、r12～r15？",
   u"ret 為什麼會回到新的執行緒？",
   u"情境切換的主要成本是什麼？"]),

lesson(u"排程器",
  u"下一個輪到誰",
  [u"比較常見的排程演算法",
   u"親手模擬排程",
   u"認識 Linux 的排程器"],
  [widget({"t": "sched", "q": u"<b>排程模擬</b>：切換演算法，比較甘特圖與平均等待時間。"}),
   ("t", [u"演算法", u"特點"],
         [[u"先到先服務", u"簡單，長工作會擋住短工作"], [u"最短工作優先", u"平均等待最短，但要預知長度，長工作可能餓死"],
          [u"輪流（Round Robin）", u"每人一個時間片，公平、反應快；時間片太小切換開銷大"], [u"優先權", u"重要的先跑；需要「老化」機制避免低優先權永遠輪不到"]]),
   code(u"""void schedule_tick(void) {               // 每次計時器中斷呼叫（第 14 課）
    if (--current->slice > 0) return;
    current->slice = TIME_SLICE;
    struct process* next = pick_next();  // 從就緒佇列挑一個
    if (next != current) { enqueue(current); switch_process(next); }
}"""),
   ("p", u"Linux 長年使用 CFS（完全公平排程器）：記錄每個行程的「虛擬執行時間」，總是挑最少的那個，用紅黑樹維護；Linux 6.6 起改為 EEVDF 演算法，兼顧公平與延遲。"),
  ],
  u"排程器在公平、反應時間與吞吐量之間取捨；計時器中斷驅動搶占式排程。",
  [u"輪流排程的時間片太小會怎樣？",
   u"什麼是餓死？怎麼避免？",
   u"CFS 怎麼決定下一個行程？"]),

lesson(u"使用者模式與核心模式",
  u"特權等級與 TSS",
  [u"理解 Ring 0 與 Ring 3",
   u"知道從使用者模式進入核心的時機",
   u"認識 TSS 的作用"],
  [fig(_RINGS, 254, u"特權等級。"),
   ("p", u"CPU 目前的特權等級記錄在程式碼區段選擇子的最低兩位。使用者程式在 Ring 3 執行，只能透過三種方式進入核心：<strong>系統呼叫、例外、硬體中斷</strong>。"),
   code(u"""// 從 Ring 3 被中斷時，CPU 必須換到核心堆疊——它從 TSS 讀取 rsp0
struct tss { uint32_t r0; uint64_t rsp0, rsp1, rsp2; uint64_t r1; uint64_t ist[7]; /* … */ } __attribute__((packed));

void set_kernel_stack(void* top) { tss.rsp0 = (uint64_t)top; }   // 每次切換行程都要更新"""),
   code(u"""; 第一次進入使用者模式：偽造一個「從中斷返回」的堆疊框架
    push USER_DS | 3      ; ss
    push user_stack_top   ; rsp
    push 0x202            ; rflags（IF=1：開中斷）
    push USER_CS | 3      ; cs
    push user_entry       ; rip
    iretq                 ; CPU 以為要「返回」Ring 3"""),
  ],
  u"使用者程式在 Ring 3 執行，只能經由系統呼叫、例外、中斷進入核心；TSS 提供核心堆疊位址。",
  [u"使用者程式有哪三種方式進入核心？",
   u"TSS 的 rsp0 是做什麼的？",
   u"第一次進入使用者模式為什麼用 iretq？"]),

lesson(u"系統呼叫",
  u"從 write() 到核心",
  [u"理解系統呼叫的流程",
   u"認識 x86-64 的呼叫慣例",
   u"實作系統呼叫表"],
  [steps(_SYS, u"<b>一次系統呼叫的旅程</b>", _SYSB),
   code(u"""typedef long (*syscall_fn)(long, long, long, long, long, long);
static syscall_fn table[] = { [0] = sys_read, [1] = sys_write, [2] = sys_open, [60] = sys_exit, /* … */ };

long syscall_dispatch(struct regs* r) {
    if (r->rax >= ARRAY_SIZE(table) || !table[r->rax]) return -ENOSYS;
    return table[r->rax](r->rdi, r->rsi, r->rdx, r->r10, r->r8, r->r9);
}

long sys_write(long fd, long buf, long len, ...) {
    if (!user_range_ok(buf, len)) return -EFAULT;   // 絕不能相信使用者給的指標！
    struct file* f = current->files[fd];
    return f ? f->ops->write(f, (const char*)buf, len) : -EBADF;
}"""),
   ("p", u"安全原則：核心必須檢查每一個來自使用者的指標與長度。否則使用者可以傳一個指向核心記憶體的指標，讓核心幫它讀寫機密資料。"),
  ],
  u"系統呼叫用 syscall 指令進入核心，以 rax 查表分派；核心必須驗證所有使用者參數。",
  [u"系統呼叫編號放在哪個暫存器？",
   u"為什麼核心要檢查使用者傳來的指標？",
   u"libc 在系統呼叫中扮演什麼角色？"]),

lesson(u"載入第一個使用者程式",
  u"解析 ELF",
  [u"理解 ELF 的程式標頭",
   u"實作簡單的 ELF 載入器",
   u"準備使用者堆疊"],
  [fig(_ELF, 258, u"ELF 載入。"),
   code(u"""int exec_elf(struct process* p, const uint8_t* img) {
    Elf64_Ehdr* eh = (Elf64_Ehdr*)img;
    if (memcmp(eh->e_ident, "\\x7f" "ELF", 4) != 0) return -ENOEXEC;
    Elf64_Phdr* ph = (Elf64_Phdr*)(img + eh->e_phoff);
    for (int i = 0; i < eh->e_phnum; i++) {
        if (ph[i].p_type != PT_LOAD) continue;
        map_user_range(p, ph[i].p_vaddr, ph[i].p_memsz, flags_of(ph[i].p_flags));
        memcpy_to_user(p, ph[i].p_vaddr, img + ph[i].p_offset, ph[i].p_filesz);
        // p_memsz > p_filesz 的部分（.bss）保持為 0
    }
    setup_user_stack(p, argv, envp);    // 放入 argc、argv 指標、環境變數
    p->entry = eh->e_entry;
    return 0;
}"""),
   ("p", u"真實系統還要處理動態連結：程式標頭裡有 <code>PT_INTERP</code> 時，核心先載入動態連結器（如 <code>ld-linux.so</code>），由它載入共用函式庫。完整過程見 " + XL("exe") + u"。"),
  ],
  u"核心依 ELF 的 PT_LOAD 程式標頭建立映射、複製內容、準備堆疊，再跳到進入點。",
  [u"核心載入 ELF 時看程式標頭還是區段表？",
   u"p_memsz 比 p_filesz 大的部分是什麼？",
   u"動態連結的程式怎麼載入？"]),

lesson(u"fork、exec、wait、exit",
  u"Unix 建立行程的方式",
  [u"理解四個行程系統呼叫",
   u"知道殭屍與孤兒行程",
   u"看見寫入時複製的作用"],
  [fig(_FORK, 218, u"行程的一生。"),
   code(u"""pid_t pid = fork();                 // 一次呼叫，兩次回傳
if (pid == 0) {                     // 子行程
    execl("/bin/ls", "ls", "-l", NULL);
    _exit(127);                     // exec 成功就不會回到這裡
} else {                            // 父行程
    int status;
    waitpid(pid, &status, 0);       // 等子行程結束
}"""),
   ("t", [u"概念", u"說明"],
         [[u"殭屍行程", u"已經結束、但父行程還沒 wait 的行程；PCB 保留著結束碼"],
          [u"孤兒行程", u"父行程先結束了，由 init（PID 1）收養"], [u"寫入時複製", u"fork 不真的複製記憶體（" + LS(22) + u"）"],
          [u"Windows 的做法", u"CreateProcess 一次完成「建立＋載入程式」，沒有 fork"]]),
  ],
  u"fork 複製行程、exec 換成新程式、wait 回收子行程、exit 結束；寫入時複製讓這套組合很有效率。",
  [u"fork 為什麼回傳兩次？",
   u"什麼是殭屍行程？",
   u"Windows 建立行程和 Unix 有什麼不同？"]),

lesson(u"同步：鎖、信號量與死結",
  u"兩條執行緒同時改一個變數",
  [u"理解競爭條件",
   u"認識自旋鎖與互斥鎖",
   u"知道死結的條件與預防"],
  [widget({"t": "race", "q": u"<b>競爭條件實驗</b>：兩條執行緒各對 counter 加 1。"}),
   code(u"""typedef struct { volatile int locked; } spinlock_t;

void spin_lock(spinlock_t* l) {
    while (__atomic_exchange_n(&l->locked, 1, __ATOMIC_ACQUIRE))   // 原子地設 1 並取回舊值
        asm volatile("pause");                                     // 舊值是 1：別人拿著，繼續等
}
void spin_unlock(spinlock_t* l) { __atomic_store_n(&l->locked, 0, __ATOMIC_RELEASE); }"""),
   ("t", [u"機制", u"等待方式", u"適合"],
         [[u"自旋鎖", u"原地空轉", u"臨界區極短、中斷處理程式中"], [u"互斥鎖", u"讓出 CPU 去睡覺", u"可能等很久的情況"],
          [u"信號量", u"計數器：允許 N 個同時進入", u"資源池、生產者消費者"], [u"關中斷", u"單核心上防止被打斷", u"極短的核心操作"]]),
   fig(_DEAD, 226, u"死結。"),
  ],
  u"共享資料要用鎖保護讀－改－寫；不同的鎖適合不同情境，固定取鎖順序可以避免死結。",
  [u"為什麼 counter++ 不是原子操作？",
   u"自旋鎖和互斥鎖有什麼不同？",
   u"怎麼避免死結？"]),
]),

(u"模組 F｜檔案系統與裝置", [

lesson(u"驅動程式模型",
  u"裝置、匯流排、驅動",
  [u"理解驅動程式的分層",
   u"認識裝置的三種類型",
   u"知道驅動與裝置的配對"],
  [fig(_DRV, 232, u"驅動程式模型。"),
   code(u"""struct block_device_ops {                // 區塊裝置介面：上層只認識這些函式
    int (*read)(struct block_dev*, uint64_t lba, void* buf, size_t count);
    int (*write)(struct block_dev*, uint64_t lba, const void* buf, size_t count);
};

struct pci_driver nvme_driver = {
    .name = "nvme",
    .class_code = 0x010802,              // 大容量儲存／非揮發性記憶體／NVMe
    .probe = nvme_probe,                 // 找到符合的裝置時呼叫
};"""),
   ("t", [u"類型", u"特點", u"例子"],
         [[u"字元裝置", u"一個位元組一個位元組地讀寫", u"鍵盤、序列埠、終端機"], [u"區塊裝置", u"以固定大小的區塊隨機存取", u"硬碟、SSD"],
          [u"網路裝置", u"收發封包", u"網卡"]]),
  ],
  u"驅動程式把各種硬體翻譯成統一的介面；匯流排負責發現裝置並找到對應的驅動。",
  [u"三種裝置類型各是什麼？",
   u"probe 函式什麼時候被呼叫？",
   u"為什麼上層只認識介面？"]),

lesson(u"PCI 與裝置探索",
  u"電腦裡插了什麼",
  [u"理解 PCI 設定空間",
   u"寫出列舉 PCI 裝置的程式",
   u"認識 BAR"],
  [code(u"""// 每個 PCI 功能有 256 位元組（PCIe 為 4 KB）的設定空間
// 0x00：廠商 ID   0x02：裝置 ID   0x0B：類別碼   0x10～0x24：BAR0～BAR5
for (int bus = 0; bus < 256; bus++)
  for (int dev = 0; dev < 32; dev++)
    for (int fn = 0; fn < 8; fn++) {
        uint16_t vendor = pci_read16(bus, dev, fn, 0x00);
        if (vendor == 0xFFFF) continue;          // 這個位置沒有裝置
        uint16_t device = pci_read16(bus, dev, fn, 0x02);
        uint32_t cls    = pci_read32(bus, dev, fn, 0x08) >> 8;
        kprintf("%x:%x.%x  %x:%x  class %x\\n", bus, dev, fn, vendor, device, cls);
        match_driver(bus, dev, fn, vendor, device, cls);
    }"""),
   ("ul", [u"<strong>BAR（基底位址暫存器）</strong>：告訴我們裝置的暫存器被映射到哪段實體位址，驅動再把它映射到核心位址空間（記憶體映射 I/O）。",
           u"<strong>PCIe 的 ECAM</strong>：設定空間本身也映射到記憶體，位址來自 ACPI 的 MCFG 表。",
           u"<strong>MSI 中斷</strong>：現代裝置用寫入特定記憶體位址的方式發出中斷，不再依賴共用的中斷線。"]),
   ("p", u"Linux 的 <code>lspci</code> 指令就是讀這些資訊。"),
  ],
  u"列舉 PCI 設定空間就能找到所有裝置；BAR 告訴驅動裝置暫存器在哪裡。",
  [u"廠商 ID 為 0xFFFF 代表什麼？",
   u"BAR 的用途是什麼？",
   u"什麼是 MSI？"]),

lesson(u"磁碟驅動",
  u"區塊、扇區與 DMA",
  [u"理解區塊與 LBA",
   u"認識 AHCI、NVMe、virtio",
   u"知道 DMA 的作用"],
  [("t", [u"介面", u"特點"],
         [[u"AHCI（SATA）", u"一個命令佇列、最多 32 個命令"], [u"NVMe", u"為 SSD 設計：最多 65535 個佇列，每個 CPU 可以有自己的佇列"],
          [u"virtio-blk", u"虛擬機專用：QEMU 等模擬器提供的簡化介面，最適合教學核心"]]),
   code(u"""// 概念：送出一個讀取請求（以 NVMe 風格的佇列為例）
struct cmd c = { .opcode = READ, .lba = 2048, .count = 8, .dma_addr = virt_to_phys(buf) };
sq[sq_tail] = c;                     // 放進「提交佇列」
sq_tail = (sq_tail + 1) % QSIZE;
mmio_write(doorbell, sq_tail);       // 按門鈴：通知控制器
// ……控制器用 DMA 把資料直接寫進 buf，完成後在「完成佇列」放一筆記錄並發出中斷"""),
   ("ul", [u"<strong>LBA</strong>：以區塊編號定位，不再用磁頭、磁柱這些物理概念。區塊常見 512 或 4096 位元組。",
           u"<strong>DMA</strong>：裝置直接讀寫記憶體，CPU 不必一個個位元組搬運，可以去做別的事。"]),
  ],
  u"磁碟以 LBA 區塊存取；現代控制器用命令佇列＋門鈴＋DMA＋完成中斷運作。",
  [u"什麼是 LBA？",
   u"NVMe 為什麼適合多核心？",
   u"DMA 讓 CPU 省下什麼工作？"]),

lesson(u"虛擬檔案系統（VFS）",
  u"一切都是檔案",
  [u"理解 VFS 的抽象",
   u"認識 inode、dentry、file",
   u"知道掛載的意義"],
  [fig(_VFS, 236, u"虛擬檔案系統。"),
   code(u"""struct file_ops {                         // 每種檔案系統（或裝置）實作這組函式
    long (*read)(struct file*, char* buf, size_t n);
    long (*write)(struct file*, const char* buf, size_t n);
};
struct inode { uint64_t ino; uint64_t size; mode_t mode; struct file_ops* ops; void* fs_private; };
struct file  { struct inode* inode; uint64_t pos; int flags; };   // 開啟後的狀態（位置、模式）"""),
   ("t", [u"物件", u"代表"],
         [[u"inode", u"一個檔案本身（中繼資料、資料位置）"], [u"dentry", u"路徑中的一個名稱 → inode（有快取）"],
          [u"file", u"一次「開啟」：讀寫位置、模式"], [u"超級區塊", u"一個已掛載的檔案系統"]]),
   ("p", u"掛載（mount）把一個檔案系統接到目錄樹的某個位置。「一切都是檔案」讓終端機、管線、甚至行程資訊（/proc）都能用 read、write 操作。"),
  ],
  u"VFS 定義統一的物件與函式介面，讓各種檔案系統與裝置都能用同一組系統呼叫存取。",
  [u"inode 和 file 有什麼不同？",
   u"dentry 快取有什麼好處？",
   u"「一切都是檔案」是什麼意思？"]),

lesson(u"設計一個簡單的檔案系統",
  u"超級區塊、inode、目錄",
  [u"理解檔案系統的磁碟配置",
   u"認識 inode 的區塊指標",
   u"實作路徑查找"],
  [fig(_FS, 258, u"簡單檔案系統的配置。"),
   code(u"""struct disk_inode {
    uint16_t mode; uint32_t size;
    uint32_t direct[12];      // 前 12 個區塊直接指向
    uint32_t indirect;        // 這個區塊裡存的是更多區塊編號
};
struct dirent { uint32_t ino; char name[28]; };   // 目錄內容就是一串 dirent

uint32_t lookup(const char* path) {               // "/home/a.txt"
    uint32_t ino = ROOT_INO;
    for (char* part = strtok(path, "/"); part; part = strtok(NULL, "/"))
        ino = dir_find(ino, part);                 // 讀目錄 inode 的內容，找名稱
    return ino;
}"""),
   ("p", u"有了這個結構，<code>open</code>＝查路徑得到 inode；<code>read</code>＝依位置算出第幾個區塊、讀出來；<code>write</code> 可能需要從資料點陣圖配置新區塊。這就是 Unix 檔案系統（以及 ext2）的基本設計。"),
  ],
  u"檔案系統用超級區塊、點陣圖、inode 表與資料區塊組織磁碟；目錄是名稱到 inode 的對照表。",
  [u"超級區塊存什麼？",
   u"直接與間接區塊指標有什麼不同？",
   u"開啟 /home/a.txt 需要讀哪些東西？"]),

lesson(u"真實檔案系統比較",
  u"FAT、ext4、NTFS、APFS",
  [u"比較主流檔案系統",
   u"理解範圍與 B 樹",
   u"知道寫入時複製檔案系統"],
  [("t", [u"檔案系統", u"系統", u"特點"],
         [[u"FAT32／exFAT", u"隨身碟、記憶卡", u"簡單、相容性最好；FAT32 單檔上限 4 GB；沒有日誌"],
          [u"ext4", u"Linux", u"日誌、範圍（extent）、成熟穩定"],
          [u"NTFS", u"Windows", u"日誌、權限（ACL）、主檔案表（MFT）"],
          [u"APFS", u"macOS／iOS", u"寫入時複製、快照、空間共用、加密"],
          [u"Btrfs／ZFS", u"Linux 等", u"寫入時複製、校驗和、快照、多磁碟管理"]]),
   ("ul", [u"<strong>範圍（extent）</strong>：不再一塊一塊記錄，而是「從第 1000 塊開始連續 200 塊」，大檔案的中繼資料大幅縮小。",
           u"<strong>B 樹</strong>：大型目錄用 B 樹索引，百萬個檔案也能快速查找。",
           u"<strong>寫入時複製檔案系統</strong>：從不覆寫舊資料，新資料寫到新位置後再切換指標——快照幾乎免費。"]),
   ("p", u"各種檔案格式的內部結構，可以對照 " + XL("ff") + u"。"),
  ],
  u"真實檔案系統在基本設計上加了範圍、B 樹、日誌、寫入時複製等技術。",
  [u"FAT32 的單檔大小上限是多少？",
   u"範圍（extent）比區塊清單好在哪？",
   u"寫入時複製檔案系統為什麼能輕鬆做快照？"]),

lesson(u"緩衝快取與頁快取",
  u"記憶體比磁碟快上千倍",
  [u"理解頁快取的作用",
   u"認識回寫與 fsync",
   u"知道預讀"],
  [fig(_CACHE, 200, u"頁快取。"),
   ("ul", [u"<strong>讀取</strong>：先查頁快取，命中就不必讀磁碟；所以同一個檔案第二次開啟特別快。",
           u"<strong>寫入</strong>：寫進頁快取並標記為「髒」，由背景執行緒稍後寫回（回寫）。",
           u"<strong>fsync</strong>：強制把某檔案的髒頁寫到磁碟並等待完成——資料庫與安全存檔都需要它（" + XL("ap", 17) + u"）。",
           u"<strong>預讀</strong>：偵測到循序讀取時，提前把後面的區塊讀進來。"]),
   ("p", u"Linux 會把「閒置」的記憶體幾乎全部拿來當頁快取，所以 <code>free</code> 指令常顯示可用記憶體很少——這是好事，需要時會立刻釋放。"),
  ],
  u"頁快取用記憶體加速檔案讀寫；寫入預設延遲回寫，需要保證時要呼叫 fsync。",
  [u"為什麼第二次開啟同一個檔案比較快？",
   u"write 回傳後資料一定在磁碟上嗎？",
   u"預讀是什麼？"]),

lesson(u"日誌式檔案系統與當機一致性",
  u"寫到一半斷電怎麼辦",
  [u"理解當機一致性的問題",
   u"認識日誌的運作",
   u"比較日誌與寫入時複製"],
  [("p", u"建立一個檔案需要修改好幾處：inode 點陣圖、inode、目錄、資料點陣圖、資料區塊。如果斷電發生在中間，檔案系統就會不一致（例如區塊被標記為使用中，卻沒有任何檔案指向它）。"),
   fig(_JOURNAL, 170, u"日誌的流程。"),
   ("t", [u"做法", u"原理", u"代表"],
         [[u"檔案系統檢查（fsck）", u"開機時掃描整個磁碟修復", u"早期 ext2、FAT"], [u"日誌", u"先把要做的修改寫進日誌，提交後才真的修改", u"ext4、NTFS"],
          [u"寫入時複製", u"新資料寫到新位置，最後原子地切換根指標", u"APFS、ZFS、Btrfs"]]),
   ("p", u"ext4 預設只記錄中繼資料到日誌，但保證資料區塊先於中繼資料寫入（ordered 模式），在效能與安全間取得平衡。"),
  ],
  u"日誌讓檔案系統在斷電後能快速恢復一致；寫入時複製則從根本上避免覆寫。",
  [u"為什麼建立檔案時斷電會造成不一致？",
   u"日誌的提交記錄有什麼作用？",
   u"日誌和寫入時複製有什麼不同？"]),
]),

(u"模組 G｜讓它能用", [

lesson(u"終端機與 TTY",
  u"打字到程式之間發生什麼事",
  [u"理解 TTY 的角色",
   u"認識行規與標準模式",
   u"知道 Ctrl+C 怎麼變成訊號"],
  [fig(_TTY, 170, u"終端機的層次。"),
   ("t", [u"功能", u"說明"],
         [[u"標準模式（canonical）", u"按 Enter 才把整行交給程式；退格在行規裡處理"], [u"原始模式（raw）", u"每個按鍵立刻交給程式（vim、遊戲）"],
          [u"回顯", u"打的字自動顯示在螢幕上（輸入密碼時關閉）"], [u"訊號", u"Ctrl+C → SIGINT、Ctrl+Z → SIGTSTP、Ctrl+\\ → SIGQUIT"]]),
   ("p", u"名稱 TTY 來自電傳打字機（teletypewriter）。今天的終端機視窗是一個<strong>虛擬終端（pty）</strong>：一端給終端機程式，一端給 shell，中間仍經過核心的行規。"),
  ],
  u"TTY 行規處理回顯、行編輯與控制字元；終端機模擬器透過 pty 與 shell 溝通。",
  [u"標準模式和原始模式有什麼不同？",
   u"Ctrl+C 是怎麼終止程式的？",
   u"什麼是 pty？"]),

lesson(u"寫一個 Shell",
  u"讀一行、拆開、執行",
  [u"理解 shell 的基本迴圈",
   u"實作執行外部指令",
   u"知道為什麼 cd 是內建指令"],
  [code(u"""// user/sh.c：一個迷你 shell
int main(void) {
    char line[256], *argv[16];
    for (;;) {
        write(1, "$ ", 2);
        if (read_line(line, sizeof line) <= 0) break;
        int argc = split(line, argv);            // "ls -l" → {"ls", "-l", NULL}
        if (argc == 0) continue;
        if (strcmp(argv[0], "cd") == 0) { chdir(argv[1]); continue; }   // 內建指令
        if (strcmp(argv[0], "exit") == 0) break;
        pid_t pid = fork();
        if (pid == 0) { execvp(argv[0], argv); write(2, "not found\\n", 10); _exit(127); }
        waitpid(pid, NULL, 0);
    }
    return 0;
}"""),
   ("p", u"<strong>為什麼 cd 必須是內建指令？</strong>因為「目前目錄」是行程自己的屬性。如果 cd 是外部程式，它改的是子行程的目錄，子行程結束後 shell 的目錄並沒有變。"),
   ("p", u"到這一步，我們的作業系統終於可以開機後讓使用者打字、執行程式了。"),
  ],
  u"shell 就是一個讀取、拆解、fork＋exec＋wait 的迴圈；改變自身狀態的指令必須內建。",
  [u"shell 執行外部指令的步驟是什麼？",
   u"為什麼 cd 不能是外部程式？",
   u"execvp 成功後還會執行下一行嗎？"]),

lesson(u"管線與重新導向",
  u"ls | grep txt > out.txt",
  [u"理解檔案描述元",
   u"實作重新導向",
   u"實作管線"],
  [fig(_PIPE, 182, u"管線。"),
   code(u"""// 重新導向：cmd > out.txt
if (fork() == 0) {
    int fd = open("out.txt", O_WRONLY | O_CREAT | O_TRUNC, 0644);
    dup2(fd, 1);          // 讓 1 號（stdout）指向 out.txt
    close(fd);
    execvp(cmd[0], cmd);  // 程式完全不知道輸出被導向檔案了
}

// 管線：ls | grep txt
int p[2]; pipe(p);        // p[0] 讀端、p[1] 寫端
if (fork() == 0) { dup2(p[1], 1); close(p[0]); close(p[1]); execlp("ls", "ls", NULL); }
if (fork() == 0) { dup2(p[0], 0); close(p[0]); close(p[1]); execlp("grep", "grep", "txt", NULL); }
close(p[0]); close(p[1]); wait(NULL); wait(NULL);"""),
   ("p", u"關鍵：fork 會複製檔案描述元表，exec 會保留它。shell 在 fork 之後、exec 之前調整描述元，程式本身完全不需要知道輸入輸出從哪裡來——這是 Unix「小工具組合」哲學的基礎。"),
  ],
  u"重新導向與管線都是在 fork 與 exec 之間用 dup2 調整檔案描述元。",
  [u"0、1、2 號描述元分別是什麼？",
   u"dup2 做什麼？",
   u"為什麼管線的兩端在父行程裡都要關掉？"]),

lesson(u"C 標準函式庫怎麼接到系統呼叫",
  u"printf 背後是 write",
  [u"理解 libc 的角色",
   u"認識 crt0 與 _start",
   u"知道緩衝的影響"],
  [code(u"""// libc/crt0.S：使用者程式真正的進入點
_start:
    mov rdi, [rsp]          ; argc
    lea rsi, [rsp + 8]      ; argv
    call main
    mov rdi, rax            ; main 的回傳值
    call exit               ; 先清空緩衝區，再呼叫 sys_exit

// libc/syscall.c
long write(int fd, const void* buf, size_t n) {
    long r;
    asm volatile("syscall" : "=a"(r) : "a"(1), "D"(fd), "S"(buf), "d"(n) : "rcx", "r11", "memory");
    return r;
}"""),
   ("t", [u"層次", u"例子"],
         [[u"高階函式", u"printf、fopen、malloc（用使用者空間緩衝與記憶體池）"], [u"系統呼叫包裝", u"write、open、mmap、fork"],
          [u"核心", u"sys_write、sys_open"]]),
   ("p", u"<code>printf</code> 不會每次都呼叫 write：它先寫進緩衝區，滿了或遇到換行（終端機）才真的系統呼叫。所以程式當掉時，最後幾行 printf 可能來不及出現。<code>malloc</code> 則向核心要大塊記憶體（brk、mmap）後自己切。常見的 libc 實作有 glibc、musl。"),
  ],
  u"libc 提供 _start、系統呼叫包裝與緩衝等高階功能，是使用者程式和核心之間的橋樑。",
  [u"使用者程式真正的進入點是什麼？",
   u"為什麼 printf 的輸出可能在當機時遺失？",
   u"malloc 怎麼向核心要記憶體？"]),

lesson(u"網路堆疊概觀",
  u"從網卡到 socket",
  [u"理解網路堆疊的分層",
   u"知道封包的收送路徑",
   u"認識 socket 介面"],
  [fig(_NETSTK, 274, u"網路堆疊。"),
   code(u"""int s = socket(AF_INET, SOCK_STREAM, 0);       // 建立 TCP socket（它也是檔案描述元）
connect(s, (struct sockaddr*)&addr, sizeof addr);
write(s, "GET / HTTP/1.0\\r\\n\\r\\n", 18);
read(s, buf, sizeof buf);"""),
   ("ul", [u"<strong>收封包</strong>：網卡用 DMA 放進環形緩衝區 → 中斷 → 驅動交給 IP 層 → TCP 依連接埠找到 socket → 喚醒在 read 等待的行程。",
           u"<strong>socket 是檔案描述元</strong>：VFS 的威力再次出現（" + LS(34) + u"）。",
           u"<strong>現代最佳化</strong>：中斷合併、多佇列網卡、零複製傳送。"]),
   ("p", u"各層協定的細節見 " + XL("net") + u"。"),
  ],
  u"核心的網路堆疊由驅動、鏈結、網路、傳輸層組成，最後以 socket 這個檔案描述元交給程式。",
  [u"封包從網卡到程式經過哪些層？",
   u"為什麼 socket 可以用 read／write？",
   u"多佇列網卡有什麼好處？"]),
]),

(u"模組 H｜真實世界", [

lesson(u"Linux 核心原始碼地圖",
  u"三千萬行程式碼從哪裡讀起",
  [u"認識 Linux 原始碼的組織",
   u"對照本主題的教學核心",
   u"知道閱讀原始碼的入口"],
  [fig(_LINUX, 212, u"Linux 原始碼的主要資料夾。"),
   ("t", [u"本主題", u"Linux 對應"],
         [[u"kmain（" + LS(8) + u"）", u"init/main.c：start_kernel()"], [u"IDT 與例外（" + LS(12) + u"）", u"arch/x86/kernel/idt.c、traps.c"],
          [u"頁框配置（" + LS(17) + u"）", u"mm/page_alloc.c（夥伴系統）"], [u"slab（" + LS(20) + u"）", u"mm/slub.c"],
          [u"情境切換（" + LS(24) + u"）", u"arch/x86/entry/entry_64.S：__switch_to_asm"], [u"排程（" + LS(25) + u"）", u"kernel/sched/"],
          [u"系統呼叫表（" + LS(27) + u"）", u"arch/x86/entry/syscalls/syscall_64.tbl"], [u"VFS（" + LS(34) + u"）", u"fs/namei.c、fs/read_write.c"]]),
   ("p", u"drivers/ 佔了原始碼的一大半——作業系統最龐大的部分往往不是核心演算法，而是支援成千上萬種硬體。"),
  ],
  u"Linux 的結構和教學核心相同，只是每個部分都深入了無數倍；drivers 佔了最多的程式碼。",
  [u"Linux 的 start_kernel 在哪個檔案？",
   u"Linux 的情境切換程式碼在哪裡？",
   u"為什麼 drivers 資料夾最大？"]),

lesson(u"Windows NT 與 macOS XNU",
  u"另外兩大作業系統的架構",
  [u"認識 Windows NT 的分層",
   u"認識 XNU 的組成",
   u"比較三大作業系統"],
  [fig(_NTXNU, 246, u"Windows NT 與 macOS XNU。"),
   ("t", [u"項目", u"Linux", u"Windows NT", u"macOS XNU"],
         [[u"架構", u"單體式＋模組", u"混合式", u"混合式（Mach＋BSD）"], [u"執行檔格式", u"ELF", u"PE", u"Mach-O"],
          [u"建立行程", u"fork＋exec", u"CreateProcess", u"fork＋exec／posix_spawn"], [u"驅動框架", u"核心模組", u"WDM／WDF", u"IOKit（C++ 子集）、DriverKit"],
          [u"主要檔案系統", u"ext4、Btrfs", u"NTFS、ReFS", u"APFS"]]),
   ("p", u"macOS 系統的使用面可參考網站上的 macOS 主題；執行檔格式的差異見 " + XL("exe") + u"。"),
  ],
  u"三大作業系統的核心概念相通，但在架構、執行檔格式、驅動框架上各有不同的歷史選擇。",
  [u"Windows NT 的 HAL 是什麼？",
   u"XNU 由哪三部分組成？",
   u"三大系統的執行檔格式各是什麼？"]),

lesson(u"多核心、安全機制與總結",
  u"從玩具核心到真實系統還差什麼",
  [u"認識多核心帶來的挑戰",
   u"知道現代核心的安全機制",
   u"總結整個主題"],
  [("h", u"1. 多核心"),
   ("ul", [u"開機時只有一顆 CPU（BSP）在跑，核心用 INIT／SIPI 訊號喚醒其他 CPU（AP）。",
           u"每顆 CPU 有自己的計時器、就緒佇列、目前行程（per-CPU 資料）。",
           u"共享資料都需要鎖或原子操作（" + LS(30) + u"）；鎖競爭成為效能瓶頸。",
           u"修改頁表後要通知其他 CPU 清 TLB（TLB shootdown）。"]),
   ("h", u"2. 安全機制"),
   ("t", [u"機制", u"防止什麼"],
         [[u"NX（不可執行）", u"在資料區（堆疊）執行注入的程式碼"], [u"ASLR／KASLR", u"攻擊者預測程式或核心的位址"],
          [u"SMEP／SMAP", u"核心執行或存取使用者空間的記憶體"], [u"堆疊保護", u"緩衝區溢位覆蓋返回位址"],
          [u"KPTI", u"Meltdown 類的推測執行漏洞（" + LS(21) + u"）"]]),
   ("h", u"3. 總結"),
   ("t", [u"模組", u"做到了什麼"],
         [[u"B", u"開機、印字"], [u"C", u"中斷、例外、計時器、鍵盤"], [u"D", u"實體記憶體、分頁、核心堆積"],
          [u"E", u"行程、排程、系統呼叫、使用者程式"], [u"F", u"驅動、磁碟、檔案系統"], [u"G", u"終端機、shell、管線、libc、網路"]]),
   ("p", u"想實際動手，可以參考 OSDev Wiki 等社群資源，或研究 xv6（MIT 的教學作業系統）原始碼。上層的應用程式怎麼使用這些服務，可以接著看 " + XL("ap") + u" 與 " + XL("ga") + u"。"),
  ],
  u"作業系統是硬體與應用之間的基礎：從開機到 shell，每一層都建立在前一層之上。",
  [u"其他 CPU 是怎麼被喚醒的？",
   u"NX 和 ASLR 分別防止什麼攻擊？",
   u"什麼是 TLB shootdown？"]),
]),
]
