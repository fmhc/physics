# TT-GLAS-2: Bleibt das Glas-Netz bei allen Wellenlaengen stabil, woher kommt seine Anisotropie, und wie faellt sie bei groesseren Netzen? (Runde 46, Finns Weiche Kristall/Glas, Zweig Glas)

- Leitung claude-primary. Karte und Wahrscheinlichkeiten geschrieben ab 2026-10-05 06:46:15 CEST (date), vor jeder Rechnung.
- **Herkunft:**
  - TT-GLAS-1: Alle 48 Zufalls-Delaunay-Netze (N = 32 bis 256) haben bei kleinem k genau zwei masselose TT-Moden; nichts waechst.
    - Spanne je Netz in omega^2/k^2: 29,7 % bis 11,4 %, bei N = 512 7,2 %, ~ N^-0,47.
    - Meist Doppelbrechung.
    - Die affine Regge-Steifigkeit ist isotrop (<= 8,2e-6).
    - Offen: Stabilitaet bei endlichem k, Anteil von Bewegungsenergie gegen nichtaffine Relaxation, groessere N [P].
  - Codex' Lektuere: Superzellen-Stabilitaet bei kleinem k ist keine Glas-Stabilitaet [P].
- Kennzeichen: [M], [E], [P], [H].

## Rechnung (Code-Agent; Code aus tt-glas-1/code)

1. **Stabilitaet ueber die ganze Brillouin-Zone der Superzelle:** k-Gitter 6^3 (bzw. so viele, wie in 10 min passen) fuer N = 128 und 256, je 12 Saaten (dieselben wie TT-GLAS-1). Messen: kleinster Eigenwert ohne die Eichnullmoden; Zahl und Ort negativer bzw. wachsender Moden.
2. **Woher die Anisotropie kommt:**
   - Spanne der langen TT-Wellen (a) voll wie in TT-GLAS-1, (b) mit affin eingefrorener Relaxation, also nur Bewegungsenergie, (c) mit isotroper Ersatzmasse, also nur Relaxation.
   - Die Zerlegung steht vor der Rechnung im Plan.
3. **Groessere Netze:** N = 512 und 1024 mit duennbesetztem Loeser, falls in 10 min je Lauf moeglich; mindestens 4 Saaten. Spanne, Doppelbrechungsanteil, Exponent.

## Ableitbarkeitsprobe (Leitung)

- **Vorab ableitbar bzw. schwach informativ:**
  - Die Fortsetzung des N-Gesetzes N^-0,47: Erwartung bei N = 1024 etwa 11,4 % x (256/1024)^0,47 = 5,9 % [M].
  - Das Ensemble-Mittel ist richtungsfrei; im periodischen Wuerfel ist vorab nur Wuerfelsymmetrie sicher.
- **Nicht ableitbar:**
  - Stabilitaet bei endlichem k (wachsende Moden irgendwo in der Zone)
  - welcher Anteil die Spanne traegt
  - ob der Doppelbrechungsanteil mit N gleich bleibt

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| TG2-0 | Kontrolle: Die TT-GLAS-1-Werte bei kleinem k fuer N = 128 und 256 werden auf 1e-3 relativ reproduziert | 90 % |
| TG2-1 | [H] Auf allen 24 Netzen (N = 128 und 256) gibt es im ganzen k-Gitter ausser den Eichnullmoden keine negativen bzw. wachsenden Moden | 55 % |
| TG2-2 | [H] Die nichtaffine Relaxation traegt mehr als die Haelfte der Spanne (b kleiner als c) | 50 % |
| TG2-3 | [H] Bei N = 1024 liegt die Spanne je Netz im Mittel unter 7 % (N-Gesetz haelt) | 60 % |

**Bedeutung (vorab):**
- **TG2-1 trifft ein:** Das Glas ist auch bei kurzen Wellen stabil, eine Bedingung fuer den Glas-Zweig.
- **TG2-1 verfehlt:** Das Glas hat wachsende Moden bei endlichem k; der Glas-Zweig braucht Zusatzstruktur.
- **TG2-2:** Traegt die Relaxation die Spanne, liegt die Anisotropie in der Netzverformung (Geometrie); traegt die Bewegungsenergie, liegt sie in der Massenverteilung. Das bestimmt den naechsten Hebel.

## Rahmen

- Code-Agent; Code aus tt-glas-1/code kopieren, dort nichts aendern.
- Laeufe nur auf der .69 ueber kleintest.sh, Spuren p4000a bzw. p4000b (GPU), sobald QBALL-DOPPELSPALT-1 sie freigibt, sonst cpu6. Je Lauf hoechstens 10 min. Zeitbox 150 min.
- Plan und Code vor den Hauptlaeufen einfrieren (sha256).
- Ein ehrlicher Teilbericht ist besser als keiner: zuerst 1, dann 2, dann 3.
