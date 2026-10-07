from pathlib import Path
import json,re,platform
import xml.etree.ElementTree as ET
from collections import Counter
from html import unescape
from playwright.sync_api import sync_playwright
p=Path(__file__).resolve().parent
assert platform.node()=='ubuntu-auto'
h=p/'paper.html'
s=h.read_text()
for name in ('ladder','radial-mode','dipole-phases','bic-winding','counterpulse-dynamics','source-shaping'):
 s=s.replace('src="'+name+'.pdf"','src="'+name+'.svg"')
 s=s.replace('<embed src="'+name+'.svg" />','<img src="'+name+'.svg" alt="'+name+'" />')
s=s.replace('src="factorial-comparison.pdf"','src="factorial-comparison.png"')
s=s.replace('<embed src="factorial-comparison.png" />','<img src="factorial-comparison.png" alt="Four fixed actuator designs on two grids" />')
s=s.replace('src="phase-response.pdf"','src="phase-response.png"')
s=s.replace('<embed src="phase-response.png" />','<img src="phase-response.png" alt="Constant relative phase response on two grids" />')
s=s.replace('src="phase-work.pdf"','src="phase-work.png"')
s=s.replace('<embed src="phase-work.png" />','<img src="phase-work.png" alt="Second-pulse source work versus constant relative phase" />')
s=s.replace('src="angular-chirp-l2.pdf"','src="angular-chirp-l2.png"')
s=s.replace('<embed src="angular-chirp-l2.png" />','<img src="angular-chirp-l2.png" alt="Stored quadrupolar density variation and diagnostic norm during inward concentration" />')
s=s.replace('src="mean-injected-work.pdf"','src="mean-injected-work.png"')
s=s.replace('<embed src="mean-injected-work.png" />','<img src="mean-injected-work.png" alt="Mean injected source work for OU and Wiener prescribed drives, not stored energy" />')
s=s.replace('src="signed-lag-kernel.pdf"','src="signed-lag-kernel.png"')
s=s.replace('<embed src="signed-lag-kernel.png" />','<img src="signed-lag-kernel.png" alt="Signed lag kernel and four source-time-pair work contributions, not instantaneous power" />')
s=s.replace('src="angular-second-order-transport.pdf"','src="angular-second-order-transport.png"')
s=s.replace('<embed src="angular-second-order-transport.png" />','<img src="angular-second-order-transport.png" alt="Second-variation core deficit and positive net transport coefficient, not finite-amplitude retained charge" />')
s=s.replace('src="fixed-energy-transport.pdf"','src="fixed-energy-transport.png"')
s=s.replace('<embed src="fixed-energy-transport.png" />','<img src="fixed-energy-transport.png" alt="Core and net-transport second-variation coefficients with and without initial-energy compensation" />')
for name,alt in (('fa-response','Finite symmetric coefficient and separate signed core-charge fractions'),
                 ('fa-fields-t0','Stored initial axisymmetric amplitude and relative phase'),
                 ('fa-fields-t32','Stored final axisymmetric amplitude and relative phase')):
 s=s.replace('src="'+name+'.pdf"','src="'+name+'.png"')
 s=s.replace('<embed src="'+name+'.png" />','<img src="'+name+'.png" alt="'+alt+'" />')
def anchors(m):
 block=m.group(0)
 labels=re.findall(r'\\label\{([^}]+)\}',block)
 return ''.join('<span id="'+label+'"></span>' for label in labels)+block
s=re.sub(r'<math\b.*?</math>',anchors,s,flags=re.S)
h.write_text(s)
# Inventory legacy conversion fallbacks without changing their source.
raw_math_spans=[dict(offset=m.start(),html=m.group(0)) for m in
 re.finditer(r'<span\b[^>]*class="math\b[^"]*"[^>]*>.*?</span>',s,re.S)]
