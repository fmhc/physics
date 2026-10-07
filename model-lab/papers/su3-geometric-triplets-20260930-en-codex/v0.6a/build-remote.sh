#!/bin/bash
set -eu
cd /home/fmh/fmhc-physics-remote/paper-english-v05-20260930
export LD_LIBRARY_PATH="$PWD/tools/lib"
export TEXMFCNF="$PWD/tools/usr/share/texlive/texmf-dist/web2c"
export TEXMFROOT="$PWD/tools/usr/share/texlive"
export TEXMFDIST="$PWD/tools/usr/share/texlive/texmf-dist"
export TEXMFSYSVAR="$PWD/tools/var/lib/texmf"
export TEXMFSYSCONFIG="$PWD/tools/etc/texmf"
export TEXMFVAR="$PWD/texmf-var"
export TEXMFCONFIG="$PWD/texmf-config"
export TEXMFHOME="$PWD/texmf-home"
export TEXMF="{$TEXMFSYSCONFIG,$TEXMFSYSVAR,$PWD/tools/usr/share/texmf,$TEXMFDIST}"
cd v0.6a
date --iso-8601=seconds > qa/BUILD-START.txt
taskset -c 11 nice -n 19 ../tools/bin/pdftex -fmt="$TEXMFSYSVAR/web2c/pdftex/pdflatex.fmt" -progname=pdflatex -no-shell-escape -interaction=nonstopmode -halt-on-error main.tex > qa/compile-first.stdout 2>&1
taskset -c 11 nice -n 19 ../tools/bin/pdftex -fmt="$TEXMFSYSVAR/web2c/pdftex/pdflatex.fmt" -progname=pdflatex -no-shell-escape -interaction=nonstopmode -halt-on-error main.tex > qa/compile-final.stdout 2>&1
cp main.pdf paper.pdf
cp main.log qa/latex-final.log
taskset -c 11 nice -n 19 ../tools/bin/pandoc --data-dir=../tools/usr/share/pandoc/data --from=latex --to=html5 --mathml --standalone --metadata title='Geometric mode triplets and symmetry-compatible interactions' main.tex -o qa/tex-semantic.html
../tools/bin/pdfinfo paper.pdf > qa/PDF-INFO.txt
../tools/bin/pdftotext -layout paper.pdf qa/pdf-layout.txt
taskset -c 11 nice -n 19 /home/fmh/fmhc-physics-gpu-venv/bin/python qa-tex.py
taskset -c 11 nice -n 19 /home/fmh/fmhc-physics-gpu-venv/bin/python qa-document.py
date --iso-8601=seconds > qa/BUILD-END.txt
