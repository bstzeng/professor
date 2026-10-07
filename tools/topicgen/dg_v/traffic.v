// traffic.v：十字路口紅綠燈（狀態機＋計時器）
// 南北向綠 5 拍 → 南北黃 2 拍 → 東西綠 5 拍 → 東西黃 2 拍；有行人按鈕時南北綠燈提早結束
module traffic(input clk, input rst, input ped, output reg [1:0] ns, output reg [1:0] ew);
  localparam RED = 2'd0, YEL = 2'd1, GRN = 2'd2;
  localparam NS_G = 2'd0, NS_Y = 2'd1, EW_G = 2'd2, EW_Y = 2'd3;
  reg [1:0] state; reg [2:0] t;              // t：在目前狀態已經待了幾拍
  always @(posedge clk) begin
    if (rst) begin state <= NS_G; t <= 0; end
    else begin
      t <= t + 1;
      case (state)
        NS_G: if (t == 4 || (ped && t >= 1)) begin state <= NS_Y; t <= 0; end
        NS_Y: if (t == 1) begin state <= EW_G; t <= 0; end
        EW_G: if (t == 4) begin state <= EW_Y; t <= 0; end
        EW_Y: if (t == 1) begin state <= NS_G; t <= 0; end
      endcase
    end
  end
  always @(*) begin                          // 輸出只看狀態（Moore）
    ns = RED; ew = RED;
    case (state)
      NS_G: ns = GRN;  NS_Y: ns = YEL;
      EW_G: ew = GRN;  EW_Y: ew = YEL;
    endcase
  end
endmodule
