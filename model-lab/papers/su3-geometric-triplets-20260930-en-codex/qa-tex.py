"""LaTeX document fidelity checks on .69; no physical computation."""
from pathlib import Path
from collections import Counter
import hashlib,json,platform,re,unicodedata
from bs4 import BeautifulSoup
assert platform.node()=='ubuntu-auto'
p=Path(__file__).resolve().parent
source=BeautifulSoup((p/'source-v0.5.html').read_text(),'html.parser')
tex=BeautifulSoup((p/'qa/tex-semantic.html').read_text(),'html.parser')
for n in tex.select('annotation'):n.decompose()
def numbers(t,german=False):
    t=unicodedata.normalize('NFKC',t).replace('−','-')
    t=re.sub(r'-\s+(?=\d)','-',t)
    if german:t=re.sub(r'(?<=\d),(?=\d)', '.',t)
    return re.findall(r'-?\d+(?:\.\d+)?',t)
report={'host':platform.node(),'tables':[]}
assert len(source.select('table'))==len(tex.select('table'))==7
for i,(a,b) in enumerate(zip(source.select('table'),tex.select('table')),1):
    x=numbers(a.get_text(' '),True);y=numbers(b.get_text(' '))
    report['tables'].append({'table':i,'equal':x==y,'source':x,'latex':y})
assert all(x['equal'] for x in report['tables']),report['tables']
report['precise_decimals']={key:dict(Counter(x for x in numbers(s.get_text(' '),g) if re.fullmatch(r'-?\d+\.\d{3,}',x))) for key,s,g in [('source',source,True),('latex',tex,False)]}
assert report['precise_decimals']['source']==report['precise_decimals']['latex'],report['precise_decimals']
code=(p/'main.tex').read_text()
assert re.findall(r'\\tag\{(\d+)\}',code)==[str(i) for i in range(1,16)]
assert not [ord(c) for c in code if ord(c)<32 and c not in '\n\r\t']
log=(p/'main.log').read_text()
assert not any(t in log for t in ['Overfull','Missing character','Undefined control sequence','duplicate ignored','LaTeX Warning:','! '])
report['equations']=15
report['latex_log']='no errors, missing characters, duplicate targets or overfull boxes'
report['hashes']={f:hashlib.sha256((p/f).read_bytes()).hexdigest() for f in ['main.tex','main.pdf','source-v0.5.html']}
(p/'qa/TEX-QA.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'status':'PASS','tables':7,'table_numbers':'unchanged','precise_decimals':'unchanged','equations':15,'latex_log':report['latex_log']}))
