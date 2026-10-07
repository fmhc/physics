"""WOLFRAM-RUHE-1 Hauptlauf Kontrollen (PLAN.md Abschn. 5 und 7): Programmprobe und WR0-Daten, 6000 Intervalle je
Kontrolle (Poisson 1+1, Nullgitter). Aufruf nur ueber kleintest.sh auf der .69: haupt_kontrollen.py <ausgabe.json>"""
import json
import os
import resource
import sys
import time

import numpy as np

import wr_kern as K


def main():
    aus = sys.argv[1]
    t0 = time.time()
    rng = np.random.default_rng(np.random.SeedSequence([20261004, 42, 2]))
    probe = K.programmprobe(rng, 40)
    kon = K.kontrollen(rng, 6000)
    hier = os.path.dirname(os.path.abspath(__file__))
    out = {
        "lauf": "haupt_kontrollen", "zeit_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "skripte_sha256": {f: K.datei_sha(os.path.join(hier, f)) for f in ("haupt_kontrollen.py", "wr_kern.py")},
        "numpy": np.__version__, "laufzeit_s": round(time.time() - t0, 2),
        "max_rss_mb": round(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0, 1),
        "programmprobe": probe, "kontrollen": kon,
    }
    with open(aus, "w") as fh:
        json.dump(out, fh)
    print(json.dumps({"laufzeit_s": out["laufzeit_s"], "max_rss_mb": out["max_rss_mb"],
                      "programmprobe_abw": probe["abweichungen"], "c_gitter": kon["c_gitter"],
                      "c_poisson": kon["c_poisson"], "n_gitter": len(kon["gitter"]["N"]),
                      "n_poisson": len(kon["poisson"]["N"])}))


if __name__ == "__main__":
    main()
