import sys
import py_compile
for f in sys.argv[1:]:
    py_compile.compile(f, doraise=True)
    print('py_compile ok', f, flush=True)
