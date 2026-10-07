# EIS-1 (Runde 34): zweite Versionsprobe (C-Compiler fuer den Monte-Carlo-Kern), nur ueber kleintest.sh.
import subprocess, shutil
for prog in ("gcc", "cc", "clang"):
    p = shutil.which(prog)
    print(prog, p)
    if p:
        r = subprocess.run([p, "--version"], capture_output=True, text=True)
        print(r.stdout.splitlines()[0] if r.stdout else r.stderr)
import ctypes
print("ctypes ok")
