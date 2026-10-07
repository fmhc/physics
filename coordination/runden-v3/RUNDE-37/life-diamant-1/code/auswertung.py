#!/usr/bin/env python3
# LIFE-DIAMANT-1 (Runde 38): mechanische Auswertung nach PLAN.md Abschnitt 7 und 4.1.
# Aufruf: auswertung.py <laufordner>   (liest kontrolle.json, stufe1.jsonl, stufe2-*.jsonl; schreibt dorthin)
import sys, os, json, glob, math
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

D = sys.argv[1]
TOL = 1e-9


def lies_jsonl(pfad):
    out = []
    with open(pfad) as fh:
        for z in fh:
            z = z.strip()
            if z:
                out.append(json.loads(z))
    return out


kontr = json.load(open(os.path.join(D, 'kontrolle.json')))
s1 = lies_jsonl(os.path.join(D, 'stufe1.jsonl'))
s2 = []
for p in sorted(glob.glob(os.path.join(D, 'stufe2-*.jsonl'))):
    s2 += lies_jsonl(p)
s1 = {r['index']: r for r in s1}
s2 = {r['index']: r for r in s2}
soll2 = [bm * 32 + sm for bm in (2, 4, 6, 8, 10, 12, 14) for sm in range(32)]

# ---------------------------------------------------------------- Gleiter sammeln (je Regel nach Kennung zusammengefuehrt)
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
alle = list(gl.values())
s1_gl = [g for g in alle if 1 in g['stufen']]


def im_kegel(g):
    d = np.abs(np.array(g['d_kart'])); p = g['p']
    return bool(d.sum() <= 2 * p and d.max() <= p)


# ---------------------------------------------------------------- Kontrollen
ld0 = bool(kontr['LD0_ok'])
z0 = bool(kontr['zusatz_ok'])
b1 = [r for r in s1.values() if 1 in r['B']]
bl = [r for r in s1.values() if len(r['B']) == 0]
z1 = bool(len(b1) == 256 and all(r['saat_klassen']['gross'] == r['n_saaten'] and r['n_gleiter'] == 0 for r in b1))
z2 = bool(len(bl) == 32 and all(r['saat_klassen']['tot'] + r['saat_klassen']['still'] == r['n_saaten']
                                and r['n_gleiter'] == 0 for r in bl))
z3 = bool(all(g['geprueft'] and im_kegel(g) for g in alle))
voll1 = bool(sorted(s1.keys()) == list(range(512)) and all(r['n_saaten'] == 48 for r in s1.values()))
voll2_regeln = sum(1 for i in soll2 if i in s2)
uebersp2 = sum(s2[i]['uebersprungen'] for i in s2)
sperre = not (ld0 and z0 and z1 and z2 and z3 and voll1)


def urteile(G):
    u = {}
    if sperre:
        for k in ('LD1', 'LD2', 'LD3'):
            u[k] = dict(urteil='nicht auswertbar', vermerk='Sperre F6: LD0, Z0 bis Z3 oder Vollstaendigkeit nicht erfuellt', werte={})
        return u
    regeln_mit = sorted({g['regel'] for g in G})
    u['LD1'] = dict(urteil='eingetroffen' if G else 'nicht eingetroffen',
                    werte=dict(gleiter=len(G), regeln_mit_gleitern=len(regeln_mit), regeln=regeln_mit,
                               bahnen=len({(g['regel_index'], g['bahn_id']) for g in G})))
    if not G:
        u['LD2'] = dict(urteil='nicht auswertbar', vermerk='keine Gleiter gefunden (bedingte Vorhersage)', werte={})
        u['LD3'] = dict(urteil='nicht auswertbar', vermerk='keine Gleiter gefunden (bedingte Vorhersage)', werte={})
        return u
    vmax = max(g['v_c'] for g in G)
    u['LD2'] = dict(urteil='eingetroffen' if vmax <= 0.5 + TOL else 'nicht eingetroffen',
                    werte=dict(v_max_c=vmax, ueber_halb=sum(g['v_c'] > 0.5 + TOL for g in G)))
    schnell = [g for g in G if g['v_c'] >= vmax * (1 - TOL)]
    u['LD3'] = dict(urteil='eingetroffen' if all(g['richtung'] == '<111>' for g in schnell) else 'nicht eingetroffen',
                    werte=dict(v_max_c=vmax, schnellste=len(schnell),
                               richtungen=sorted({g['richtung'] for g in schnell}),
                               regeln=sorted({g['regel'] for g in schnell})))
    return u


