"""PONZANO-1 (Runde 37): Umgebungsprobe auf der .69 (welche Bibliotheken sind da)."""
import importlib
import json
import sys

werte = {"python": sys.version}
for name in ["numpy", "scipy", "mpmath", "sympy", "matplotlib"]:
    try:
        m = importlib.import_module(name)
        werte[name] = getattr(m, "__version__", "da")
    except Exception as exc:  # noqa: BLE001
        werte[name] = "fehlt: " + repr(exc)
try:
    from sympy.physics.wigner import wigner_6j  # noqa: F401
    werte["sympy_wigner_6j"] = "da"
except Exception as exc:  # noqa: BLE001
    werte["sympy_wigner_6j"] = "fehlt: " + repr(exc)
print(json.dumps(werte, indent=1))
