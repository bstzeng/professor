// sync.v：兩級正反器同步器——把來自另一個時脈域的訊號安全地帶進來
module sync2(input clk, input async_in, output reg sync_out);
  reg meta;                                  // 第一級可能進入亞穩態
  always @(posedge clk) begin
    meta     <= async_in;
    sync_out <= meta;                        // 第二級給第一級一整個週期去「安定下來」
  end
endmodule
