# EPIC 201395714.01: an Earth-sized planet candidate on a 7.5-day orbit around a nearby M dwarf

Advait Paliwal (independent researcher, advaitpaliwal@gmail.com), 2026-10-11.

A small dip in brightness repeats every 7.5 days in K2 Campaign 10 photometry of EPIC 201395714, an M3 dwarf 64 pc away. If it is a planet, it is about the size of Earth and receives about seven times the sunlight Earth does.

| | |
|---|---|
| Host | EPIC 201395714 = TIC 349446806 = 2MASS J12153638−0101354, M dwarf, 63.9 pc, Kp = 14.16 |
| Period | 7.49781 (+0.00086/−0.00084) d |
| Mid-transit | 2457621.9758 (+0.0024/−0.0022) BJD_TDB |
| Depth / duration | 608 (+66/−63) ppm / 1.71 h (EVEREST light curve) |
| Radius | 0.88 (+0.10/−0.09) R⊕ |
| Equilibrium temperature | 449 ± 22 K |
| Data | K2 Campaign 10 (2016 July–September), 30-minute cadence; 7 transits |
| False-positive probability | 0.019 ± 0.003 (TRICERATOPS with MOLUSC Gaia limits); 0.080 without; NFPP 0 |

Status: **planet candidate**. Not a TOI, CTOI or K2 candidate in the NASA Exoplanet Archive as of 2026-10-11. The transit depth grows with aperture size and the difference-image centroid sits 2.5″ (1.7σ) from the star, so the source of the signal on the pixels is not settled; high-resolution imaging and new transits are needed. TESS covers the star in Sector 115 (March–April 2027), where the predicted transit time is uncertain by about 10.5 hours.

## Contents

- `note/figure1_EPIC201395714.png` — folded K2 light curve with the exposure-integrated model and residuals
- `data/lc/folded_lc_everest.csv` — the folded EVEREST data and model shown in Figure 1
- `data/fit/` — posterior summary (`posterior_summary_everest.csv`) and full fit outputs for EVEREST, K2SFF and a fresh aperture
- `data/vetting/`, `data/injection/` — odd/even, secondary-eclipse and per-transit checks; injection-recovery tests
- `data/pixels/` — difference image, pixel-level fit and depth-versus-aperture results
- `data/fpp/` — false-positive probability runs (`fpp_summary.csv`, scenario tables, MOLUSC summary)
- `data/tess/`, `data/catalogue/`, `data/search/` — TESS coverage check, catalogue queries with their URLs, and the search detection
- `code/` — search, light-curve, fit, vetting, pixel, FPP, TESS, catalogue and figure scripts

Data: K2 (NASA, via MAST), EVEREST, K2SFF and K2SC high-level science products, ESA Gaia DR3, TIC v8. Software: lightkurve, batman, emcee, transitleastsquares, wotan, TRICERATOPS, MOLUSC, tess-point, astropy, matplotlib. Licences: code MIT; text, figures and data CC BY 4.0.

Scripts are kept exactly as run, with the author's absolute working paths (`~/Scratch/k2-hunt`, `~/Scratch/k2-deep`); edit those paths to rerun them elsewhere.
