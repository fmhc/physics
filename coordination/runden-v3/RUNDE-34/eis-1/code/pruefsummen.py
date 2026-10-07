# EIS-1 (Runde 34): sha256 der eingefrorenen Kopien gegen die in den Laufausgaben vermerkten Pruefsummen (nach den Laeufen).
import sys, hashlib
for f in sys.argv[1:]:
    print(hashlib.sha256(open(f, "rb").read()).hexdigest(), f)