(p/'RAW-MATH-SPANS.json').write_text(json.dumps(raw_math_spans,indent=2))
assert not raw_math_spans,raw_math_spans
def math_fingerprint(tex):
 tex=re.sub(r'\\label\{[^}]+\}','',tex)
 tex=re.sub(r'\\mathrm\{([^{}]+)\}',r'\1',tex)
 tex=re.sub(r'\\rm\s+','',tex)
 return re.sub(r'\s+','',tex)
legacy=json.loads((p/'LEGACY-MATH-BASELINE.json').read_text())
assert len(legacy)==34
expected_legacy=Counter()
for row in legacy:
 tex=unescape(re.sub(r'<[^>]+>','',row['html'])).strip().strip('$')
 expected_legacy[math_fingerprint(tex)]+=1
 for label in re.findall(r'\\label\{([^}]+)\}',tex):
  assert 'id="'+label+'"' in s,label
actual_math=Counter()
for block in re.findall(r'<math\b.*?</math>',s,re.S):
 node=ET.fromstring(block)
 for annotation in node.iter():
  if annotation.tag.endswith('}annotation') and annotation.attrib.get('encoding')=='application/x-tex':
   actual_math[math_fingerprint(''.join(annotation.itertext()))]+=1
assert all(actual_math[k]>=v for k,v in expected_legacy.items()),(expected_legacy-actual_math)
rigidity_start=s.index('<h4 id="phase-rotation-and-the-fixed-charge-kinetic-gap.">')
rigidity_end=s.index('<h4 ',rigidity_start+4)
rigidity_html=s[rigidity_start:rigidity_end]
assert not re.search(r'<span\b[^>]*class="math\b',rigidity_html),rigidity_html
rigidity_math=[]
for block in re.findall(r'<math\b.*?</math>',rigidity_html,re.S):
 root=ET.fromstring(block)
 annotations=[''.join(node.itertext()) for node in root.iter() if node.tag.endswith('}annotation')]
 rigidity_math.append(dict(display=root.attrib.get('display'),tex=re.sub(r'\s+','',annotations[0]) if annotations else '',
                           fractions=sum(node.tag.endswith('}mfrac') for node in root.iter())))
