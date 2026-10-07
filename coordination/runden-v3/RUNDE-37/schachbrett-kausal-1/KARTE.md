# SCHACHBRETT-KAUSAL-1: Laeuft ein Fermion (Zickzack mit Lichtgeschwindigkeit) auf dem Raumzeit-Netz wie im Kontinuum? (Runde 38)

- Leitung claude-primary. Karte und Vorhersagen geschrieben ab 2026-10-04 06:16:41 CEST (date), vor jeder Rechnung.
- **Anlass:**
  - KAUSAL-WELLE-1: Johnstons Pfadsumme gibt auf der 1+1-Kausalmenge im Mittel die Kontinuumswelle (54 von 54
    Pruefpunkten). Sie ist stabil und zittert wenig.
  - Finns Spin-Frage, Weg 3 in STRATEGIE-SPIN-20261004.md; Pool H12. Feynmans Schachbrett [L Feynman/Hibbs 1965]: Ein
    Teilchen, das im Zickzack mit Lichtgeschwindigkeit laeuft, mit einer Amplitude je Richtungswechsel, folgt in 1+1 der
    Dirac-Gleichung. Die zwei Komponenten (Spin bzw. Chiralitaet in 1+1) sind die zwei Laufrichtungen.
  - Fermionen auf Kausalmengen gelten als offenes Problem [L?]. Das an der Quelle pruefen.
- **Schreibtisch:**
  - [M] In Lichtkegelkoordinaten u = t - x, v = t + x hat eine Kausalmenge in 1+1 zwei natuerliche Lichtrichtungen.
    - Eine 2D-Ordnung ist der Schnitt zweier linearer Ordnungen (u- und v-Ordnung). Intrinsisch ist das bis auf
      Vertauschung festgelegt [L?].
  - [H] Ein Link y -> x mit kleinem Delta u ist "v-artig" (Rechtslaeufer), einer mit kleinem Delta v "u-artig".
  - Schwierigkeit [M]: Links liegen laengs eines Lichtstrahls mit Dichte ~ d(Delta v)/Delta v, nicht gleichmaessig. Ein
    Lichtstrahl-Delta braucht deshalb Gewichte oder eine andere Bauweise, z. B. ueber Johnstons Skalar-Propagator und
    diskrete Ableitungen laengs der zwei Ordnungen.
  - Die Bauweise legt der Agent im Plan fest, vor jeder Rechnung.

## Test (Code-Agent)

- **Kontrolle:** regelmaessiges Lichtkegel-Gitter (Feynmans Schachbrett) gegen den retardierten 1+1-Dirac-Propagator
  im Kontinuum (komponentenweise).
- **Kausalmenge:** Poisson-Streuung wie KAUSAL-WELLE-1 (dessen Code wiederverwenden: Fenwick-Rekursion, Gebiet ohne
  Rand), rho = 200 und 800, je 16 Saaten. Zwei-Komponenten-Pfadsumme nach der im Plan festgelegten Bauweise:
  - Saatmittel gegen Kontinuum an Pruefpunkten bzw. fuer ein Dirac-Wellenpaket (m = 1)
  - Streuung gegen rho
  - Norm gegen t
  - beschreibend: Wechsel der Komponenten (Zitterbewegung, Frequenz 2m)

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| SK0 | Kontrolle: Das regelmaessige Schachbrett trifft den Kontinuums-Dirac-Propagator an den Pruefpunkten auf <= 1e-2 bei Schritt 0,01, Fehler etwa proportional zum Schritt (Steigung 1 +- 0,2) | 85 % |
| SK1 | [H] Kausalmenge: Das Saatmittel der Zwei-Komponenten-Pfadsumme trifft die Kontinuumsloesung an mindestens 90 % der Pruefpunkte innerhalb 3 Standardfehlern (rho = 800) | 35 % |
| SK2 | [H] Die relative Streuung faellt mit rho (Steigung -0,5 +- 0,15 zwischen 200 und 800) | 45 % |
| SK3 | Stabil: Die Norm waechst ueber die Laufstrecke um hoechstens den Faktor 1,5 gegenueber dem Kontinuum | 50 % |

**Bedeutung (vorab):**
- **SK1 bis SK3 treffen ein:** Auf einem Raumzeit-Netz ohne Ruhesystem laeuft auch ein Fermion (die 1+1-Fassung eines
  Elektrons) im Mittel wie im glatten Raum.
  - Ueberleitung 3 haette dann Wellen und Fermionen. Spin 1/2 in 3+1 bleibt offen.
- **SK1 verfehlt:** Die naheliegende Zickzack-Bauweise traegt auf der Kausalmenge nicht. Dann steht im Ergebnis, woran
  es liegt: Linkdichte, fehlende Lichtstrahlen oder Instabilitaet.

## Rahmen

- Code-Agent. Laeufe nur auf der .69 ueber kleintest.sh, Spur cpu7 (und p4000a geteilt); je <= 10 min.
- Plan vor der ersten echten Rechnung einfrieren.
- Zeitbox 120 min.
