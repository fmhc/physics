#!/bin/bash
set -eu
cd /home/fmh/fmhc-physics-remote/qball-quantization-20261005-en-codex
TEXTOOLS=/home/fmh/fmhc-physics-remote/paper-english-v05-20260930/tools
export LD_LIBRARY_PATH="$TEXTOOLS/lib"
export TEXMFCNF="$TEXTOOLS/usr/share/texlive/texmf-dist/web2c"
export TEXMFROOT="$TEXTOOLS/usr/share/texlive"
export TEXMFDIST="$TEXTOOLS/usr/share/texlive/texmf-dist"
export TEXMFSYSVAR="$TEXTOOLS/var/lib/texmf"
export TEXMFSYSCONFIG="$TEXTOOLS/etc/texmf"
export TEXMFVAR="$PWD/texmf-var"
export TEXMFCONFIG="$PWD/texmf-config"
export TEXMFHOME="$PWD/texmf-home"
export TEXMF="{$TEXMFSYSCONFIG,$TEXMFSYSVAR,$TEXTOOLS/usr/share/texmf,$TEXMFDIST}"
mkdir -p qa
date --iso-8601=seconds > qa/START.txt
sha256sum main.tex > qa/INPUT.sha256
"$TEXTOOLS/bin/pdftex" -fmt="$TEXMFSYSVAR/web2c/pdftex/pdflatex.fmt" -progname=pdflatex -no-shell-escape -interaction=nonstopmode -halt-on-error main.tex > qa/compile-first.stdout 2>&1
"$TEXTOOLS/bin/pdftex" -fmt="$TEXMFSYSVAR/web2c/pdftex/pdflatex.fmt" -progname=pdflatex -no-shell-escape -interaction=nonstopmode -halt-on-error main.tex > qa/compile-final.stdout 2>&1
cp main.pdf paper.pdf
cp main.log qa/latex-final.log
"$TEXTOOLS/bin/pdfinfo" paper.pdf > qa/PDF-INFO.txt
"$TEXTOOLS/bin/pdftotext" -layout paper.pdf qa/pdf-layout.txt
"$TEXTOOLS/bin/pdftoppm" -scale-to 1100 -png paper.pdf qa/page >/dev/null 2>&1
"$TEXTOOLS/bin/pandoc" --data-dir="$TEXTOOLS/usr/share/pandoc/data" --from=latex --to=html5 --mathml --standalone --metadata title='Quantizing the sextic Q-ball sector' main.tex -o paper.html
sha256sum main.tex paper.pdf paper.html > qa/OUTPUT.sha256
date --iso-8601=seconds > qa/END.txt
