# asm.py：極小的 RISC-V（RV32I 子集）組譯器，把 prog.s 轉成 prog.hex 給 Verilog 的 $readmemh 讀取
# 用法：python asm.py prog.s prog.hex
import re, sys

REG = {**{"x%d" % i: i for i in range(32)}, "zero": 0, "ra": 1, "sp": 2, "gp": 3, "tp": 4, "t0": 5, "t1": 6, "t2": 7,
       "s0": 8, "fp": 8, "s1": 9, **{"a%d" % i: 10 + i for i in range(8)}, **{"s%d" % i: 16 + i for i in range(2, 12)},
       **{"t%d" % i: 25 + i for i in range(3, 7)}}
R = {"add": (0, 0x00), "sub": (0, 0x20), "sll": (1, 0), "slt": (2, 0), "xor": (4, 0), "srl": (5, 0), "or": (6, 0), "and": (7, 0)}
I = {"addi": 0, "slti": 2, "xori": 4, "ori": 6, "andi": 7}
B = {"beq": 0, "bne": 1, "blt": 4, "bge": 5}

def reg(s): return REG[s.strip()]

def imm(s, labels, pc, rel=False):
    s = s.strip()
    if s in labels: return labels[s] - pc if rel else labels[s]
    return int(s, 0)

def enc(op, args, labels, pc):
    if op in R:
        f3, f7 = R[op]; rd, rs1, rs2 = map(reg, args)
        return f7 << 25 | rs2 << 20 | rs1 << 15 | f3 << 12 | rd << 7 | 0x33
    if op in I:
        rd, rs1 = reg(args[0]), reg(args[1]); v = imm(args[2], labels, pc) & 0xFFF
        return v << 20 | rs1 << 15 | I[op] << 12 | rd << 7 | 0x13
    if op in ("lw", "sw", "jalr"):
        m = re.match(r"(-?\w+)\((\w+)\)", args[1].strip())
        off, base = int(m.group(1), 0), reg(m.group(2))
        if op == "lw":   return (off & 0xFFF) << 20 | base << 15 | 2 << 12 | reg(args[0]) << 7 | 0x03
        if op == "jalr": return (off & 0xFFF) << 20 | base << 15 | 0 << 12 | reg(args[0]) << 7 | 0x67
        v = off & 0xFFF; rs2 = reg(args[0])
        return (v >> 5) << 25 | rs2 << 20 | base << 15 | 2 << 12 | (v & 0x1F) << 7 | 0x23
    if op in B:
        rs1, rs2 = reg(args[0]), reg(args[1]); v = imm(args[2], labels, pc, True) & 0x1FFF
        return ((v >> 12) & 1) << 31 | ((v >> 5) & 0x3F) << 25 | rs2 << 20 | rs1 << 15 | B[op] << 12 | ((v >> 1) & 0xF) << 8 | ((v >> 11) & 1) << 7 | 0x63
    if op == "jal":
        rd = reg(args[0]); v = imm(args[1], labels, pc, True) & 0x1FFFFF
        return ((v >> 20) & 1) << 31 | ((v >> 1) & 0x3FF) << 21 | ((v >> 11) & 1) << 20 | ((v >> 12) & 0xFF) << 12 | rd << 7 | 0x6F
    if op == "lui":
        return (imm(args[1], labels, pc) & 0xFFFFF) << 12 | reg(args[0]) << 7 | 0x37
    raise ValueError("unknown instruction: " + op)

def assemble(text):
    lines, labels, pc = [], {}, 0
    for raw in text.splitlines():
        line = raw.split("#")[0].strip()
        while ":" in line:
            lab, line = line.split(":", 1); labels[lab.strip()] = pc; line = line.strip()
        if line:
            lines.append((pc, line, raw.split("#")[0].strip())); pc += 4
    out = []
    for pc, line, src in lines:
        op, *rest = line.split(None, 1)
        args = [a for a in re.split(r",\s*", rest[0])] if rest else []
        out.append((pc, enc(op, args, labels, pc), line))
    return out

if __name__ == "__main__":
    words = assemble(open(sys.argv[1], encoding="utf-8").read())
    with open(sys.argv[2], "w") as f:
        for pc, w, line in words:
            f.write("%08x\n" % w)
            print("%04x: %08x   %s" % (pc, w, line))
        for _ in range(64 - len(words)):        # 剩下的位置補 nop（addi x0, x0, 0），填滿 64 個字
            f.write("00000013\n")
