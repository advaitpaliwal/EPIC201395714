# Joint TRICERATOPS(K2)+MOLUSC FPP for EPIC 201395714. Copied from ../../scripts/trc_k2.py (K2 target, aperture, EVEREST LC, 15-min bins, depth 608 ppm,
# filt Kepler, seed 2000+k) plus the joint pattern of planet-hunt/deep/240488148-joint/run_joint.py (molusc_file, parallel=True, read-only-array shim).
# usage: run_joint.py VARIANT RUN ; VARIANT in {exp30 (exptime 30 min, as the submitted TESS joint runs), exp294 (K2 long cadence 29.4 min)}
import sys, os, json, pickle, time, glob, types, numpy as np, warnings; warnings.filterwarnings('ignore')
D = '/Users/advaitpaliwal/Scratch/k2-deep/201395714/fpp_joint'; os.chdir(D)
import triceratops.triceratops as tr, triceratops.marginal_likelihoods as ml, lightkurve as lk
class _F:  # pandas>=3 copy-on-write makes Series.values read-only; TRICERATOPS 1.1.0 writes into it (molusc branch only)
    def __init__(s, d): s.d = d
    def __getitem__(s, k):
        if isinstance(k, str): return types.SimpleNamespace(values=s.d[k].to_numpy(copy=True))
        return _F(s.d[np.asarray(k)])
_rc = ml.read_csv
ml.read_csv = lambda f, *a, **kw: _F(_rc(f, *a, **kw)) if 'molusc' in str(f) else _rc(f, *a, **kw)
var, k = sys.argv[1], int(sys.argv[2]); exptime = {'exp30': 30/1440, 'exp294': 29.4/1440, 'none294': 29.4/1440}[var]
epic, P, T0, dur, depth, seg = 201395714, 7.49781, 2788.97577, 1.71/24, 608e-6, 'c102'
tg = pickle.load(open('out/target_201395714_obj.pkl', 'rb'))  # ../fpp/out/target_201395714.pkl re-pickled for pandas 2.3.3 by scripts/repickle.py
assert len(tg.stars) == 1 and tg.mission == 'K2'
tpp = [p for p in glob.glob(f'/Users/advaitpaliwal/Scratch/k2-deep/{epic}/lc/mastDownload/K2/*/*lpd-targ.fits.gz') if seg in p][0]
tp = lk.read(tpp)
ap = tp.create_threshold_mask(threshold=3, reference_pixel='center')
rows, cols = np.nonzero(ap); apx = np.column_stack([cols + tp.column, rows + tp.row])
z = np.load(f'/Users/advaitpaliwal/Scratch/k2-deep/{epic}/lc/everest.npz'); t, f = z['t'], z['f']
ph = t - T0 - np.round((t - T0)/P)*P; w = np.abs(ph) < 0.3
edges = np.arange(-0.3, 0.3 + 1e-9, 15/1440); idx = np.digitize(ph[w], edges)
tb = np.array([ph[w][idx == i].mean() for i in np.unique(idx)]); fb = np.array([f[w][idx == i].mean() for i in np.unique(idx)])
err = float(np.std(fb[np.abs(tb) > dur]))
ref = json.load(open('../fpp/out/res_201395714_0.json'))
assert np.isclose(err*1e6, ref['err_ppm'], rtol=0, atol=1e-9) and len(tb) == ref['nbins'] and apx.tolist() == ref['aperture']
tg.calc_depths(tdepth=depth, all_ap_pixels=[apx])
mf = None if var == 'none294' else D + '/molusc_out/molusc_for_trc_N1e6.csv'  # none294 = reproduction check of the unconstrained ../fpp run
np.random.seed(2000 + k); t0 = time.time()
tg.calc_probs(time=tb, flux_0=fb, flux_err_0=err, P_orb=P, contrast_curve_file=None, filt='Kepler', N=1000000, parallel=True,
              exptime=exptime, nsamples=20, verbose=0, molusc_file=mf)
tag = f'{var}_{k}'
tg.probs.to_csv(f'out/probs_{tag}.csv', index=False)
json.dump(dict(epic=epic, variant=var, run=k, seed=2000+k, N=1000000, exptime_min=exptime*1440, P=P, T0=T0, depth_ppm=depth*1e6, err_ppm=err*1e6, nbins=len(tb),
               molusc=mf, filt='Kepler', FPP=float(tg.FPP), NFPP=float(tg.NFPP), sec=time.time() - t0), open(f'out/res_{tag}.json', 'w'), indent=1)
print(tag, tg.FPP, tg.NFPP, round(time.time() - t0), flush=True)
