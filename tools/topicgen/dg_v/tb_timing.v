`timescale 1ns/1ps
// 每個時脈送進一組新的 a、b；加法器只有「一個週期」的時間算出結果
module tb_timing;
  reg clk = 0; reg [7:0] a_in, b_in; wire [7:0] sum;
  reg_adder_reg dut(clk, a_in, b_in, sum);
  reg [7:0] A [0:5], Bv [0:5];
  integer period, i, err;
  task run(input integer p);
    begin
      period = p; err = 0;
      $display("--- clock period %0d ns ---", p);
      for (i = 0; i < 8; i = i + 1) begin
        a_in = A[i % 6]; b_in = Bv[i % 6];
        #(p / 2) clk = 1; #(p - p / 2) clk = 0;     // 一個時脈週期
        if (i >= 1) begin                           // sum 是上一拍送進去的那一組
          $display("  %3d + %3d = %3d  (expected %3d) %s", A[(i - 1) % 6], Bv[(i - 1) % 6], sum,
                   (A[(i - 1) % 6] + Bv[(i - 1) % 6]) & 8'hFF, (sum == ((A[(i - 1) % 6] + Bv[(i - 1) % 6]) & 8'hFF)) ? "" : "<-- WRONG");
          if (sum != ((A[(i - 1) % 6] + Bv[(i - 1) % 6]) & 8'hFF)) err = err + 1;
        end
      end
      $display("  errors: %0d / 7", err);
    end
  endtask
  initial begin
    A[0] = 0;   Bv[0] = 0;
    A[1] = 127; Bv[1] = 1;     // 進位從第 0 位傳到第 7 位：最長路徑
    A[2] = 0;   Bv[2] = 0;
    A[3] = 255; Bv[3] = 1;
    A[4] = 3;   Bv[4] = 4;     // 沒有進位：很快
    A[5] = 100; Bv[5] = 27;
    run(30);
    run(10);
    run(6);
    $finish;
  end
endmodule
