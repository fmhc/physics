# Figure 1 (overview figure): script, receipt and inputs

Provenance of the overview figure of preprint 0.52 (`../qball-overview.pdf`, `.png`, `.svg`). The figure plots
archived data and evaluates formulas stated in the paper. No new simulation, fit or certificate run was made for it.
Supplement Section S7 of the preprint describes the same provenance.

| File | Content |
|---|---|
| `plot_overview.py` | plotting script (Python 3, numpy, scipy, matplotlib); reads `inputs/`, writes `out/` |
| `inputs/PROFILE.json`, `inputs/figure-data.json`, `inputs/sprossen.json` | byte copies of the 0.51 archive files `figures/modes/PROFILE.json`, `ladder/figure/figure-data.json`, `ladder/extension/sprossen.json` (checksums in `INPUTS-FIG.sha256`, paths relative to `inputs/`, and in the 0.51 archive manifest) |
| `inputs/SEQUENCE-v051.tex`, `inputs/PROOF-v051.tex` | byte copies of `sections/SEQUENCE.tex` and `sections/PROOF.tex` of preprint 0.51 (ladder table and certificate table, used only for consistency checks) |
| `out/FIG-OVERVIEW-RECEIPT.json` | receipt of the run that produced the published figure: checksums of script, inputs and outputs, all check results, derived values, the data source of every ladder point, evidence classes, and the list of schematic elements |
| `CLEAN-MAP.tsv` | checksums of the run copies and of the published copies of script and receipt |
| `SHA256SUMS` | checksums of all other files in this folder (`sha256sum -c SHA256SUMS` inside `fig-overview/`) |

## Checks in the script

Before rendering, the script stops on any failed check:

* G1, G1b: every plotted ladder location n = 1–18 is read from its archived field and agrees with the value shown in the
  paper's ladder table to one unit of the last displayed digit.
* G2, G2b: two certified radial modes, one certified dipole mode, 16 uncertified radial candidates (n = 3–18); every
  plotted evidence class is derived from the evidence column of the ladder table.
* G3, G7: the stored C0 profile and the hard-coded C0/C1/C2 midpoints agree with the paper's certificate table.
* G4, G5: the C0 sideband condition (one open, one closed channel) and the two equal hill tops of the mechanical
  potential at the thin-wall threshold.
* G6: all three outputs written and hashed.

These are consistency checks of the rendering, not additional evidence for the physics. The phase inset in panel (a),
the dashed tail in panel (d) and the width curve in panel (e) are schematic. For n = 3–18 the plotted locations are
uncertified numerical candidates.

## Published copies

The run used the script with checksum `ff60bc0f…` (recorded in the receipt and printed in Supplement S7). In the
published copies, three lines of the script's header text and the receipt's `host` field were replaced by neutral
wording (machine name and internal file references). No code line, number or other field changed. `CLEAN-MAP.tsv` lists
both checksums. The figure files in the paper folder are byte-identical to the outputs listed in the receipt.

To rerun: `cd fig-overview && python3 plot_overview.py` (writes new outputs and a new receipt to `out/`; the
`time`, `host` and version fields will differ, and rendered bytes may differ with other library versions).

Licence: code MIT (`../LICENSE-CODE`), everything else CC BY 4.0 (`../LICENSE`).