U = dict(LD0=dict(urteil='eingetroffen' if ld0 else 'nicht eingetroffen',
                  werte=dict(a=kontr['a_ok'], b=kontr['b_ok'], c=kontr['c_ok'], gitter=kontr['a_gitter'],
                             fest=kontr['b_fest'], kunst_faelle=sum(f['ok'] for f in kontr['c_kunst']['faelle']),
                             kunst_soll=len(kontr['c_kunst']['faelle']))))
U.update(urteile(alle))
U1 = urteile(s1_gl)

# ---------------------------------------------------------------- Nebenlesarten und eigene Vorhersagen
neben = {}
if alle and not sperre:
    fmax = max(g['f_lichtkegel'] for g in alle)
    neben['LD2_life'] = dict(f_max=fmax, eingetroffen=bool(fmax <= 0.5 + TOL))
    fs = [g for g in alle if g['f_lichtkegel'] >= fmax * (1 - TOL)]
    neben['LD3_nach_f'] = dict(richtungen=sorted({g['richtung'] for g in fs}), anzahl=len(fs))
    jr = {}
    for g in alle:
        jr.setdefault(g['regel'], []).append(g)
    n111 = 0
    for k, G in jr.items():
        vm = max(g['v_c'] for g in G)
        if all(g['richtung'] == '<111>' for g in G if g['v_c'] >= vm * (1 - TOL)):
            n111 += 1
    neben['LD3_je_regel'] = dict(regeln=len(jr), schnellster_111=n111)
agent = {}
agent['A1'] = z1; agent['A2'] = z2; agent['A3'] = z3
agent['A4'] = U['LD1']['urteil']
agent['A5'] = ('nicht auswertbar' if not alle else bool(all(2 in s1.get(g['regel_index'], s2.get(g['regel_index']))['B'] for g in alle)))
if alle:
    vmax = max(g['v_c'] for g in alle)
    schnell = [g for g in alle if g['v_c'] >= vmax * (1 - TOL)]
    agent['A6'] = U['LD2']['urteil']
    agent['A7'] = bool(all(g['richtung'] == '<110>' for g in schnell))
    agent['A8'] = U['LD3']['urteil']
else:
    agent['A6'] = agent['A7'] = agent['A8'] = 'nicht auswertbar'

# ---------------------------------------------------------------- Tabellen
klassen = ['Gleiter', 'Wachstum', 'offen', 'Oszillator', 'Stilleben', 'ausgestorben']
zeilen = ['index\tregel\tB\tS\tklasse_stufe1\ttot\tstill\tosz\tgleiter_ganz\tgross\toffen\tn_gleiter_s1\tn_bahnen_s1\t'
          'klasse_stufe2\tn_saaten_s2\tuebersprungen_s2\tn_gleiter_s2\tn_bahnen_s2\tv_max_c\tzeit_s1\tzeit_s2']
for i in range(512):
    r = s1.get(i)
    if r is None:
        continue
    q = s2.get(i)
    G = [g for g in alle if g['regel_index'] == i]
    vm = max((g['v_c'] for g in G), default=float('nan'))
    sk = r['saat_klassen']
    zeilen.append('\t'.join(str(x) for x in [
        i, r['name'], ''.join(map(str, r['B'])), ''.join(map(str, r['S'])), r['klasse'], sk['tot'], sk['still'],
        sk['osz'], sk['gleiter'], sk['gross'], sk['offen'], r['n_gleiter'], r['n_bahnen'],
        q['klasse'] if q else '-', q['n_saaten'] if q else '-', q['uebersprungen'] if q else '-',
        q['n_gleiter'] if q else '-', q['n_bahnen'] if q else '-', ('%.6f' % vm) if G else '-', r['zeit_s'],
        q['zeit_s'] if q else '-']))
open(os.path.join(D, 'regeln.tsv'), 'w').write('\n'.join(zeilen) + '\n')
klassenzahl = {k: sum(1 for r in s1.values() if r['klasse'] == k) for k in klassen}
klassenzahl2 = {k: sum(1 for r in s2.values() if r['klasse'] == k) for k in klassen}
alle_sorted = sorted(alle, key=lambda g: (-g['v_c'], g['regel_index'], g['id']))
json.dump(alle_sorted, open(os.path.join(D, 'gleiter.json'), 'w'), indent=1)

