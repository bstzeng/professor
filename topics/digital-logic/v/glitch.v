// glitch.v：靜態 1 危障。F = A·B + A'·C，當 B = C = 1 時 F 理論上恆為 1，
// 但 A 從 1 變 0 時，A' 要多經過一個反相器才變 1，中間會出現短暫的 0。
`timescale 1ns/1ps
module hazard(input a, input b, input c, output f);
  wire an, t1, t2;
  not #2 g0(an, a);          // 反相器延遲 2 ns
  and #2 g1(t1, a, b);       // 及閘延遲 2 ns
  and #2 g2(t2, an, c);
  or  #2 g3(f, t1, t2);      // 或閘延遲 2 ns
endmodule

// 加上共識項 B·C 後，A 怎麼變都不會出現毛刺
module hazard_free(input a, input b, input c, output f);
  wire an, t1, t2, t3;
  not #2 g0(an, a);
  and #2 g1(t1, a, b);
  and #2 g2(t2, an, c);
  and #2 g4(t3, b, c);       // 共識項
  or  #2 g3(f, t1, t2, t3);
endmodule
