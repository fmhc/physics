"""PONZANO-1: Trockenlauf (Rauch) - nur ob alle Codepfade ohne Ausnahme laufen; gibt keine Pruefergebnisse aus."""
import sys
import time

sys.path.insert(0, "code")
import ponzano as P  # noqa: E402
from sympy import Rational, sign  # noqa: E402
from sympy.physics.wigner import wigner_6j  # noqa: E402

t0 = time.time()
# sympy-Pfad: ein zulaessiges, ein paritaetsverletzendes, ein dreiecksverletzendes Tupel (nur Typen pruefen)
for J in ((2, 2, 2, 2, 2, 2), (1, 1, 1, 1, 1, 1), (0, 0, 4, 0, 0, 0)):
    try:
        v = wigner_6j(*[Rational(x, 2) for x in J])
        v2 = (v * v).expand()
        _ = (int(sign(v)), int(v2.p), int(v2.q), bool(v2.is_Rational))
    except ValueError:
        pass
# exakte Summen (ein BE-Satz, Ergebnis nicht ausgegeben)
K = (2, 2, 2, 2, 2, 2, 2, 2, 2)
xs = P.be_x_bereich(K)
_ = P.summe_exakt([(P.be_phase(K, X) * (X + 1), list(P.be_tripel(K, X))) for X in xs])
_ = P.summe_exakt([(1, list(P.be_rechts(K)))])
_ = P.symmetrien()
# PO3-Codepfad bei lambda = 2 (nicht geurteilt)
out = P.teil_po3("K1", 2)
print("durchgelaufen", round(time.time() - t0, 2), "s; po3-Schluessel", len(out))