aus = dict(urteile=U, urteile_nur_stufe1={k: U1[k] for k in U1}, nebenlesarten=neben, agenten=agent,
           kontrollen=dict(Z0=z0, Z1=z1, Z2=z2, Z3=z3, stufe1_vollstaendig=voll1, stufe2_regeln=voll2_regeln,
                           stufe2_soll=len(soll2), stufe2_uebersprungene_saaten=uebersp2, sperre=sperre),
           zusammenfassung=dict(klassen_stufe1=klassenzahl, klassen_stufe2=klassenzahl2, gleiter=len(alle),
                                gleiter_stufe1=len(s1_gl),
                                saaten_stufe1=sum(r['n_saaten'] for r in s1.values()),
                                saaten_stufe2=sum(r['n_saaten'] for r in s2.values()),
                                zeit_stufe1_s=round(sum(r['zeit_s'] for r in s1.values()), 1),
                                zeit_stufe2_s=round(sum(r['zeit_s'] for r in s2.values()), 1),
                                stufe1_saatklassen={k: sum(r['saat_klassen'][k] for r in s1.values())
                                                    for k in ('tot', 'still', 'osz', 'gleiter', 'gross', 'offen')},
                                stufe2_saatklassen={k: sum(r['saat_klassen'][k] for r in s2.values())
                                                    for k in ('tot', 'still', 'osz', 'gleiter', 'gross', 'offen')}))
json.dump(aus, open(os.path.join(D, 'auswertung.json'), 'w'), indent=1)

# ---------------------------------------------------------------- Bilder
farben = {'Gleiter': '#d62728', 'Wachstum': '#ff7f0e', 'offen': '#9467bd', 'Oszillator': '#2ca02c',
          'Stilleben': '#1f77b4', 'ausgestorben': '#c7c7c7'}
fig, ax = plt.subplots(figsize=(15, 6.5))
for i, r in s1.items():
    bm, sm = i // 32, i % 32
    ax.add_patch(plt.Rectangle((sm, bm), 1, 1, color=farben[r['klasse']], ec='white', lw=0.5))
    if any(g['regel_index'] == i for g in alle):
        ax.plot(sm + 0.5, bm + 0.5, 'k*', ms=8)
ax.set_xlim(0, 32); ax.set_ylim(16, 0)
ax.set_xticks(np.arange(32) + 0.5)
ax.set_xticklabels(['S' + ''.join(str(k) for k in range(5) if (sm >> k) & 1) for sm in range(32)], rotation=90, fontsize=7)
ax.set_yticks(np.arange(16) + 0.5)
ax.set_yticklabels(['B' + ''.join(str(k) for k in range(1, 5) if (bm >> (k - 1)) & 1) for bm in range(16)], fontsize=8)
for k in klassen:
    ax.plot([], [], 's', color=farben[k], label='%s (%d)' % (k, klassenzahl[k]))
ax.plot([], [], 'k*', label='Gleiter gefunden (Stufe 1 oder 2)')
ax.legend(loc='upper left', bbox_to_anchor=(1.01, 1), fontsize=8)
ax.set_title('LIFE-DIAMANT-1: Klassen der 512 Regeln (Stufe 1, 48 Saaten je Regel); Zeilen B, Spalten S')
fig.tight_layout(); fig.savefig(os.path.join(D, 'klassenkarte.png'), dpi=110); plt.close(fig)

rfarbe = {'<111>': '#d62728', '<110>': '#1f77b4', '<100>': '#2ca02c'}
fig, axs = plt.subplots(1, 2, figsize=(13, 5))
for lab, v, c in (('c/2 (LD2)', 0.5, 'k'), ('Lichtkegel <100>: 0,577 c', 1 / math.sqrt(3), '#2ca02c'),
                  ('Lichtkegel <111>: 0,667 c', 2 / 3, '#d62728'), ('Lichtkegel <110>: 0,816 c', math.sqrt(2 / 3), '#1f77b4')):
    axs[0].axhline(v, color=c, ls='--' if lab.startswith('c/2') else ':', lw=1, label=lab)
if alle:
    for g in alle:
        axs[0].plot(g['p'], g['v_c'], 'o', color=rfarbe.get(g['richtung'], '#7f7f7f'), alpha=0.7)
        axs[1].plot(g['p'], g['f_lichtkegel'], 'o', color=rfarbe.get(g['richtung'], '#7f7f7f'), alpha=0.7)
    for k, c in list(rfarbe.items()) + [('andere', '#7f7f7f')]:
        axs[1].plot([], [], 'o', color=c, label=k)
    axs[1].axhline(0.5, color='k', ls='--', lw=1, label='halber Lichtkegel (Life-Konvention)')
    axs[1].legend(fontsize=8)
