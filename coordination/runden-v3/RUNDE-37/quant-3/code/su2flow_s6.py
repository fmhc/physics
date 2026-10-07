#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""QUANT-3 S6 (07.10.2026): Huelle um su2flow.py (unveraendert) mit speicherschonendem Staple (Blockweise ueber die Inzidenzeintraege).
Gleiche Rechnung wie su2flow.Fluss.staple (gleiche Operationen, nur in Bloecken summiert); nur der Speicherspitzenbedarf sinkt.
Aufruf wie su2flow.py (nur ueber kleintest.sh auf der .69)."""
import os
os.environ.setdefault('PYTORCH_CUDA_ALLOC_CONF', 'expandable_segments:True')
import sys
import torch

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)
import su2flow as SF  # noqa: E402

DEV, DT = SF.DEV, SF.DT
qmul = SF.qmul
BLOCK = int(os.environ.get('S6_BLOCK', '1000000'))


class FlussBlock(SF.Fluss):
    def staple(self, Q):
        F = self.F
        W = torch.zeros((Q.shape[0], F.ned, 4), dtype=DT, device=DEV)
        n = F.n_inz
        for i0 in range(0, n, BLOCK):
            i1 = min(n, i0 + BLOCK)
            A = Q[:, F.oth[0][i0:i1]] * F.om[0][i0:i1]
            for j in range(1, self.G.m - 1):
                A = qmul(A, Q[:, F.oth[j][i0:i1]] * F.om[j][i0:i1])
            A = A * F.spw[i0:i1]
            W.index_add_(1, F.loc[i0:i1], A)
            del A
        return W


SF.Fluss = FlussBlock

if __name__ == '__main__':
    SF.main()
