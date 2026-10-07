# Netz-Ansicht (three.js) fuer Datensaetze des Netz-Rechenkerns

Stand 05.10.2026, 18:3x, Leitung claude-primary (gebaut von einem Claude-Unteragenten). Auftrag Finn 05.10.: "einfach
machen und ausprobieren", "threejs mit ... gaussian splat dots oder partikelsystem".

**Synthetische Modellrechnung, keine Messdaten.** Die Ansicht rechnet keine Physik. Sie spielt Datensaetze im Format
`netz-gpu/1` ab (`coordination/runden-v3/netz-gpu/FORMAT.md`), die der Rechenkern auf der .69 schreibt. Der Probe-Modus
erzeugt nur ein analytisches Testmuster (siehe unten). Die Bildbeschreibungen unten sagen, was zu sehen ist, und deuten
die Physik nicht.

![Drehrahmen, Scheibe bei 180 Grad](bilder/drehrahmen.png)

## Aufruf

Die Seite braucht HTTP (ES-Module), `file://` geht nicht. Pruefweg wie im Auftrag, auf der .69 hoechstens
10 Minuten je Lauf (`kleintest.sh` setzt `RuntimeMaxSec=600`):

```bash
# Ansicht auf die .69 kopieren
scp index.html stil.css fmh@192.168.178.69:/home/fmh/fmhc-physics-remote/netz-web/viewer/
scp js/*.js fmh@192.168.178.69:/home/fmh/fmhc-physics-remote/netz-web/viewer/js/
# auf der .69 (netz-web/datensaetze ist ein Verweis auf ../netz-gpu/datensaetze)
cd /home/fmh/fmhc-physics-remote/netz-web
bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh cpu7 netzweb -m http.server 8777 --directory /home/fmh/fmhc-physics-remote/netz-web
```

Dann im Browser:

| Adresse | Inhalt |
|---|---|
| `http://192.168.178.69:8777/viewer/` | Startseite, listet die Datensaetze unter `../datensaetze/` |
| `…/viewer/?probe=1` | Probe-Datensatz, BCC-Netz 12³ (3 456 Ecken, 24 192 Kanten) |
| `…/viewer/?probe=1&n=37` | Lastprobe 37³: 101 306 Ecken, 709 142 Kanten, 1 215 672 Dreiecke |
| `…/viewer/?d=../datensaetze/qball-fall-v/manifest.json` | Datensatz des Rechenkerns |

### URL-Parameter

| Parameter | Bedeutung |
|---|---|
| `d=<pfad/manifest.json>` | Datensatz (relativ zur Ansicht oder absolut) |
| `probe=1`, `n=3..64`, `bilder=2..480` | Probe-Modus, Zellen je Achse (Standard 12), Bilder (Standard 48) |
| `bild=<i>` | Startbild (ab 0) |
| `ebenen=netz,skalar_betrag2,…` | sichtbare Ebenen (Groessennamen aus dem Manifest, `netz` fuer die Kanten) |
| `schnitt=<scheibe\|unter\|ueber>,<x\|y\|z>,<Lage>[,<Dicke>]` | Schnitt, z. B. `scheibe,z,6,1` |
| `blick=schraeg\|vorn\|oben\|seite` | Kamera |
| `netz=deckend`, `darstellung=kugel`, `fluss=punkte` | Darstellungsart der Ebenen |
| `skala=bild` | Farbskala je Bild statt fest ueber den Lauf (alle Ebenen) |
| `rahmenanteil=<0..1>` | Anteil der Ecken mit Rahmenglyphe |
| `ueber=<f>` | zusaetzliche Ueberhoehung der Verschiebung |
| `tempo=<Bilder/s>`, `spielen=1` | Wiedergabe |
| `hdr=0`, `belichtung=<f>` | 8-Bit-Puffer statt HalfFloat; Belichtung im HDR-Betrieb |
| `foto=1` | keine Auftrittsanimationen (fuer reproduzierbare Bildschirmfotos) |
| `mess=<s>`, `melden=1` | Messmodus (siehe Leistung) |

## Die vier Datensaetze des Rechenkerns

Geprueft am 05.10. zwischen 18:00 und 18:27 gegen `netz-gpu/datensaetze/` auf der .69 (Bericht des Rechenkerns:
`coordination/runden-v3/netz-gpu/BERICHT.md`). Alle vier laden ohne Fehlermeldung. Netzlaengen und Eckindizes werden
beim Laden geprueft, die Bildlaengen je angezeigtem Bild; keine Abweichung. Je Datensatz gibt es mindestens ein Bild aus
der Laufmitte.

