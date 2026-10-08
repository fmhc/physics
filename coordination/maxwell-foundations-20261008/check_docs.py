"""Check local Markdown targets of this review patch; no numerical computation."""
from pathlib import Path
import re
import sys
from urllib.parse import unquote
root = Path(sys.argv[1]).resolve()
files = [root / p for p in ['README.md', 'RESULTS.md', 'CLAIMS.md', 'REPRODUCIBILITY.md', 'STAND-UND-NAECHSTE-SCHRITTE.md']]
files += list((root / 'coordination/maxwell-foundations-20261008').glob('*.md'))
files += list((root / 'reproducibility/maxwell-holdout').glob('*.md'))
files += list((root / 'reproducibility/maxwell-reflection').glob('*.md'))
errors = []
count = 0
for path in files:
    for target in re.findall(r'\]\(([^\s)]+)(?:\s+"[^"]*")?\)', path.read_text()):
        if target.startswith(('http:', 'https:', 'mailto:', '#')):
            continue
        local = unquote(target.split('#')[0])
        if local:
            count += 1
            if not (path.parent / local).exists():
                errors.append(f'{path.relative_to(root)}: {target}')
print(f'Checked {len(files)} Markdown files, {count} local targets; {len(errors)} missing')
print('\n'.join(errors))
sys.exit(bool(errors))
