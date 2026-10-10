# Lean-Pilot: Ergebnis-Kurzfassung vom 10.10.2026

In Lean sind die endliche Zellkombinatorik von V, die Korandidentität, die Positivsemidefinitheit gewichteter Korandoperatoren, eine Obstruktion zweiter Ordnung des 12-Ecken-Stabmodells und das Trägheitslemma in der Fassung mit negativem Trägheitsindex formal geprüft; die Gleichsetzung dieses Index mit der Eigenwertzählung bleibt offen.

Die hier enthaltenen neun Lean-Quelldateien sind bytegleich mit dem Abschlussstand der zweiten Runde.
Der dokumentierte Abschlussbuild auf dem CPU-Rechenhost `ubuntu-auto` meldete 37 Axiomabfragen ohne `sorryAx`.
Endliche Identitäten verwenden `decide` beziehungsweise `decide +kernel`; das bedeutet **Kernelprüfung**,
keine unabhängige Neureproduktion der Simulationen. Es wurden keine eigenen Axiome und kein `native_decide`
verwendet. Die ausgewiesenen logischen Abhängigkeiten sind höchstens `propext`, `Classical.choice` und `Quot.sound`.
Für diese Veröffentlichung wurde kein neuer Lean-Build und keine Physikrechnung gestartet.

| Teil | Formal geprüft | Grenze |
|---|---|---|
| Zellkombinatorik | 10 Ecken, 68 Kanten, 116 Dreiecke, 58 Tetraeder; Euler-Summe 0; Kantenmittel 87/17 | Identitäten der festgelegten endlichen 3D-Zellbeschreibung, kein Homöomorphie- oder Dynamiknachweis |
| Korand und Positivität | `d1 ∘ d0 = 0`; `Dᵀ diag(w) D` positiv semidefinit für nichtnegative Gewichte | Positivsemidefinitheit allein beweist keine vollständige physikalische Stabilität |
| 12-Ecken-Stabmodell | Rang der Steifigkeitsmatrix über ℚ gleich 29, `R u = 0`, `Rᵀ w = 0`, `wᵀ q = −8`; keine Beschleunigung mit `R a = −q` über ℚ und ℝ | Rang über ℝ nicht formalisiert; Obstruktion zweiter Ordnung des geprüften Flexes, keine vollständige lokale Starrheit und kein Teilchenmechanismus |
| Trägheitslemma | `neg(Zᵀ A⁻¹ Z) = neg(A) − 1 + [gᵀ A g > 0]` in ℤ; Kongruenzinvarianz, Inversion, Additivität und separates Haynsworth-Lemma | `neg` ist der negative Trägheitsindex; die Gleichsetzung mit der Eigenwertzählung ist nicht formalisiert |

`neg M := QuadraticForm.sigNeg (qf M)` bezeichnet die maximale Dimension eines Unterraums,
auf dem die quadratische Form negativ definit ist. Die genauen Satzvoraussetzungen stehen in
[Inertia.lean](LeanPilot/Inertia.lean), der separate Blockmatrixsatz in [Haynsworth.lean](LeanPilot/Haynsworth.lean).
„Alle vier Zielbereiche bewiesen“ gilt ausschließlich in der Fassung des datierten Nachtrags mit dieser Definition.

Runde 1 formalisiert die Zellzählungen, die Korandidentität, Positivsemidefinitheit und die algebraische Obstruktion des untersuchten Stabmodells, während das Trägheitslemma in dieser historischen Runde noch offene Beweisschritte enthält.
Die historische erste Runde ist hier nicht als eigenes Quellenpaket enthalten. Die aktuelle Kurzfassung ersetzt
keinen historischen Ergebnis-Hash und schreibt der ersten Runde keinen späteren Beweis zu.

Die Matrixaussagen gelten unter ihren algebraischen Voraussetzungen unabhängig von einer räumlichen Deutung.
Die konkreten Zell- und Stabdaten beschreiben 3D-Geometrien; daraus folgt kein unveränderter Befund für 1D, 2D
oder zusätzliche Raumdimensionen. Matrixdimension, räumliche Dimension und innere Feldkomponenten sind zu trennen.

## Quellenstand und Nachbau

- Lean: `leanprover/lean4:v4.34.1`, gemäß [lean-toolchain](lean-toolchain).
- Mathlib: Commit `966709390232ef085fa4d934646024701a3d090f` (v4.34.1).
- [lakefile.toml](lakefile.toml) ersetzt ausschließlich die lokale Mathlib-Pfadabhängigkeit des ursprünglichen
  Builds durch diesen festgelegten Git-Commit. Das ist eine Exportanpassung, kein bereits ausgeführter neuer Build.
- [SHA256SUMS](SHA256SUMS) bindet die hier veröffentlichten Quellen und die Kurzfassung.
- [QUELLSTAND.sha256](QUELLSTAND.sha256) enthält die originalen Abschluss-Hashes der neun Lean-Dateien,
  der Toolchain-Datei und der ursprünglichen Lake-Konfiguration; nur deren Hash weicht im Export ab.

Mit installierter passender Lean-Toolchain im Verzeichnis `lean/`:

```sh
lake update
lake exe cache get
lake build
```

Der Abruf lädt Mathlib und seine Abhängigkeiten. Die archivierte Kernelprüfung bezog sich auf das ursprüngliche
lokale Abhängigkeitspaket. Ein frischer Nachbau muss den Build und die Axiomabfragen erneut prüfen.
Bewiesen ist die Mathematik der angegebenen Objekte, nicht ihre physikalische Gültigkeit.
