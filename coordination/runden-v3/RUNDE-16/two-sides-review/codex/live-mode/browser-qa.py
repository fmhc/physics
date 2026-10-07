import functools, http.server, threading, pathlib, json, socket
from playwright.sync_api import sync_playwright
root=pathlib.Path('/tmp/fmhc-physics-causal-live-20261002')
server=http.server.ThreadingHTTPServer(('127.0.0.1',0),functools.partial(http.server.SimpleHTTPRequestHandler,directory=str(root)))
threading.Thread(target=server.serve_forever,daemon=True).start()
results={'host':socket.gethostname(),'checks':[]}
with sync_playwright() as p:
 browser=p.chromium.launch(executable_path='/home/fmh/.cache/ms-playwright/chromium_headless_shell-1243/chrome-headless-shell-linux64/chrome-headless-shell',args=['--no-sandbox','--use-angle=swiftshader','--enable-unsafe-swiftshader'])
 page=browser.new_page(viewport={'width':1400,'height':1000},accept_downloads=True)
 errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
 page.goto(f'http://127.0.0.1:{server.server_port}/model-lab/simulation-environment/qball-explorer/causal.html')
 page.wait_for_function('window.causalLab !== undefined')
 snap=lambda:page.evaluate('causalLab.snapshot()')
 assert snap()['steps']==0 and not snap()['running']
 test=(root/'solver-test.mjs').read_text().splitlines()
 js="""const assert={ok:(v,m)=>{if(!v)throw Error(m||'ok')},equal:(a,b)=>{if(a!==b)throw Error(`${a} != ${b}`)},deepEqual:(a,b)=>{if(JSON.stringify(a)!==JSON.stringify(b))throw Error('deepEqual')},throws:f=>{let yes=false;try{f()}catch{yes=true}if(!yes)throw Error('expected throw')}};
 const {createGraph,RotorSimulation,FieldSimulation,sectionMeasure}=await import('/model-lab/simulation-environment/qball-explorer/causal-solver.js');
 """+'\n'.join(test[2:])
 page.evaluate('async()=>{'+js+';return true;}')
 results['checks'].append('solver geometry, gradients, convergence, conservation, fail-stop PASS')
 page.locator('#step').click();assert snap()['state']['eventIndex']==1
 page.locator('#token').uncheck();page.locator('#step').click();assert snap()['state']['eventIndex']==0
 for graph,n in [('triangle',3),('square',4),('star4',4),('tetrahedron',4),('chain12',12),('chain20',20)]:
  page.select_option('#graph',graph);assert len(snap()['state']['positions'])==n
 page.select_option('#model','elastic');before=snap();page.locator('#step').click();after=snap()
 assert after['state']['positions']!=before['state']['positions'] and after['state']['time']==.005
 page.wait_for_timeout(250);assert snap()['state']==after['state']
 page.locator('#angle').fill('70');page.locator('#angle').dispatch_event('input');assert snap()['state']==after['state']
 page.select_option('#model','two-field');assert page.locator('#kick').is_disabled()
 before=snap();page.locator('#step').click();after=snap()
 assert after['state']['psi']!=before['state']['psi'] and after['state']['positions']==before['state']['positions']
 page.locator('#moving').check();before=snap();page.locator('#step').click();assert snap()['state']['positions']!=before['state']['positions']
 page.locator('#play').click();page.wait_for_timeout(500);assert snap()['running'] and snap()['steps']>1
 page.locator('#play').click();before=snap();page.wait_for_timeout(250);assert snap()['state']==before['state']
 page.locator('#play').click()
 page.evaluate("Object.defineProperty(document,'hidden',{configurable:true,value:true});document.dispatchEvent(new Event('visibilitychange'))")
 assert not snap()['running']
 page.evaluate("delete document.hidden")
 page.locator('#reduced').check();assert page.locator('#play').is_disabled()
 with page.expect_download() as d:page.locator('#export').click()
 d.value.save_as(str(root/'export.json'));export=json.loads((root/'export.json').read_text());assert export['state']==snap()['state']
 page.screenshot(path=str(root/'desktop.png'),full_page=True)
 page.set_viewport_size({'width':390,'height':844});page.screenshot(path=str(root/'mobile.png'),full_page=True)
 assert page.evaluate('document.documentElement.scrollWidth <= innerWidth')
 assert not errors,errors
 results['checks'].append('UI models, reset, passive detector, pause, visibility handler, reduced motion, export, mobile PASS')
 results['visibility_note']='Synthetic hidden event tests handler; not an OS tab lifecycle certification.'
 browser.close()
server.shutdown()
(root/'QA.json').write_text(json.dumps(results,indent=2))
print(json.dumps(results))
