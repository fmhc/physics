"""WOLFRAM-KEV-SCAN: HTML zu Text, Abschnitte von etwa 300 bis 600 Woertern, blinde Stichprobe fuer die Gegenprobe.

Laeuft auf der .69 ueber kleintest.sh (CPU-Spur, Physik-venv, nur Standardbibliothek).
Aufruf: python code/aufbereiten.py seiten/ seiten/INDEX.tsv daten/
Ausgabe: daten/abschnitte.jsonl, daten/aufbereitung-statistik.json, daten/gegenprobe-stichprobe.jsonl, daten/gegenprobe-ids.txt
"""
import html.parser, json, os, random, re, sys, time

SEED = 20261004          # Stichprobe der Gegenprobe (im Plan festgelegt)
N_STICHPROBE = 25
MIN_W, ZIEL_W, MAX_W = 300, 450, 600   # Woerter je Abschnitt: Ziel 300-450, hart hoechstens ~600
MIN_ABSCHNITT_W = 20     # kuerzere Reste (Navigation, leere Seiten) werden nicht bewertet, aber gezaehlt

SKIP_TAGS = {"script", "style", "noscript", "nav", "header", "footer", "svg", "form", "button", "select",
             "template", "iframe", "head", "textarea", "label", "option"}
SKIP_MARK = re.compile(r"(?<![a-z])(tableofcontents|side-nav|search|breadcrumb|pagination|running-head|menu|cookie|share|"
                       r"related-qa|notebook-download|open-in-cloud|c2c|copyexpr|tb-meta-footer|nav-toggler)(?![a-z])", re.I)
BLOCK = {"p", "li", "h1", "h2", "h3", "h4", "h5", "h6", "td", "th", "dt", "dd", "figcaption", "blockquote", "pre",
         "div", "section", "article", "tr", "caption", "summary", "details", "main", "table", "ul", "ol", "dl", "figure"}
HEAD = {"h1", "h2", "h3", "h4", "h5", "h6"}
VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"}


class Leser(html.parser.HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []          # (tag, ueberspringen, ist_main)
        self.skip = 0
        self.main = 0
        self.blocks = []         # (art, text, in_main)
        self.buf = []
        self.art = "p"
        self.titel = ""
        self.in_titel = False
        self.main_gesehen = False

    def flush(self):
        t = re.sub(r"\s+", " ", "".join(self.buf)).strip()
        if t:
            self.blocks.append((self.art, t, self.main > 0))
        self.buf = []
        self.art = "p"

    def handle_starttag(self, tag, attrs):
        if tag == "title":
            self.in_titel = True
        if tag in VOID:
            if tag == "br" and not self.skip:
                self.buf.append(" ")
            return
        a = dict(attrs)
        marke = " ".join(str(a.get(k) or "") for k in ("class", "id", "role"))
        ueber = tag in SKIP_TAGS or bool(SKIP_MARK.search(marke)) or a.get("aria-hidden") == "true"
        ist_main = tag == "main"
        self.stack.append((tag, ueber, ist_main))
        if ueber:
            self.skip += 1
        if ist_main:
            self.main += 1
            self.main_gesehen = True
        if self.skip:
            return
        if tag in BLOCK:
            self.flush()
        if tag in HEAD:
            self.art = tag

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_titel = False
        if tag in VOID:
            return
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i][0] == tag:
                vorher = self.skip
                for _, ueber, ist_main in self.stack[i:]:
                    if ueber:
                        self.skip -= 1
                    if ist_main:
                        self.main -= 1
                del self.stack[i:]
                if not vorher and tag in BLOCK:
                    self.flush()
                return

    def handle_data(self, d):
        if self.in_titel:
            self.titel += d
        if self.skip:
            return
        self.buf.append(d)


def woerter(t):
    return len(t.split())


def saetze_teilen(t, maxw):
    """Absatz > maxw Woerter an Satzgrenzen in Stuecke <= maxw teilen."""
    saetze = re.split(r"(?<=[.!?])\s+", t)
    stuecke, cur = [], []
    for s in saetze:
        if cur and woerter(" ".join(cur + [s])) > maxw:
            stuecke.append(" ".join(cur)); cur = []
        cur.append(s)
    if cur:
        stuecke.append(" ".join(cur))
    out = []
    for s in stuecke:                       # einzelne Riesensaetze hart teilen
        w = s.split()
        for i in range(0, len(w), maxw):
            out.append(" ".join(w[i:i + maxw]))
    return out


def abschnitte_bilden(blocks, seitentitel):
    """blocks: [(art, text)] -> [(ueberschrift, text)]. Packt Absaetze bis ZIEL_W, trennt bevorzugt an Ueberschriften."""
    einheiten, h = [], None                 # (ueberschrift, text, beginnt_neue_ueberschrift)
    neu = False
    for art, t in blocks:
        if art in HEAD:
            h = t; neu = True
            continue
        for st in (saetze_teilen(t, ZIEL_W) if woerter(t) > ZIEL_W else [t]):
            einheiten.append((h, st, neu)); neu = False
    out, cur_h, cur, cur_w = [], None, [], 0
    for h, t, neu in einheiten:
        w = woerter(t)
        if cur and ((cur_w >= MIN_W and (neu or cur_w + w > ZIEL_W)) or cur_w + w > MAX_W):
            out.append([cur_h, " ".join(cur)]); cur, cur_w = [], 0
        if not cur:
            cur_h = h
        cur.append(t); cur_w += w
    if cur:
        if out and cur_w < MIN_W // 2 and woerter(out[-1][1]) + cur_w <= MAX_W + 50:
            out[-1][1] += " " + " ".join(cur)
        else:
            out.append([cur_h, " ".join(cur)])
    return [(hh or seitentitel, tt) for hh, tt in out]


