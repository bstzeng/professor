// fsm_seq.v：偵測輸入序列 1011（允許重疊），Moore 與 Mealy 兩種寫法
module seq1011_moore(input clk, input rst, input x, output y);
  localparam S0 = 3'd0, S1 = 3'd1, S10 = 3'd2, S101 = 3'd3, S1011 = 3'd4;
  reg [2:0] state, next;
  always @(posedge clk) state <= rst ? S0 : next;        // 狀態暫存器
  always @(*) begin                                       // 下一狀態邏輯
    case (state)
      S0:    next = x ? S1    : S0;
      S1:    next = x ? S1    : S10;
      S10:   next = x ? S101  : S0;
      S101:  next = x ? S1011 : S10;
      S1011: next = x ? S1    : S10;   // 重疊：結尾的 1 可以當下一次的開頭
      default: next = S0;
    endcase
  end
  assign y = (state == S1011);                            // 輸出只看狀態
endmodule

module seq1011_mealy(input clk, input rst, input x, output y);
  localparam S0 = 2'd0, S1 = 2'd1, S10 = 2'd2, S101 = 2'd3;
  reg [1:0] state, next;
  always @(posedge clk) state <= rst ? S0 : next;
  always @(*) begin
    case (state)
      S0:   next = x ? S1   : S0;
      S1:   next = x ? S1   : S10;
      S10:  next = x ? S101 : S0;
      S101: next = x ? S1   : S10;
    endcase
  end
  assign y = (state == S101) && x;                        // 輸出看狀態與目前輸入
endmodule
