# QCA-WINDUNG-1: Traegt der Takt unserer Automaten eine Haendigkeit (Windungszahl W3)? (Runde 41)

- Leitung claude-primary. Karte, Rohdatenprobe und Wahrscheinlichkeiten geschrieben ab 2026-10-04 15:06:04 CEST (date),
  vor jeder Rechnung.
- **Herkunft:**
  - Kartenvorschlag aus CHIRAL-L (RUNDE-37/chiral-l/DOSSIER.md, V4 und Abschn. 7; ARBEITSFELD Abschn. 2b und Z. 335-340).
  - Finns Frage (04.10., Nachricht zwischen 14:55 und 15:03, woertlich): "kann es sein das linksdrehende bzw
    rechtsdrehende teilchen so sind weil deren takt falsch rum geht?"
  - Antwort der Leitung im Chat und im Protokoll von RUNDE-41.md, Eintrag 15:03:39.
- **Worum es geht:**
  - Auf Gittern ohne Takt kommen Fermionen in Links-rechts-Paaren (Nielsen/Ninomiya).
  - Mit diskretem Takt (QCA, Floquet) kann der Einschritt-Operator U(k) selbst gewunden sein. Die Windungszahl ist
    W3 = (1/24 pi^2) Int d^3k eps^ijk tr(U^dag d_i U U^dag d_j U U^dag d_k U).
  - Dann tragen die Quasienergie-Luecken eine Netto-Chiralitaet [S CHIRAL-L V4: "Periodic driving provides a viable
    route to circumvent this no-go"; M, Skizze ARBEITSFELD Z. 340: alle Luecken dieselbe Netto-Chiralitaet = W3].
  - Den Ausgleich (die Anomalie) uebernimmt die Windung des Takts, nicht ein Partner bei derselben Quasienergie.
  - Finns "Takt falsch rum" in dieser Lesart: Zustaende im Gegentakt (Quasienergie pi, Vorzeichenwechsel je Schritt).
- Kennzeichen: [M] Mathematik, [E] Messung im Modell, [P] Projektdatei, [S] an der Quelle gelesen, [L] Literatur aus dem
  Gedaechtnis, [H] Hypothese.

## Projektbezug und Ableitbarkeitsprobe (Leitung, vor der Karte)

- **QCA-TETRA-1, Tabelle QT3 [P]:** DP-Weyl-Automat A^+ mit W(k) = +I bei Gamma und P', -I bei P und H. A^- hat +I bei
  Gamma und P, -I bei H und P'. Zwei Kegel liegen also im Takt (Quasienergie 0), zwei im Gegentakt (pi). Das ist
  bekannt und kein Befund.
- **DP-Automat (Grad 0):** Laut CHIRAL-L [M, nicht gegengelesen] haben Gamma und P' entgegengesetzte Chiralitaet; der
  Abbildungsgrad T^3 -> SU(2) ist 0. Fuer W(k) in SU(2) zaehlt der Grad die Chiralitaeten der Urbilder von +I
  (Quasienergie 0) und von -I (pi) jeweils gleich [M, Leitung, ungeprueft]. Der DP-Automat dient damit als Kontrolle.
- **Inversion:** k -> -k mit festem Unitaer erzwingt W3 = 0 [M, CHIRAL-L Z. 242]. Automaten mit Inversion sind nur
  Kontrollen.
- **Rohdatenprobe (Leitung, jq auf RUNDE-37/qca-bcc-rueck-1/lauf-69/haupt_*.json):**
  - Je Treffer gespeichert sind D, D_poliert, D_voll, nebenbed_rest, kovarianz_abw, gueltig, rueck (nur Kennzahlen und
    Merker; "spruenge" ist ein Wahrheitswert), klass (Kegel bei Gamma mit "phase" und "chiral_det"; an H, P, P' ohne
    Chiralitaet) und kategorie.
  - **Die Sprungmatrizen A stehen nur fuer den Repraesentanten je Fall** ("repr": "freqs" und "A"; Code
    qca_rueck.py Z. 778-780). In den 8-Zustands-Laeufen sind das 9 Faelle mit gespeichertem A (8Na: 3, 8Oa: 5, 8Ob: 1,
    8Nb: 0).
  - W3 und die Netto-Chiralitaet je Luecke stehen nirgends. Sie sind aus den gespeicherten Daten nicht ablesbar und fuer
    die Automaten ohne Inversion nicht vorab ableitbar.
  - Die uebrigen Treffer lassen sich nur durch Wiederholung der eingefrorenen Suche erzeugen. Die Saaten sind
    deterministisch: seed = seedbase*10000 + 10*vi, default_rng.
  - Die Zahl "17 Treffer ohne Inversion" stammt aus CHIRAL-L und ist an den Daten zu pruefen.

## Auftrag (Code-Agent)

1. **Literatur (hoechstens 3 Abrufe, keine Websuche):**
   - Floquet-Version von Nielsen/Ninomiya an der Quelle: Bessho/Sato 2021 [L?] bzw. die CHIRAL-L-Quelle zu V4.
   - Beispiel eines Floquet- bzw. QCA-Modells mit W3 != 0 (z. B. Higashikawa/Nakagawa/Ueda 2019 [L?]).
   - Den 1D-Index (GNVW 2012) [L] nur nennen.
   - Formel, Normierung und Vorzeichen von W3 sowie die Beziehung "Netto-Chiralitaet je Luecke = W3" mit Fundstelle in
     PLAN.md.
2. **Stufe A (gespeicherte Daten):**
   - W3 fuer alle gespeicherten Repraesentanten (2, 4 und 8 Zustaende) und fuer die DP-Automaten A^+ und A^-.
   - Je Automat feststellen, ob er Inversion hat (fester Unitaer V mit U(-k) = V U(k) V^dag, numerisch pruefen).
3. **Stufe B (Wiederholung):**
   - Die eingefrorene Suche fuer die 8-Zustands-Faelle mit denselben Saaten wiederholen (1 Thread), A fuer alle
     Treffer speichern.
   - Reproduktionsprobe: D-Werte gleich den gespeicherten bis 1e-10 relativ.
   - Misslingt die Probe, neue Saaten verwenden, als neue Stichprobe kennzeichnen und die alte Zaehlung nicht
     verwenden.
   - Dann W3 fuer alle Treffer ohne Inversion.
4. **Zusatz je Automat:**
   - Weyl-Punkte mit Quasienergie und Chiralitaet, soweit mit vertretbarem Aufwand findbar (lokaler Berry-Fluss bzw.
     Grad).
   - Tabelle "im Takt (0), im Gegentakt (pi), dazwischen".
5. **Numerik:**
   - U(k) = Sum_j A_j exp(i k . f_j), Ableitungen analytisch.
   - Integral ueber eine primitive Zelle des reziproken Gitters mit Jacobi-Faktor; Gitter N = 16, 24, 32, 48
     (Konvergenz).
   - Ganzzahligkeit: abs(W3 - round(W3)) < 0,05 beim feinsten Gitter, sonst "nicht konvergiert".
6. **Plan, Rauchlauf, Einfrieren wie ueblich.** Die Kontrollen laufen vor den Treffern.

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| WI0 | Kontrollen: DP-Automaten A^+, A^- und alle Automaten mit Inversion W3 = 0; eine synthetische Grad-1-Abbildung (normiert (sin kx, sin ky, sin kz, 2 - Sum cos k) als SU(2)-Element) ergibt abs(W3) = 1; jeweils innerhalb 0,05 | 90 % |
| WI1 | [H] Mindestens ein Projekt-Automat ohne Inversion (Repraesentant oder wiederholter Treffer) hat abs(W3) >= 1 | 20 % |
| WI2 | Kontrolle der Floquet-Aussage [M]: Wo die Weyl-Punkte vollstaendig gefunden sind, ist die Netto-Chiralitaet in jeder Quasienergie-Luecke gleich W3 | 85 % |

**Bedeutung (vorab):**
- **WI1 trifft ein:** Ein Projekt-Automat traegt eine Netto-Haendigkeit. Das ist ein erster Baustein fuer chirale
  Fermionen in K-A bzw. K-AM, frei und ohne Eichfeld. Der Ort der Anomalie ist die Windung des Takts. Naechste Fragen:
  - Bleiben die Kegel isotrop?
  - Koennen zwei Teilchen im Takt bei Wechselwirkung in zwei Teilchen im Gegentakt uebergehen? Die Quasienergie ist nur
    modulo 2 pi erhalten.
- **WI1 verfehlt:** Die gefundenen Automaten sind alle vektorartig. Der Floquet-Weg braucht dann eine gezielte
  Konstruktion; Folgekarte QCA-WINDUNG-2: einen BCC- bzw. Pyrochlor-Automaten mit W3 = 1 bauen und Kegel und Isotropie
  pruefen.
- **WI0 oder WI2 verfehlt:** Erst die Numerik bzw. die Formel pruefen, keine Physik-Aussage.
- **Fuer Finns Frage:** Das Ergebnis sagt, ob in unseren Automaten der Takt selbst eine Haendigkeit traegt.
- **Grenze:** Eine echte Zeitumkehr allein tauscht nie links und rechts [L].

## Rahmen

- Code-Agent. Laeufe nur auf der .69 ueber kleintest.sh, auf den Spuren, die die Leitung beim Start eintraegt; je Lauf
  <= 10 min, 1 Thread.
- Code von RUNDE-37/qca-bcc-rueck-1/code/ nur lesen; Kopie in den eigenen Ordner.
- Zeitbox 120 min.
- Negativliste aus QCA-GEGENLESEN-2 beachten (keine Saetze "ab 8 Zustaenden", "Masse nur mit Inversion" als
  Allgemeinaussage).

## Start (Leitung, 2026-10-04 15:20:15 CEST)

- Spuren: p4000b (Haupt; der Starter sperrt sie, solange WM-1-MB laeuft, dann p4000a) und p4000a (geteilt mit GUERTEL-1,
  der Lock regelt die Reihenfolge). Numpy auf der CPU innerhalb der Einheit ist erlaubt; GPU nur, wenn sie wirklich
  hilft (Pascal, vorhandenes torch, keine neuen Pakete).
- Ordner auf der .69: /home/fmh/fmhc-physics-remote/runde41-qca-windung/ (code/, rauch/, lauf/).
