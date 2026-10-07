module tb_alu;
  reg [31:0] a, b; reg [3:0] op; wire [31:0] y; wire zero;
  alu dut(a, b, op, y, zero);
  reg [31:0] x; reg [4:0] sh; wire [31:0] ys;
  barrel_sll bs(x, sh, ys);
  integer i, err, seed;
  initial begin
    a = 32'd7; b = 32'd5;
    for (i = 0; i < 10; i = i + 1) begin op = i; #1 $display("op=%0d  7, 5 -> %0d", op, $signed(y)); end
    a = -32'sd8; b = 32'd1;
    op = 5; #1 $display("slt(-8, 1)  = %0d   (signed: -8 < 1)", y);
    op = 6; #1 $display("sltu(-8, 1) = %0d   (unsigned: 0xFFFFFFF8 > 1)", y);
    op = 8; #1 $display("srl(-8, 1)  = 0x%h", y);
    op = 9; #1 $display("sra(-8, 1)  = %0d", $signed(y));
    a = 32'd42; b = 32'd42; op = 1; #1 $display("42 - 42 = %0d, zero = %b", y, zero);
    err = 0; seed = 1;
    for (i = 0; i < 10000; i = i + 1) begin
      x = $random(seed); sh = $random(seed);
      #1 if (ys !== (x << sh)) err = err + 1;
    end
    $display("barrel shifter: 10000 random tests, errors = %0d", err);
  end
endmodule