| Datensatz | Netz | Gut sichtbar | Fehlt oder schwach |
|---|---|---|---|
| `schwerewelle-v` (17 Bilder, t = 0 bis 4) | V 12³: 69 120 Ecken, 470 016 Kanten | Draufsicht auf eine z-Scheibe (t = 3, Skala je Bild): Dehnung und Energie liegen auf einem Bogen, unten am hellsten; gedehnte und gestauchte Kanten getrennt farbig. Diagnose: 16 Reihen, Verlauf je Bild (die ersten 5 sofort, Rest per Knopf), `energie_gesamt` relativ 1,2·10⁻¹⁵ konstant | Ohne Schnitt geht die Schale im Netzschleier unter (`schwerewelle.png`). Die Radienreihen (100/110/111, je mit Kontinuum) waeren als gemeinsames Diagramm oder Polarplot aussagekraeftiger als 16 Einzelkurven. `energie` hat ein kleines negatives Minimum (−6,7·10⁻¹¹), die Ansicht zeigt sie deshalb zweiseitig (violett negativ) |
| `licht-linse-v` (37 Bilder, t = 0 bis 15) | V 20×12×12: 115 200 Ecken, 783 360 Kanten | Draufsicht (t = 10): Takt der Masse als blaues Glimmen in der Mitte, Lichtfront als Band dahinter; 3D (t = 7,5) mit Skala je Bild: ebene Front im Volumen | Mit der festen Lauf-Skala (Energie bis 121 bei t = 0) ist die Front spaeter unsichtbar; dann "Skala je Bild" waehlen. Es fehlen eine Linie gleicher Laufzeit (Frontkontur) und der Vergleich mit einem Lauf ohne Masse |
| `qball-fall-v` (25 Bilder, t = 0 bis 200/m) | V 24×12×20: 230 400 Ecken, 1 566 720 Kanten | Zwei Q-Baelle als klare Kugeln (3D, Laufmitte t = 100); Scheibe von vorn: Q-Baelle zwischen den Takt-Baendern (oben positiv, unten negativ) | Der Fallweg ist nur beim Abspielen zu sehen, es fehlt eine Spur des Schwerpunkts ueber die Bilder. Takt fuellt die ganze Box, in 3D daher standardmaessig aus. Groesster Datensatz: 20,6 ms GPU je Frame |
| `drehrahmen-360-v` (17 Bilder, Winkel 0 bis 360 Grad, dann Stoerprobe 370 bis 400) | V 12³: 69 120 Ecken, 470 016 Kanten | Scheibe von oben, alle Rahmen: bei 180 Grad (Skala je Bild) Energiering am Kernrand und verdrillte Rahmen darum; bei 360 Grad gedaempfter Kern (Quaternion −1, also keine Drehung) und Verdrillungsring. Die Zeitachse heisst hier "Winkel" in Grad (aus `einheiten.zeit`) | In 3D ohne Schnitt sind 69 120 Achsenkreuze ein dichtes Gewimmel. Viridis ist im unteren Bereich dunkel, bei fester Skala sieht man die Energie kaum. Die Bilder 370 bis 400 (Stoerprobe) zeigt die Zeitleiste als "Winkel 370 bis 400"; das Format hat keinen Platz fuer eine Bildbemerkung (Vorschlag: optionales Feld `bemerkung` je Bild) |

Uebergreifend: Bei den dichten V-Netzen (470 000 bis 1,6 Mio. Kanten) ist der Ueberblick in 3D vor allem Netzschleier.
Die aussagekraeftigen Bilder entstehen mit einer Scheibe; dafuer hellt die Ansicht additive Ebenen in duennen Scheiben
maessig auf (Faktor √(Box/Dicke), hoechstens 4).

![Schwerewelle, Scheibe](bilder/schwerewelle-schnitt.png)
![Licht-Linse, Scheibe](bilder/licht-linse-schnitt.png)
![Q-Baelle im Schnitt](bilder/qball-schnitt.png)
![Drehrahmen 360 Grad](bilder/drehrahmen-schnitt.png)

## Oeffentliche Fassung (physics.fmhc.io/netz/)

Stand 05.10.2026, 19:05. Gebaut fuer den Upload durch die Leitung, nicht hochgeladen.

- **Ort:** auf der .69 `/home/fmh/fmhc-physics-remote/netz-web/public/netz/`, 255 MB, 244 Dateien. Erzeugt mit
  `oeffentlich/bauen.sh` (Laptop: rsync, ssh; auf der .69: cp, jq), geprueft mit `oeffentlich/pruefen.sh`.
