#!/bin/bash
set -euo pipefail
# Invoke only inside Root's existing .69 cpu2 allocation: CPU11, <=60 CPU-s
# total and <=90 wall-s for the complete build/QA, including descendants.
# Per-command timeouts below are secondary guards, not aggregate budgets.
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
cd /home/fmh/fmhc-physics-remote/paper-bic-v44-20261003
test "$(hostname)" = ubuntu-auto
paper_tools=/home/fmh/fmhc-physics-remote/paper-english-v05-20260930/tools
export LD_LIBRARY_PATH="$paper_tools/lib"
export TEXMFCNF="$paper_tools/usr/share/texlive/texmf-dist/web2c"
export TEXMF="{$paper_tools/var/lib/texmf,$paper_tools/etc/texmf,$paper_tools/usr/share/texmf,$paper_tools/usr/share/texlive/texmf-dist}"
export TEXMFDBS="$TEXMF"
export TEXFORMATS="$paper_tools/var/lib/texmf/web2c/pdftex//"
export TEXINPUTS=".:$paper_tools/usr/share/texlive/texmf-dist/tex//:$paper_tools/usr/share/texmf/tex//"
export TFMFONTS="$paper_tools/usr/share/texlive/texmf-dist/fonts/tfm//:$paper_tools/usr/share/texmf/fonts/tfm//"
export T1FONTS="$paper_tools/usr/share/texlive/texmf-dist/fonts/type1//:$paper_tools/usr/share/texmf/fonts/type1//"
export TEXFONTMAPS="$paper_tools/var/lib/texmf/fonts/map//:$paper_tools/usr/share/texlive/texmf-dist/fonts/map//:$paper_tools/usr/share/texmf/fonts/map//"
export ENCFONTS="$paper_tools/usr/share/texlive/texmf-dist/fonts/enc//:$paper_tools/usr/share/texmf/fonts/enc//"
export MKTEXPK=0 MKTEXTFM=0 MKTEXFMT=0
sha256sum -c INPUTS.sha256 > INPUT-CHECK-BEFORE.txt
sha256sum "$paper_tools/bin/pdftex" "$paper_tools/bin/pandoc" "$paper_tools/bin/pdftotext" "$paper_tools/bin/pdfinfo" "$paper_tools/bin/pdftoppm" "$paper_tools/lib/"* "$paper_tools/var/lib/texmf/web2c/pdftex/pdflatex.fmt" > TOOLS.sha256
for pass in 1 2 3; do
  timeout --kill-after=2 80 taskset -c 11 nice -n 19 "$paper_tools/bin/pdftex" -progname=pdflatex -fmt=pdflatex -no-shell-escape -interaction=nonstopmode -halt-on-error main.tex > "build-$pass.log" 2>&1
done
cp main.pdf paper.pdf
timeout --kill-after=2 80 taskset -c 11 nice -n 19 "$paper_tools/bin/pandoc" --data-dir="$paper_tools/usr/share/pandoc/data" --from=latex --to=html5 --standalone --mathml --css=style.css main.tex -o paper.html > pandoc.log 2>&1
timeout --kill-after=2 80 taskset -c 11 nice -n 19 "$paper_tools/bin/pdftotext" -layout paper.pdf paper.txt
timeout --kill-after=2 80 taskset -c 11 nice -n 19 /home/fmh/fmhc-physics-gpu-venv/bin/python document-qa.py > document-qa.log 2>&1
timeout --kill-after=2 80 taskset -c 11 nice -n 19 "$paper_tools/bin/pdfinfo" paper.pdf > PDF-INFO.txt
timeout --kill-after=2 80 taskset -c 11 nice -n 19 "$paper_tools/bin/pdftoppm" -f 1 -singlefile -scale-to 1600 -png paper.pdf pdf-first-page
sha256sum -c INPUTS.sha256 > INPUT-CHECK-AFTER.txt
sha256sum paper.pdf paper.html paper.txt DOCUMENT-QA.json build-3.log html-preview.png figure-preview.png pdf-first-page.png > ARTIFACTS.sha256
sha256sum radial-mode.pdf radial-mode.svg dipole-phases.pdf dipole-phases.svg bic-winding.pdf bic-winding.svg >> ARTIFACTS.sha256
sha256sum counterpulse-dynamics.pdf counterpulse-dynamics.svg >> ARTIFACTS.sha256
sha256sum source-shaping.pdf source-shaping.svg >> ARTIFACTS.sha256
sha256sum factorial-comparison.pdf factorial-comparison.png >> ARTIFACTS.sha256
sha256sum phase-response.pdf phase-response.png >> ARTIFACTS.sha256

sha256sum phase-work.pdf phase-work.png >> ARTIFACTS.sha256
sha256sum angular-chirp-l2.pdf angular-chirp-l2.png >> ARTIFACTS.sha256
sha256sum mean-injected-work.pdf mean-injected-work.png >> ARTIFACTS.sha256
sha256sum signed-lag-kernel.pdf signed-lag-kernel.png >> ARTIFACTS.sha256
sha256sum angular-second-order-transport.pdf angular-second-order-transport.png >> ARTIFACTS.sha256
sha256sum fixed-energy-transport.pdf fixed-energy-transport.png >> ARTIFACTS.sha256
sha256sum fa-response.pdf fa-response.png fa-fields-t0.pdf fa-fields-t0.png fa-fields-t32.pdf fa-fields-t32.png >> ARTIFACTS.sha256
sha256sum RAW-MATH-SPANS.json >> ARTIFACTS.sha256
sha256sum rigidity-math-preview.png kinetic-gap-math-preview.png fonts/DejaVuMathTeXGyre.ttf fonts/DejaVu-COPYRIGHT.txt >> ARTIFACTS.sha256
