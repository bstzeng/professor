// latches.v：從 SR 閂鎖器到主從式 D 正反器
`timescale 1ns/1ps
// SR 閂鎖器：兩個 NOR 閘交叉回授
module sr_latch(input s, input r, output q, output qn);
  nor #1 g1(q,  r, qn);
  nor #1 g2(qn, s, q);
endmodule

// D 閂鎖器：en = 1 時 q 跟著 d（透明），en = 0 時保持
module d_latch(input d, input en, output q, output qn);
  wire s, r, dn;
  not #1 g0(dn, d);
  and #1 g1(s, d, en);
  and #1 g2(r, dn, en);
  sr_latch l(s, r, q, qn);
endmodule

// 主從式 D 正反器：clk = 0 時主閂鎖器透明，clk = 1 時從閂鎖器透明
// 結果：q 只會在 clk 由 0 變 1 的瞬間更新
module dff_ms(input d, input clk, output q);
  wire m, mn, clkn, qn;
  not #1 g(clkn, clk);
  d_latch master(d, clkn, m, mn);
  d_latch slave (m, clk,  q, qn);
endmodule

// 行為描述的 D 正反器（實務上都這樣寫，交給合成工具）
module dff(input d, input clk, input rst, output reg q);
  always @(posedge clk or posedge rst)
    if (rst) q <= 1'b0;
    else     q <= d;
endmodule
