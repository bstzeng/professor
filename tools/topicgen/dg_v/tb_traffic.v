module tb_traffic;
  reg clk = 0, rst = 1, ped = 0;
  wire [1:0] ns, ew;
  traffic dut(clk, rst, ped, ns, ew);
  always #5 clk = ~clk;
  function [23:0] name(input [1:0] c);
    name = (c == 2) ? "GRN" : (c == 1) ? "YEL" : "red";
  endfunction
  integer n;
  initial begin
    @(posedge clk); #1 rst = 0;
    $display("cycle | N-S  E-W | ped");
    for (n = 0; n < 22; n = n + 1) begin
      ped = (n == 16);                       // 第 16 拍有人按行人按鈕
      $display("%5d | %s  %s |  %b", n, name(ns), name(ew), ped);
      @(posedge clk); #1;
    end
    $finish;
  end
endmodule
