import sys, json, numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
epic = sys.argv[1]; D = f'/Users/advaitpaliwal/Scratch/k2-deep/{epic}'
fig, ax = plt.subplots(1, 3, figsize=(15, 4), sharey=True)
for a, src in zip(ax, ['everest', 'k2sff', 'fresh']):
    b = np.load(f'{D}/fit/bestmodel_{src}.npz'); r = json.load(open(f'{D}/fit/result_{src}.json'))
    P = r['P_d'][0]; T0 = r['T0_BKJD'][0]
    ph = (((b['t'] - T0 + 0.5*P) % P) - 0.5*P)*24; o = np.argsort(ph)
    a.plot(ph, (b['f']-1)*1e6, '.', color='0.6', ms=3)
    edges = np.arange(-6, 6.01, 0.5); idx = np.digitize(ph, edges)
    a.plot([ph[idx == i].mean() for i in np.unique(idx)], [(b['f'][idx == i].mean()-1)*1e6 for i in np.unique(idx)], 'ko')
    a.plot(ph[o], (b['mod'][o]-1)*1e6, 'r-'); a.set_xlim(-6, 6); a.set_ylim(-2000, 1000)
    a.set_title(f"{src}: depth {r['depth_ppm'][0]:.0f} ppm, Rp {r['Rp_earth'][0]:.2f} Re"); a.set_xlabel('hours from mid-transit')
ax[0].set_ylabel('ppm'); plt.suptitle(f'EPIC {epic}'); plt.tight_layout(); plt.savefig(f'{D}/fit/folded.png', dpi=90)