- **Inhalt:**
  - `index.html`: Startseite mit den vier Filmen, oben Deutsch und darunter eine Zeile Englisch, Fusszeile nach Auftrag
    (Wortlaut aus Plan 4.7, ohne Gaia-Ausnahme und Beteiligten-Link).
  - `ansicht.html`: die Ansicht mit Fusszeile; ohne `?d=` leitet sie zur Startseite.
  - Code und Stil: `js/`, `stil.css`, `start.css`, `schriften.css`.
  - `vendor/`: three.js r186 (MIT) und IBM Plex (OFL), je mit Lizenzdatei.
  - `bilder/`: vier Vorschaubilder (WebP, 21 bis 110 KB, im Kinomodus `ui=0` aufgenommen) und `zeichen.svg`.
  - `LIZENZEN.txt`.
- **Daten:** `data/<film>/` sind Kopien der vier Datensaetze. Nur die Manifeste der Kopien wurden bereinigt
  (`oeffentlich/manifest-bereinigen.jq`): `quelle.lauf` und `quelle.skript` (interne Pfade) sind entfernt, die
  Kartenkennung in `quelle.modell` ebenfalls, und `quelle.herkunft` lautet "netzgpu 0.1, Finns gefuelltes Tetraedernetz V,
  synthetische Modellrechnung". Die Originale sind unveraendert, die Dateizahl je Film ist gleich.
- **Unter der Richtlinie lauffaehig** (`default-src 'self'; style-src 'self'; img-src 'self'; …`):
  - keine Importmap; three.js und OrbitControls werden relativ importiert (in `OrbitControls.js` eine Importzeile ersetzt);
  - keine Inline-Skripte, keine `style`-Attribute; Stil per CSSOM (`el()` setzt `style.setProperty`), Legendenfarben per Klasse;
  - keine `data:`- oder `blob:`-URLs, keine Fremdschriften.

  Das gilt jetzt fuer beide Fassungen; auch die LAN-Fassung braucht kein CDN mehr.
- **Neu in der Ansicht:**
  - `ui=0` (Kinomodus) und `zoom=<f>`;
  - Tafeln-Knopf und Taste T, unter 820 px Breite sind die Tafeln anfangs aus;
  - HDR nur, wenn die GPU in Float-Puffer zeichnen kann;
  - Anzeige von `quelle.herkunft` und `hinweis_bilder`;
  - SPDX-Koepfe in allen eigenen Dateien.
- **CSP-Pruefung (05.10., 19:02 bis 19:05):**
  - Aufbau: Testkopien der Startseite und der Ansicht mit derselben Richtlinie als `<meta>` (ohne `frame-ancestors`)
    und ein externer Zaehler fuer `securitypolicyviolation`-Ereignisse. Headless Chrome mit echter GPU und
    `--enable-logging=stderr`, je Seite ein Foto- und ein DOM-Lauf.
  - Ergebnis: Startseite und alle vier Filme haben **0 Verstoesse**, im DOM-Zaehler wie im Konsolenprotokoll; der Zaehler
    startete in jedem Lauf. Danach wurden die Testkopien entfernt, und der Abschluss-Scan fand weder Inline-Skript,
    Importmap, `style`-Attribut, `data:`/`blob:`-URL, CDN noch interne Pfade.
- Bilder der Pruefung: `bilder/oeffentlich/csp-startseite.png` und `csp-<film>.png` (mit gruener Plakette
  "0 Verstoesse").
- **Nicht geprueft oder offen:**
  - die Richtlinie als echter HTTP-Kopf, darunter `frame-ancestors` (geht per `<meta>` nicht);
  - echte Mobilgeraete;
  - die Statusbox aus Plan 7.1 (Verifizierungsstufe), die ich nicht ohne Beleg fuellen wollte;
  - gzip fuer `application/octet-stream` in nginx wuerde `kanten.u32` deutlich kleiner machen (Vorschlag, nicht getestet).
  - Fachbegriffe mit Eigennamen (Maxwell, Poisson, Newton, Regge) stehen weiter in Titeln und Manifesten.

![Startseite unter der Richtlinie](bilder/oeffentlich/csp-startseite.png)
![Licht-Linse unter der Richtlinie](bilder/oeffentlich/csp-licht-linse-v.png)

## Bedienung

