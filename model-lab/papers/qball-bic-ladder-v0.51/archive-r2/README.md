# Companion archive r2 (release asset)

The companion archive of preprint 0.51 is not stored in this Git repository. It is attached to release
[`qball-bic-v0.51`](https://github.com/fmhc/physics/releases/tag/qball-bic-v0.51) as
`qball-bic-v0.51-archive-r2.zip`.

| Item | Value |
|---|---|
| ZIP file | `qball-bic-v0.51-archive-r2.zip`, 36 882 721 bytes; 494 payload files plus `MANIFEST.sha256` (495 files in total) under `archive/` |
| SHA-256 of the ZIP | `b74a313a8f0a22ae04158c54475ac6c7136675bde94d7631a110c6726264e830` |
| SHA-256 of `archive/MANIFEST.sha256` | `a8db87191292a19a753dbcf3970005392303db583179c91c18ed5317e26fd990` (copy: [`MANIFEST.sha256`](MANIFEST.sha256)) |
| Licences | code (`.py`, `.pyi`, `.jq`) MIT; everything else CC BY 4.0 (files `LICENSE-CODE`, `LICENSE` in the ZIP) |

Check after download:

```
sha256sum qball-bic-v0.51-archive-r2.zip
unzip qball-bic-v0.51-archive-r2.zip
cd archive && sha256sum -c MANIFEST.sha256
```

Start with `archive/README.md` (overview, environment, rerun of the linear certificates C0/C1/C2, coverage table,
verification status) and `archive/MANIFEST.md` (origin of every file). Only the linear certificates are offered as a
rerun; all other parts are records or hash bindings. File timestamps in the ZIP are set to a fixed date.
