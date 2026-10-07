#!/usr/bin/env python3
# LIFE-FCC-1 (Runde 38): mechanische Auswertung nach PLAN.md Abschnitt 7 (Urteilsregeln) und 4.1.
# Aufruf: auswertung.py <laufordner>
#   liest kontrolle.json, stufe1.jsonl, stufe2*.jsonl, optional zusatz-s-leer.jsonl; schreibt dorthin:
#   auswertung.json, regeln.tsv, gleiter.json, gleiter-uebersicht.tsv, klassenkarte.png, geschwindigkeiten.png,
#   gleiter-3d.png und gleiter-3d-phase-NN.png (ein Gleiter ueber eine Periode).
import sys, os, json, glob, math
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

D = sys.argv[1]
TOL = 1e-9
KL = ['tot', 'still', 'osz', 'gleiter', 'gross', 'offen']
B_INT = [(b1, b2) for b1 in range(1, 13) for b2 in range(b1, 13)]
S_INT = [(s1, s2) for s1 in range(0, 13) for s2 in range(s1, 13)]
NREG = len(B_INT) * len(S_INT)


def bs(idx):
    bi, si = divmod(idx, len(S_INT))
    return B_INT[bi] + S_INT[si]


def lies_jsonl(pfad):
    out = []
    if not os.path.exists(pfad):
        return out
    with open(pfad) as fh:
        for z in fh:
            z = z.strip()
            if z:
                out.append(json.loads(z))
    return out


kontr = json.load(open(os.path.join(D, 'kontrolle.json')))
s1 = {r['index']: r for r in lies_jsonl(os.path.join(D, 'stufe1.jsonl'))}
s2 = {}
for p in sorted(glob.glob(os.path.join(D, 'stufe2*.jsonl'))):
    for r in lies_jsonl(p):
        s2[r['index']] = r
zus = {r['index']: r for r in lies_jsonl(os.path.join(D, 'zusatz-s-leer.jsonl'))}

# Stufe-2-Kandidaten nach der eingefrorenen Auswahlregel (zur Vollstaendigkeitsmeldung)
kand = [(r['score'], i) for i, r in s1.items() if r['score'] >= 1 and bs(i)[0] != 1 and not (bs(i)[2] == 0 and bs(i)[3] == 12)]
kand.sort(key=lambda x: (-x[0], x[1]))
kand_idx = [i for _, i in kand]
nicht_erreicht = [i for i in kand_idx if i not in s2]

# ---------------------------------------------------------------- Gleiter sammeln (je Regel nach Kennung)
gl = {}
for stufe, R in ((1, s1), (2, s2)):
    for idx, r in R.items():
        for g in r['gleiter']:
            key = (idx, g['id'])
            if key not in gl:
                g = dict(g); g['stufen'] = [stufe]; g['funde_je_stufe'] = {str(stufe): g['funde']}
                gl[key] = g
            else:
                gl[key]['stufen'].append(stufe)
                gl[key]['funde_je_stufe'][str(stufe)] = g['funde']
alle_roh = list(gl.values())
alle = [g for g in alle_roh if g['geprueft']]
s1_gl = [g for g in alle if 1 in g['stufen']]


def im_kegel(g):
    d = np.abs(np.array(g['d'])); p = g['p']
    return bool(d.sum() <= 2 * p and d.max() <= p)


# ---------------------------------------------------------------- Kontrollen
lf0 = bool(kontr['LF0_ok'])
z0 = bool(kontr['zusatz_ok'])
b1r = [r for i, r in s1.items() if bs(i)[0] == 1]
z1 = bool(len(b1r) == 1092 and all(all(s[0] in (4, 5) for s in r['saaten']) and r['n_gleiter'] == 0 for r in b1r))
svr = [r for i, r in s1.items() if bs(i)[2] == 0 and bs(i)[3] == 12]
z2 = bool(len(svr) == 78 and all(all(s[0] not in (2, 3) for s in r['saaten']) and r['n_gleiter'] == 0
                                 and not r['objekt_klassen'].get('osz') and not r['objekt_klassen'].get('gleiter')
                                 for r in svr))
