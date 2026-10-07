`timescale 1ns/1ps
module tb_glitch;
  reg a, b, c; wire f1, f2;
  hazard      h1(a, b, c, f1);
  hazard_free h2(a, b, c, f2);
  initial begin
    $timeformat(-9, 0, " ns", 6);
    $monitor("t=%t  a=%b  f(hazard)=%b  f(hazard_free)=%b", $time, a, f1, f2);
    b = 1; c = 1; a = 1;
    #20 a = 0;     // 在 20 ns 時把 A 從 1 改成 0
    #20 $finish;
  end
endmodule
