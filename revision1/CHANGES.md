Changes made in Revision 1 of the research note. The revised note text is with the journal and is not in this repository; the figure, new runs, scripts and source files it cites are in this folder. Paths in this file are the author's working paths.

# AAS82179 (EPIC 201395714): revision 1, changes from submission6/rnaas6.md

Files: `rnaas_rev1.md` (body 889 words, abstract 143), `Paliwal_EPIC201395714_RNAAS_rev1.docx` (built with `../../tools/mkdocx.py` through `uv run --with python-docx`, the same script and layout as the AAS82088 R1 docx: 41 paragraphs, 1 figure), `figure1_combined_EPIC201395714.png` (new 3-panel Figure 1, from `prerev/201395714`), `unfolded_EPIC201395714.png` (stand-alone unfolded figure, spare).
Recompute: `../scripts/recompute.py` → `../scripts/recompute.log`. It reads every quoted number from `~/Scratch/k2-deep/201395714/` (fit, vet, inj, pix, fpp, fpp_joint, catalogue, TPFs). No number changed except the FPP range minimum (below).

## Mapped to the editor's six AAS82088 questions

1. **Which data went into the difference image.** Added: the 14 in-transit cadences of segment c102 only; each is subtracted from the 8 out-of-transit cadences within 1.5 d closest in pointing (POS_CORR); noise from 60 random-phase difference images (`k2-deep/scripts/pix.py`; `pix/diff_c102.json` n_in 14, n_fake 60). Added why c101 (one more transit, epoch −6, 4 cadences) was not used: its TPF has no finite POS_CORR (0 of 300 good cadences) and the brightest pixel sits 3 rows from its c102 position (recompute.log). States that K2 observed the star only in C10.
2. **χ² definitions.** Added the per-transit estimator (median OOT minus mean of central 70% of transit, error std(OOT)/√n) and that χ² = 6.45/6 is about the weighted mean (`fit/vet_everest.json`, `vet.py`). The localisation tests in this note are not χ² values except the PSF fit (Δχ² 11.7), which the note does not quote, so no other definition is needed.
3. **Neighbours removed.** Added: TRICERATOPS's 40″ K2 field contains only the target; none removed. Every `probs_exp294_*.csv` holds only TIC 349446806 (recompute.log). Added that the G = 11.07 giant at 44.24″ lies outside the field. Abstract now says "no neighbours removed".
4. **Detrending.** Search step now described: wotan biweight 0.4 d, no transit mask, +3σ clip (`k2-hunt/scripts/k2tls_hunt.py` `clean()`). Fit step added: wotan biweight 0.75 d, cadences within ±0.75 × D of each transit masked (D 1.925–2.0 h, so ±1.44–1.5 h; written "about ±1.5 h"), trend interpolated across, 160 points fitted (`k2-deep/scripts/lcs.py` `flat()`; `result_everest.json` npts 160).
5. **Unfolded light curve.** Figure 1 replaced by the 3-panel figure: folded / unfolded C10 with the 0.75 d trend and 6 h bins / four single transits (epochs −5, −1, +1, +3). Caption rewritten; old caption's "posterior draws (blue) and residuals" removed since the new figure has neither. The 15-day gap (BKJD ~2756–2771) is called "a data gap": it lies inside c102 (TPF spans BKJD 2749.6–2818.7), not at the c101/c102 break, so PREREV's "segment break" reading is not used.
6. **MOLUSC.** "companion limits from Gaia astrometry and imaging via MOLUSC" replaced: MOLUSC with only its Gaia RUWE and contrast tests (no imaging, RV or duration test), 200,000 generated, 51% kept (102,728; `molusc_summary.txt`), kept companions replace TRICERATOPS's default prior for the bound-companion scenarios.

## Other changes
- "2.5″ (1.7σ) from the target" → "from the out-of-transit centroid" (`diff_c102.json` measures dcx−ocx; from the catalogue position it is 2.36″).
- "No other Gaia source lies within 44″; the nearest is…" → reworded to "The nearest other Gaia source, the G = 11.1 giant TYC 4940-277-1, lies 44″ (eleven pixels) away" (44.24″, `gaia_dr3_60as.csv`).
- High-resolution imaging statement: "ExoFOP lists no high-resolution imaging, spectroscopy or other follow-up" and, in the FPP section, "ExoFOP holds no high-resolution imaging of the star". Checked: ExoFOP TIC 349446806 JSON, imaging 0 rows, spectroscopy 0, files 0 (`../_sources/exofop_tic349446806.json`, fetched 2026-10-15). `~/Scratch/k2-deep/imaging/IMAGING.md` does not cover this star, so the wording is limited to ExoFOP.
- FPP range 0.015–0.026 → 0.014–0.026 (minimum run 0.01446, `fpp_joint/summary.json` exp294; old text rounded wrongly).
- "Almost all of the remaining FPP (0.019)" → "Almost all of the FPP" (STP 0.0186 of 0.0194).
- Collier et al. sentence shortened to "(cf. Collier et al. 2026)", as in the AAS82088 R1.
- TESS: "Sector 115 (2027 March–April)" → "expected around 2027 March". The published orbit table (`../_sources/TESS_orbit_times.csv`, fetched 2026-10-15) ends at Sector 111 (starts 2026-11-26); extrapolating 26.9 d per sector gives an S115 midpoint near 2027-03-27 (inferred). Transit-time σ at that epoch: 10.6 h ("about 11 h"), recomputed.
- Affiliation: the postal address removed; "Independent researcher" only.
- Small trims for length: "therefore … across extractions", "periodic", "observed in the same campaign" → "in the same segment".

## Numbers checked unchanged (recompute.log)
P 7.49781 ± 0.00085; T0 2457621.9758 ± 0.0023; Rp/R★ 0.0220 ± 0.0018; a/R★ 31.3 ± 1.5; b 0.40 +0.18/−0.25; depth 608 +66/−63; T14 1.71 +0.13/−0.15 h; Rp 0.88 ± 0.09; a 0.053 AU; S 6.8 +1.4/−1.2; Teq 449 +22/−21; K2SFF 716 +96/−90; fresh 801 +83/−75; K2SC 752 ± 140; odd–even 1.02σ; phase 0.5 62 ± 42; max other feature 2.56σ; injections 96/100; masked SDE 6.8 vs 22.7; diff offset 2.47″ (1.74σ), 14 cadences; K2-153 b 0.65″; core4 418 ± 135, core6–thresh1 716–794; FPP 0.0194 ± 0.0034, NFPP 0; no-limits FPP 0.080 ± 0.002; EB scenarios sum 0.0006; star Kp 14.16, Teff 3448 ± 157, R 0.365 ± 0.011, M 0.352 ± 0.020, d 63.9 pc, RUWE 1.12, M3 (J/ApJS/247/28).

## Not done
- No response letter is needed until the editor writes about this note; the six answers above are in the text.
