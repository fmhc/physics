"""Document QA only; run on ubuntu-auto, no physics execution."""
from pathlib import Path
from collections import Counter
import hashlib
import json
import platform
import re
import unicodedata
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright

assert platform.node() == 'ubuntu-auto'
p=Path(__file__).resolve().parent
qa=p/'qa';qa.mkdir(exist_ok=True)
a=BeautifulSoup((p/'source-v0.5.html').read_text(),'html.parser')
b=BeautifulSoup((p/'paper.html').read_text(),'html.parser')
def numbers(t, german=False):
    t=unicodedata.normalize('NFKC',t).replace('−','-')
    if german:t=re.sub(r'(?<=\d),(?=\d)', '.', t)
    return re.findall(r'-?\d+(?:\.\d+)?',t)
report={'host':platform.node(),'source_sha256':hashlib.sha256((p/'source-v0.5.html').read_bytes()).hexdigest()}
report['counts']={tag:[len(a.select(tag)),len(b.select(tag))] for tag in ['h1','h2','p','table','tr','td','th','div.eq','li','figure']}
assert all(x==y for x,y in report['counts'].values()),report['counts']
report['table_numbers']=[]
for i,(s,t) in enumerate(zip(a.select('table'),b.select('table')),1):
    sn=numbers(s.get_text(' '),True);tn=numbers(t.get_text(' '))
    report['table_numbers'].append({'table':i,'equal':sn==tn,'source':sn,'translation':tn})
assert all(v['equal'] for v in report['table_numbers']),report['table_numbers']
report['citation_links_equal']=[x['href'] for x in a.select('a[href]')]==[x['href'] for x in b.select('a[href]')]
assert report['citation_links_equal']
report['precise_decimal_counts']={}
for key,soup,german in [('source',a,True),('english',b,False)]:
    report['precise_decimal_counts'][key]=dict(Counter(x for x in numbers(soup.get_text(' '),german) if re.fullmatch(r'-?\d+\.\d{3,}',x)))
assert report['precise_decimal_counts']['source']==report['precise_decimal_counts']['english']
errors=[]
with sync_playwright() as pw:
    browser=pw.chromium.launch(headless=True,executable_path='/home/fmh/.cache/ms-playwright/chromium_headless_shell-1243/chrome-headless-shell-linux64/chrome-headless-shell',args=['--no-sandbox','--disable-dev-shm-usage','--disable-gpu'])
    page=browser.new_page(viewport={'width':1000,'height':1200},device_scale_factor=1)
    page.on('pageerror',lambda e:errors.append(str(e)))
    page.goto((p/'paper.html').as_uri(),wait_until='networkidle')
    page.evaluate('document.fonts.ready')
    report['browser']=page.evaluate('''() => ({title:document.title,language:document.documentElement.lang,
       horizontalOverflow:document.documentElement.scrollWidth>document.documentElement.clientWidth,
       images:Array.from(document.images).map(x=>({src:x.getAttribute('src'),loaded:x.complete&&x.naturalWidth>0})),
       equations:document.querySelectorAll('.eq').length})''')
    assert report['browser']['language']=='en'
    assert not report['browser']['horizontalOverflow']
    assert all(x['loaded'] for x in report['browser']['images'])
    page.screenshot(path=str(qa/'html-first-page.png'))
    page.locator('figure').screenshot(path=str(qa/'html-figure.png'))
    page.pdf(path=str(p/'paper-html.pdf'),format='A4',print_background=True,prefer_css_page_size=True)
    browser.close()
report['browser_errors']=errors
assert not errors
(qa/'DOCUMENT-QA.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'status':'PASS','counts':report['counts'],'table_numbers':'unchanged','precise_decimals':'unchanged','links':'unchanged','browser':report['browser']}))
