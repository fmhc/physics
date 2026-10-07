# BEUTEL-1 Plan-Nachtrag 1 (NACHTRAEGLICH, nach Lauf 1)

- Geschrieben ab 2026-10-02 09:07:03 CEST (date), NACH Lauf 1 (.69, 09:02:52-09:03:07) und Auswertung 1 (09:05:35).
- Aendert nichts an M1-M3, B1-B7, Wertungsregeln und Bedeutung. Die Wertung aus Lauf 1 bleibt die Wertung.
- Anlass (gesehen nach Lauf 1):
  1. Die Gitterkontrolle dr = 0,04 gegen 0,02 erfuellt "Q und E auf 1e-4" bei festem Q ueberall (<= 2,4e-5),
     bei festem omega aber nur fuer M1 (1,0e-4); M2 1,8e-4, M3 1,9e-4. Das bleibt so berichtet ("teilweise").
  2. Die Trapez-Probe dE/dQ = omega hat bei M3 einen Eigenfehler (omega ~ Q^(-1/4), Schrittfaktor 1,25),
     max 2,0e-3. Das ist eine Schwaeche der Probe, nicht unbedingt der Loesung.
  3. Konkurrenzzustand wurde in Lauf 1 nicht geprueft (Saat nur aus einem Startprofil).

## Zusatzrechnungen (alle als Nachtrag gekennzeichnet)

- N1 drittes Gitter: dr = 0,01 (R_max 350) fuer alle Punkte. Konvergenzordnung aus
  (X_0,04 - X_0,02)/(X_0,02 - X_0,01), erwartet ~4 (zweite Ordnung). Zusaetzlich 0,02 gegen 0,01 gegen 1e-4.
- N2 Probe dE/dQ = omega mit kubischem Spline von omega Q ueber ln Q je Ast (Integral statt Trapez);
  Trapez-Probe bleibt daneben stehen.
- N3 Konkurrenzzustand: Gradientenfluss bei festem Q aus zwei verschiedenen Starts (A: Stufen-/Beutelprofil wie Lauf 1;
  B: Gauss-Profil mit chi = 1 ueberall), danach Newton-Politur. M1 bei Q = 200, 800, 1e4; M2 bei Q = 150, 1100, 1e4;
  M3 bei Q = 100, 1000, 1e4. Gleiche Energie (relativ < 1e-8) = kein Nebental gefunden; tiefere Energie aus B
  = Konkurrenzzustand, der berichtet werden muss.
- N4 Wiederholung: Lauf 2 rechnet die Grobgitterpunkte neu; Abweichung zu Lauf 1 wird berichtet (Reproduktion).

Code: beutel_v2.py (Kopie von beutel.py plus Optionen --dr3 und --konkurrenz), auswertung_v2.py. beutel.py und
auswertung.py bleiben unveraendert.
