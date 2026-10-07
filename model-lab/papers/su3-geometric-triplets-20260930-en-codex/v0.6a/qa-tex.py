"""Document checks only, executed on .69 after typesetting."""
from pathlib import Path
from collections import Counter
import hashlib
import json
import platform
import re
import unicodedata
from bs4 import BeautifulSoup

assert platform.node() == 'ubuntu-auto'
p = Path(__file__).resolve().parent
source = BeautifulSoup((p/'source-v0.6a.html').read_text(), 'html.parser')
tex = BeautifulSoup((p/'qa/tex-semantic.html').read_text(), 'html.parser')
for n in tex.select('annotation'):
    n.decompose()
def numbers(t, german=False):
    t = unicodedata.normalize('NFKC', t).replace('−', '-')
    t = re.sub(r'-\s+(?=\d)', '-', t)
    if german:
        t = re.sub(r'(?<=\d),(?=\d)', '.', t)
    return re.findall(r'-?\d+(?:\.\d+)?', t)
report = {'host': platform.node(), 'tables': []}
assert len(source.select('table')) == len(tex.select('table')) == 8
for i, (a, b) in enumerate(zip(source.select('table'), tex.select('table')), 1):
    x = numbers(a.get_text(' '), True)
    y = numbers(b.get_text(' '))
    report['tables'].append({'table': i, 'equal': x == y, 'source': x, 'latex': y})
assert all(x['equal'] for x in report['tables']), report['tables']
report['precise_decimals'] = {
    key: dict(Counter(x for x in numbers(s.get_text(' '), g)
                      if re.fullmatch(r'-?\d+\.\d{3,}', x)))
    for key, s, g in [('source', source, True), ('latex', tex, False)]}
assert report['precise_decimals']['source'] == report['precise_decimals']['latex'], report['precise_decimals']
code = (p/'main.tex').read_text()
assert not [ord(c) for c in code if ord(c) < 32 and c not in '\n\r\t']
assert len(re.findall(r'\\begin\{equation\*?\}', code)) == 15
assert r'\begin{thebibliography}' in code
assert len(re.findall(r'\\bibitem', code)) == 7
assert r'\cite' in code and r'\eqref' in code and r'\ref' in code
assert len(re.findall(r'\\section\{', code)) == 10
assert not re.search(r'\b(gates?|arms|Computing location|using it in isolation)\b', code)
aux = (p/'main.aux').read_text()
report['label_count'] = len(re.findall(r'\\newlabel\{', aux))
assert report['label_count'] >= 25
out = (p/'main.out').read_text()
report['bookmarks'] = len(re.findall(r'\\BOOKMARK', out))
assert report['bookmarks'] >= 10
log = (p/'main.log').read_text()
assert not any(t in log for t in [
    'Overfull', 'Missing character', 'Undefined control sequence',
    'duplicate ignored', 'LaTeX Warning:', 'Package hyperref Warning:', '! '])
report['equations'] = 15
report['latex_log'] = 'No unresolved references, missing characters, duplicate targets or overfull boxes'
report['hashes'] = {f: hashlib.sha256((p/f).read_bytes()).hexdigest()
                    for f in ['main.tex', 'paper.pdf', 'source-v0.6a.html']}
(p/'qa/TEX-QA.json').write_text(json.dumps(report, indent=2)+'\n')
print(json.dumps({'status': 'PASS', 'tables': 8, 'equations': 15,
                  'labels': report['label_count'], 'bookmarks': report['bookmarks'],
                  'table_numbers': 'unchanged', 'precise_decimals': 'unchanged'}))