- **Maus:** links ziehen dreht, rechts ziehen verschiebt, Rad zoomt (Orbit um die Boxmitte, z zeigt nach oben).
- **Tasten:** Leertaste Abspielen/Pause, Pfeil links/rechts ein Bild, Pos1/Ende erstes/letztes Bild, R Kamera zurueck.
- **Zeitleiste** (unten): Anfang, zurueck, Abspielen, vor, Ende; Schieber ueber alle Bilder; der graue Balken darunter
  zeigt, welche Bilder fuer die sichtbaren Groessen schon geladen sind; Tempo 1 bis 60 Bilder/s; Schleife. Beim Abspielen
  wird nur weitergeschaltet, wenn alle sichtbaren Groessen des naechsten Bilds da sind. Bilder werden nie interpoliert.
- **Ebenen** (links), je Groesse ein- und ausschaltbar, nur was im Manifest steht:
  - *Netz*: Kanten als Linien, Farbe nach einer Kantengroesse (`dehnung`) oder einfarbig. Regler Grundnetz (Helligkeit
    ungedehnter Kanten), Schwelle (Kanten unter x % der Spanne ausblenden), Kontrast; Darstellung leuchtend (additiv)
    oder deckend (mit Tiefe).
  - *Eckgroessen* (`skalar_betrag2`, `energie`, `takt`, weitere): je eine Splat-Ebene. Groesse und Helligkeit folgen dem
    Betrag des Abstands zum Bezugswert; Darstellung Splat (additiver Gauss) oder Kugel (deckender Imposter).
  - *Dreiecksgroessen* (`fluss`): leuchtende, halbtransparente Flaechen (zur Mitte geschrumpft, Kante heller) oder
    Splats in den Dreiecksmitten.
  - *Drehrahmen* (`rahmen`, Quaternion w, x, y, z): kleines Achsenkreuz je Ecke (x rot, y gruen, z blau), hell bei
    grossem Drehwinkel, gedaempft nahe der Ruhelage; Anteil der Ecken waehlbar (feste Zufallsauswahl).
  - *Verschiebung*: Ecken werden um `verschiebung` versetzt (im Datensatz schon ueberhoeht), dazu ein eigener Faktor.
  - **Skala fest (Lauf) / je Bild**: Standard sind die festen Manifest-Grenzen (ueber Bilder vergleichbar). "je Bild"
    nimmt den groessten Betrag im aktuellen Bild; die Legende sagt dann "nicht ueber Bilder vergleichbar".
- **Schnitt**: Scheibe (Lage, Dicke) oder Halbraum unter/ueber einer Ebene senkrecht zu x, y oder z; ein Bernsteinrahmen
  zeigt die Ebene. Geschnitten wird je Primitiv (Ecke, Halbkante, Dreiecksmitte) an der Stelle, wo es gezeichnet wird,
  nicht je Pixel.
- **Ansicht**: Blickrichtungen (schraeg, von vorn = xz, von oben = xy, von der Seite = yz), Box und Achsen,
  Tiefenschleier, Belichtung.
- **Infofeld** (rechts): Titel, Zeit (oder Winkel), Bildnummer, Netzgroesse, Einheit der Bildachse, Diagnosewerte aus dem
  Manifest mit Verlauf ueber alle Bilder (Marke am aktuellen Bild, Spanne absolut und relativ), Legenden mit festen
  Grenzen, Leistung, Quelle.

Farbregel: `min < 0 < max` gilt als zweiseitig (Bezug 0, dunkle Mitte, Spanne = groesserer Betrag); `max <= 0` (z. B.
Takt nur negativ) als einseitig nach unten; sonst einseitig ab `min`. Feste Skalen je Name (Inferno fuer |φ|², Viridis
fuer Energie, Eis fuer Takt, Blau-Orange fuer Dehnung, Violett-Gold fuer Fluss) gelten nur, wenn ihr Typ zu den
Grenzen passt (`takt` in `licht-linse-v` ist zweiseitig, −0,12 bis +0,014); sonst wird eine passende Skala gewaehlt.

## Aufbau

