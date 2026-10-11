# A 0.9 Earth-radius Planet Candidate on a 7.5-day Orbit around the M Dwarf EPIC 201395714

Advait Paliwal
Independent researcher, Sterling Heights, MI 48314, USA
advaitpaliwal@gmail.com

## Abstract

I report a transit-like signal on EPIC 201395714 (UCAC4 445-054690), an M dwarf at 63.9 pc, in K2 Campaign 10 photometry. A transit fit gives a period of 7.4978 ± 0.0009 d, a depth of 608 ± 65 ppm and a duration of 1.71 h, implying a radius of 0.88 ± 0.09 R⊕ and an equilibrium temperature of 449 ± 22 K. The star is not a K2 candidate, TOI or CTOI, and it is absent from published K2 candidate catalogues. Seven transits appear in four light-curve extractions, with consistent odd and even depths and no secondary eclipse. No Gaia source lies within 44″. With Gaia companion limits, TRICERATOPS gives FPP = 0.019 ± 0.003 and NFPP = 0. The pixel data localize the signal only to about one pixel, so the candidate awaits high-resolution imaging and further photometry.

## Star and search

EPIC 201395714 has Kp = 14.16, Teff = 3448 ± 157 K, R★ = 0.365 ± 0.011 R☉ and M★ = 0.352 ± 0.020 M☉ (Stassun et al. 2019), and Hardegree-Ullman et al. (2020) classify it as M3. Its Gaia DR3 RUWE is 1.12, with no non-single-star solution (Gaia Collaboration et al. 2023). ExoFOP lists no imaging or spectroscopic follow-up.

I searched EVEREST light curves (Luger et al. 2016, 2018) of the 1,288 nearest cool dwarfs (within 74 pc) observed in K2 Campaigns 1–18 (Howell et al. 2014), selected from Hardegree-Ullman et al. (2020). I detrended them with wotan (Hippke et al. 2019) and searched 0.5–30 d with Transit Least Squares (Hippke & Heller 2019). Each detection had to appear at a consistent depth in both EVEREST and K2SFF (Vanderburg & Johnson 2014) and in both halves of the campaign. It also had to pass odd–even, secondary-eclipse, shape and stellar-density tests, and have no Gaia neighbour within 12″ bright enough to produce it. The search recovered seven known K2 planets and candidates.

## Transit fit

I fitted the EVEREST light curve (29.4-minute cadence, 2016 July 13 to September 20) with batman (Kreidberg 2015) and emcee (Foreman-Mackey et al. 2013). The model integrates over each exposure, assumes a circular orbit, and uses a TIC stellar-density prior and uninformative quadratic limb darkening (Kipping 2013). It gives P = 7.49781 ± 0.00085 d, T0 = 2457621.9758 ± 0.0023 BJD_TDB, Rp/R★ = 0.0220 ± 0.0018, a/R★ = 31.3 ± 1.5, b = 0.40 (+0.18/−0.25), a depth of 608 (+66/−63) ppm and T14 = 1.71 (+0.13/−0.15) h (Figure 1). This implies Rp = 0.88 ± 0.09 R⊕, a = 0.053 AU, an insolation of 6.8 (+1.4/−1.2) S⊕ and Teq = 449 (+22/−21) K (zero albedo, full redistribution).

## Vetting

The seven transits have consistent depths (χ² = 6.5 for 6 degrees of freedom). Fits to the K2SFF light curve and to a fresh aperture from the target pixel file give 716 (+96/−90) and 801 (+83/−75) ppm. A box fit to the K2SC light curve (Aigrain et al. 2016) gives 752 ± 140 ppm. The implied radius therefore spans 0.88–1.01 R⊕ across extractions. Odd and even depths agree to 1.0σ (EVEREST) and 0.2σ (fresh aperture), and the depth at phase 0.5 is 62 ± 42 ppm. No other feature in the phase-folded light curve exceeds 2.6σ. Transits of the same size injected at other periods were recovered in 96 of 100 trials. With the candidate's transits masked, the strongest remaining periodic signal has SDE 6.8, against 22.7 for the candidate.

