#!/bin/zsh
# MOLUSC 4 x 50k (RUWE + Gaia contrast), M = 0.351881 Msun (TIC value, = TRICERATOPS M_s), default age. Pattern: deep/375939912/fpp/scripts/run_all.sh
F=/Users/advaitpaliwal/Scratch/k2-deep/201395714/fpp_joint
PYM=/Users/advaitpaliwal/Scratch/planet-hunt/tic240488148-companions/.venv-molusc/bin/python
cd $F
for s in 11 12 13 14; do
  SEED=$s $PYM -I -W ignore molusc_run.py -v --ruwe --gaia -a $F/molusc_out/m50k_s$s 12h15m36.2885s -- -01d01m35.3358s 50000 0.351881 > molusc_out/m50k_s$s.log 2>&1 &
  echo $! >> molusc_out/pids
done
wait; echo MOLUSC_DONE >> molusc_out/pids