z3 = bool(all(g['geprueft'] and im_kegel(g) and g['f_lichtkegel'] <= 1 + 1e-12 for g in alle_roh))
h7 = [r for i, r in list(s1.items()) + list(s2.items()) if bs(i)[0] >= 7]
z4 = bool(sum(1 for i in s1 if bs(i)[0] >= 7) == 1911 and all(
    r['saat_klassen']['gross'] == 0 and r['saat_klassen']['gleiter'] == 0 and r['n_gleiter'] == 0 for r in h7))
voll1 = bool(sorted(s1.keys()) == list(range(NREG)) and all(r['n_saaten'] == 24 for r in s1.values()))
sperre = not (lf0 and z0 and z1 and z2 and z3 and z4 and voll1)


def urteile(G, vermerk_s2=None):
    u = {}
    if sperre:
        for k in ('LF1', 'LF2', 'LF3'):
            u[k] = dict(urteil='nicht auswertbar', vermerk='Sperre: LF0, Z0 bis Z4 oder Vollstaendigkeit Stufe 1 nicht erfuellt',
                        werte={})
        return u
    regeln_mit = sorted({g['regel'] for g in G})
    bahnen = sorted({g['bahn_id'] for g in G})
    paare = sorted({(g['regel_index'], g['bahn_id']) for g in G})
    u['LF1'] = dict(urteil='eingetroffen' if G else 'nicht eingetroffen',
                    werte=dict(gleiter=len(G), regeln_mit_gleitern=len(regeln_mit), bahnen=len(bahnen),
                               regeln=regeln_mit[:200]))
    if vermerk_s2:
        u['LF1']['vermerk'] = vermerk_s2
    if not G:
        for k in ('LF2', 'LF3'):
            u[k] = dict(urteil='nicht auswertbar', vermerk='keine Gleiter gefunden (bedingte Vorhersage)', werte={})
        return u
    fmax = max(g['f_lichtkegel'] for g in G)
    schnell = [g for g in G if g['f_lichtkegel'] >= fmax * (1 - TOL)]
    u['LF2'] = dict(urteil='eingetroffen' if fmax <= 0.5 + TOL else 'nicht eingetroffen',
                    werte=dict(f_max=fmax, ueber_halb=sum(g['f_lichtkegel'] > 0.5 + TOL for g in G), gleiter=len(G),
                               schnellste=[dict(regel=g['regel'], p=g['p'], d=g['d'], richtung=g['richtung']) for g in schnell[:20]]))
    u['LF3'] = dict(urteil='eingetroffen' if len(bahnen) >= 2 else 'nicht eingetroffen',
                    werte=dict(bahnen=len(bahnen), paare_regel_bahn=len(paare), regeln=len(regeln_mit)))
    if vermerk_s2:
        for k in ('LF2', 'LF3'):
            u[k]['vermerk'] = vermerk_s2
    return u


vermerk_s2 = None
if nicht_erreicht:
    vermerk_s2 = 'Stufe 2 unvollstaendig: %d von %d Kandidaten gerechnet; Urteil auf Stufe 1 plus gerechnetem Teil' % (
        len(kand_idx) - len(nicht_erreicht), len(kand_idx))
U = dict(LF0=dict(urteil='eingetroffen' if lf0 else 'nicht eingetroffen',
                  werte=dict(a=kontr['a_ok'], b=kontr['b_ok'], c=kontr['c_ok'], gitter=kontr['a_gitter'],
                             kunstfolgen=sum(f['ok'] for f in kontr['b_kunstfolgen']['faelle']),
                             kunstfolgen_soll=len(kontr['b_kunstfolgen']['faelle']),
                             durchgangsprobe=[dict(typ=x['typ'], gefunden=x['n_gleiter'], mit_erwartung=x['mit_erwartung'],
                                                   ok=x['ok']) for x in kontr['c_durchgangsprobe']])))
U.update(urteile(alle, vermerk_s2))
U1 = urteile(s1_gl)

# ---------------------------------------------------------------- Nebenlesarten und eigene Vorhersagen
neben = {}
if alle and not sperre:
    neben['LF3_kartenklammer_paare'] = dict(paare=len({(g['regel_index'], g['bahn_id']) for g in alle}),
                                            eingetroffen=bool(len({(g['regel_index'], g['bahn_id']) for g in alle}) >= 2))
    neben['LF2_karteneinheit'] = dict(v_max_c=max(g['v_c'] for g in alle))
    jr = {}
    for g in alle:
        jr.setdefault(g['richtung'], []).append(g)
    neben['je_richtung'] = {k: dict(gleiter=len(v), f_max=max(x['f_lichtkegel'] for x in v),
                                    v_max_c=max(x['v_c'] for x in v)) for k, v in jr.items()}
