// tb_adders.v：用窮舉法驗證加法器，並示範加減法與溢位
module tb_adders;
  reg [7:0] a, b; reg cin;
  wire [7:0] s; wire cout;
  ripple_adder #(8) r8(a, b, cin, s, cout);
  reg [3:0] x, y; reg ci; wire [3:0] sc; wire co;
  cla4 c4(x, y, ci, sc, co);
  integer i, j, k, err;
  initial begin
    err = 0;
    for (i = 0; i < 256; i = i + 1) for (j = 0; j < 256; j = j + 1) for (k = 0; k < 2; k = k + 1) begin
      a = i; b = j; cin = k;
      #1 if ({cout, s} !== i + j + k) err = err + 1;
    end
    $display("ripple_adder 8-bit: %0d cases, errors = %0d", 256*256*2, err);
    err = 0;
    for (i = 0; i < 16; i = i + 1) for (j = 0; j < 16; j = j + 1) for (k = 0; k < 2; k = k + 1) begin
      x = i; y = j; ci = k;
      #1 if ({co, sc} !== i + j + k) err = err + 1;
    end
    $display("cla4: %0d cases, errors = %0d", 16*16*2, err);
    // 二補數減法：a - b = a + ~b + 1
    a = 8'd100; b = ~8'd37; cin = 1; #1 $display("100 - 37 = %0d (cout=%b)", s, cout);
    a = 8'd20;  b = ~8'd50; cin = 1; #1 $display("20 - 50 = %0d as signed (bits %b)", $signed(s), s);
    // 有號溢位：兩個正數相加得到負數
    a = 8'd100; b = 8'd50; cin = 0;   #1 $display("100 + 50 = %0d as signed -> overflow = %b", $signed(s), (a[7] == b[7]) && (s[7] != a[7]));
  end
endmodule
