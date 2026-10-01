# -*- coding: utf-8 -*-
"""作業系統是怎麼寫出來的：參考頁。"""
from sa_common import LS, SALIB, widget, steps
from os_a import _PT, _BOOT, _BOOTB
from os_e import _SYS, _SYSB

CHEATSHEET = {
    "file": "cheatsheet.html", "title": u"作業系統開發速查表", "h1": u"作業系統是怎麼寫出來的：速查表", "icon": u"🗂️",
    "description": u"x86-64 重要暫存器、例外向量、頁表位元、系統呼叫慣例與術語中英對照，一頁查完",
    "body": [
        ("h", u"1. 四層頁表"),
        ("fig", _PT, "0 0 640 202", u"x86-64 的四層頁表。"),
        ("h", u"2. 重要暫存器與指令"),
        ("t", [u"名稱", u"用途", u"課"],
         [[u"CR0.PG／CR4.PAE／EFER.LME", u"開啟分頁與長模式", LS(7)], [u"CR2", u"分頁錯誤的位址", LS(13)], [u"CR3", u"目前頁表（PML4）的實體位址", LS(21)],
          [u"lgdt／lidt", u"載入 GDT／IDT", LS(12)], [u"iretq", u"從中斷返回", LS(12)], [u"syscall／sysretq", u"進入／離開系統呼叫", LS(27)],
          [u"invlpg", u"清除一頁的 TLB", LS(18)], [u"in／out", u"連接埠 I/O", LS(10)], [u"cli／sti／hlt", u"關中斷／開中斷／休眠到下一次中斷", LS(8)]]),
        ("h", u"3. 常見例外向量"),
        ("t", [u"向量", u"名稱"], [[u"0", u"#DE 除以零"], [u"6", u"#UD 無效指令"], [u"8", u"#DF 雙重錯誤"], [u"13", u"#GP 一般保護錯誤"], [u"14", u"#PF 分頁錯誤"], [u"32 以後", u"硬體中斷（重新對應後）"]]),
        ("h", u"4. 頁表項位元"),
        ("t", [u"位元", u"意義"], [[u"0 P", u"存在"], [u"1 R/W", u"可寫"], [u"2 U/S", u"使用者可存取"], [u"5 A／6 D", u"已存取／已寫入（髒）"], [u"63 NX", u"不可執行"]]),
        ("h", u"5. Linux x86-64 系統呼叫慣例"),
        ("t", [u"項目", u"暫存器"], [[u"系統呼叫編號", u"rax"], [u"參數 1～6", u"rdi、rsi、rdx、r10、r8、r9"], [u"回傳值", u"rax（負值為 -errno）"], [u"被破壞", u"rcx、r11"]]),
        ("h", u"6. 術語中英對照"),
        ("t", [u"中文", u"英文", u"課"],
         [[u"核心", u"Kernel", LS(1)], [u"開機載入程式", u"Bootloader", LS(6)], [u"中斷描述表", u"IDT", LS(12)], [u"頁框", u"Page Frame", LS(17)],
          [u"轉譯後備緩衝區", u"TLB", LS(18)], [u"寫入時複製", u"Copy-on-Write", LS(22)], [u"情境切換", u"Context Switch", LS(24)],
          [u"系統呼叫", u"System Call", LS(27)], [u"自旋鎖", u"Spinlock", LS(30)], [u"直接記憶體存取", u"DMA", LS(33)],
          [u"虛擬檔案系統", u"VFS", LS(34)], [u"頁快取", u"Page Cache", LS(37)], [u"行規", u"Line Discipline", LS(39)]]),
    ],
}

SIM = {
    "file": "playground.html", "title": u"作業系統互動實驗室", "h1": u"作業系統互動實驗室", "icon": u"🕹️",
    "description": u"開機流程、頁框配置、位址轉換、排程、系統呼叫、競爭條件，六個互動實驗",
    "body": [
        ("raw", u"<script>%s</script>" % SALIB),
        ("h", u"1. 開機流程"), steps(_BOOT, u"", _BOOTB),
        ("h", u"2. 實體頁框配置"), widget({"t": "frames"}),
        ("h", u"3. 位址轉換"), widget({"t": "xlate"}),
        ("h", u"4. 排程演算法"), widget({"t": "sched"}),
        ("h", u"5. 系統呼叫的旅程"), steps(_SYS, u"", _SYSB),
        ("h", u"6. 競爭條件"), widget({"t": "race"}),
    ],
}

REFERENCES = [CHEATSHEET, SIM]