agent = dict(A1=z1, A2=z2, A3=z4, A4=U['LF1']['urteil'])
if alle and not sperre:
    agent['A5'] = bool(all(bs(g['regel_index'])[0] in (3, 4) for g in alle))
    agent['A6'] = U['LF2']['urteil']
    agent['A7'] = U['LF3']['urteil']
    fmax = max(g['f_lichtkegel'] for g in alle)
    agent['A8'] = bool(all(g['richtung'] == '<110>' for g in alle if g['f_lichtkegel'] >= fmax * (1 - TOL)))
else:
    agent['A5'] = agent['A6'] = agent['A7'] = agent['A8'] = 'nicht auswertbar'

# ---------------------------------------------------------------- Tabellen
klassen = ['Gleiter', 'Wachstum', 'offen', 'Oszillator', 'Stilleben', 'ausgestorben']
zeilen = ['index\tregel\tb1\tb2\ts1\ts2\tklasse_stufe1\ttot\tstill\tosz\tgleiter_ganz\tgross\toffen\tscore\tgekappt\t'
          'n_gleiter_s1\tn_bahnen_s1\tklasse_stufe2\tn_saaten_s2\tn_gleiter_s2\tn_bahnen_s2\tf_max\tzeit_s1\tzeit_s2']
for i in range(NREG):
    r = s1.get(i)
    if r is None:
        continue
    q = s2.get(i)
    G = [g for g in alle if g['regel_index'] == i]
    fm = max((g['f_lichtkegel'] for g in G), default=float('nan'))
    sk = r['saat_klassen']
    zeilen.append('\t'.join(str(x) for x in [
        i, r['name'], *bs(i), r['klasse'], sk['tot'], sk['still'], sk['osz'], sk['gleiter'], sk['gross'], sk['offen'],
        r['score'], int(r['gekappt']), r['n_gleiter'], r['n_bahnen'], q['klasse'] if q else '-', q['n_saaten'] if q else '-',
        q['n_gleiter'] if q else '-', q['n_bahnen'] if q else '-', ('%.6f' % fm) if G else '-', r['zeit_s'],
        q['zeit_s'] if q else '-']))
open(os.path.join(D, 'regeln.tsv'), 'w').write('\n'.join(zeilen) + '\n')

alle_sorted = sorted(alle_roh, key=lambda g: (-g['f_lichtkegel'], g['regel_index'], g['id']))
gl_json = []
for g in alle_sorted:
    h = {k: v for k, v in g.items() if k != 'symmetrie'}
    gl_json.append(h)
json.dump(gl_json, open(os.path.join(D, 'gleiter.json'), 'w'), indent=1)
uz = ['regel\tregel_index\tid\tbahn_id\tp\td\tbetrag_d\tv_c\tf_lichtkegel\tv_grenze_c\trichtung\tzellen_min\tzellen_max\t'
      'stufen\tfunde\terste_quelle\tgeprueft\tstabilisator\tbahn_groesse\tdreh24_selbst\tdreh12T_selbst\thalbe_periode']
for g in alle_sorted:
    uz.append('\t'.join(str(x) for x in [
        g['regel'], g['regel_index'], g['id'], g['bahn_id'], g['p'], g['d'], '%.4f' % math.sqrt(sum(c * c for c in g['d'])),
        '%.6f' % g['v_c'], '%.6f' % g['f_lichtkegel'], '%.6f' % g['v_grenze_c'], g['richtung'], g['zellen_min'],
        g['zellen_max'], g['stufen'], g['funde_je_stufe'], g['erste_quelle'].get('art'), g['geprueft'],
        '|'.join('%s:%d' % (s['typ'], s['phasenversatz']) for s in g['stabilisator']), g['bahn_groesse'],
        g['dreh24']['selbst'], g['dreh12_T']['selbst'], '|'.join(x['typ'] for x in g['halbe_periode_um_laufachse'])]))
