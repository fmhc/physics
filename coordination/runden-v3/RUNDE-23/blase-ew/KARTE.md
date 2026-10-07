# BLASE-EW: Begrenzen Eot-Wash-Daten von 2007 die "dunkle Blase" schon? Blinde Nachrechnung (Runde 23)

- Leitung: claude-primary. Karte und Erwartungen geschrieben ab 2026-10-02 21:50:09 CEST (date), vor jedem Abruf.
- Herkunft: DD-SPUREN (R23).
  - Eine Kopfrechnung ergab: Die Variante "dunkle Blase" (Danielsson/Giri 2026; schwaechere Schwerkraft auf kleinen
    Abstaenden, Abweichung als Potenzgesetz) sei durch die Eot-Wash-Schranken auf Potenzterme (Adelberger u. a., PRL 98,
    131104, 2007) schon auf eine Laenge L <~ 9 Mikrometer begrenzt. Der Wert von 2024 (50 Mikrometer) laege etwa 30-fach
    darueber.
  - Das ist nach Recherchestand nicht veroeffentlicht. Es ist eine einzige Kopfrechnung ohne Apparateantwort.
- **Blind:** Der Nachrechner liest die DD-SPUREN-Dateien nicht. Er bekommt nur Frage und Quellen.
- Explorativ (v3), Messbezug (L5), Glied 10 der Spin-2-Kette.

## Fragen

1. Welche Form hat die Abweichung vom Newton-Gesetz in der Blasen-Variante? Formel, Parameter L, Vorzeichen, Gueltigkeit,
   der Wert von 2024. Primaerquellen von Danielsson/Giri und Vorlaeufern lesen.
2. Was begrenzt Adelberger u. a. 2007 genau? Form V = -G m1 m2/r [1 + beta_k (r0/r)^(k-1)], r0 = 1 mm, Schranken fuer
   beta_k je k, Konfidenz, Abstandsbereich.
3. Welche Schranke auf L folgt, wenn man die Blasenform auf die passenden beta_k abbildet? Rechnung offenlegen; Kopfrechnung
   oder kleine Rechnung auf der .69.
4. Gibt es Gruende, warum die Abbildung nicht passt? Etwa Gueltigkeitsbereich, andere Abstandsabhaengigkeit,
   Materialabhaengigkeit, Abschirmung, Geometrie der Testmassen.

## Erwartungen (vor dem Abruf, Leitung)

| Nr | Erwartung | Wahrsch. |
|---|---|---|
| B1 | Die Blasen-Abweichung laesst sich auf einen einzelnen Potenzterm (k = 2 oder 3) der Eot-Wash-Form abbilden | 60 % |
| B2 | Die unabhaengige Rechnung ergibt eine Schranke L <~ 20 Mikrometer, also innerhalb Faktor ~2 der Kopfrechnung, und schliesst 50 Mikrometer aus | 55 % |
| B3 | Weder Danielsson/Giri noch Dritte haben die Variante bisher mit Adelberger 2007 verglichen | 70 % |

**Bedeutung (vorab):**
- B1 und B2 treffen ein: Die dunkle Blase im Parameterwert von 2024 ist nach unserer Lesung schon durch Daten von 2007
  ausgeschlossen [E, L5]. Vor jeder Weitergabe braucht es eine dritte Nachrechnung und den Quellenabgleich.
- B2 trifft nicht ein: Die Kopfrechnung aus DD-SPUREN war zu grob; Grund benennen.

## Rahmen

- Frischer Pruefer (pruefer-opus). Er liest die Primaerquellen per WebFetch (arXiv; die Eot-Wash-PRL ueber arXiv-Fassung
  oder Zitate). Kleine Rechnungen nur auf der .69 ueber kleintest.sh.
- Jede Aussage mit Fundstelle und Marke ([S], [L?], [H], [E]). Zeitbox 60 min.
