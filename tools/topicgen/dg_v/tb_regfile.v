module tb_regfile;
  reg clk = 0, we = 0; reg [4:0] ra1, ra2, wa; reg [31:0] wd; wire [31:0] rd1, rd2;
  regfile rf(clk, we, ra1, ra2, wa, wd, rd1, rd2);
  always #5 clk = ~clk;
  initial begin
    we = 1; wa = 5;  wd = 32'd123; @(posedge clk); #1;
    wa = 6;  wd = 32'd456; @(posedge clk); #1;
    wa = 0;  wd = 32'd999; @(posedge clk); #1;   // 寫 x0 會被忽略
    we = 0; ra1 = 5; ra2 = 6; #1 $display("x5 = %0d, x6 = %0d", rd1, rd2);
    ra1 = 0; #1 $display("x0 = %0d (writes to x0 are ignored)", rd1);
    $finish;
  end
endmodule
