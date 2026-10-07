// adders.v：半加器、全加器、漣波進位加法器、4 位元超前進位加法器
module half_adder(input a, input b, output s, output c);
  assign s = a ^ b;
  assign c = a & b;
endmodule

module full_adder(input a, input b, input cin, output s, output cout);
  assign s    = a ^ b ^ cin;
  assign cout = (a & b) | (cin & (a ^ b));
endmodule

// N 位元漣波進位：進位一級一級往上傳
module ripple_adder #(parameter N = 8) (input [N-1:0] a, input [N-1:0] b, input cin,
                                         output [N-1:0] s, output cout);
  wire [N:0] c;
  assign c[0] = cin;
  genvar i;
  generate
    for (i = 0; i < N; i = i + 1) begin : stage
      full_adder fa(a[i], b[i], c[i], s[i], c[i+1]);
    end
  endgenerate
  assign cout = c[N];
endmodule

// 4 位元超前進位：用 g（產生）與 p（傳遞）直接算出每一位的進位
module cla4(input [3:0] a, input [3:0] b, input cin, output [3:0] s, output cout);
  wire [3:0] g = a & b;      // 這一位自己就會產生進位
  wire [3:0] p = a ^ b;      // 這一位會把下面來的進位傳上去
  wire c1 = g[0] | (p[0] & cin);
  wire c2 = g[1] | (p[1] & g[0]) | (p[1] & p[0] & cin);
  wire c3 = g[2] | (p[2] & g[1]) | (p[2] & p[1] & g[0]) | (p[2] & p[1] & p[0] & cin);
  assign cout = g[3] | (p[3] & g[2]) | (p[3] & p[2] & g[1]) | (p[3] & p[2] & p[1] & g[0])
              | (p[3] & p[2] & p[1] & p[0] & cin);
  assign s = p ^ {c3, c2, c1, cin};
endmodule
