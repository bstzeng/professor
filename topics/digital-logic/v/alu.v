// alu.v：RV32I 用的 32 位元 ALU
module alu(input [31:0] a, input [31:0] b, input [3:0] op, output reg [31:0] y, output zero);
  localparam ADD = 4'd0, SUB = 4'd1, AND = 4'd2, OR = 4'd3, XOR = 4'd4,
             SLT = 4'd5, SLTU = 4'd6, SLL = 4'd7, SRL = 4'd8, SRA = 4'd9;
  always @(*) begin
    case (op)
      ADD:  y = a + b;
      SUB:  y = a - b;
      AND:  y = a & b;
      OR:   y = a | b;
      XOR:  y = a ^ b;
      SLT:  y = ($signed(a) < $signed(b)) ? 32'd1 : 32'd0;   // 有號比較
      SLTU: y = (a < b) ? 32'd1 : 32'd0;                     // 無號比較
      SLL:  y = a << b[4:0];                                  // 只取低 5 位當移位量
      SRL:  y = a >> b[4:0];                                  // 邏輯右移：補 0
      SRA:  y = $signed(a) >>> b[4:0];                        // 算術右移：補符號位
      default: y = 32'd0;
    endcase
  end
  assign zero = (y == 32'd0);
endmodule

// barrel.v 的概念：32 位元桶式左移器，用 5 層 2 選 1 多工器組成
module barrel_sll(input [31:0] a, input [4:0] sh, output [31:0] y);
  wire [31:0] s0 = sh[0] ? {a[30:0], 1'b0}   : a;    // 移 1
  wire [31:0] s1 = sh[1] ? {s0[29:0], 2'b0}  : s0;   // 移 2
  wire [31:0] s2 = sh[2] ? {s1[27:0], 4'b0}  : s1;   // 移 4
  wire [31:0] s3 = sh[3] ? {s2[23:0], 8'b0}  : s2;   // 移 8
  assign      y  = sh[4] ? {s3[15:0], 16'b0} : s3;   // 移 16
endmodule