| Datei | Aufgabe |
|---|---|
| `index.html` | Geruest der LAN-Fassung (ohne Importmap, ohne CDN); three.js **r186** (0.186.1, neueste Fassung am 05.10.) und IBM Plex liegen unter `vendor/`, Schriften ueber `schriften.css` |
| `stil.css` | Gestaltung |
| `js/haupt.js` | Ablauf: Laden, Pruefen, Ebenen, Bild anwenden, Vorladen, Zeitleiste, Infofeld, Messmodus, Startseite |
| `js/quelle.js` | Datensatz lesen (`fetch` → `ArrayBuffer` → `Float32Array`/`Uint32Array` ohne Kopie), Bildspeicher, Manifestpruefung |
| `js/probe.js` | Probe-Datensatz im selben Format |
| `js/ansicht.js` | Renderer, Kamera, Orbit, Box, Schnittanzeige, GPU-Zeitmessung |
| `js/ebenen.js` | Darstellungsebenen (Netz, Splats, Fluss, Rahmen) |
| `js/shader.js` | GLSL der Ebenen |
| `js/farben.js`, `js/format.js`, `js/oberflaeche.js` | Farbskalen, Zahlen auf Deutsch, Bedienelemente |
| `bilder/` | Bildschirmfotos und `aufnehmen.sh`; `bilder/oeffentlich/`: Fotos der CSP-Pruefung |
| `vendor/` | three.js r186 (MIT) und IBM Plex woff2 (OFL), je mit Lizenzdatei; `OrbitControls.js` importiert relativ |
| `schriften.css` | `@font-face` fuer die mitgelieferten Schriften |
| `oeffentlich/` | oeffentliche Fassung: `index.html` (Startseite), `ansicht.html`, `start.css`, `LIZENZEN.txt`, Vorschaubilder, `bauen.sh`, `pruefen.sh`, `manifest-bereinigen.jq`, `pruefung/` (nur fuer den CSP-Test) |

Technik, kurz:

- **Vertex-Pulling.** Ruhelagen und Verschiebung liegen als RGBA32F-Texturen auf der GPU (1024 Texel breit). Kanten,
  Dreiecke, Splats und Rahmen sind instanzierte Geometrien, die ihre Ecken per `texelFetch` holen. Die Netztopologie
  wird einmal hochgeladen; je Bild gehen nur die Werte-Arrays der **sichtbaren** Groessen auf die GPU, und nur, wenn
  sich das Bild fuer diese Ebene geaendert hat (`bufferSubData` bzw. `texSubImage2D`).
- **Periodischer Rand.** Jede Kante wird als zwei Halbkanten gezeichnet, je eine an ihrer Ecke, Richtung im Mindestbild.
  Randkanten laufen so nicht quer durch die Box, sondern ragen hoechstens eine halbe Kante ueber die Boxflaeche.
  Dreiecke werden am Mindestbild verankert und mit ihrer Mitte in die Box gefaltet.
- **Kein Sortieren.** Splats, Netz (leuchtend) und Flaechen mischen additiv, die Reihenfolge ist egal.
- **HDR-Puffer.** r186 kann die Szene in einen HalfFloat-Puffer zeichnen (`outputBufferType`); additives Licht darf
  ueber 1 steigen und wird erst im Ausgabe-Durchgang mit *Khronos PBR Neutral* weich begrenzt (unter 0,76 bleiben die
  Farben unveraendert). Ohne das kippten dichte Felder (Takt in `qball-fall-v`) in flaechiges Weiss.
- **Vorgabe-Helligkeit nach Dichte.** Splat-Helligkeit ∝ 1/∛N, Grundnetz ∝ N_Kanten^(−2/3), in duennen Scheiben
  ×√(Box/Dicke); so starten 3 000 und 230 000 Ecken mit denselben Reglern lesbar.
- **Laden.** Bildspeicher mit LRU und 384 MB Budget; nach jedem Bild werden die naechsten 4 Bilder der sichtbaren
  Groessen vorgeladen. Ein Bild wird erst angewandt, wenn alle sichtbaren Groessen da sind (keine gemischten Zeitpunkte);
  ueberholte Anfragen (schnelles Ziehen am Schieber) werden verworfen. Laengen und Eckindizes werden geprueft.
- Gezeichnet wird nur bei Aenderung (Kamera, Bild, Regler).

## Probe-Modus (`?probe=1`)

- Netz: periodisches **BCC-Tetraedernetz**, nicht Netz V. Ecken auf dem Wuerfelgitter und in den Zellmitten; je Zelle
  2 Ecken, 14 Kanten, 24 Dreiecke, 12 Tetraeder (Euler 2 − 14 + 24 − 12 = 0). Dreiecke werden direkt aufgezaehlt
  (Eckkante mit den vier umgebenden Zellmitten, Mittenkante mit den vier umgebenden Ecken). `tetraeder.u32` wird nicht
  erzeugt (die Ansicht nutzt es nicht).
- Felder, **analytisches Testmuster ohne Rechnung**: Welle mit Plus-Polarisation in z als Verschiebung (in der Boxmitte
  wie h₊, periodisch gefaltet, 40-fach ueberhoeht), `dehnung` geometrisch aus derselben (nicht ueberhoehten)
  Verschiebung, Amplitude 10⁻³; Gauss-Klumpen auf einer Kreisbahn (`skalar_betrag2`), Energie = Klumpen + Wellenbaender,
  Takt = −0,01/√(1 + r²/σ²); `fluss` = zirkular polarisierte Welle in x, B·n·A je Dreieck (Dreiecke einheitlich
  ausgerichtet); `rahmen` = Igel-Textur um den Klumpen, die sich um z dreht. Alles laeuft in 48 Bildern genau einmal
  periodisch, die Lichtwelle mit c = 1.