assert any(m['display']=='inline' and m['tex']==r'\omega_{\mathrm{fit}}=Q/(2I)' for m in rigidity_math)
assert any(m['display']=='block' and 'r_v=' in m['tex'] and 'r_a=' in m['tex'] and m['fractions']>=2 for m in rigidity_math)
assert any(m['display']=='block' and r'E_h(U,V)-E_{Q,h}[U]' in m['tex'] and 'J_v=' in m['tex'] and m['fractions']>=2 for m in rigidity_math)
log=(p/'build-3.log').read_text()
assert 'Output written on main.pdf' in log
assert 'Overfull' not in log and 'undefined' not in log
text=(p/'paper.txt').read_text()
assert 'Finn Malte Hinrichsen' in text and 'Hamburg, Germany' in text
assert 'Authorship and affiliations to be determined' not in text
assert not re.search(r'\?\?',text)
assert 'Draft 0.44' in text
channel_scope = ' '.join(text.split())
assert 'every propagating tail must vanish separately' in channel_scope
assert 'the coupled background and mode can change at higher order' in channel_scope
assert 'conditions for a future coupled calculation, not results for an extension' in channel_scope
channel_html = ' '.join(unescape(re.sub(r'<[^>]+>', ' ', s)).split())
assert 'every propagating tail must vanish separately' in channel_html
assert 'conditions for a future coupled calculation, not results for an extension' in channel_html
assert all(key in s for key in ('Flach2003','Flach2005','Watabe2012','Heeck2021','InagakiMurakami2026'))
assert 'leading second-harmonic radiation amplitude' in ' '.join(text.split())
assert 'leading small-amplitude decay' in ' '.join(text.split())
assert 'half-density radius' in ' '.join(text.split())
assert 'fully coherent homogeneous' in ' '.join(text.split())
flat=' '.join(text.split())
assert all(v in flat for v in ('2.3053','2.3068','Friedberg','Sirlin','Classical Decay Rates of Oscillons'))
assert all(key in s for key in ('ZhangZhouZhu2025','ZhangOscillons2020'))
assert all(v in text for v in ('0.0282474','0.0282631','0.0586355','0.0588005','0.0830'))
assert all(v in ' '.join(text.split()) for v in ('fixed-charge kinetic gap','no further time integration','not a physical projection','does not minimize the spatial profile'))
assert all(v in text for v in ('0.0727746617','0.0730141978','0.0726948531','1.2055721','7.9808621'))
assert all(v in ' '.join(text.split()) for v in ('no measured Taylor order','dimensionless charge-fraction','fourteen completed','six remaining'))
assert all(('id="'+label+'"') in s for label in ('fig:fa-response','fig:fa-fields-initial','fig:fa-fields-final'))
assert 'Prescribed driving and response diagnostics' in ' '.join(text.split())
assert 'Exploratory concentration and constrained transport' in ' '.join(text.split())
assert all(('id="'+label+'"') in s for label in ('app:driving','app:formation','app:provenance'))
main_source=(p/'main.tex').read_text()
assert main_source.index(r'\input{sections/PROOF.tex}') < main_source.index(r'\section{Conclusion}') < main_source.index(r'\appendix')
assert main_source.index(r'\appendix') < main_source.index(r'\input{sections/APPENDIX-DRIVING.tex}') < main_source.index(r'\input{sections/APPENDIX-FORMATION.tex}') < main_source.index(r'\section{Reproducibility and provenance}')
assert r'\input{sections/ANGULAR-SECOND-ORDER.tex}' not in main_source
assert r'\input{sections/FINITE-CORRELATION.tex}' not in main_source
assert 'A local two-observable time-shift test' in ' '.join(text.split())
assert all(v in text for v in ('1.0936132','0.0021220476','6.820019','9.1439597'))
assert 'not a measured finite time shift' in ' '.join(text.split())
assert 'neither persistence of the core enhancement' in ' '.join(text.split())
assert 'Neither curve represents a finite deformation or a percentage increase' in ' '.join(text.split())
assert 'Compensating the initial energy through second order' in ' '.join(text.split())
assert all(v in text for v in ('0.1785687477','0.0873658344','0.0912029133','0.0726948606','0.0185080526','1.525216'))
assert 'does not assert exactly equal energies at finite deformation' in ' '.join(text.split())
assert 'cannot isolate geometry alone' in ' '.join(text.split())
assert 'no additional endpoint-success gate was introduced' in ' '.join(text.split())
assert 'Leading angular feedback on core-charge transport' in ' '.join(text.split())
assert all(v in text for v in ('0.08737135','0.08736583','0.10587389','0.01850805','0.0224455','2.864'))
assert 'positive net core inflow' in ' '.join(text.split())
assert 'leaves the final correction negative' in ' '.join(text.split())
assert 'preparation fixes charge, not energy' in ' '.join(text.split())
assert 'not the coefficient of normalized' in ' '.join(text.split())
assert 'constitutes a new acceptance criterion' in ' '.join(text.split())
assert 'Signed contributions from source-time separations' in ' '.join(text.split())
assert all(v in text for v in ('23.13074873','9.08245885','11.01641674','1.03681136','1.99506177879','8.47524'))
assert 'not assigned to any lag bin' in ' '.join(text.split())
assert 'not instantaneous positive or negative power' in ' '.join(text.split())
assert 'no continuous kernel error band is asserted' in ' '.join(text.split())
assert 'kernel-mechanism/' in text
assert 'A prescribed weak-potential extension' in ' '.join(text.split())
assert 'four tested points, not a uniform robustness region' in ' '.join(text.split())
assert 'unresolved Poisson-residual and matching-map regularity' in ' '.join(text.split())
assert 'not identified with the compactness' in ' '.join(text.split())
assert 'One exterior-domain sensitivity check' in ' '.join(text.split())
assert 'byte-identical source values and interior coefficients' in ' '.join(text.split())
assert '1.14' in text and '1.27' in text
assert 'agreement at floating-point roundoff scale' in ' '.join(text.split())
assert 'nor reduces the original comparison guard' in ' '.join(text.split())
assert 'Small correlation-time limit' in ' '.join(text.split())
assert 'nor imply global monotonicity' in ' '.join(text.split())
assert 'Separate numerical-method controls' in ' '.join(text.split())
assert 'finite-step defect in the RK4 quadratic balance' in ' '.join(text.split())
assert 'smooth manufactured solution' in ' '.join(text.split())
assert '499 interior nodes' in ' '.join(text.split())
assert 'not the prescribed physical pulse, an OU mean, or a continuum limit' in ' '.join(text.split())
assert 'A separate finite-correlation pulse comparison' in ' '.join(text.split())
assert all(v in text for v in ('2.1932622828','2.1733143747','1.9947908110','1.2658579115'))
assert 'not evidence of retained energy' in ' '.join(text.split())
assert 'neither a confidence interval nor a certified total-error bar' in ' '.join(text.split())
assert '2.09020168' in text and '2.93069596' in text
assert 'Correlated instantaneous frequency' in ' '.join(text.split())
assert 'failed the preselected modified quadratic-balance tolerance' in ' '.join(text.split())
assert 'That implementation therefore yielded no accepted finite-correlation field result' in ' '.join(text.split())
assert 'original outcome and thresholds remain unchanged' in ' '.join(text.split())
assert 'Prescribed finite phase coherence' in ' '.join(text.split())
assert 'One finite-coherence comparison' in ' '.join(text.split())
assert '2.173314375' in text and '1.039941139' in text
assert 'not a gain in energetic efficiency' in ' '.join(text.split())
assert 'Local direction and one mirror detuning' in ' '.join(text.split())
assert all(v in text for v in ('1.0285198','1.1333732','1.2486325','1.1006065','5.20289'))
assert 'not an identification of rotation as its cause' in ' '.join(text.split())
assert 'One prescribed temporal phase drift' in ' '.join(text.split())
assert '1.133373236' in text and '1.248632464' in text and '1.152592277' in text
assert 'not a certified error bound' in ' '.join(text.split())
assert 'Spatial mode shapes and phase-resolved reconstruction' in ' '.join(text.split())
assert 'Canceling one excitation is not stopping the Q-ball' in ' '.join(text.split())
assert 'A finite-time radial counterpulse test' in ' '.join(text.split())
assert 'Changing the complete pulse shape' in ' '.join(text.split())
assert 'does not isolate a spatial cause' in ' '.join(text.split())
assert '0.03872' in text and '0.001055' in text
assert '0.1586' in text and '0.02024' in text
assert 'A fixed factorial actuator comparison' in ' '.join(text.split())
assert 'test phase-error robustness' in ' '.join(text.split())
assert 'A constant relative pulse phase' in ' '.join(text.split())
assert 'Quadratic endpoint energy and the rotating generator' in ' '.join(text.split())
assert 'stored-profile audit identifies' in ' '.join(text.split())
assert 'not the complete laboratory energy change' in ' '.join(text.split())
assert '0.05203' in text and '0.03759' in text
assert 'Time-integrated source work in the nominal linear model' in ' '.join(text.split())
assert 'Net second-pulse source work' in ' '.join(text.split())
assert 'Phase dependence of the second-pulse source work' in ' '.join(text.split())
assert 'One angular direction during chirped concentration' in ' '.join(text.split())
assert 'Direction of the exterior field' in ' '.join(text.split())
assert '0.904702' in text and '0.888886' in text and '0.939306' in text
assert 'asymptotically free radiation, stationary Q-ball formation or binding of' in ' '.join(text.split())
assert '1.356829' in text and '1.139233' in text and '0.0062849' in text
assert 'not a conserved perturbation energy' in ' '.join(text.split())
assert '66.53' in text and '57.03' in text and '1.1334' in text
assert '5.939' in text and '1.122' in text
assert 'not identical to' in ' '.join(text.split())
assert 'not establish a better storage or erasure protocol at equal preparation' in ' '.join(text.split())
assert '0.007123' in text and '0.01954' in text
assert '0.0036%' in ''.join(text.split())
assert 'A prescribed local pulse' in text
assert 'Finite detuning' in text
assert 'Battye' in text and 'Malomed' in text and 'Weinstein' in text
assert 'This prediction remains untested' not in ' '.join(text.split())
assert 'R13' in text
for value in ('0.569360','0.559848','0.552619','0.546940','0.542364'):
 assert value in text, value
