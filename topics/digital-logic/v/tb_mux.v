// tb_mux.v：窮舉 64 種輸入，檢查三種寫法是否完全相同
module tb_mux;
  reg [3:0] d; reg [1:0] s;
  wire ya, yc, yg;
  mux4_assign m1(d, s, ya);
  mux4_case   m2(d, s, yc);
  mux4_gates  m3(d, s, yg);
  integer i, err;
  initial begin
    err = 0;
    for (i = 0; i < 64; i = i + 1) begin
      {s, d} = i;
      #1 if (ya !== d[s] || yc !== d[s] || yg !== d[s]) err = err + 1;
    end
    $display("checked 64 cases, errors = %0d", err);
    d = 4'b1010;
    for (i = 0; i < 4; i = i + 1) begin s = i; #1 $display("d=%b s=%0d -> y=%b", d, s, ya); end
  end
endmodule