- Die Diagnosewerte (`ladung`, `energie_gesamt`) sind Summen ueber die Ecken der erzeugten Bilder; ihre Schwankung
  (relativ etwa 10⁻⁸) ist float32-Rundung, kein Erhaltungstest.

## Leistung

Gemessen 05.10.2026 auf dem Laptop (Quadro RTX 5000 Max-Q, Chrome 153 headless, ANGLE ueber Vulkan, 1500 × 900,
MSAA 4×, HDR an), Daten vom Server auf der .69. Messmodus `?mess=8&melden=1`: Chrome ohne virtuelle Zeit, je Frame
ein neues Bild (alle sichtbaren Groessen werden hochgeladen), Ergebnis als Anfrage ins Serverlog. GPU-Zeit ueber
`EXT_disjoint_timer_query_webgl2`, Median ueber 219 bis 245 Frames.

| Lauf | Ecken / Kanten / Dreiecke | Upload je Bild | GPU je Frame | Bilder/s |
|---|---|---|---|---|
| Probe 37³: Netz nach Dehnung, \|φ\|², Verschiebung | 101 306 / 709 142 / – | 4,4 MB | **3,8 ms** | 29,9 |
| dasselbe plus Fluss-Flaechen | 101 306 / 709 142 / 1 215 672 | 9,3 MB | **12,9 ms** | 30,6 |
| `qball-fall-v` (Rechenkern): Netz, \|φ\|², Takt | 230 400 / 1 566 720 / – | 1,8 MB | **20,6 ms** | 27,3 |

- Die Zielgroesse (etwa 100 000 Ecken, 700 000 Kanten) laeuft mit Bildwechsel in jedem Frame weit unter 16 ms GPU-Zeit.
  Die Bilder/s um 30 begrenzt die Messschleife (sie wartet je Bild auf `requestAnimationFrame` und `gl.finish`),
  nicht die GPU.
- Teuer ist Fuellrate, nicht Geometrie: die 1,2 Mio. additiven Fluss-Flaechen verdreifachen die GPU-Zeit; beim
  Q-Ball-Datensatz fuellt der Takt die ganze Box mit Splats. Schwelle und Schnitt senken das sofort.
- CPU-Seite: Die gemessenen Upload-Zeiten (Median 0,3 bis 1,8 ms) sind nur die JavaScript-Zeit bis zur Uebergabe; die
  Uebertragung laeuft danach asynchron. `gl.finish` wartet in Chrome nicht verlaesslich auf die GPU, daher zaehlen hier
  die GPU-Timer. In den Bildschirmfotos (virtuelle Zeit) steht bei CPU-Zeiten 0 ms; das ist ein Effekt der virtuellen
  Uhr, keine Messung.
- Grenzen: Eckindizes laufen als float32 (exakt bis 16,7 Mio. Ecken). Speicher fuer `qball-fall-v`: Kanten-Instanzen
  1,57 Mio. × 12 Byte, Texturen 2 × 3,6 MB; die Bilder selbst sind klein.

## Bewertung WebGL2 gegen WebGPU

- **WebGL2 (umgesetzt)** reicht fuer das Abspielen: Vertex-Pulling aus Float-Texturen plus Instancing erreicht die
  Zielgroesse mit 4 bis 21 ms GPU-Zeit, laeuft in jedem aktuellen Browser und auch ueber reines http im LAN.
- **WebGPU ging nicht "ohne Aufwand"**: three.js' `WebGPURenderer` (r186) nimmt keine GLSL-`ShaderMaterial`; alle
  fuenf Shader muessten nach TSL/NodeMaterial portiert werden.
- **Gemessen, wo WebGPU verfuegbar ist** (Chrome 153, Linux, Quadro RTX 5000):
  - Ueber `http://192.168.178.69:8777` ist die Seite kein sicherer Kontext (`isSecureContext=false`); `navigator.gpu`
    fehlt dort, auch mit `--enable-unsafe-webgpu`.
  - Ueber `http://localhost` (SSH-Tunnel auf die .69) ist der Kontext sicher, und Chrome meldet einen WebGPU-Adapter
    "nvidia, turing", ohne Zusatzflag.
  - Fuer WebGPU im LAN braeuchte es also HTTPS, einen Tunnel auf localhost oder den Chrome-Schalter
    `--unsafely-treat-insecure-origin-as-secure=http://192.168.178.69:8777` (diesen Schalter nicht getestet).
