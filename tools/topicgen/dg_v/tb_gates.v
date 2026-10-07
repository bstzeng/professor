// tb_gates.v：列出所有輸入組合的真值表
module tb_gates;
  reg a, b;
  wire y_and, y_or, y_xor, y_nand, y_nor, y_not;
  gates dut(a, b, y_and, y_or, y_xor, y_nand, y_nor, y_not);
  integer i;
  initial begin
    $display(" a b | AND OR XOR NAND NOR NOT(a)");
    for (i = 0; i < 4; i = i + 1) begin
      {a, b} = i;
      #1 $display(" %b %b |  %b   %b   %b    %b    %b    %b", a, b, y_and, y_or, y_xor, y_nand, y_nor, y_not);
    end
  end
endmodule
