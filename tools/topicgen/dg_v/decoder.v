// decoder.v：3 對 8 解碼器與 8 對 3 優先權編碼器
module dec3to8(input [2:0] a, input en, output [7:0] y);
  assign y = en ? (8'b1 << a) : 8'b0;      // 只有第 a 條輸出為 1
endmodule

module prienc8(input [7:0] r, output reg [2:0] code, output reg valid);
  integer i;
  always @(*) begin
    code = 3'd0; valid = 1'b0;
    for (i = 0; i < 8; i = i + 1)          // 從低到高掃描，最後找到的（最高位）勝出
      if (r[i]) begin code = i[2:0]; valid = 1'b1; end
  end
endmodule