assert 'Linear coupling to the localized mode' in text
assert 'Spatial separation' in text
for label in ('env:time','env:generator','env:norm','env:projection','env:pulse'):
 assert ('id="'+label+'"') in s, label
errors=[]
with sync_playwright() as pw:
 browser=pw.chromium.launch(headless=True,executable_path='/home/fmh/.cache/ms-playwright/chromium_headless_shell-1243/chrome-headless-shell-linux64/chrome-headless-shell',args=['--no-sandbox','--disable-dev-shm-usage','--disable-gpu'])
 page=browser.new_page(viewport={'width':1100,'height':1000})
 page.on('pageerror',lambda e:errors.append(str(e)))
 page.goto(h.as_uri(),wait_until='load')
 font_report=page.evaluate('''async()=>{
  const loaded=await document.fonts.load('20px PaperMath');
  await document.fonts.ready;
  return {loaded:loaded.length,faces:[...document.fonts].filter(f=>f.family.replaceAll('"','').replaceAll("'",'')==='PaperMath').map(f=>({family:f.family,status:f.status})),mathFamilies:[...document.querySelectorAll('math')].map(m=>getComputedStyle(m).fontFamily)};
 }''')
 assert font_report['loaded']>0 and font_report['faces'] and all(f['status']=='loaded' for f in font_report['faces']),font_report
 assert font_report['mathFamilies'] and all('PaperMath' in f for f in font_report['mathFamilies']),font_report
 report=page.evaluate('''()=>({title:document.title,author:document.querySelector('.author')?.textContent,overflow:document.documentElement.scrollWidth>document.documentElement.clientWidth,math:document.querySelectorAll('math').length,images:[...document.images].map(x=>({loaded:x.complete&&x.naturalWidth>0})),missingAnchors:[...document.querySelectorAll('a[href^="#"]')].map(x=>x.getAttribute('href').slice(1)).filter(x=>!document.getElementById(x))})''')
 assert report['math']>40,report
 assert not report['overflow'],report
 assert len(report['images'])==17 and all(x['loaded'] for x in report['images']),report
 assert not report['missingAnchors'],report
 assert not errors,errors
 page.screenshot(path=str(p/'html-preview.png'))
 page.locator('figure').first.screenshot(path=str(p/'figure-preview.png'))
 page.locator('[id="phase-rotation-and-the-fixed-charge-kinetic-gap."] + p').screenshot(path=str(p/'rigidity-math-preview.png'))
 page.locator('[id="phase-rotation-and-the-fixed-charge-kinetic-gap."] + p + p').screenshot(path=str(p/'kinetic-gap-math-preview.png'))
 browser.close()
report.update(host=platform.node(),pdf_checks='author, no unresolved references or overfull boxes',browser_errors=errors)
report.update(raw_math_span_count=len(raw_math_spans),rigidity_mathml=rigidity_math)
report.update(font_loading=font_report,legacy_blocks_converted=34,legacy_unique_expressions=len(expected_legacy))
(p/'DOCUMENT-QA.json').write_text(json.dumps(report,indent=2))
print(json.dumps(report))
