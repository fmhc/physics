#!/usr/bin/env python3
"""Check package integrity and recorded outcome; does not rerun physics."""
import hashlib
import json
from pathlib import Path

root=Path(__file__).resolve().parent
r=json.loads((root/'result.json').read_text())
for name,digest in r['provenance']['sha256'].items():
    actual=hashlib.sha256((root/name).read_bytes()).hexdigest()
    if actual!=digest:
        raise SystemExit('Input hash mismatch: '+name)
if not r['passed'] or not all(all(x.values()) for x in r['checks'].values()):
    raise SystemExit('Archived calculation did not pass all checks')
if len(r['momenta'])!=96 or any(len(q)!=4 for q in r['momenta']):
    raise SystemExit('Momentum sample is not 96 four-dimensional vectors')
for name,arm in r['arms'].items():
    if len(arm['weights'])!=484 or len(arm['spectra'])!=96:
        raise SystemExit('Incomplete arm: '+name)
c=json.loads((root/'face-classification.json').read_text())
for name,arm in c['arms'].items():
    if arm['count']!=r['arms'][name]['n_negative_weights']:
        raise SystemExit('Face count mismatch: '+name)
print('PASS: input hashes, archived checks, 96 four-dimensional momenta, both full weight arrays and face counts. No physics rerun.')
