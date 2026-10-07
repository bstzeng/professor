module tb_decoder;
  reg [2:0] a; reg en; wire [7:0] y;
  reg [7:0] r; wire [2:0] code; wire valid;
  dec3to8 d(a, en, y);
  prienc8 p(r, code, valid);
  integer i;
  initial begin
    en = 1;
    $display("decoder:");
    for (i = 0; i < 8; i = i + 1) begin a = i; #1 $display("  a=%0d -> y=%b", a, y); end
    $display("priority encoder:");
    r = 8'b0000_0000; #1 $display("  r=%b -> valid=%b", r, valid);
    r = 8'b0001_0110; #1 $display("  r=%b -> code=%0d valid=%b", r, code, valid);
    r = 8'b1000_0001; #1 $display("  r=%b -> code=%0d valid=%b", r, code, valid);
  end
endmodule
