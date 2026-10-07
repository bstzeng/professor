// gates.v：基本邏輯閘（結構式寫法，直接使用 Verilog 內建的閘）
module gates(input a, input b, output y_and, output y_or, output y_xor,
             output y_nand, output y_nor, output y_not);
  and  g1(y_and,  a, b);
  or   g2(y_or,   a, b);
  xor  g3(y_xor,  a, b);
  nand g4(y_nand, a, b);
  nor  g5(y_nor,  a, b);
  not  g6(y_not,  a);
endmodule
