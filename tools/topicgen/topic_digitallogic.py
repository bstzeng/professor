# -*- coding: utf-8 -*-
"""數位邏輯設計主題的規格。產生頁面時會把 Verilog 範例複製到 topics/digital-logic/v/ 並打包成 zip。"""
import io
import os
import shutil
import zipfile
import dg_a, dg_b, dg_c, dg_d, dg_ref
from dg_common import VDIR, PUBLISH

TOPIC = {
    "id": "digital-logic",
    "category": "tech",
    "title": u"數位邏輯設計：從邏輯閘到一顆 CPU",
    "short": u"數位邏輯設計",
    "crumb": u"數位邏輯設計",
    "icon": u"🔌",
    "description": u"大學部程度的數位邏輯設計，附推導與可執行的 Verilog 範例：雜訊邊限、二補數、CMOS 閘、NAND 萬用；布林代數、卡諾圖、Quine–McCluskey；"
                   u"閘延遲、邏輯努力、關鍵路徑、毛刺與危障、為什麼需要時脈；多工器、解碼器、加法器、超前進位與平行前綴、ALU、乘法器、桶式移位器；"
                   u"閂鎖器、主從式正反器、setup／hold、亞穩態；暫存器、計數器、有限狀態機、時脈偏移與同步器；Verilog、合成與 FPGA；SRAM、DRAM、快閃；"
                   u"最後用約 70 行 Verilog 做出一顆執行 RISC-V 程式的單週期 CPU，並介紹多週期與管線化。所有範例都以 Icarus Verilog 實跑、可整包下載，附九個互動工具。",
}

MODULES = dg_a.MODULES + dg_b.MODULES + dg_c.MODULES + dg_d.MODULES

REFERENCES = dg_ref.REFERENCES


def _publish():
    out = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "topics", TOPIC["id"], "v")
    if os.path.isdir(out):
        shutil.rmtree(out)
    os.makedirs(out)
    for n in PUBLISH:
        shutil.copyfile(os.path.join(VDIR, n), os.path.join(out, n))
    readme = (u"數位邏輯設計：Verilog 範例\n\n"
              u"需要 Icarus Verilog 12（iverilog、vvp）與 Python 3。\n"
              u"  Linux：apt install iverilog    macOS：brew install icarus-verilog    Windows：bleyer.org/icarus\n\n"
              u"執行全部範例：sh run_all.sh\n"
              u"輸出會寫到 _out/<名稱>.txt，與課程頁面上的模擬結果相同。\n\n"
              u"單獨執行一個範例，例如：\n"
              u"  iverilog -g2012 -o adders tb_adders.v adders.v && vvp adders\n\n"
              u"RISC-V CPU：\n"
              u"  python3 asm.py prog.s prog.hex\n"
              u"  iverilog -g2012 -o rv tb_rv_single.v rv_single.v regfile.v alu.v && vvp rv\n")
    with zipfile.ZipFile(os.path.join(out, "digital-logic-verilog.zip"), "w", zipfile.ZIP_DEFLATED) as z:
        def add(name, data, mode=0o644):
            info = zipfile.ZipInfo("digital-logic-verilog/" + name, date_time=(2026, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = mode << 16
            z.writestr(info, data)
        add("README.txt", readme.encode("utf-8"))
        for n in PUBLISH:
            add(n, io.open(os.path.join(VDIR, n), "rb").read(), 0o755 if n.endswith(".sh") else 0o644)


_publish()
