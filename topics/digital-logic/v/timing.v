// timing.v：時脈太快會怎樣？
// 兩排暫存器之間夾一個 8 位元漣波進位加法器，每個閘延遲 1 ns
`timescale 1ns/1ps
module fa_d(input a, input b, input cin, output s, output cout);
  wire p, g, t;
  xor #1 x1(p, a, b);
  xor #1 x2(s, p, cin);
  and #1 a1(g, a, b);
  and #1 a2(t, p, cin);
  or  #1 o1(cout, g, t);
endmodule

module adder8_d(input [7:0] a, input [7:0] b, output [7:0] s);
  wire [8:0] c; assign c[0] = 1'b0;
  genvar i;
  generate for (i = 0; i < 8; i = i + 1) begin : st
    fa_d fa(a[i], b[i], c[i], s[i], c[i+1]);
  end endgenerate
endmodule

// 暫存器 → 加法器 → 暫存器：每個時脈把新的 a、b 打進來，同時把上一拍的和存起來
module reg_adder_reg(input clk, input [7:0] a_in, input [7:0] b_in, output reg [7:0] sum);
  reg [7:0] a, b; wire [7:0] s;
  adder8_d add(a, b, s);
  always @(posedge clk) begin
    a <= a_in; b <= b_in;
    sum <= s;
  end
endmodule