open(os.path.join(D, 'gleiter-uebersicht.tsv'), 'w').write('\n'.join(uz) + '\n')

klassenzahl = {k: sum(1 for r in s1.values() if r['klasse'] == k) for k in klassen}
klassenzahl2 = {k: sum(1 for r in s2.values() if r['klasse'] == k) for k in klassen}
bahnen_info = {}
for g in alle:
    b = bahnen_info.setdefault(g['bahn_id'], dict(regeln=set(), p=g['p'], f=g['f_lichtkegel'], richtung=g['richtung'],
                                                   zellen=g['zellen_min'], funde=0))
    b['regeln'].add(g['regel']); b['funde'] += sum(g['funde_je_stufe'].values())
bahnen_out = sorted([dict(bahn_id=k, regeln=len(v['regeln']), regel_beispiele=sorted(v['regeln'])[:8], p=v['p'],
                          f=v['f'], richtung=v['richtung'], zellen_min=v['zellen'], funde=v['funde'])
                     for k, v in bahnen_info.items()], key=lambda x: (-x['funde'], x['bahn_id']))

zus_info = None
if zus:
    zus_info = dict(regeln=len(zus), klassen={k: sum(1 for r in zus.values() if r['klasse'] == k) for k in klassen},
                    gleiter=sum(r['n_gleiter'] for r in zus.values()),
                    regeln_mit_gleitern=sorted(r['name'] for r in zus.values() if r['n_gleiter']),
                    f_max=max([g['f_lichtkegel'] for r in zus.values() for g in r['gleiter'] if g['geprueft']] or [None]))

aus = dict(urteile=U, urteile_nur_stufe1=U1, nebenlesarten=neben, agenten=agent,
           kontrollen=dict(LF0=lf0, Z0=z0, Z1=z1, Z2=z2, Z3=z3, Z4=z4, stufe1_vollstaendig=voll1,
                           stufe2_kandidaten=len(kand_idx), stufe2_gerechnet=len(kand_idx) - len(nicht_erreicht),
                           stufe2_nicht_erreicht=len(nicht_erreicht), sperre=sperre),
           zusammenfassung=dict(klassen_stufe1=klassenzahl, klassen_stufe2=klassenzahl2, gleiter_geprueft=len(alle),
                                gleiter_roh=len(alle_roh), gleiter_stufe1=len(s1_gl), bahnen=bahnen_out[:100],
                                n_bahnen=len(bahnen_out),
                                saaten_stufe1=sum(r['n_saaten'] for r in s1.values()),
                                saaten_stufe2=sum(r['n_saaten'] for r in s2.values()),
                                gekappt_stufe1=sum(1 for r in s1.values() if r['gekappt']),
                                gekappt_stufe2=sum(1 for r in s2.values() if r['gekappt']),
                                objekt_gekappt_stufe1=sum(1 for r in s1.values() if r['objekt_gekappt']),
                                objekt_gekappt_stufe2=sum(1 for r in s2.values() if r['objekt_gekappt']),
                                objekt_laeufe_stufe1=sum(r['objekt_laeufe'] for r in s1.values()),
                                objekt_laeufe_stufe2=sum(r['objekt_laeufe'] for r in s2.values()),
                                zeit_stufe1_s=round(sum(r['zeit_s'] for r in s1.values()), 1),
                                zeit_stufe2_s=round(sum(r['zeit_s'] for r in s2.values()), 1),
                                stufe1_saatklassen={k: sum(r['saat_klassen'][k] for r in s1.values()) for k in KL},
                                stufe2_saatklassen={k: sum(r['saat_klassen'][k] for r in s2.values()) for k in KL}),
           zusatz_s_leer=zus_info)
json.dump(aus, open(os.path.join(D, 'auswertung.json'), 'w'), indent=1)

# ---------------------------------------------------------------- Bilder
farben = {'Gleiter': '#d62728', 'Wachstum': '#ff7f0e', 'offen': '#9467bd', 'Oszillator': '#2ca02c',
          'Stilleben': '#1f77b4', 'ausgestorben': '#c7c7c7'}
