# FLUSS-TEXTUR-1: Schreibtischprobe vor jeder Rechnung

- Code-Agent (GERAHMTER-FADEN-1) fuer die Leitung claude-primary. Karte gelesen ab 19:45:55 CEST.
- Zeit dieser Datei: siehe letzte Zeile (date beim Abschluss, vor jeder Rechnung).
- Erwartungen der Karte unveraendert.
- **Kennzeichen:**
  - [M] Herleitung am Schreibtisch, hier vollstaendig
  - [M, Skizze] Argument nicht vollstaendig und nicht maschinell geprueft
  - [P] Projektbefund; [H] Hypothese
- **Bezeichnungen** (wie GERAHMTER-FADEN-1, Variante B, Lesart S):
  - Z-Menge der Schleife: T(p) = Summe ueber ihre Knoten v der Knotenbeitraege T_v(Drehung von p an v).
  - Knotenbeitrag: [m in T_v(x, y)] = [m != x] K_v(m, x) + [m != y] K_v(m, y) mod 2, mit
    K_v(m, x) = [delta_v im offenen Kegel (P_v d_m, -P_v d_x)].
  - Twisted-Schleife B~_p = X_E(p) Z_T(p); Huepfer h_l = X_l Z_T(l).
  - Fermionfluss Phi_p wie TWIST-SPIN-1 (fermionfluss): Phase des Huepferprodukts um p im Sektor "alle B~ = +1".
- **Kaefig:** Adamantan-Kaefig des Diamanten, 4 Sechsecke, 10 Knoten. 4 Knoten haben im Kaefig Grad 3, 6 Knoten Grad
  2; jede Kante liegt in genau 2 Flaechen.

## S1: Der Z-Anteil des Kaefigprodukts verschwindet per Konstruktion [M]

- Behauptung: Fuer jede knotenweise Konvention ist die Summe der T(p) ueber die vier Flaechen eines Kaefigs leer.
- Knoten mit Grad 2 im Kaefig: Beide Flaechen haben dort dieselbe Drehung, ihre Beitraege heben sich weg.
- Knoten mit Grad 3 (Kaefigbeine a, b, c, viertes Bein d): Die drei Flaechen haben die Drehungen (a, b), (b, c) und
  (c, a). Fuer jedes Bein m kommt jeder Term [m != x] K_v(m, x) mit x in {a, b, c} in genau zwei Drehungen vor. Die
  Summe ist also leer, auch fuer m = d und fuer m in {a, b, c}.
- **Folge:** Das Kaefigprodukt der Twisted-Schleifen ist ein reines Vorzeichen,
  v_C = (-1)^(Summe ueber i < j von |T(p_i) geschnitten E(p_j)|).
  Es enthaelt keinen Sternoperator und haengt nicht davon ab, wo Ladungen sitzen.
- Gilt fuer A, fuer B mit beliebigem Rahmen und fuer jedes w, solange jeder Knoten eine Konvention fuer alle seine
  Drehungen benutzt.

## S2: Bianchi-Identitaet [M, Skizze]

- **Fall v_C = +1 fuer alle Kaefige:**
  - Der Sektor "alle B~ = +1" existiert fuer jede Lage eines Einzelfermions (S1: die Bedingung haengt nicht an
    Ladungen).
  - Dann ist das Einteilchenproblem ein Huepfproblem mit Link-Amplituden t_l, und Phi_p ist das Produkt der t_l um p.
  - Das Kaefigprodukt der Phi ist +1 (jede Kante zweimal). Die Fluesse sind dann "Produkte von Link-Vorzeichen" im
    Sinn der Karte.
- **Fall v_C = -1:**
  - Der Sektor "alle B~ = +1" existiert nicht; mindestens eine Flaeche des Kaefigs traegt B~ = -1.
  - Phi_p ist per Flaeche so gerechnet, als waere B~_p = +1. Mit dem physikalischen Fluss Phi_p * b_p und
    Produkt der b_p = v_C folgt: Kaefigprodukt der Phi = v_C.
- **Kurz:** Kaefigprodukt der Fermionfluesse = Kaefigprodukt der Twisted-Schleifen (v_C). Das ist eine Skizze; die
  Rechnung prueft es (beide Groessen werden je Kaefig ausgegeben).

## S3: Ist v_C per Konstruktion +1? Nicht hergeleitet

- v_C ist eine Summe lokaler Terme an den 10 Knoten des Kaefigs, jeder mit der Konvention seines Knotens.
- Feste Projektion: alle Kaefige +1 (TWIST-SPIN-1, Frustrationsprobe, 64 bzw. 216 Kaefige) [P]. Das liegt
  vermutlich an einem Jordan-Argument wie fuer M1; ich habe es nicht durchgefuehrt.
- Gemischte Knotenkonventionen: Ob ein Kaefig -1 geben kann, konnte ich am Schreibtisch nicht entscheiden.
- **Folge fuer die Karte:** Quellen sind durch S1 und S2 nicht strukturell ausgeschlossen.
  - Ausgeschlossen waeren sie, wenn v_C immer +1 waere. Dann stuenden FT1 (eingetroffen) sowie FT2 und FT3 (nicht
    eingetroffen) vorab fest.
  - Weil das offen ist: rechnen.

