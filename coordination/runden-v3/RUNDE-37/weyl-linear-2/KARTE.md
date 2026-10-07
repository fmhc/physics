# WEYL-LINEAR-2: Ist der Gleichteil lambda1 = +0,0010 echt oder ein Fit-Artefakt? (Runde 42, Fast Lane, messnah)

- Leitung claude-primary. Karte und Wahrscheinlichkeiten geschrieben ab 2026-10-04 18:59:04 CEST (date), vor jeder Rechnung.
- **Herkunft:** WEYL-LINEAR-1 (RUNDE-37/weyl-linear-1/ERGEBNIS.md).
  - Gleichteil +0,0010 +- 0,0006 (1,7 sigma) bei N = 32 000 mit 4 Netzen.
  - Die Streuung je Netz faellt wie etwa N^(-1/2).
  - Verdacht: ein k^4-Glied, das der Fit nicht kennt.
- **Messanker:** LHAASO (linear E_QG,1 > 1,0e20 GeV) bzw. JLM. Ein echter Gleichteil verlangte l < ~55 l_P (bedingt: wenn
  das Netz das Photon traegt).
- Kennzeichen: [M] Mathematik, [E] Rechnung, [S] Quelle, [H] Hypothese.

## Ableitbarkeitsprobe

- Der gegenlaeufige Teil (E > 0 gegen E < 0) mittelt wegen der Spiegelsymmetrie des Ensembles zu null; das ist vorab
  ableitbar und nur Kontrolle.
- Der Gleichteil ist nicht ableitbar; die Stoerungsrechnung des Vorgaengers wurde von den Daten widerlegt.

## Auftrag (Code-Agent)

1. **Code von weyl-linear-1 kopieren** (nicht dort aendern).
2. **Netze:** 16 Netze bei N = 32 000 und so viele wie in 10-min-Laeufen moeglich bei N = 128 000 (mindestens 4).
   Beide Aeste.
3. **Fits:** E/(c k) = 1 + lambda1 k + lambda2 k^2 (Ansatz A, wie WL1) und zusaetzlich mit lambda3 k^3 + lambda4 k^4
   (Ansatz B). Fitfenster vorab festlegen, dazu je ein kleineres und groesseres Probefenster (beschreibend).
4. **Bootstrap ueber Netze.** Gleichteil und Gegenteil getrennt.

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| WM0 | Kontrolle: Die 4 alten Netze bei N = 32 000 geben mit Ansatz A wieder +0,0010 auf 1e-4; das Gegenteil mittelt auf < 2 sigma | 85 % |
| WM1 | [H] Mit Ansatz B ist der Gleichteil bei der groessten Netzgroesse mit null vertraeglich (< 2 sigma) | 60 % |
| WM2 | [H] Die Streuung je Netz faellt wie N^p mit p = -0,5 +- 0,15 (ueber N = 2000 bis 128 000) | 70 % |

**Bedeutung (vorab):**
- **WM1 trifft ein:** Das Zufallsnetz hat kein lineares Glied; fuer Licht gilt dann nur der quadratische Anker
  (l < 5,9e-28 m).
- **WM1 verfehlt:** Ein echter linearer Gleichteil; ein lichttragendes Zufallsnetz waere Planck-nah oder muesste das
  Glied wegheben [H].

## Rahmen

- Code-Agent.
- Laeufe nur auf der .69 ueber kleintest.sh, Spur cpu10 (frei seit GUERTEL-2). Je Lauf <= 10 min, 1 Thread.
  Zeitbox 75 min.