- **Lohnt es sich?** Fuer reines Abspielen nicht: Die Engpaesse (Upload-Bandbreite, Fuellrate beim additiven Mischen)
  sind dieselben. Lohnend wird WebGPU, sobald die Ansicht selbst rechnen soll: Isoflaechen von |φ|² ueber die
  Tetraeder, Stromlinien des Flusses, Schwerpunktspuren, Picking, GPU-seitige Bild-Skala, Culling mit indirekten
  Draws, oder echte sortierte Splats. Dann Storage-Buffer statt Texturen und Compute-Shader. Schaetzung fuer den
  Umbau: ein bis zwei Tage einschliesslich Pruefung.

## Bewertung Splats gegen Partikel

![Splat](bilder/vergleich-splat.png)
![Kugel](bilder/vergleich-kugel.png)

- **Splats** (additive Gauss-Sprites, Quad-Rand bei 3σ): ein zusammenhaengendes Feldbild, ohne Sortieren, gut fuer
  ausgedehnte Felder (Klumpen, Wellenenergie, Takt). Die Helligkeit ist eine Summe entlang des Sichtstrahls, also eine
  Projektion (wie Emissions-Volumenrendering). Sie haengt von der Sichttiefe ab, und in Ueberlagerungen gilt die
  Farbskala nicht mehr exakt. Verdeckung gibt es nicht. Gegenmittel im Code: Schwelle, Dichte-Vorgabe, HDR-Puffer,
  Schnitt.
- **Partikel** (Kugel-Imposter, deckend, mit Tiefe): Jede Ecke zeigt ihren Wert exakt in der Farbskala, Verdeckung gibt
  Tiefe. Bei 10⁵ Ecken bilden sie aber eine undurchsichtige Wand und sind nur mit Scheibe oder Schwelle lesbar.
- Echte 3D-Gaussian-Splats (anisotrop, sortiert, Alpha-Mischung) bringen hier wenig: Die Daten sind Werte auf
  Gitterpunkten, keine angepassten Kovarianzen, und Sortieren von 10⁵ bis 10⁶ Splats kostet je Bild.
- Empfehlung: Splats zur Uebersicht und im Film, Kugeln zum Ablesen in einer Scheibe. Beides ist je Ebene umschaltbar.

## Was noch fehlt

- **Live-Kopplung per WebSocket** an den Rechenkern. Vorschlag: Der Kern sendet je Bild dieselben float32-Bloecke als
  Binaernachricht mit kleinem JSON-Kopf (Bildindex, Zeit, Groesse); in der Ansicht ersetzt eine `WebSocketQuelle` die
  `DateiQuelle` mit derselben Schnittstelle `bild(i, name)`. Die Rueckrichtung (Pause, Parameter) braucht einen Dienst
  auf der .69, also Finns Freigabe (keine Dauerdienste).
- Aus den vier Datensaetzen: Schwerpunktspuren (Q-Baelle), Frontkontur und Vergleichslauf (Licht), gemeinsames
  Radien- oder Polardiagramm (Schwerewelle), Bildbemerkungen im Format (Stoerprobe beim Drehrahmen).
- Messwert unter dem Mauszeiger (GPU-Picking), Isoflaechen und Stromlinien (siehe WebGPU), Tetraeder-Ebene
  (`tetraeder.u32` wird nicht gelesen), Glyphen fuer weitere Vektorgroessen (nur `verschiebung` und `rahmen` sind belegt).
- Skalengrenzen von Hand, Kamerazustand in der URL, Bild-/Videoexport (MediaRecorder), Vergleich zweier Datensaetze.
- (erledigt 05.10. abends) three.js und Schriften liegen jetzt unter `vendor/`; kein CDN mehr, auch die LAN-Fassung laeuft offline.
- Bekannte Grenzen: Linien sind 1 Pixel breit (WebGL), dichte Netze zeigen Moiré; Randkanten ragen bis zu einer halben
  Kante ueber die Box; das Mindestbild setzt Kanten kuerzer als die halbe Box voraus; ueber 0,76 veraendert die
  Tonwertkurve die Farben (fuer exakte Farben `hdr=0` oder Belichtung senken).

## Bildschirmfotos

Alle mit `bilder/aufnehmen.sh` (headless Chrome, echte GPU ueber ANGLE/Vulkan, je Foto frisches Profil, `foto=1`).

