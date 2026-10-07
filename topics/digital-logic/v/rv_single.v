// rv_single.v：單週期 RISC-V CPU（RV32I 子集）
// 支援：add sub and or xor slt sll srl / addi andi ori xori slti / lw sw / beq bne blt bge / jal jalr / lui
// 每個時脈週期完成一條指令：提取 → 解碼 → 執行 → 存取記憶體 → 寫回
module rv_single(input clk, input rst, output [31:0] pc_out, output [31:0] instr_out);
  // ---------- 提取 ----------
  reg  [31:0] pc;
  reg  [31:0] imem [0:63];
  initial $readmemh("prog.hex", imem);
  wire [31:0] instr = imem[pc[7:2]];

  // ---------- 解碼 ----------
  wire [6:0] opcode = instr[6:0];
  wire [4:0] rd = instr[11:7], rs1 = instr[19:15], rs2 = instr[24:20];
  wire [2:0] f3 = instr[14:12];
  wire [6:0] f7 = instr[31:25];

  // 立即值產生器：依指令格式把散落各處的位元拼回來，並做符號延伸
  wire [31:0] imm_i = {{20{instr[31]}}, instr[31:20]};
  wire [31:0] imm_s = {{20{instr[31]}}, instr[31:25], instr[11:7]};
  wire [31:0] imm_b = {{19{instr[31]}}, instr[31], instr[7], instr[30:25], instr[11:8], 1'b0};
  wire [31:0] imm_j = {{11{instr[31]}}, instr[31], instr[19:12], instr[20], instr[30:21], 1'b0};
  wire [31:0] imm_u = {instr[31:12], 12'b0};

  // 主控制單元：由 opcode 決定這條指令要打開哪些開關
  localparam OP_R = 7'h33, OP_I = 7'h13, OP_LW = 7'h03, OP_SW = 7'h23, OP_B = 7'h63, OP_JAL = 7'h6f, OP_JALR = 7'h67, OP_LUI = 7'h37;
  wire is_r = opcode == OP_R, is_i = opcode == OP_I, is_lw = opcode == OP_LW, is_sw = opcode == OP_SW,
       is_b = opcode == OP_B, is_jal = opcode == OP_JAL, is_jalr = opcode == OP_JALR, is_lui = opcode == OP_LUI;
  wire reg_write = is_r | is_i | is_lw | is_jal | is_jalr | is_lui;
  wire alu_src_imm = is_i | is_lw | is_sw | is_jalr;          // ALU 第二個輸入用立即值還是暫存器

  // ALU 控制：把 funct3/funct7 翻譯成 ALU 運算碼（與 alu.v 相同的編碼）
  reg [3:0] alu_op;
  always @(*) begin
    if (is_lw | is_sw | is_jalr) alu_op = 4'd0;                // 位址計算用加法
    else if (is_b)               alu_op = 4'd1;                // 比較用減法
    else case (f3)
      3'b000: alu_op = (is_r && f7[5]) ? 4'd1 : 4'd0;          // add / sub
      3'b001: alu_op = 4'd7;                                   // sll
      3'b010: alu_op = 4'd5;                                   // slt
      3'b100: alu_op = 4'd4;                                   // xor
      3'b101: alu_op = 4'd8;                                   // srl
      3'b110: alu_op = 4'd3;                                   // or
      default: alu_op = 4'd2;                                  // and
    endcase
  end

  // ---------- 執行 ----------
  wire [31:0] rd1, rd2, wb;
  regfile rf(clk, reg_write, rs1, rs2, rd, wb, rd1, rd2);
  wire [31:0] alu_b = alu_src_imm ? (is_sw ? imm_s : imm_i) : rd2;
  wire [31:0] alu_y; wire zero;
  alu u_alu(rd1, alu_b, alu_op, alu_y, zero);

  // ---------- 存取記憶體 ----------
  reg [31:0] dmem [0:63];
  integer k; initial for (k = 0; k < 64; k = k + 1) dmem[k] = 0;
  always @(posedge clk) if (is_sw) dmem[alu_y[7:2]] <= rd2;
  wire [31:0] load_data = dmem[alu_y[7:2]];

  // ---------- 寫回與下一個 PC ----------
  wire [31:0] pc4 = pc + 4;
  assign wb = is_lw ? load_data : (is_jal | is_jalr) ? pc4 : is_lui ? imm_u : alu_y;
  wire lt = $signed(rd1) < $signed(rd2);
  wire take = is_b & ((f3 == 3'b000 & zero) | (f3 == 3'b001 & ~zero) | (f3 == 3'b100 & lt) | (f3 == 3'b101 & ~lt));
  wire [31:0] pc_next = is_jal ? pc + imm_j : is_jalr ? (alu_y & ~32'd1) : take ? pc + imm_b : pc4;
  always @(posedge clk) pc <= rst ? 32'd0 : pc_next;

  assign pc_out = pc; assign instr_out = instr;
endmodule
