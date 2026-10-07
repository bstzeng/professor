module tb_counter;
  reg clk = 0, rst = 1, en = 1, din = 0;
  wire [3:0] q; wire [7:0] sq; wire [3:0] lq;
  counter4 c(clk, rst, en, q);
  shift8   s(clk, rst, din, sq);
  lfsr4    l(clk, rst, lq);
  always #5 clk = ~clk;
  reg [7:0] pattern = 8'b1011_0010;
  integer n;
  initial begin
    @(posedge clk); #1 rst = 0;
    $display("cycle | counter | shift8 (din) | lfsr");
    for (n = 1; n <= 18; n = n + 1) begin
      din = pattern[7 - (n - 1) % 8];
      if (n == 10) en = 0;                    // 第 10 拍暫停計數
      if (n == 12) en = 1;
      @(posedge clk); #1;
      $display("%5d |  %2d     | %b (%b)   | %b", n, q, sq, din, lq);
    end
    $finish;
  end
endmodule
