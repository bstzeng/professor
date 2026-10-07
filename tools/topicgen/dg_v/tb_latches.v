`timescale 1ns/1ps
module tb_latches;
  reg s, r; wire q, qn;
  sr_latch sr(s, r, q, qn);
  reg d, clk; wire ql, qln, qf;
  d_latch  dl(d, clk, ql, qln);
  dff_ms   ff(d, clk, qf);
  initial begin
    $timeformat(-9, 0, " ns", 5);
    $display("--- SR latch ---");
    s = 0; r = 1; #5 $display("reset       : q=%b", q);
    s = 0; r = 0; #5 $display("hold        : q=%b", q);
    s = 1; r = 0; #5 $display("set         : q=%b", q);
    s = 0; r = 0; #5 $display("hold        : q=%b  <- 記住了", q);
    $display("--- D latch vs D flip-flop (clk 週期 20 ns，50/70/90 ns 上升) ---");
    $display("   time   clk d | latch flipflop");
  end
  // 時脈：前 40 ns 留給 SR 閂鎖器測試；之後週期 20 ns，在 50、70、90 ns 變成 1
  initial begin clk = 0; #40; forever #10 clk = ~clk; end
  // 資料：故意在 clk = 1 的期間改變，看兩者的差別
  initial begin
    d = 0; #40 d = 1;
    #13 d = 0; #2 d = 1; #2 d = 0;       // 53~57 ns：clk = 1 時 d 抖動
    #8  d = 1;                           // 65 ns：clk = 0 時改成 1
    #10 d = 0;                           // 75 ns：clk = 1 時改成 0
    #20 d = 1;                           // 95 ns：clk = 1 時改成 1
  end
  always @(clk or d or ql or qf) if ($time >= 50) $display("%t   %b   %b |   %b      %b", $time, clk, d, ql, qf);
  initial #112 $finish;
endmodule
