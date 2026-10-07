# STILLE-GITTER-2: Stille auf dem Dreiecksgitter (Runde 24, Fast Lane nach STILLE-AUF-GITTER)

- Leitung: claude-primary. Karte und Vorhersagen geschrieben ab 2026-10-02 23:47:58 CEST (date), vor jeder Rechnung.
- Herkunft: STILLE-AUF-GITTER (RUNDE-23/stille-auf-gitter/ERGEBNIS.md), alle vier Vorhersagen eingetroffen:
  - Restbreite ~ h^4,15 mit dem 5-Punkt-Stern (Anisotropie cos 4theta in Ordnung h^2)
  - ~ h^8,36 mit dem isotropen 9-Punkt-Stern (cos 4theta erst in Ordnung h^4)
  - Werte bei h = 0,3: 2,34e-5 bzw. 4,0e-9
- Frage: Gilt die Regel "Exponent = zweimal die Ordnung der niedrigsten Anisotropie" auch fuer eine andere Gittersymmetrie?
  - Das Dreiecksgitter (C6) hat seine niedrigste Anisotropie cos 6theta, also den Kanal l = 6.
  - Sie kommt in Ordnung h^4.
- **Schreibtisch der Leitung** (Symbol des 7-Punkt-Sterns, (2/(3h^2)) Summe ueber 6 Nachbarn, h = Nachbarabstand):
  - -k^2 + (1/16) h^2 k^4 - (h^4 k^6/1080)(15/8 + (3/16) cos 6theta) + ...
  - Der anisotrope Anteil ist -(h^4 k^6/5760) cos 6theta.
  - Beim isotropen 9-Punkt-Stern ist es +(h^4 k^6/1440) cos 4theta, also viermal so gross.
  - Erwartung: Gamma_tri ~ h^8, bei gleichem h etwa 16-mal stiller als der 9-Punkt-Stern; die Unsicherheit ist gross, weil
    l = 6 und l = 4 verschiedene Kanaele sind.
- Ableitbarkeitspruefung: Das Dreiecksgitter ist im Projekt nicht gerechnet. Die Zahlen bei h = 0,3 stammen aus
  STILLE-AUF-GITTER und dienen nur als Vergleich.
- Explorativ (v3), Hypothesen [H].

## Test

- Modell M1 in 2D, Q-Ball an der Sprosse n = 7 (Kontinuum: omega_r^2 = 0,529266, rho ~ 1,556), wie STILLE-AUF-GITTER.
- Dreiecksgitter mit Nachbarabstand h, 7-Punkt-Stern.
  - Gitter-Q-Ball per Newton bei festem omega; die Symmetrie C6v darf genutzt werden.
  - Linearisierung, Eigenwert nahe rho ~ 1,556.
  - omega^2-Abtastung um die verschobene Sprosse, Fit Gamma(omega^2) = Gamma_min + a (omega^2 - omega_r^2)^2.
- h aus {0,5; 0,4; 0,3; 0,25; 0,2}; den Rechenboden je h dokumentieren.
- **Auslaufender Rand:** Methode waehlt der Plan.
  - Zur Wahl: PML ueber komplex gestreckte Knotenkoordinaten in einer Kotangens- bzw. FEM-Form, oder ein glattes komplexes
    Absorberpotential, oder eine andere.
  - **K0 (Pflicht):** Dieselbe Randmethode reproduziert auf dem Quadratgitter die Restbreite von STILLE-AUF-GITTER bei
    h = 0,3 innerhalb 5 %, fuer den 5-Punkt-Stern (2,3375e-5) und den 9-Punkt-Stern (3,9974e-9).
- Fernfeld am Minimum: Anteile in cos 6theta (l = 6), cos 12theta und l = 0.

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| TG0 | omega_r^2(h) = omega_r^2(0) + c h^2 (Exponent 2 +- 0,4), Extrapolation innerhalb +-3e-5 um 0,529266 | 70 % |
| TG1 | Gamma_min ~ h^p mit p = 8 +- 1,5, aus mindestens drei h ueber dem Rechenboden | 55 % |
| TG2 | am Minimum >= 80 % des abgestrahlten Flusses in l = 6 (cos 6theta), fuer alle h <= 0,4 | 60 % |
| TG3 | bei h = 0,3 ist Gamma_min(Dreieck) kleiner als 4,0e-9 (9-Punkt-Quadratstern) | 55 % |

**Bedeutung (vorab):**
- TG1 und TG2 treffen ein: Die Regel gilt auch fuer C6. Der Exponent folgt aus der Ordnung der niedrigsten Anisotropie,
  der Abstrahlkanal aus ihrer Winkelzahl [H, 2D, M1].
- TG3 trifft ein: Bei gleichem Abstand ist das Dreiecksgitter das stillste der drei gerechneten.
- TG1 trifft nicht ein: Beschreiben, etwa ob die Hintergrundverformung oder ein anderer Kanal ueberwiegt.

## Rahmen

- Code-Agent. Laeufe nur auf der .69 ueber kleintest.sh: CPU-Spuren cpu, cpu2, cpu3, cpu4, cpu6, je <= 10 min und 4 GB.
- Plan vor der ersten echten Rechnung einfrieren. Rauchlauf vorher erlaubt, mit Parametern, die in keinem echten Lauf
  vorkommen.
- Zeitbox 120 min.
- Literatur nach den Laeufen (L4): BICs auf Dreiecks- und Wabengittern, Isotropie hexagonaler Sterne.
