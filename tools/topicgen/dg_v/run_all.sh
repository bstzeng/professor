#!/bin/sh
# run_all.sh：編譯並執行所有範例（需要 Icarus Verilog：iverilog、vvp）
# 每個範例的輸出寫到 _out/<名稱>.txt
set -e
mkdir -p _out build
python3 asm.py prog.s prog.hex > _out/asm.txt
run() { name=$1; shift
  iverilog -g2012 -o build/$name "$@"
  vvp -n build/$name | grep -v '\$finish called' | sed 's/[ ]*$//' > _out/$name.txt
  echo "ok  $name"; }
run gates     tb_gates.v gates.v
run mux       tb_mux.v mux.v
run decoder   tb_decoder.v decoder.v
run adders    tb_adders.v adders.v
run glitch    tb_glitch.v glitch.v
run alu       tb_alu.v alu.v
run timing    tb_timing.v timing.v
run latches   tb_latches.v latches.v
run counter   tb_counter.v counter.v
run fsm_seq   tb_fsm_seq.v fsm_seq.v
run traffic   tb_traffic.v traffic.v
run regfile   tb_regfile.v regfile.v
run rv_single tb_rv_single.v rv_single.v regfile.v alu.v
iverilog -g2012 -o build/sync sync.v && echo "ok  sync (compile only)"
