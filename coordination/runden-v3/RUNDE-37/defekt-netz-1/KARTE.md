# DEFEKT-NETZ-1: Laufen Schwerewellen auf den Frank-Kasper-Kristallen C15 und A15 gleichmaessiger als auf Finns Netz V? (Runde 47, Kristall-Zweig von Finns Weiche)

- Leitung claude-primary. Karte geschrieben ab 2026-10-05 07:41:03 CEST (date), vor jeder Rechnung.
- **Herkunft:** Kartenvorschlag aus WELTKRISTALL-L (RUNDE-37/weltkristall-l/DOSSIER.md, Abschnitt 6), geschrieben vor jeder Rechnung. Frage, Netze, DN0 bis DN3 und die Bedeutung sind von dort **woertlich bindend**.
- **Finns Weiche (05.10.):** "Kristall/Glas: beide Zweige testen".
  - Den Glas-Zweig decken TT-GLAS-1 und TT-GLAS-2 ab [P].
  - Den Kristall-Zweig deckte bisher nur V ab (Spanne 6,34 %, TT-ISO-1 [P]).
- **Warum C15:** Er ist der Kristall, den die 600-Zelle im flachen Raum vorschlaegt.
  - Seine Defektlinien (Kanten mit 6 Tetraedern) bilden ein Diamantgitter (Doye/Wales 2001 [S]).
  - Sein Cu-Teilgitter ist ein Pyrochlor [L].
  - Finns Diamant- bzw. Pyrochlor-Netz ist damit das Defektgeruest dieses Kristalls.
- Kennzeichen: [M], [E], [P], [S], [L], [H].

## Netze (woertlich aus dem Vorschlag)

- C15 (MgCu2-Typ, 24 Atome je kubischer Zelle) und A15 (Cr3Si-Typ, 8 Atome), Ideallagen ohne freie Parameter.
- Die Wyckoff-Lagen vor dem Bau an einer Kristallographie-Quelle lesen; bisher nur [L].
- Tetraedrisierung per Delaunay mit demselben Code wie TT-GLAS-1.

## Vorhersagen (woertlich aus WELTKRISTALL-L, vor jeder Rechnung)

| Nr | Vorhersage | Art | Wahrsch. |
|---|---|---|---|
| DN0 | Kontrolle: Delaunay gibt nur Tetraeder; jede Kante traegt 5 oder 6; q = 5,1000 (C15) und 46/9 = 5,1111 (A15) auf 1e-9; die 6er-Kanten von C15 bilden ein Diamantnetz | Kontrolle, vorab ableitbar | 85 % |
| DN1 | Spanne s(C15) < s(V) = 6,34 % | [H] | 55 % |
| DN2 | s(C15) < s(A15) | [H] | 55 % |
| DN3 | s(C15) < 3 % | [H] | 30 % |

**Bedeutung (woertlich, gekuerzt):**
- **DN1 und DN2 treffen ein:** Ikosaedrische Nahordnung, also die 600-Zellen-Mitte, ist im Kristall-Zweig der Weg zur TT-Isotropie.
  - Begruendung [M]: Die Ikosaedergruppe hat Invarianten erst bei l = 0, 6, 10 usw., also keine bei l = 4.
  - C15 hat 2/3 Ikosaederplaetze, A15 nur 1/4.
- **DN1 scheitert:** Die kubische l = 4-Anisotropie dominiert unabhaengig von der Nahordnung. Die 600-Zellen-Bruecke bringt fuer TT keinen Vorteil.
- **DN0 scheitert:** Delaunay ist entartet (kosphaerische Punkte). Dann die FK-Tetraeder zuerst aus der Kristallographie statt per Delaunay bauen.

## Ableitbarkeitsprobe der Leitung (07:30, RUNDE-47.md)

- **C15 je kubischer Zelle:**
  - 16 Z12- und 8 Z16-Plaetze, also (192 + 128)/2 = 160 Kanten.
  - Die 6er-Kanten sind die Mg-Mg-Bindungen: 8 x 4/2 = 16.
  - Damit 816/6 = 136 Tetraeder, q = 816/160 = 5,1000 und f6 = 10 %. Die 6er-Kanten bilden das Diamantgitter der Mg [M, L].
- **A15:** 2 Z12- und 6 Z14-Plaetze, also 54 Kanten mit 6 Kettenkanten. Damit q = 276/54 = 46/9 = 5,1111 [M, L].
- **Urteil:**
  - DN0 ist vorab ableitbar und nur Kontrolle.
  - DN1 bis DN3 sind nicht ableitbar: Kubisch bleibt ein freier l = 4-Koeffizient, dessen Wert an den verzerrten Kantenlaengen haengt. Sie koennen scheitern und bestehen.

## Zusatz der Leitung (nicht aus dem Vorschlag; Grund: DANZER-NAEHERUNG-1, Ergebnis 07:40)

- **Lehre aus DANZER-NAEHERUNG-1 [P]:**
  - Zufaellig aufgeloeste Delaunay-Gleichstaende erzeugten dort eine glasartige Richtungsabhaengigkeit von 1 bis 7 %, schon im Grundtempo, die die kubische Symmetrie bricht.
  - Ursache waren Einheitsgewichte auf Kanten mit *1 = 0.
- **Darum:**
  1. Gleichstaende (5 oder mehr Punkte auf einer Kugel) vor dem Bau zaehlen und melden.
  2. Gibt es Gleichstaende, sie nicht per Zitter aufloesen. Dann die FK-Tetraeder aus der Kristallographie bauen, wie es der Fehlerzweig von DN0 vorsieht.
  3. Pruefen, dass das gebaute Netz die volle kubische Symmetrie behaelt. Das Grundtempo muss isotrop sein (Kontrolle, vorab ableitbar).
- Die Spanne wird genauso gemessen wie in TT-ISO-1 fuer V (mindestens 13 Richtungen), damit s(V) = 6,34 % vergleichbar ist. Stabilitaet bei kleinem k und Zahl masseloser TT-Moden kommen mit in den Bericht.

## Rahmen

- Code-Agent. Code aus tt-glas-1/code und tt-iso-1/code kopieren, dort nichts aendern.
- Laeufe nur auf der .69 ueber kleintest.sh, Spuren cpu3 und cpu4 (TAKT-UMKLAPP-1 hat Vorrang bei geteilten Locks). Je Lauf hoechstens 10 min, ein Thread. Zeitbox 120 min.
- Plan und Code vor den Hauptlaeufen einfrieren (sha256).
- Synthetisch, keine Messdatenbestaetigung.
