"""Starter-Einstieg (Physik-venv): ruft die Kev-Umgebung ~/brain-kev/kev/.venv als Unterprozess innerhalb derselben Einheit auf.

Kein Dienst, kein Server: kev_bewerten.py laedt das Modell im Prozess, bewertet und endet.
Aufruf ueber kleintest.sh: bash .../kleintest.sh p4000b kevlauf code/kev_lauf.py <argumente fuer kev_bewerten.py>
"""
import os, subprocess, sys

KEV_PY = "/home/fmh/brain-kev/kev/.venv/bin/python"
HIER = os.path.dirname(os.path.abspath(__file__))
ORDNER = os.path.dirname(HIER)
env = dict(os.environ)
env.update({
    "HF_HOME": os.path.join(ORDNER, "hf-leer"),      # nichts in ~/brain-kev schreiben; Modelle werden ueber absolute Pfade geladen
    "HF_HUB_OFFLINE": "1", "TRANSFORMERS_OFFLINE": "1", "HF_DATASETS_OFFLINE": "1",
    "PYTHONDONTWRITEBYTECODE": "1", "PYTHONUNBUFFERED": "1", "TOKENIZERS_PARALLELISM": "false",
    "TRITON_CACHE_DIR": os.path.join(ORDNER, "triton-cache"),
})
rc = subprocess.call([KEV_PY, os.path.join(HIER, "kev_bewerten.py")] + sys.argv[1:], env=env)
sys.exit(rc)
