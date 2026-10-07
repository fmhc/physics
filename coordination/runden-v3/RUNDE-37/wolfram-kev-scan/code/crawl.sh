# WOLFRAM-KEV-SCAN (Runde 37, .69-Ordner runde41-wolfram-kev): hoeflicher Abruf von wolframphysics.org.
# Wird im Shell des Agenten per "source" ausgefuehrt (kein python/awk/perl). Nur curl, sed, grep, sort, cut, sha256sum, date.
# robots.txt (2026-10-04T14:20:16+02:00): "User-agent: * / Disallow: (leer)" -> alles erlaubt; Sitemap genutzt.
# Regeln: nacheinander, nach jedem Abruf 1,2 s Pause, erkennbarer User-Agent, nur https://www.wolframphysics.org,
# nur text/html (sonst Datei sofort geloescht), hoechstens 600 Abrufe, keine Formulare (ask-a-question, downloads?i= ausgelassen),
# keine PDFs/Notebooks/Programme (Endungsfilter vor dem Abruf).
set -u
UA="fmhc-physics-research-scan (contact: project lead)"
D=/home/fmh/fmhc-physics/coordination/runden-v3/RUNDE-37/wolfram-kev-scan
IDX=$D/seiten/INDEX.tsv
MAX=600
cd "$D" || return 1
[ -f "$IDX" ] || printf 'nr\turl\tzeit\thttp\tcontent_type\tbytes\tsha256\turl_effektiv\tdatei\tstatus\n' > "$IDX"

anzahl() { echo $(( $(wc -l < "$IDX") - 1 )); }

holen() {  # $1 = URL; gibt 1 zurueck, wenn die Obergrenze erreicht ist
  local url="$1" n nr f t w code ct by eff st sh
  grep -q -F "	$url	" "$IDX" && return 0
  n=$(anzahl); [ "$n" -ge "$MAX" ] && return 1
  n=$((n+1)); nr=$(printf '%04d' "$n"); f=seiten/$nr.html
  t=$(date --iso-8601=seconds)
  w=$(curl -sS -L --max-redirs 3 --proto '=https' --max-time 40 --max-filesize 8000000 -A "$UA" -o "$f" \
        -w '%{http_code}\t%{content_type}\t%{size_download}\t%{url_effective}' "$url" 2>>meta/crawl-fehler.log)
  code=$(printf '%s' "$w" | cut -f1); ct=$(printf '%s' "$w" | cut -f2); by=$(printf '%s' "$w" | cut -f3); eff=$(printf '%s' "$w" | cut -f4)
  st=ok
  case "$ct" in text/html*) ;; *) st=nicht-html; rm -f "$f" ;; esac
  case "$eff" in https://www.wolframphysics.org/*) ;; *) st=fremder-host; rm -f "$f" ;; esac
  [ "$code" = 200 ] || st="http-$code"
  sh=-; [ -f "$f" ] && sh=$(sha256sum "$f" | cut -d' ' -f1)
  printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' "$nr" "$url" "$t" "$code" "$ct" "$by" "$sh" "$eff" "$f" "$st" >> "$IDX"
  sleep 1.2
  return 0
}

liste_holen() {  # $1 = Datei mit URLs
  local u
  while IFS= read -r u; do
    [ -z "$u" ] && continue
    holen "$u" || return 1
  done < "$1"
}

# Links aus allen bisher geholten Seiten; relative Links gegen url_effektiv aufgeloest.
entdecken() {
  local nr url t code ct by sh eff f st dir
  : > meta/links-roh.txt
  while IFS=$'\t' read -r nr url t code ct by sh eff f st; do
    [ "$st" = ok ] || continue
    dir=$(printf '%s' "$eff" | sed -E 's#[^/]*$##')
    grep -o -E 'href="[^"]*"' "$f" | sed -E 's/^href="//; s/"$//; s/#.*$//; s/&amp;/\&/g' | while IFS= read -r l; do
      case "$l" in
        ''|mailto:*|javascript:*|tel:*|data:*) ;;
        https://www.wolframphysics.org/*) echo "$l" ;;
        http://www.wolframphysics.org/*|http://wolframphysics.org/*|https://wolframphysics.org/*)
          echo "$l" | sed -E 's#^https?://(www\.)?wolframphysics\.org/#https://www.wolframphysics.org/#' ;;
        //www.wolframphysics.org/*|//wolframphysics.org/*) echo "$l" | sed -E 's#^//(www\.)?wolframphysics\.org/#https://www.wolframphysics.org/#' ;;
        /*) echo "https://www.wolframphysics.org$l" ;;
        *:*) ;;
        *) echo "$dir$l" ;;
      esac
    done >> meta/links-roh.txt
  done < <(tail -n +2 "$IDX")
  # ./ und ../ aufloesen, index.html auf / abbilden, Endungen ausser html/htm verwerfen, Formulare und Downloads verwerfen
  sed -E ':a; s#/\./#/#g; s#/[^/]+/\.\./#/#; ta; s#/index\.html?$#/#' meta/links-roh.txt \
    | grep -E '^https://www\.wolframphysics\.org/' \
    | grep -v -E '\.[A-Za-z0-9]{1,5}$' | cat - <(sed -E 's#/index\.html?$#/#' meta/links-roh.txt | grep -E '^https://www\.wolframphysics\.org/.*\.html?$') \
    | grep -v -E 'downloads\?|ask-a-question|\?(.*&)?(q|query|search)=' \
    | grep -v -E '\?' | sort -u > meta/links-entdeckt.txt
  # Neu = nicht in den Sitemap-Listen und noch nicht geholt
  cat meta/liste-p1.txt meta/liste-p2.txt meta/liste-p4.txt meta/sitemap-urls.txt > meta/bekannt.tmp
  cut -f2 "$IDX" >> meta/bekannt.tmp
  grep -v -F -x -f meta/bekannt.tmp meta/links-entdeckt.txt > meta/liste-p3.txt
  rm -f meta/bekannt.tmp
}

echo "crawl start $(date --iso-8601=seconds)" >> meta/crawl.log
liste_holen meta/liste-p1.txt; echo "p1 fertig $(date --iso-8601=seconds) n=$(anzahl)" >> meta/crawl.log
liste_holen meta/liste-p2.txt; echo "p2 fertig $(date --iso-8601=seconds) n=$(anzahl)" >> meta/crawl.log
entdecken; echo "entdeckt $(wc -l < meta/liste-p3.txt) neue Links $(date --iso-8601=seconds)" >> meta/crawl.log
liste_holen meta/liste-p3.txt; echo "p3 fertig $(date --iso-8601=seconds) n=$(anzahl)" >> meta/crawl.log
liste_holen meta/liste-p4.txt; echo "p4 fertig $(date --iso-8601=seconds) n=$(anzahl)" >> meta/crawl.log
echo "crawl ende $(date --iso-8601=seconds) n=$(anzahl)" >> meta/crawl.log
