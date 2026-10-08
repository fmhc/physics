# Maxwell package read-only code review

8 October 2026, Codex reviewer separate from the implementation agent. No independent test run by this reviewer;
this is AI software review, not external human validation.

No blocking issue found in the inspected implementation:

- Full SVD U[:, rank:] removes the image of d0 from edge space; d1 d0 is checked separately.
- Hodge weights and spectra are recomputed from geometry. Archived extrema and counts enter only the subsequent
  comparisons, not the computed spectra.
- Negative-mode counts and relative spectral minima are substantive reproduction checks; the count of 96 evaluated
  momenta is bookkeeping, not separate physical evidence.
- Documentation correctly identifies the same historical 96 momenta, shared geometry assumptions and CUDA requirement.
- The frozen plan's phrase '96 projected modes' should be read as 96 spectral problems, each with 136 eigenvalues
  (146 edge classes minus 10 gauge directions). The plan remains unchanged; the result report clarifies this wording.

The sign classification of triangles does not establish reflection positivity. Whole-zone positivity, refinement,
independent geometry construction and independent human reproduction remain unverified.
