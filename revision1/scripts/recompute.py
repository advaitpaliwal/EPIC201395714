"""Recompute every number quoted in rnaas_rev1.md from the saved files."""
import json, csv, glob, datetime as dt
import numpy as np
from astropy.io import fits
KD = '~/Scratch/k2-deep/201395714/'
J = lambda p: json.load(open(KD + p))
r = J('fit/result_everest.json'); v = J('fit/vet_everest.json')
def pm(k, f=1):
    m, lo, hi = r[k]; return f'{m*f:.6g} -{lo*f:.3g} +{hi*f:.3g}'
for k in ['P_d','RpRs','a_Rs','b','depth_ppm','T14_h','Rp_earth','Teq_K','S_earth']: print(k, pm(k))
print('T0 BJD', r['T0_BKJD'][0] + 2454833, r['T0_BKJD'][1:], 'npts', r['npts'])
print('priors', r['priors'])
for s in ['k2sff', 'fresh']:
    x = J(f'fit/result_{s}.json'); print(s, 'depth', x['depth_ppm'], 'Rp', x['Rp_earth'][0])
print('k2sc box', J('lc/depths_box.json')['k2sc'])
print('per-transit chi2', v['per_transit_chi2'], v['per_transit_dof'], 'n_in', [p['n_in'] for p in v['per_transit']], sum(p['n_in'] for p in v['per_transit']))
from scipy.stats import chi2; print('p', chi2.sf(v['per_transit_chi2'], 6))
print('odd', v['odd'], 'even', v['even'], 'sig', v['odd_even_sigma'])
print('sec', v['secondary_phase0.5'], 'scan max', v['phase_scan_max_snr'], v['phase_scan_argmax'])
inj = J('inj/summary.json'); print('inj', inj)
for f in ['inj/null.json', 'inj/real.json']:
    try: print(f, json.dumps(json.load(open(KD + f)))[:300])
    except Exception as e: print(f, e)
d = J('pix/diff_c102.json'); print('diff', d['n_in_cadences'], d['offset_arcsec'], d['offset_sigma'], d['diff_centroid_err'], d['snr_summed_ap'], d['depth_ap_ppm'], d['depth_ap_err_ppm'], d['n_fake'])
print('offset from catalogue arcsec', np.hypot(*d['offset_from_gaia_pix']) * 3.98)
p = J('pix/pld_c102.json'); print('psf', p['chi2_null'], p['chi2_psf'], p['chi2_null'] - p['chi2_psf'], p['dof'], p['best_shift_arcsec'])
a = J('pix/apdepth.json'); print('ap', {k: (round(a[k]['depth_ppm']), round(a[k]['err_ppm']), a[k]['npix']) for k in a if isinstance(a[k], dict)})
ref = json.load(open('~/Scratch/k2-deep/reference/K2-153/diff_c102.json')); print('K2-153 diff', ref['n_in_cadences'], ref['offset_arcsec'], ref['snr_summed_ap'])
s = J('fpp_joint/summary.json')['exp294']; print('FPP', s['FPP'], 'NFPP', s['NFPP'])
print('STP', s['scenarios']['STP']['mean'], 'EB-like sum', sum(s['scenarios'][k]['mean'] for k in s['scenarios'] if 'EB' in k))
print('no-limits', J('fpp/summary.json'))
# stars in the TRICERATOPS field
ids = set()
for f in glob.glob(KD + 'fpp_joint/out/probs_exp294_*.csv'):
    for row in csv.DictReader(open(f)): ids.add(row.get('ID') or row.get('id'))
print('stars in TRICERATOPS runs', ids)
g = list(csv.DictReader(open(KD + 'catalogue/gaia_dr3_60as.csv')))
g.sort(key=lambda x: float(x['sep']))
for x in g[:4]: print('gaia', x['source_id'], x['phot_g_mean_mag'], x['sep'], x['ruwe'])
print(open(KD + 'fpp_joint/molusc_summary.txt').read().splitlines()[:3])
# campaigns
for c in ['c101', 'c102']:
    h = fits.open(KD + f'lc/mastDownload/K2/ktwo201395714-c10_lc/ktwo201395714-{c}_lpd-targ.fits.gz')
    dd = h[1].data; t = dd['TIME']; q = dd['QUALITY']; g0 = np.isfinite(t) & (q == 0)
    img = np.nan_to_num(np.nanmedian(dd['FLUX'][g0], axis=0))
    tm = r['T0_BKJD'][0] + np.arange(-8, 6) * r['P_d'][0]
    ins = [(int(e), int((g0 & (abs(t - x) < 0.6 * 1.706 / 24)).sum())) for e, x in zip(range(-8, 6), tm) if np.nanmin(t) <= x <= np.nanmax(t)]
    print(c, 'BJD', np.nanmin(t) + 2454833, np.nanmax(t) + 2454833, 'brightest px (row,col)', np.unravel_index(img.argmax(), img.shape),
          'POS_CORR finite', np.isfinite(dd['POS_CORR1'][g0]).sum(), 'transits', ins)
# TESS S115 timing: S111 start + 4 x mean sector length S100-S111 (inferred schedule)
rows = list(csv.reader(open('_sources/TESS_orbit_times.csv')))[1:]
rows = [x for x in rows if x and x[0].isdigit()]
st = {}
for x in rows:
    s_, a_ = int(x[0]), dt.datetime.fromisoformat(x[2]); st[s_] = min(st.get(s_, a_), a_)
L = (st[111] - st[100]).days / 11; mid = st[111] + dt.timedelta(days=4 * L + L / 2)
from astropy.time import Time
bk = Time(mid).jd - 2454833; n = round((bk - r['T0_BKJD'][0]) / r['P_d'][0])
sig = np.hypot(max(r['T0_BKJD'][1:]), n * max(r['P_d'][1:])) * 24
print('S115 est mid', mid.date(), 'mean sector d', round(L, 2), 'epochs', n, 'sigma_T h', round(sig, 1))
