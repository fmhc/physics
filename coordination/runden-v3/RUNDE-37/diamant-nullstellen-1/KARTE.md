# DIAMANT-NULLSTELLEN-1: Wo hat der Spin-1/2-Operator auf Finns Diamant-Netz Nullstellen, und was aendern die zwei Abstimmungswege? (Runde 44, Fast Lane)

- Leitung claude-primary. Karte geschrieben ab 2026-10-04 23:02:45 CEST (date), vor jeder Rechnung.
- **Herkunft:** Kartenvorschlag aus DIAMANT-FERMION-L (RUNDE-37/diamant-fermion-l/DOSSIER.md, Abschnitt 7.1). Frage,
  Messgroessen, Vorab-Ableitungen und Vorhersagen von dort sind **bindend und woertlich**; die Wahrscheinlichkeiten stammen
  aus dem Vorschlag. Zusaetze der Leitung sind markiert.
- **Bezug:**
  - LICHT-FINN-NETZ-1: W-D, a1 = +-0,354 laengs 110; gerechnet nur bis k = 0,6.
  - Luecke L6 (Fermionen auf Finns Geometrie).
- Kennzeichen: [M] Mathematik, [E] Rechnung, [S] Quelle, [H] Hypothese.

## Frage (woertlich aus dem Dossier)

Wo liegen die Nullstellen von W-D im ganzen BZ? Was aendern (i) der Gegenterm W-D+S3 (w3 = w1/9) und (ii) FKM bei
t = 4 lambda_SO an a1, a2, a3, Tempo-Isotropie und Nullstellen?

## Messgroessen (woertlich)

- min abs(E) auf einem BZ-Gitter; Dimension der Nullmenge (Punkte oder Linien).
- a1 bis a3 je Richtung (26 Richtungen).
- FKM: groesste Spinspaltung und Kegeltempo an X je Richtung.

## Ableitbarkeitsprobe

- **Vorab abgeleitet [M, Dossier]:** Das ist eine Pruefung der Mathematik des feldforschers, keine Messung.
  - W-D-Schleife durch W und durch (1; 0,392; 0,392) 2 pi/a.
  - W-D+S3: a1 = 0.
  - FKM bei t = 4 lambda: isotroper Kegel, Spaltung 0.
- **Offen (nicht abgeleitet):** Nullstellen von W-D+S3, a3 von W-D+S3, a2-Anisotropie von FKM.
- **Projektsuche [Zusatz Leitung]:** "Knotenlinie", "Nullstellen", "FKM", "Fu-Kane" vor dem Plan mit den Ausschluessen; Treffer nennen.
- **[Zusatz Leitung] Wortlaut-Frage:** DIAMANT-FERMION-L sagt, die W-D-Spaltung trenne keine Helizitaeten (Spin quer zu k). LICHT-FINN-NETZ-1 sagt "spaltet die beiden Haendigkeiten".
  - Bitte beschreibend angeben: Welche Groesse unterscheidet die zwei Zweige lo/hi, Helizitaet oder Chiralitaet (Erwartungswert von sigma.k-Dach bzw. gamma5-artiger Untergitter-Operator)?

## Vorhersagen (woertlich aus dem Dossier, vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| DN0 | [Zusatz Leitung] Kontrolle: Die drei Vorab-Ableitungen oben treffen (Schleife durch W und den genannten Punkt; a1 = 0 fuer W-D+S3 auf 1e-6; FKM-Spaltung < 1e-10 und Kegel isotrop auf 1e-6 bei t = 4 lambda) | 85 % |
| DN1 | [H] W-D+S3 hat weiter Knotenlinien | 70 % |
| DN2 | [H] W-D+S3 hat a3 ungleich null laengs 110 | 80 % |
| DN3 | [H] FKM bei t = 4 lambda: a2-Spannweite > 10 % | 60 % |

**Bedeutung (woertlich):**
- **DN1 ja:** Die W-D-Familie ist ohne Wilson-artigen Term (tau_z, bricht 4_1 bzw. Untergittertausch) als Elektron mehrfach verdoppelt; die FKM-Familie wird der Kandidat.
- **DN1 nein:** W-D+S3 ist ein symmetrischer Einzel-Dirac-Operator mit einem Rest der Dimension 7.

## Rahmen

- Code-Agent. Exakte Bloch-Matrizen 4x4.
- Laeufe nur auf der .69 ueber kleintest.sh, Spuren cpu und cpu11.
  - cpu5 und cpu10 nutzt TT-GRUND-1; cpu3, cpu4 und p4000a nutzt claude-video; cpu2 haelt Codex.
- Je Lauf hoechstens 10 min, 1 Thread. Zeitbox 45 min.
