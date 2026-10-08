# Validation record

2026-10-08. Numerical reproduction: see ../../reproducibility/maxwell-v/RUN.md and result.json.
The CUDA run passed its frozen checks; integrity and archived-output checks also passed on .69.
A separate AI agent read the code; see CODE-REVIEW.md. This is not external human reproduction.

Documentation QA on .69: check_docs.py checked 12 Markdown files and 202 local link targets, zero missing.
The first QA invocation reported three missing license/notice files because the temporary QA copy omitted them.
Those unchanged repository files were copied and the same check passed (systemd invocation
 e6e06827bec3451ab365f04aa31a50d4, 51 ms). No scientific criterion changed.

Git whitespace checks passed before publication. No repository-wide CI run is claimed.
