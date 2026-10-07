# prog.s：在我們的單週期 CPU 上執行的程式
# 1) 計算 1 + 2 + ... + 10，存到記憶體位址 0
# 2) 把前 10 個費氏數列存到位址 16 開始的陣列
# 3) 用 jal/jalr 呼叫一個副程式，計算 max(a0, a1)
        addi t0, zero, 0        # t0 = 總和
        addi t1, zero, 1        # t1 = i
        addi t2, zero, 11       # t2 = 上限
loop:   add  t0, t0, t1         # 總和 += i
        addi t1, t1, 1          # i++
        bne  t1, t2, loop       # i != 11 就繼續
        sw   t0, 0(zero)        # mem[0] = 55

        addi s0, zero, 16       # s0 = 陣列位址
        addi a0, zero, 0        # f(0) = 0
        addi a1, zero, 1        # f(1) = 1
        addi s1, zero, 10       # 要存 10 個
fib:    sw   a0, 0(s0)
        add  a2, a0, a1         # 下一項
        addi a0, a1, 0
        addi a1, a2, 0
        addi s0, s0, 4
        addi s1, s1, -1
        bne  s1, zero, fib

        addi a0, zero, 17
        addi a1, zero, 42
        jal  ra, max            # 呼叫副程式，回傳位址存在 ra
        sw   a0, 4(zero)        # mem[4] = max(17, 42)
        lui  a3, 0x12345        # 載入高位：a3 = 0x12345000
        lw   a4, 0(zero)        # 讀回 55
done:   beq  zero, zero, done   # 停在這裡（無窮迴圈）

max:    blt  a0, a1, take_b     # 副程式：a0 = max(a0, a1)
        jalr zero, 0(ra)
take_b: addi a0, a1, 0
        jalr zero, 0(ra)