mit_gl1 = {g['regel_index'] for g in alle if 1 in g['stufen']}
mit_gl2 = {g['regel_index'] for g in alle if 1 not in g['stufen']}
fig, ax = plt.subplots(figsize=(24, 16))
for i, r in s1.items():
    bi, si = divmod(i, len(S_INT))
    ax.add_patch(plt.Rectangle((si, bi), 1, 1, color=farben[r['klasse']], ec='white', lw=0.3))
    if i in mit_gl1:
        ax.plot(si + 0.5, bi + 0.5, 'k*', ms=5)
    elif i in mit_gl2:
        ax.plot(si + 0.5, bi + 0.5, 'kx', ms=4)
ax.set_xlim(0, len(S_INT)); ax.set_ylim(len(B_INT), 0)
ax.set_xticks(np.arange(len(S_INT)) + 0.5)
ax.set_xticklabels(['%d-%d' % s for s in S_INT], rotation=90, fontsize=5)
ax.set_yticks(np.arange(len(B_INT)) + 0.5)
ax.set_yticklabels(['%d-%d' % b for b in B_INT], fontsize=5)
for k in range(1, 13):
    ax.axhline(B_INT.index((k, k)), color='k', lw=0.4)
for k in range(13):
    ax.axvline(S_INT.index((k, k)), color='k', lw=0.4)
for k in klassen:
    ax.plot([], [], 's', color=farben[k], label='%s (%d)' % (k, klassenzahl[k]))
ax.plot([], [], 'k*', label='Gleiter (Stufe 1)')
ax.plot([], [], 'kx', label='Gleiter nur in Stufe 2')
ax.legend(loc='upper left', bbox_to_anchor=(1.005, 1), fontsize=9)
ax.set_xlabel('S = [s1..s2]'); ax.set_ylabel('B = [b1..b2]')
ax.set_title('LIFE-FCC-1: Klassen der 7098 Intervallregeln auf dem fcc-Gitter (Stufe 1, 24 Saaten je Regel); '
             'Zeilen B, Spalten S; Linien trennen b1 bzw. s1')
fig.tight_layout(); fig.savefig(os.path.join(D, 'klassenkarte.png'), dpi=100); plt.close(fig)

rfarbe = {'<110>': '#1f77b4', '<111>': '#d62728', '<100>': '#2ca02c'}
fig, axs = plt.subplots(1, 2, figsize=(14, 5.5))
for lab, v, c in (('Lichtkegel <100>: 0,707 c', 1 / math.sqrt(2), '#2ca02c'), ('Lichtkegel <111>: 0,816 c', math.sqrt(2 / 3), '#d62728'),
                  ('Lichtkegel <110>: 1 c', 1.0, '#1f77b4')):
    axs[0].axhline(v, color=c, ls=':', lw=1, label=lab)
rng = np.random.default_rng(0)
if alle:
    for g in alle:
        j = rng.uniform(-0.15, 0.15)
        axs[0].plot(g['p'] + j, g['v_c'], 'o', color=rfarbe.get(g['richtung'], '#7f7f7f'), alpha=0.6, ms=5)
        axs[1].plot(g['p'] + j, g['f_lichtkegel'], 'o', color=rfarbe.get(g['richtung'], '#7f7f7f'), alpha=0.6, ms=5)
    for k, c in list(rfarbe.items()) + [('andere', '#7f7f7f')]:
        axs[1].plot([], [], 'o', color=c, label=k)
    axs[1].set_xscale('log', base=2); axs[0].set_xscale('log', base=2)
else:
    axs[0].text(0.5, 0.3, 'keine Gleiter gefunden', transform=axs[0].transAxes, ha='center', fontsize=14)
    axs[1].text(0.5, 0.5, 'keine Gleiter gefunden', transform=axs[1].transAxes, ha='center', fontsize=14)
axs[1].axhline(0.5, color='k', ls='--', lw=1, label='halber Lichtkegel (LF2)')
axs[1].legend(fontsize=8)
axs[0].set_ylim(0, 1.05); axs[0].set_xlabel('Periode p'); axs[0].set_ylabel('v / c  (c = eine Nachbarkante je Schritt)')
axs[0].legend(fontsize=8, loc='upper right'); axs[0].set_title('Geschwindigkeit in Karteneinheit (geprueft: %d)' % len(alle))
axs[1].set_ylim(0, 1.05); axs[1].set_xlabel('Periode p'); axs[1].set_ylabel('f = Anteil am Lichtkegel der eigenen Richtung')
axs[1].set_title('Lichtkegelanteil f (LF2: alle <= 0,5?)')
fig.tight_layout(); fig.savefig(os.path.join(D, 'geschwindigkeiten.png'), dpi=110); plt.close(fig)


