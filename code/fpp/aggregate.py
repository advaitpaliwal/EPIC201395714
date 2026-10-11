"""Aggregate the joint runs (pattern: planet-hunt/deep/240488148-joint/aggregate.py); checks probability sums and FPP/NFPP definitions."""
import json, hashlib, numpy as np, pandas as pd
from pathlib import Path
D = Path('/Users/advaitpaliwal/Scratch/k2-deep/201395714/fpp_joint')
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
out = {'input_sha256': {f: sha(D / f) for f in ['201395714_gaia_background.csv', 'out/target_201395714_obj.pkl', 'molusc_out/molusc_for_trc_N1e6.csv']},
       'repro_check_none294_0_vs_fpp_run0': [json.loads((D/'out/res_none294_0.json').read_text())['FPP'], json.loads((D/'../fpp/out/res_201395714_0.json').read_text())['FPP']]}
for v in ['exp30', 'exp294']:
    rows, sc = [], []
    for k in range(10):
        r = json.loads((D / f'out/res_{v}_{k}.json').read_text()); p = pd.read_csv(D / f'out/probs_{v}_{k}.csv')
        assert np.isclose(p.prob.sum(), 1, atol=1e-12) and (p.prob >= 0).all()
        fpp = 1 - p.loc[p.scenario.isin(['TP', 'PTP', 'DTP']), 'prob'].sum(); nfpp = p.loc[p.scenario.isin(['NTP', 'NEB', 'NEBx2P']), 'prob'].sum()
        assert np.isclose(fpp, r['FPP'], atol=1e-12) and np.isclose(nfpp, r['NFPP'], atol=1e-12)
        rows.append(r); sc.append(p.groupby('scenario').prob.sum().rename(k))
    d = pd.DataFrame(rows); s = pd.concat(sc, axis=1).fillna(0)
    st = pd.DataFrame({'mean': s.mean(axis=1), 'sd': s.std(axis=1, ddof=1), 'min': s.min(axis=1), 'max': s.max(axis=1)})
    st.to_csv(D / f'scenario_summary_{v}.csv'); d.to_csv(D / f'run_results_{v}.csv', index=False)
    out[v] = {'exptime_min': float(d.exptime_min.iloc[0]), 'seeds': d.seed.tolist(), 'err_ppm': float(d.err_ppm.iloc[0]), 'nbins': int(d.nbins.iloc[0]),
              'FPP': {'mean': d.FPP.mean(), 'sd': d.FPP.std(ddof=1), 'min': d.FPP.min(), 'max': d.FPP.max(), 'runs_le_0.035': int((d.FPP <= 0.035).sum())},
              'NFPP': {'mean': d.NFPP.mean(), 'sd': d.NFPP.std(ddof=1), 'max': d.NFPP.max()},
              'scenarios': {i: {c: float(st.loc[i, c]) for c in st.columns} for i in st.index}}
(D / 'summary.json').write_text(json.dumps(out, indent=1, default=float) + '\n'); print(json.dumps(out, indent=1, default=float))
