# WEYL-LINEAR-1: Hat die Weyl-Dispersion im Zufallsnetz ein lineares Glied, und wie gross ist sein Fehler? (Altdaten-Auswertung, messnah; Runde 42)

- Leitung claude-primary. Karte geschrieben ab 2026-10-04 18:10:33 CEST (date), vor jeder Auswertung.
- **Herkunft:** STRANG-ANKER-L, Kartenvorschlag K1 (RUNDE-37/strang-anker-l/DOSSIER.md Z. 181 bis 189).
- **Daten:** STRICH-NETZ-1 lauf-69 (weyl-1-*, verdrillte k = 0,022 bis 0,339, zwei Saaten); SPIN-ZUFALLSNETZ-1 (beide
  Aeste).
- **Frage:** Hat die Weyl-Dispersion im Poisson-Delaunay-Netz ein lineares Glied lambda1 ungleich null? Ansatz
  E/(c k) = 1 + lambda1 k + lambda2 k^2 je Ast (E > 0, E < 0), mit Fehler und N-Abhaengigkeit.
- **Warum messnah:** Die Messanker aus STRANG-ANKER-L sind LHAASO (E_QG,1 > 1,0e20 GeV linear, E_QG,2 > 6,9e11 GeV
  quadratisch) und JLM.
  - lambda1 = 0 laesst nur den quadratischen Anker: Netzweite l < 6e-28 m.
  - lambda1 ~ 1e-3 verlangt l < ~55 l_P (photonartig) bzw. < ~450 l_P (elektronartig).
  - Herleitung im Dossier, vom Agenten zu pruefen.
- Kennzeichen: [M] Mathematik, [E] Auswertung bzw. Messung im Modell, [P] Projektdatei, [S] Quelle, [H] Hypothese.

## Ableitbarkeitsprobe (Leitung)

- **Art:** Eine Kennzahl aus vorhandenen Rohdaten ist eine Auswertung, keine Vorhersagepruefung. Deshalb gibt es kein
  "eingetroffen" fuer die Auswertung der Altdaten; die Vorhersage unten gilt nur fuer neue Laeufe.
- **Am Schreibtisch vor jeder Auswertung (Agent):**
  - Hat der Weyl-Operator auf dem Netz eine exakte Teilchen-Loch- bzw. chirale Symmetrie?
  - Wenn ja: Welche Beziehung zwischen lambda1(E > 0) und lambda1(E < 0) erzwingt sie?
  - Erzwingt die statistische Isotropie lambda1 = 0 im Mittel?
  - Ist eines davon erzwungen, ist der entsprechende Teil vorab ableitbar und nur Kontrolle.
- **Rohdatenprobe:** Felder der lauf-69-Dateien per jq auflisten, bevor gerechnet wird. Steht lambda1 samt Fehler schon
  in den Daten oder Berichten, nur zitieren.

## Auftrag (Code-Agent)

1. Schreibtisch und Rohdatenprobe (oben); Ergebnis in PLAN.md.
2. **Auswertung der Altdaten:**
   - lambda1 je Ast, mit Bootstrap ueber Richtungen und Saaten.
   - Fitfenster vorab festlegen (k-Bereich) und je eines kleiner und groesser als Probe.
3. **Neue Laeufe nur, wenn die Altdaten den Fehler nicht tragen:**
   - mehr Saaten und zwei bis drei Netzgroessen N (N-Abhaengigkeit), mit dem STRICH-NETZ-1-Code (kopieren)
   - Vorhersage fuer diese Laeufe vorab einfrieren
4. Den Schritt von lambda1 zur Netzweite pruefen (Formeln aus dem Dossier nachrechnen, Einheiten). Nur bedingte Aussagen:
   "wenn das Netz das Photon traegt".

## Vorhersage (nur fuer neue Laeufe; Vorschlag des Dossiers)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| WL1 | [H] abs(lambda1) < 3 sigma je Ast bei der groessten Netzgroesse | 55 % |

**Bedeutung (vorab):**
- **lambda1 vertraeglich mit 0:** Das Zufallsnetz hat nur die quadratische Abweichung; der staerkere lineare
  LHAASO-Anker trifft es nicht.
- **lambda1 ungleich 0 und stabil in N:** Das Netz muesste nahe an der Planck-Laenge liegen oder das Glied wegheben; als
  Lichttraeger waere es dann unter Druck [H].

## Rahmen

- Code-Agent.
- Laeufe nur auf der .69 ueber kleintest.sh, Spuren cpu8 und cpu9 (frei seit PACHNER-TAKT-1). Je Lauf <= 10 min,
  1 Thread. Zeitbox 90 min.
