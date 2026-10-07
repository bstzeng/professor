module tb_fsm_seq;
  reg clk = 0, rst = 1, x = 0;
  wire ymo, yme;
  seq1011_moore mo(clk, rst, x, ymo);
  seq1011_mealy me(clk, rst, x, yme);
  always #5 clk = ~clk;
  reg [15:0] bits = 16'b0101_1011_0110_1100;
  integer i;
  initial begin
    @(posedge clk); #1 rst = 0;
    $display("input bits: %b", bits);
    $display(" n  x | Mealy y | Moore y (one cycle later)");
    for (i = 15; i >= 0; i = i - 1) begin
      x = bits[i];
      #1 $write("%2d  %b |    %b    |", 15 - i, x, yme);
      @(posedge clk); #1 $display("    %b", ymo);
    end
    $finish;
  end
endmodule
