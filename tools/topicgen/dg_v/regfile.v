// regfile.v：RISC-V 的 32 個 32 位元暫存器，兩個讀埠、一個寫埠，x0 永遠是 0
module regfile(input clk, input we, input [4:0] ra1, input [4:0] ra2, input [4:0] wa,
               input [31:0] wd, output [31:0] rd1, output [31:0] rd2);
  reg [31:0] r [1:31];
  assign rd1 = (ra1 == 0) ? 32'd0 : r[ra1];  // 讀取是組合邏輯：立刻得到
  assign rd2 = (ra2 == 0) ? 32'd0 : r[ra2];
  always @(posedge clk)                      // 寫入在時脈邊緣
    if (we && wa != 0) r[wa] <= wd;
endmodule
