# GUERTEL-FELD-STAB-2: Haelt der Guertel-Trick im Feld auf groberen und feineren Gittern, und wie hoch ist die Gitter-Grenze? (Runde 43, Fast Lane, Robustheit)

- Leitung claude-primary. Karte und Wahrscheinlichkeiten geschrieben ab 2026-10-04 19:24:02 CEST (date), vor jeder Rechnung.
- **Herkunft:** GUERTEL-FELD-STAB-1 (RUNDE-37/guertel-feld-stab-1/ERGEBNIS.md).
  - Auf dem Gitter (12, 24) ist der Vorwaertsast jenseits von 360 Grad ein Sattel.
  - Alle sechs Stoesse (420 und 450 Grad) fuehren ohne Gittersprung in die umgekehrte Verdrillung, E faellt auf
    E(720 - theta) (auf 2e-10).
  - Ohne Stoss zerfaellt der Ast langsam, also kein metastabiler Zustand.
  - Gezeigt nur fuer SO(3) auf einem 3D-Gitter, quasistatisch (FIRE).
- **Finn (04.10.):** Guertel als Basis fuer kleinste Bewegungen; halber Spin (RUNDE-41, RUNDE-42).
- **Regel Dimensionsvergleich (AGENTS.md):** SO(2) (Ebene) gegen SO(3) (Raum) getrennt; das Kontinuum-Argument
  (pi_1(SO(3)) = Z_2) nicht ungeprueft aufs Gitter uebertragen.
- Kennzeichen: [M], [E], [L], [H].

## Ableitbarkeitsprobe

**Vorab ableitbar [M, L]:**
- Im Kontinuum ist 720 Grad stetig zusammenziehbar, 360 Grad nicht (pi_1(SO(3)) = Z_2).
- Fuer SO(2) gibt es keine Entdrillung (pi_1 = Z). Die SO(2)-Kontrolle ist also nur Werkzeugprobe.

**Nicht ableitbar:**
- Ob die Entdrillung ohne Gittersprung auch auf groeberen und feineren Gittern gelingt.
- Ab welcher Verdrillung theta_max der Vorwaertsast auf jedem Gitter springt, statt sich glatt umzulegen. GUERTEL-2
  sah Spruenge bei 270 Grad auf (3, 12), 450 Grad auf (6, 24) und 540 Grad auf (12, 24).
- Ob die Sprunggrenze mit der Aufloesung waechst (Kontinuum-Annaeherung).

## Auftrag (Code-Agent)

1. Code aus guertel-feld-stab-1/code/ und guertel-2/code/ kopieren (dort nichts aendern).
2. **Teil A:** Stossprotokoll von GUERTEL-FELD-STAB-1 (eps = 0,01, 0,1, 0,3; Sinusprofil wie dort; FIRE mit
   Gittersprung-Sonde) bei 450 Grad auf den Gittern (8, 16) und (16, 32); bei 420 Grad nur auf (16, 32), wenn die Zeit
   reicht.
3. **Teil B:** Sprunggrenze theta_max des ungestossenen Vorwaertsasts (Schritte von 30 Grad) auf (8, 16), (12, 24) und
   (16, 32).
4. **Teil C, Kontrolle:** SO(2)-Feld bei 450 Grad mit Stoss: keine Entdrillung.

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| GT0 | Kontrolle: SO(2) entdrillt nicht (E bleibt auf dem Ast oder springt); Gitter (12, 24) bei 450 Grad reproduziert GUERTEL-FELD-STAB-1 auf 1e-6 relativ | 90 % |
| GT1 | [H] Auf (8, 16) und (16, 32) fuehren je 3 von 3 Stoessen bei 450 Grad ohne Gittersprung in die umgekehrte Verdrillung (E auf E(270) auf 1e-6 relativ) | 60 % |
| GT2 | [H] Die Sprunggrenze theta_max waechst streng mit der Aufloesung: (8, 16) < (12, 24) < (16, 32) | 55 % |

**Bedeutung (vorab):**
- **GT1 und GT2 treffen ein:** Der Guertel-Trick im Feld ist kein Zufall eines Gitters. Je feiner das Gitter, desto
  naeher kommt es dem Kontinuum, in dem 720 Grad glatt verschwinden. Damit ist das Feld ein belastbarer Traeger fuer den
  halben Spin (Luecke L4 in GEMEINSAMES-NETZ-v1) [H].
- **GT1 verfehlt:** Der Befund haengt am Gitter (12, 24); ein weiterer Schritt wie GUERTEL-3 waere noetig.

## Rahmen

- Code-Agent.
- Laeufe nur auf der .69 ueber kleintest.sh, Spuren cpu3 und cpu5 (frei seit GUERTEL-FELD-STAB-1). Je Lauf <= 10 min
  (Laufzeit vorab messen; (16, 32) ist teurer), 1 Thread. Zeitbox 90 min.
