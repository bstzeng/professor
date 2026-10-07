// mux.v：4 選 1 多工器的三種寫法
module mux4_assign(input [3:0] d, input [1:0] s, output y);
  assign y = s[1] ? (s[0] ? d[3] : d[2]) : (s[0] ? d[1] : d[0]);  // 條件運算子
endmodule

module mux4_case(input [3:0] d, input [1:0] s, output reg y);
  always @(*) begin           // 組合邏輯：任何輸入改變就重新計算
    case (s)
      2'b00: y = d[0];
      2'b01: y = d[1];
      2'b10: y = d[2];
      default: y = d[3];
    endcase
  end
endmodule

module mux4_gates(input [3:0] d, input [1:0] s, output y);
  // 積之和：y = s1's0'd0 + s1's0 d1 + s1 s0'd2 + s1 s0 d3
  wire n1, n0;
  not (n1, s[1]); not (n0, s[0]);
  wire t0, t1, t2, t3;
  and (t0, n1, n0, d[0]); and (t1, n1, s[0], d[1]);
  and (t2, s[1], n0, d[2]); and (t3, s[1], s[0], d[3]);
  or  (y, t0, t1, t2, t3);
endmodule