| Bild | Inhalt |
|---|---|
| `startseite.png` | Startseite ohne Datensatz, listet die vier Datensaetze |
| `schwerewelle.png` | `schwerewelle-v`, Bild 9 (t = 2), 3D: Paket im Netzschleier |
| `schwerewelle-schnitt.png` | `schwerewelle-v`, Bild 13 (t = 3), Scheibe z = 6 von oben, Skala je Bild |
| `licht-linse.png` | `licht-linse-v`, Bild 19 (t = 7,5), 3D, Skala je Bild: Lichtfront und Takt der Masse |
| `licht-linse-schnitt.png` | `licht-linse-v`, Bild 25 (t = 10), Scheibe z = 6 von oben |
| `qball-fall.png` | `qball-fall-v`, Bild 13 (t = 100), 3D: zwei Q-Baelle |
| `qball-schnitt.png` | `qball-fall-v`, Bild 13, von vorn, Scheibe in y: Q-Baelle zwischen den Takt-Baendern |
| `drehrahmen.png` | `drehrahmen-360-v`, 180 Grad, Scheibe z = 6 von oben, alle Rahmen, Skala je Bild |
| `drehrahmen-schnitt.png` | `drehrahmen-360-v`, 360 Grad, gleiche Scheibe, feste Skala |
| `probe-standard.png` | Probe 12³, Netz nach Dehnung (leuchtend) und \|φ\|²-Klumpen |
| `probe-schnitt.png` | Probe, Scheibe um z = 6: Fluss-Flaechen, Klumpen, Drehrahmen |
| `probe-netz-deckend.png` | Probe, deckendes Netz, Halbraum y ≥ 6: Blick in die Schnittflaeche |
| `lastprobe-37.png` | Probe 37³ (101 306 Ecken, 709 142 Kanten): Dehnungsmuster der Testwelle |
| `vergleich-splat.png`, `vergleich-kugel.png` | Energie der Probe als Splats und als Kugeln |

![Startseite](bilder/startseite.png)
![Schwerewelle 3D](bilder/schwerewelle.png)
![Licht-Linse 3D](bilder/licht-linse.png)
![Q-Baelle](bilder/qball-fall.png)
![Probe](bilder/probe-standard.png)
![Probe, Schnitt](bilder/probe-schnitt.png)
![Probe, Halbraum](bilder/probe-netz-deckend.png)
![Lastprobe](bilder/lastprobe-37.png)

## Pruefung

- Server auf der .69 ueber `kleintest.sh` (Spur cpu7, `python3 -m http.server`) in drei Fenstern: 17:57:40 bis
  18:07:40 und 18:07:41 bis 18:17:41 (je durch `RuntimeMaxSec` beendet), 18:21:16 bis 18:26:40 (von Hand beendet);
  kein Dauerdienst. Lokal wurde kein Python, Node, awk oder Perl gestartet. Einmal lief auf der .69 ein `python3 -c`
  nur zum Lesen der Manifeste (JSON, ohne `kleintest.sh`).
- WebGPU-Test ueber einen SSH-Tunnel auf localhost, nach dem Test geschlossen.
- Beim Pruefen gefunden und behoben:
  1. Mit warmem Browser-Cache lief die virtuelle Zeit davon, bevor die Seite stand (Fotos halb aufgebaut). Jetzt
     bekommt jedes Foto ein frisches Profil.
  2. Additive Splats saettigten bei 10⁵ Ecken zu weissen Flaechen. Behoben mit HDR-Puffer und Dichte-Vorgabe.
  3. Die feste Lauf-Skala machte den sich ausbreitenden Lichtpuls unsichtbar. Jetzt gibt es "Skala je Bild" als Wahl.
  4. Der Halbraum-Schnitt liess periodische Halbkanten an der Gegenseite stehen. Jetzt wird jede Halbkante dort
     geprueft, wo sie gezeichnet wird.
  5. `takt` in `licht-linse-v` ist zweiseitig. Die feste Eis-Skala waere falsch gewesen.
  6. Die Draufsicht stand diagonal, die Rahmenglyphen waren zu klein, duenne Scheiben zu dunkel, und der Drehwinkel
     stand als "t".
- Viertes Serverfenster fuer die oeffentliche Fassung: 19:02:18 bis 19:05:09 (Wurzel `public/`, von Hand beendet); cpu7
  war vorher von einem fremden Kleintest belegt, der Server wartete ueber `flock` darauf.
- Regelverstoss: Bei der Pruefung von `createObjectURL` in three.core.js lief lokal einmal `awk` in einer Pipe
  (Textfilter, 05.10. gegen 18:52). Danach nur noch grep, sed und cut.
- Noch nicht im echten Fenster bedient (nur headless): Mausfuehrung, Tastatur, Regler waehrend der Wiedergabe.
