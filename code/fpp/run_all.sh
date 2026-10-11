#!/bin/sh
# 2 variants x 10 runs, at most 4 simultaneous workers.
D=/Users/advaitpaliwal/Scratch/k2-deep/201395714/fpp_joint
PY=/Users/advaitpaliwal/Scratch/planet-hunt/hunt4/.venv/bin/python
(echo none294 0; for v in exp30 exp294; do seq 0 9 | sed "s/^/$v /"; done) | xargs -P 4 -n 2 sh -c 'OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 '"$PY"' -I -u '"$D"'/scripts/run_joint.py "$1" "$2" > '"$D"'/out/run_$1_$2.log 2>&1' sh
echo ALL_DONE > $D/out/done