No other Gaia source lies within 44″; the nearest is the G = 11.1 giant TYC 4940-277-1, eleven pixels away. The difference-image centroid lies 2.5″ (1.7σ) from the target, compared with 0.65″ for the known planet K2-153 b observed in the same campaign. The depth is lower in the central four pixels (418 ± 135 ppm) than in larger apertures (716–794 ppm), a trend K2-153 b does not show. With only 14 in-transit cadences, these tests localize the signal to about one 4″ pixel and cannot exclude an unresolved source.

## False-positive probability

I averaged TRICERATOPS (Giacalone & Dressing 2020; Giacalone et al. 2021), run in its K2 mode, over ten runs of 10⁶ draws each, with companion limits from Gaia astrometry and imaging via MOLUSC (Wood et al. 2021). The result is FPP = 0.0194 ± 0.0034 (range 0.015–0.026) and NFPP = 0. Without companion limits the FPP is 0.080 ± 0.002. Almost all of the remaining FPP (0.019) comes from a planet orbiting an unresolved bound companion, and eclipsing-binary scenarios sum to less than 0.001. The FPP is above the 0.015 validation threshold, the star has no high-resolution imaging, and Collier et al. (2026) find that small validated planets in their imaging sample needed contrast curves, so I make no validation claim.

## Summary

EPIC 201395714.01 is an Earth-sized candidate with Teq ≈ 450 K around a nearby mid-M dwarf. TESS has not yet observed the star on its detectors. Sector 115 (2027 March–April) may cover it, with a predicted transit-time uncertainty of about 11 h. High-resolution imaging and further transit photometry are the next steps. Code and data are at https://github.com/advaitpaliwal/EPIC201395714.

## Acknowledgments

This paper includes data collected by the K2 mission, funded by the NASA Science Mission Directorate, and obtained from MAST. It uses data from the ESA mission Gaia, processed by the Gaia DPAC.

## Figure 1

K2 Campaign 10 EVEREST photometry of EPIC 201395714 folded on the fitted ephemeris (grey points), with 15-minute bins (black), the exposure-integrated median model and posterior draws (blue) and residuals (bottom).

## References

Aigrain, S., Parviainen, H., & Pope, B. J. S. 2016, MNRAS, 459, 2408
Collier, M., Giacalone, S., Derfer, B., et al. 2026, AAS Journals, accepted, arXiv:2608.21560
Foreman-Mackey, D., Hogg, D. W., Lang, D., & Goodman, J. 2013, PASP, 125, 306
Gaia Collaboration, Vallenari, A., Brown, A. G. A., et al. 2023, A&A, 674, A1
Giacalone, S., & Dressing, C. D. 2020, triceratops, ascl:2002.004
Giacalone, S., Dressing, C. D., Jensen, E. L. N., et al. 2021, AJ, 161, 24
Hardegree-Ullman, K. K., Zink, J. K., Christiansen, J. L., et al. 2020, ApJS, 247, 28
Hippke, M., David, T. J., Mulders, G. D., & Heller, R. 2019, AJ, 158, 143
Hippke, M., & Heller, R. 2019, A&A, 623, A39
Howell, S. B., Sobeck, C., Haas, M., et al. 2014, PASP, 126, 398
Kipping, D. M. 2013, MNRAS, 435, 2152
Kreidberg, L. 2015, PASP, 127, 1161
Luger, R., Agol, E., Kruse, E., et al. 2016, AJ, 152, 100
Luger, R., Kruse, E., Foreman-Mackey, D., Agol, E., & Saunders, N. 2018, AJ, 156, 99
Stassun, K. G., Oelkers, R. J., Paegert, M., et al. 2019, AJ, 158, 138
Vanderburg, A., & Johnson, J. A. 2014, PASP, 126, 948
Wood, M. L., Mann, A. W., & Kraus, A. L. 2021, AJ, 161, 85
