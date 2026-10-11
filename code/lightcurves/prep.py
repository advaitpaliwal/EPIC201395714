import sys, json, numpy as np; sys.path.insert(0, '/Users/advaitpaliwal/Scratch/k2-deep/scripts'); import lcs
epic, P, T0, dur, seg = int(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4])/24, sys.argv[5]
D = f'/Users/advaitpaliwal/Scratch/k2-deep/{epic}'
out = {}
for name in ['everest', 'k2sff', 'k2sc', 'fresh']:
    r = lcs.fresh(epic, P, T0, dur, seg=seg)[:2] if name == 'fresh' else getattr(lcs, name)(epic)
    if r is None: continue
    t, f = r; tf, ff = lcs.flat(t, f, P, T0, dur)
    np.savez(f'{D}/lc/{name}.npz', t_raw=t, f_raw=f, t=tf, f=ff)
    d, e, n = lcs.boxdepth(tf, ff, P, T0, dur)
    out[name] = dict(n=len(tf), rms_ppm=float(np.std(ff)*1e6), box_depth_ppm=float(d*1e6), box_err_ppm=float(e*1e6), n_in=n)
    print(name, out[name], flush=True)
json.dump(out, open(f'{D}/lc/depths_box.json', 'w'), indent=1)
