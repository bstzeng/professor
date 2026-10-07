// counter.v：同步計數器、移位暫存器與 LFSR
module counter4(input clk, input rst, input en, output reg [3:0] q);
  always @(posedge clk)
    if (rst)     q <= 4'd0;
    else if (en) q <= q + 4'd1;          // 所有位元在同一個時脈邊緣一起更新
endmodule

module shift8(input clk, input rst, input din, output reg [7:0] q);
  always @(posedge clk)
    if (rst) q <= 8'd0;
    else     q <= {q[6:0], din};          // 往左移，新的位元從右邊進來
endmodule

// 4 位元線性回授移位暫存器：x^4 + x^3 + 1，會走過全部 15 個非零狀態
module lfsr4(input clk, input rst, output reg [3:0] q);
  always @(posedge clk)
    if (rst) q <= 4'b0001;
    else     q <= {q[2:0], q[3] ^ q[2]};
endmodule
