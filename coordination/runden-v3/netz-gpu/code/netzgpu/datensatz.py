# -*- coding: utf-8 -*-
"""Schreiber fuer das Datenformat netz-gpu/1 (coordination/runden-v3/netz-gpu/FORMAT.md).

Alles kleine Endian; Lagen und Groessen float32, Indizes uint32. Ein Bild = ein Ordner frames/<6 Ziffern>/ mit je einer
Datei <name>.f32 (Orte x Komponenten). min/max der Groessen sind feste Farbskalen ueber den ganzen Lauf; werden sie
nicht vorgegeben, nimmt schliessen() die beobachteten Extremwerte (bei symmetrischen Groessen +- max |x|).
"""
import json
import os
import shutil
import time

import numpy as np
import torch

from . import FASSUNG

ORTE = ('ecke', 'kante', 'dreieck', 'tetraeder')


def _np(a):
    if isinstance(a, torch.Tensor):
        a = a.detach().to('cpu')
        if a.is_floating_point():
            a = a.double()
        a = a.numpy()
    return np.asarray(a)


def _f32(pfad, a):
    np.ascontiguousarray(_np(a), dtype='<f4').tofile(pfad)


def _u32(pfad, a):
    np.ascontiguousarray(_np(a), dtype='<u4').tofile(pfad)


def platte_frei_gb(pfad='/home'):
    st = os.statvfs(pfad)
    return st.f_bavail * st.f_frsize / 1e9


class Datensatz:
    def __init__(self, pfad, titel, netz, quelle=None, hinweis='synthetisch, keine Messdaten', mit_tetraeder=True,
                 zeit_einheit='a/c (Eigenzeit der Zeltstangen)', netz_typ=None, extra=None):
        frei = platte_frei_gb()
        if frei < 10.0:
            raise SystemExit('Platte: nur %.1f GB frei (< 10 GB), Abbruch' % frei)
        if os.path.isdir(pfad):
            shutil.rmtree(pfad)                     # aeltere Fassung desselben Datensatzes ueberschreiben
        os.makedirs(os.path.join(pfad, 'netz'))
        os.makedirs(os.path.join(pfad, 'frames'))
        self.pfad, self.titel, self.netz = pfad, titel, netz
        _f32(os.path.join(pfad, 'netz', 'ecken.f32'), netz.x)
        _u32(os.path.join(pfad, 'netz', 'kanten.u32'), netz.kanten)
        _u32(os.path.join(pfad, 'netz', 'dreiecke.u32'), netz.dreiecke)
        if mit_tetraeder:
            _u32(os.path.join(pfad, 'netz', 'tetraeder.u32'), netz.tetraeder)
        self.manifest = {
            'format': 'netz-gpu/1', 'titel': titel,
            'erzeugt': time.strftime('%Y-%m-%dT%H:%M:%S%z'),
            'netz': {'typ': netz_typ or netz.typ, 'zellen': list(netz.zellen), 'N_ecken': int(netz.N_e),
                     'N_kanten': int(netz.N_k), 'N_dreiecke': int(netz.N_d),
                     'N_tetraeder': int(netz.N_t) if mit_tetraeder else 0,
                     'box': list(netz.box), 'periodisch': True},
            'einheiten': {'laenge': 'a (kubische Kante von V)', 'zeit': zeit_einheit},
            'groessen': [], 'frames': [], 'diagnose': {},
            'quelle': {'code': FASSUNG, 'lauf': pfad, 'hinweis': hinweis}}
        if quelle:
            self.manifest['quelle'].update(quelle)
        if extra:
            self.manifest.update(extra)
        self._g = {}
        self._mm = {}
        self.n_bild = 0
        self.bytes = 0

    def groesse(self, name, ort, komponenten, bedeutung, vmin=None, vmax=None, symmetrisch=False):
        assert ort in ORTE
        self._g[name] = {'name': name, 'ort': ort, 'komponenten': int(komponenten), 'bedeutung': bedeutung,
                         'min': vmin, 'max': vmax, '_sym': symmetrisch}

    def anzahl(self, ort):
        n = self.netz
        return {'ecke': n.N_e, 'kante': n.N_k, 'dreieck': n.N_d, 'tetraeder': n.N_t}[ort]

    def bild(self, zeit, **felder):
        ordner = 'frames/%06d' % self.n_bild
        os.makedirs(os.path.join(self.pfad, ordner), exist_ok=True)
        for name, a in felder.items():
            g = self._g[name]
            a = _np(a).astype(np.float32)
            assert a.shape[0] == self.anzahl(g['ort']), (name, a.shape)
            if g['komponenten'] > 1:
                assert a.shape[1] == g['komponenten'], (name, a.shape)
            a.astype('<f4').tofile(os.path.join(self.pfad, ordner, name + '.f32'))
            self.bytes += a.nbytes
            lo, hi = float(np.nanmin(a)), float(np.nanmax(a))
            mm = self._mm.get(name, (np.inf, -np.inf))
            self._mm[name] = (min(mm[0], lo), max(mm[1], hi))
        self.manifest['frames'].append({'index': self.n_bild, 'zeit': float(zeit), 'ordner': ordner})
        self.n_bild += 1

    def diagnose(self, schluessel, wert):
        self.manifest['diagnose'].setdefault(schluessel, []).append(float(wert))

    def setze(self, schluessel, wert):
        self.manifest[schluessel] = wert

    def schliessen(self):
        gr = []
        for name, g in self._g.items():
            lo, hi = self._mm.get(name, (0.0, 1.0))
            if g['_sym']:
                m = max(abs(lo), abs(hi))
                lo, hi = -m, m
            gg = {k: v for k, v in g.items() if not k.startswith('_')}
            if gg['min'] is None:
                gg['min'] = float(lo)
            if gg['max'] is None:
                gg['max'] = float(hi)
            gr.append(gg)
        self.manifest['groessen'] = gr
        self.manifest['groesse_MB'] = round(self.bytes / 1e6, 2)
        p = os.path.join(self.pfad, 'manifest.json')
        with open(p + '.tmp', 'w') as f:
            json.dump(self.manifest, f, indent=1, ensure_ascii=True)
        os.replace(p + '.tmp', p)
        return p
