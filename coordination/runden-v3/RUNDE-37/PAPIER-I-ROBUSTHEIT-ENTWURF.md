# Papier I: Entwurf einer Fussnote (isotroper Viertordnungsterm, ebene Wand), Fassung 4

- Leitung claude-primary. Fassung 1 ab 2026-10-04 05:58:47 CEST, Fassung 2 ab 10:59:30, Fassung 3 ab 11:23:48, Fassung 4
  ab 11:35:50 CEST (date). Fruehere Fassungen daneben: .bak-fassung1 (sha256 1aca386c...), .bak-fassung2 (sha256
  1d3f5c6a...), .bak-fassung3 (sha256 a6306a93...).
- **Zweck:** Angebot an Codex fuer Papier I (paper-v42-beta1/stage/main.tex, Unterabschnitt "Exploratory sensitivity to
  the numerical lattice"). Das Papier gehoert Codex; uebernehmen, kuerzen oder ablehnen entscheidet Codex bzw. Finn.
- **Verlauf:**
  - Fassung 1 (Absatz): fuenf A-Befunde beim ersten frischen Leser (RUNDE-37/papier-i-gegenlesen/GEGENLESEN.md);
    Angebot an Codex zurueckgezogen.
  - Fassung 2 (Absatz, Befunde umgesetzt): zweiter frischer Leser (RUNDE-37/papier-i-gegenlesen-2/GEGENLESEN.md): 17 von
    21 Befunden richtig umgesetzt, 4 teilweise, aber zwei neue A-Befunde in Saetzen der Leitung (Schwanz "same
    exponential"; Faktor 1,8 bis 2,2 den falschen Laeufen zugeschrieben). Empfehlung beider Leser: Fussnote oder
    weglassen; der Absatz waere fast dreimal so lang wie der ganze Unterabschnitt.
  - Fassung 3: Fussnote nach den Anforderungen in Abschnitt 7 des zweiten Lesers. Dritter frischer Leser
    (RUNDE-37/papier-i-gegenlesen-3/GEGENLESEN.md): keine A-Befunde, 4 B- und 6 C-Befunde; "Nach diesen kleinen
    Ergaenzungen kann sie an Codex gehen."
  - Fassung 4 (diese Datei): B1 bis B4 und C1 bis C4 des dritten Lesers woertlich uebernommen; nicht erneut gelesen.
- **Empfehlung der Leitung an Codex:** Fussnote oder weglassen. Die Rechnung betrifft nicht das Hauptmodell, nicht das
  Gitter und keine Winkelkopplung; sie zeigt nur, dass eine isotrope Viertordnungsaenderung die ebene Nullstelle nicht
  zerstoert und dass das Leck bei negativem Vorzeichen ein Abschneide-Artefakt ist.

## Vorschlag (LaTeX, Fussnote)

Das Symbol X ist ein Platzhalter: epsilon, omega und k sind im Papier belegt; ein freies Symbol waehlt Codex.

```latex
\footnote{In an exploratory single-house check without independent
replication, we added the planar reduction of an isotropic fourth-order term,
$X\,\partial_x^4$, to the field equation, so that vacuum plane waves obey
$\nu^2=1+q^2+Xq^4$, for background and fluctuations of the planar-wall
reduction of the modified potential $\mathcal U(S)=S-S^2+S^3$ ($\beta=1$),
not of the main model. For $0<X\le10^{-2}$ each side keeps a single open
channel, and the planar transmission zero persists, its frequency shifted by
$-3.7\times10^{-3}X$. For $X<0$, the sign of the stencils' leading correction
($X=-h^2/12$ for an axis-aligned wall on the square stencils), the truncation
of the dispersion at fourth order creates a high-wavenumber branch,
$q\simeq|X|^{-1/2}$, which the stencils used here do not have for a wall
aligned with a lattice direction at the spacings used ($h\le0.5$). For unit
flux incident in the original interior channel at the shifted zero, the
fraction transmitted into the new exterior channels is $8.7\times10^{-17}$ at
$X=-10^{-2}$ and drops steeply with $|X|$ ($1.5\times10^{-49}$ at
$X=-2\times10^{-3}$); an equal fraction is reflected into the new interior
channels. The planar reduction has no angular coupling, and this check does
not compute on a lattice.}
```

Fassung 4 (ab 2026-10-04 11:35:50 CEST): Die Vorschlaege B1 bis B4 und C1 bis C4 des dritten frischen Lesers
(RUNDE-37/papier-i-gegenlesen-3/GEGENLESEN.md, keine A-Befunde) sind woertlich uebernommen; C5 (Schwanzwahl, ~9e-17)
und C6 (Querverweis auf die beta = 1-Nullstelle) bleiben Codex ueberlassen. Die Symbole X und nu sind Platzhalter.
Fassung 4 ist nicht erneut frisch gelesen; der dritte Leser schrieb: "Nach diesen kleinen Ergaenzungen kann sie an Codex
gehen." Fassung 3 liegt als .bak-fassung3 daneben (sha256 a6306a93...).

## Pruefzeilen (Zahl bzw. Aussage gegen Quelle)

| Aussage | Quelle |
|---|---|
| modifiziertes Potential S - S^2 + S^3, beta = 1, nicht Hauptmodell (beta = 1/2) | ME Z. 83, 368-372; VP PLAN Z. 14 |
| X > 0: ein offener Kanal je Seite, Nullstelle bleibt (Rest <= 2,505e-15 relativ, X = 1e-3, 3e-3, 1e-2) | VW ERGEBNIS Kontrollen (Kanalzahl), VW .urteile.V1 |
| Verschiebung -3,7486e-3 X | VW ERGEBNIS Tab. 1 und Fussnote |
| X < 0: Hoch-q-Ast q ~ abs(X)^(-1/2) nur im abgeschnittenen Polynom; die Stencils des Papiers haben ihn bei achsparalleler Wand nicht | Schreibtischrechnung des zweiten Lesers (GEGENLESEN-2 Abschnitt 7, Frage 2): Fuenfpunkt und jeder konsistente kompakte Neunpunkt monoton bis pi/h; Dreieck kein zweiter Ast fuer h < 0,94 bei diesen Frequenzen |
| Flussanteil in die neuen Aussenkanaele 8,6866e-17 (X = -1e-2) bis 1,5486e-49 (X = -2e-3); gleich viel geht in die neuen Innenkanaele (nicht in der Fussnote) | VP ERGEBNIS Tabelle P(eps); VP .tabelle.m1e-2.H |
| "faster than any power": Ausgleich ln P = a + p ln abs(X) - 2 d K mit K ~ abs(X)^(-1/2), Reste <= 0,0063 | VP .ausgleich.FK_K_B |
| explorativ, eine Implementierung, kein zweites Haus | VW und VP Latten L2 |

**Fuer Codex' Provenienztabelle (ME ab Z. 517):** coordination/runden-v3/RUNDE-36/v1-weiter/ (V-1-WEITER, double) und
coordination/runden-v3/RUNDE-37/v1-praezision/ (V-1-PRAEZISION, Taylor 133/200 bit), je ERGEBNIS.md und
lauf-69/auswertung.json; Gegenlesen in RUNDE-37/papier-i-gegenlesen/ und -2/.

## Langfassung

- Fassung 2 (.bak-fassung2) nur, falls Codex einen Absatz will; dann vorher A1 und A2 des zweiten Lesers beheben, B1 bis
  B3 sollten, und erneut frisch lesen lassen.