else:
    axs[0].text(0.5, 0.3, 'keine Gleiter gefunden', transform=axs[0].transAxes, ha='center', fontsize=14)
    axs[1].text(0.5, 0.5, 'keine Gleiter gefunden', transform=axs[1].transAxes, ha='center', fontsize=14)
axs[0].set_ylim(0, 1.05); axs[0].set_xlabel('Periode p'); axs[0].set_ylabel('v / c  (c = ein Strich je Schritt)')
axs[0].legend(fontsize=8, loc='upper right'); axs[0].set_title('Geschwindigkeit in Karteneinheit')
axs[1].set_ylim(0, 1.05); axs[1].set_xlabel('Periode p'); axs[1].set_ylabel('f = Anteil am Lichtkegel der Richtung')
axs[1].set_title('Life-Konvention (beschreibend)')
fig.tight_layout(); fig.savefig(os.path.join(D, 'geschwindigkeiten.png'), dpi=110); plt.close(fig)


def kanten(xyz):
    e = []
    for a in range(len(xyz)):
        for b in range(a + 1, len(xyz)):
            if int(((np.array(xyz[a]) - np.array(xyz[b])) ** 2).sum()) == 3:
                e.append((a, b))
    return e


if alle:
    g = alle_sorted[0]
    n = min(g['p'], 4)
    fig = plt.figure(figsize=(4.2 * n, 4.6))
    dc = np.array(g['d_kart'])
    for k in range(n):
        ax = fig.add_subplot(1, n, k + 1, projection='3d')
        xyz = np.array(g['phasen_kart'][k]); s = np.array(g['phasen_s'][k])
        for a, b in kanten(xyz.tolist()):
            ax.plot(*zip(xyz[a], xyz[b]), color='0.5', lw=1)
        ax.scatter(xyz[s == 0, 0], xyz[s == 0, 1], xyz[s == 0, 2], c='#1f77b4', s=60, label='A')
        ax.scatter(xyz[s == 1, 0], xyz[s == 1, 1], xyz[s == 1, 2], c='#ff7f0e', s=60, label='B')
        c0 = xyz.mean(0)
        ax.quiver(c0[0], c0[1], c0[2], dc[0], dc[1], dc[2], color='k', lw=1.5)
        ax.set_title('Phase %d von %d' % (k, g['p']), fontsize=9)
        ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_zlabel('z')
        if k == 0:
            ax.legend(fontsize=7)
    fig.suptitle('%s: Gleiter p = %d, d = %s (a/4), v = %.4f c, Richtung %s %s' % (
        g['regel'], g['p'], g['d_kart'], g['v_c'], g['richtung'], g['richtung_art']), fontsize=10)
    fig.tight_layout(); fig.savefig(os.path.join(D, 'gleiter-3d.png'), dpi=110); plt.close(fig)
else:
    fig = plt.figure(figsize=(6, 5))
    ax = fig.add_subplot(111, projection='3d')
    pts = np.array([(x, y, z) for x in range(5) for y in range(5) for z in range(5)])
    s = pts[:, 0] & 1
    ok = ((pts[:, 1] & 1) == s) & ((pts[:, 2] & 1) == s) & (((pts - s[:, None]).sum(1) % 4) == 0)
    pts = pts[ok]; s = pts[:, 0] & 1
    for a, b in kanten(pts.tolist()):
        ax.plot(*zip(pts[a], pts[b]), color='0.6', lw=1)
    ax.scatter(pts[s == 0, 0], pts[s == 0, 1], pts[s == 0, 2], c='#1f77b4', s=40)
    ax.scatter(pts[s == 1, 0], pts[s == 1, 1], pts[s == 1, 2], c='#ff7f0e', s=40)
    ax.set_title('Kein Gleiter gefunden. Gezeigt: Diamantgitter (A blau, B orange)', fontsize=9)
    fig.tight_layout(); fig.savefig(os.path.join(D, 'gleiter-3d.png'), dpi=110); plt.close(fig)

print(json.dumps({k: v['urteil'] for k, v in U.items()}), json.dumps(aus['kontrollen']), 'gleiter', len(alle))