def main():
    seiten_dir, index_pfad, aus = sys.argv[1], sys.argv[2], sys.argv[3]
    os.makedirs(aus, exist_ok=True)
    t0 = time.time()
    zeilen = open(index_pfad, encoding="utf-8").read().splitlines()
    kopf = zeilen[0].split("\t")
    seiten = [dict(zip(kopf, z.split("\t"))) for z in zeilen[1:] if z.strip()]
    alle, stat_seiten = [], []
    gesehen_seite, gesehen_text = {}, {}      # Dubletten: gleiche Datei (sha256) bzw. gleicher Abschnittstext
    dup_abschnitte = 0
    for s in seiten:
        if s.get("status") != "ok":
            stat_seiten.append({"nr": s["nr"], "url": s["url"], "status": s.get("status"), "abschnitte": 0, "woerter": 0})
            continue
        if s.get("sha256") in gesehen_seite:
            stat_seiten.append({"nr": s["nr"], "url": s["url"], "status": "dublette-von-" + gesehen_seite[s["sha256"]], "abschnitte": 0, "woerter": 0})
            continue
        gesehen_seite[s.get("sha256")] = s["nr"]
        pfad = os.path.join(seiten_dir, os.path.basename(s["datei"]))
        roh = open(pfad, "rb").read().decode("utf-8", errors="replace")
        p = Leser(); p.feed(roh); p.flush()
        blocks = [(a, t) for a, t, m in p.blocks if (m or not p.main_gesehen)]
        titel = re.sub(r"\s+", " ", p.titel).strip() or s["url"]
        absch = abschnitte_bilden(blocks, titel)
        n_ok = 0; w_sum = 0
        for k, (h, t) in enumerate(absch, start=1):
            w = woerter(t)
            if w < MIN_ABSCHNITT_W:
                continue
            if t in gesehen_text:
                dup_abschnitte += 1
                continue
            gesehen_text[t] = s["nr"]
            n_ok += 1; w_sum += w
            alle.append({"id": f"{s['nr']}-{n_ok:02d}", "seite": s["nr"], "url": s["url"], "titel": titel,
                         "ueberschrift": h, "woerter": w, "text": t,
                         "zustand": f"Page: {titel}\nSection: {h}\n\n{t}"})
        stat_seiten.append({"nr": s["nr"], "url": s["url"], "status": "ok", "abschnitte": n_ok, "woerter": w_sum})
    with open(os.path.join(aus, "abschnitte.jsonl"), "w", encoding="utf-8") as f:
        for a in alle:
            f.write(json.dumps(a, ensure_ascii=False) + "\n")
    ids = sorted(a["id"] for a in alle)
    stich = sorted(random.Random(SEED).sample(ids, min(N_STICHPROBE, len(ids))))
    nach_id = {a["id"]: a for a in alle}
    with open(os.path.join(aus, "gegenprobe-stichprobe.jsonl"), "w", encoding="utf-8") as f:
        for i in stich:
            a = nach_id[i]
            f.write(json.dumps({k: a[k] for k in ("id", "url", "titel", "ueberschrift", "woerter", "text")}, ensure_ascii=False) + "\n")
    open(os.path.join(aus, "gegenprobe-ids.txt"), "w").write("\n".join(stich) + "\n")
    ws = sorted(a["woerter"] for a in alle)
    bereich = {}
    for a in alle:
        b = re.sub(r"^https://www\.wolframphysics\.org/([^/?]*).*$", r"\1", a["url"]) or "(start)"
        bereich[b] = bereich.get(b, 0) + 1
    stat = {"seiten_im_index": len(seiten), "seiten_ok": sum(1 for s in seiten if s.get("status") == "ok"),
            "seiten_mit_abschnitten": sum(1 for s in stat_seiten if s["abschnitte"] > 0),
            "seiten_dubletten": sum(1 for s in stat_seiten if str(s["status"]).startswith("dublette")),
            "abschnitt_dubletten_verworfen": dup_abschnitte,
            "abschnitte": len(alle), "woerter_gesamt": sum(ws),
            "woerter_je_abschnitt": {"min": ws[0] if ws else 0, "median": ws[len(ws) // 2] if ws else 0, "max": ws[-1] if ws else 0,
                                      "unter_300": sum(1 for w in ws if w < 300), "300_bis_600": sum(1 for w in ws if 300 <= w <= 600),
                                      "ueber_600": sum(1 for w in ws if w > 600)},
            "abschnitte_je_bereich": dict(sorted(bereich.items(), key=lambda x: -x[1])),
            "stichprobe": {"seed": SEED, "n": len(stich), "ids": stich},
            "parameter": {"MIN_W": MIN_W, "ZIEL_W": ZIEL_W, "MAX_W": MAX_W, "MIN_ABSCHNITT_W": MIN_ABSCHNITT_W},
            "laufzeit_s": round(time.time() - t0, 2), "seiten": stat_seiten}
    json.dump(stat, open(os.path.join(aus, "aufbereitung-statistik.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(json.dumps({k: v for k, v in stat.items() if k != "seiten"}, ensure_ascii=False))


if __name__ == "__main__":
    main()
