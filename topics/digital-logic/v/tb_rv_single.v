module tb_rv_single;
  reg clk = 0, rst = 1;
  wire [31:0] pc, instr;
  rv_single cpu(clk, rst, pc, instr);
  always #5 clk = ~clk;
  integer cycle, i;
  initial begin
    @(posedge clk); #1 rst = 0;
    for (cycle = 1; cycle <= 120; cycle = cycle + 1) begin
      if (cycle <= 9 || (cycle >= 105 && cycle <= 120))
        $display("cycle %3d  pc=%h  instr=%h", cycle, pc, instr);
      else if (cycle == 10) $display("   ... (sum and fib loops omitted) ...");
      @(posedge clk); #1;
    end
    $display("after 120 cycles, pc = %h (spinning at 'done')", pc);
    $display("mem[0]  = %0d   (1 + 2 + ... + 10)", cpu.dmem[0]);
    $display("mem[4]  = %0d   (max(17, 42))", cpu.dmem[1]);
    $write("fib     = ");
    for (i = 4; i < 14; i = i + 1) $write("%0d ", cpu.dmem[i]);
    $display("");
    $display("x13(a3) = 0x%h   (lui 0x12345)", cpu.rf.r[13]);
    $display("x14(a4) = %0d   (lw 0(zero))", cpu.rf.r[14]);
    $display("x1(ra)  = 0x%h   (return address saved by jal)", cpu.rf.r[1]);
    $finish;
  end
endmodule