def kanten(xyz):
    xyz = np.asarray(xyz)
    d2 = ((xyz[:, None, :] - xyz[None, :, :]) ** 2).sum(-1)
    a, b = np.nonzero(np.triu(d2 == 2))
    return list(zip(a.tolist(), b.tolist()))


def zeichne(ax, xyz, dc, titel):
    xyz = np.asarray(xyz)
    for a, b in kanten(xyz):
        ax.plot(*zip(xyz[a], xyz[b]), color='0.6', lw=0.8)
    ax.scatter(xyz[:, 0], xyz[:, 1], xyz[:, 2], c='#1f77b4', s=50, depthshade=True)
    c0 = xyz.mean(0)
    ax.quiver(c0[0], c0[1], c0[2], dc[0], dc[1], dc[2], color='#d62728', lw=2)
    m = max(3, int(xyz.max()) + 2)
    ax.set_xlim(-1, m); ax.set_ylim(-1, m); ax.set_zlim(-1, m)
    ax.set_title(titel, fontsize=9)
    ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_zlabel('z')


if alle:
    # Gezeigter Gleiter: Bahn mit den meisten Funden, darin der kleinste (zellen_max), dann Regelindex.
    best_bahn = bahnen_out[0]['bahn_id']
    g = sorted([x for x in alle if x['bahn_id'] == best_bahn], key=lambda x: (x['zellen_max'], x['regel_index']))[0]
    dc = np.array(g['d'])
    n = min(g['p'], 12)
    for k in range(n):
        fig = plt.figure(figsize=(5.2, 5.2))
        ax = fig.add_subplot(111, projection='3d')
        zeichne(ax, g['phasen_kart'][k], dc, '%s: Phase %d von %d (%d Knoten)' % (g['regel'], k, g['p'], len(g['phasen_kart'][k])))
        fig.text(0.5, 0.02, 'p = %d, d = %s (a/2), v = %.3f c, f = %.3f, %s' % (g['p'], g['d'], g['v_c'], g['f_lichtkegel'],
                                                                         g['richtung']), ha='center', fontsize=8)
        fig.savefig(os.path.join(D, 'gleiter-3d-phase-%02d.png' % k), dpi=100); plt.close(fig)
    m = min(g['p'], 6)
    fig = plt.figure(figsize=(4.2 * m, 4.8))
    for k in range(m):
        ax = fig.add_subplot(1, m, k + 1, projection='3d')
        zeichne(ax, g['phasen_kart'][k], dc, 'Phase %d von %d' % (k, g['p']))
    fig.suptitle('%s: Gleiter p = %d, d = %s (a/2), v = %.4f c, f = %.4f, Richtung %s, Bahn %s' % (
        g['regel'], g['p'], g['d'], g['v_c'], g['f_lichtkegel'], g['richtung'], g['bahn_id']), fontsize=10)
    fig.tight_layout(); fig.savefig(os.path.join(D, 'gleiter-3d.png'), dpi=100); plt.close(fig)
    aus['bild_gleiter'] = dict(regel=g['regel'], id=g['id'], bahn_id=g['bahn_id'], p=g['p'], d=g['d'])
    json.dump(aus, open(os.path.join(D, 'auswertung.json'), 'w'), indent=1)
else:
    fig = plt.figure(figsize=(6, 5))
    ax = fig.add_subplot(111, projection='3d')
    pts = np.array([(x, y, z) for x in range(3) for y in range(3) for z in range(3) if (x + y + z) % 2 == 0])
    zeichne(ax, pts, np.zeros(3), 'Kein Gleiter gefunden. Gezeigt: fcc-Gitter (Wuerfel 2 x 2 x 2)')
    fig.tight_layout(); fig.savefig(os.path.join(D, 'gleiter-3d.png'), dpi=100); plt.close(fig)

print(json.dumps({k: v['urteil'] for k, v in U.items()}), json.dumps(aus['kontrollen']), 'gleiter', len(alle),
      'bahnen', len(bahnen_out))