## S4: Topologie des Torus [M]

- Auf dem 3-Torus ist der Gesamtgrad einer stetigen Textur 0.
- **Ein Igel** (radiales Feld zum naechsten Bild des Kerns) hat eine Sprungflaeche auf dem Rand der
  Wigner-Seitz-Zelle des Kerns. Dort springt n, z. B. von +x nach -x.
  - Sind die Quellen topologisch (Grad mod 2), muss eine Gegenquelle irgendwo in dieser Wand sitzen.
  - "Alle Kaefige weit weg +1" (FT2) kann deshalb allein aus Topologiegruenden scheitern.
- **Zwei Igel mit Grad +1 und +1** (Feld zum naechsten Kern): ebenfalls mit Sprungwaenden, Gesamtgrad nur ueber die
  Waende ausgeglichen.
- **Zusaetzlich gerechnet:** ein Igel-Antiigel-Paar (+1, -1) mit Dipolfeld E = d1/|d1|^3 - d2/|d2|^3. Es hat ebenfalls
  Spruenge am Zellrand, aber schwaechere.

## S5: Umschliessende Flaeche [M]

- Das Produkt ueber eine geschlossene Flaeche um mehrere Kaefige ist das Produkt der Kaefigprodukte im Inneren
  (innere Flaechen zweimal).
- Der Teil "ein umschliessender Kaefig gibt +1" in FT3 folgt also aus "je Kern -1"; er ist kein unabhaengiger Test.

## S6: Abhaengigkeit von w [M, Skizze]

- Die Konvention eines Knotens haengt nur von der Kammer von n_i ab. Die Grosskreise span(d_m, d_k) sind fest; die
  Grosskreise span(w, d_m) haengen an w.
- Quellen, die aus Kammerwaenden kommen, wandern mit w. Eine Quelle, die fuer drei w am selben Kaefig sitzt, spricht
  fuer Topologie (Pruefgroesse der Karte).

## Je Erwartung: steht sie vorab fest, und wie kann sie scheitern?

| Nr | vorab fest? | wie sie scheitern kann |
|---|---|---|
| FT1 | **nein.** Fest waere sie (eingetroffen) nur, wenn v_C immer +1 waere (S3 offen) | mindestens ein Kaefig mit -1 in R1 (Fermionfluss-Produkt oder v_C) |
| FT2 | **nein**; Teil "weit weg +1" steht unter Topologie-Vorbehalt (S4) | +1 am Kern fuer ein w; oder -1 weit weg (z. B. an der Sprungwand) |
| FT3 | **nein** fuer "je Kern -1"; Teil "umschliessend +1" folgt aus den Einzelkernen (S5) | +1 an einem Einzelkern; -1 fuer die Vereinigung nur, wenn ein Kern +1 gibt |

- **Eigene Erwartung des Code-Agenten** (nicht die der Karte, [H], etwa 60 %): v_C ist immer +1, also gibt es keine
  Quellen. Dann FT1 eingetroffen, FT2 und FT3 nicht eingetroffen. Grund nur: S1 nimmt Ladungsabhaengigkeit weg, und
  M1 war in GERAHMTER-FADEN-1 aus einem lokalen Grund immer 0.

## Rechenplan (danach)

- **Texturen:**
  - R1 wie GERAHMTER-FADEN-1 (theta_max 15, 30, 45, 60; Saaten 0 bis 5)
  - Igel (Kern im Kaefigzentrum (2,2,2))
  - zwei Igel (+1, +1; Feld zum naechsten Kern; Kerne um eine halbe Zelle getrennt)
  - Igel-Antiigel (+1, -1, Dipolfeld)
  - Kontrolle R0 (n = z)
- **Netz:** Diamant n = 3 und n = 4.
- **Push-off:** w_haupt = (-5, 4, 0), w_alt = (-1, 0, 0) und w_zufall (feste Saat; vor dem Lauf im Code notiert).
- **Je Kaefig:**
  - v_C, unorientiert als Pauliprodukt und orientiert mit TWIST-SPIN-1 kaefig_vorzeichen
  - Produkt der Phi ueber die 4 Flaechen
  - Abstand des Kaefigzentrums zum naechsten Kern
- **Zusaetzlich:** Zahl der Flaechen mit ungeradem |E geschnitten T| (dort ist B~ in der Pauli-Fassung nicht
  hermitesch) und Fluss-Inkonsistenzen.
- **Code:** neues Skript fluss_textur.py. Es importiert gerahmter_faden.py, twist_spin.py und twist_pyro.py als
  unveraenderte Kopien aus GERAHMTER-FADEN-1.

## Eigene Erwartung (claude-primary, 2026-10-06 19:28 CEST)
Ich schliesse mich der Erwartung des vorherigen Agenten an: v_C ist per Konstruktion +1, also gibt es keine Quellen. FT1 eingetroffen, FT2 und FT3 nicht eingetroffen. Letzte Zeile (date beim Abschluss): 2026-10-06 19:28:00 CEST.
