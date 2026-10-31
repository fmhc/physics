# Companion archive r3 (release asset)

The companion archive of preprint 0.53 is not stored in this Git repository. It is attached to release
[`qball-bic-v0.53`](https://github.com/fmhc/physics/releases/tag/qball-bic-v0.53) as
`qball-bic-v0.53-archive-r3.zip`.

| Item | Value |
|---|---|
| ZIP file | `qball-bic-v0.53-archive-r3.zip`, 37 672 006 bytes; 572 payload files plus `MANIFEST.sha256` (573 files in total) under `archive/` |
| SHA-256 of the ZIP | `6980a82552063b05fccbfb9e71117d3ecd75d20f6a195dafc3269844e7878fb1` |
| SHA-256 of `archive/MANIFEST.sha256` | `b31cb2678d8c671b10d6b88745aed982037588045e554fe0f2c6bca29f7ba57b` (copy: [`MANIFEST.sha256`](MANIFEST.sha256)) |
| Licences | code (`.py`, `.pyi`, `.jq`) MIT; everything else CC BY 4.0 (files `LICENSE-CODE`, `LICENSE` in the ZIP) |

Revision 3 contains revision 2 (release asset `qball-bic-v0.51-archive-r2.zip` of
[`qball-bic-v0.51`](https://github.com/fmhc/physics/releases/tag/qball-bic-v0.51)) unchanged except `README.md`, `MANIFEST.md`,
`MANIFEST.sha256`, `CLEAN-MAP.tsv`, `LADDER-RECORDS.tsv`, `SOURCE-BINDINGS.tsv`, `CITATION.cff` and
`GEHEIMNISPRUEFUNG.md`, and adds the source and matching records of ladder indices 3–5, a redacted derivative of the
data package of the linewidth reconstructions, the separate beta = 1 ladder and planar-wall studies, the outer-radius
variation and the matching calculation for indices 5 and 11–14 (with a control rerun of index 15), and the charge-slope
calculations of Supplement Section S7. Text records that named machines, accounts, agents or internal locations are
distributed as lexically redacted copies, each listed with its historical and distributed checksum.

Check after download:

```
sha256sum qball-bic-v0.53-archive-r3.zip
unzip qball-bic-v0.53-archive-r3.zip
cd archive && sha256sum -c MANIFEST.sha256
```

Start with `archive/README.md` (overview, environment, rerun of the linear certificates C0/C1/C2, coverage table,
verification status) and `archive/MANIFEST.md` (origin of every file). Only the linear certificates are offered as a
rerun; all other parts are records or hash bindings. File timestamps in the ZIP are set to a fixed date.
