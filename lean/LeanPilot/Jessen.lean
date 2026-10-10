import LeanPilot.JessenData
import Mathlib.LinearAlgebra.Matrix.Rank
import Mathlib.Tactic.NormNum
import Mathlib.Basic.Real.Basic
import Mathlib.Data.Rat.Cast.CharZero

/-!
# D — Jessen: exakte Starrheitsmatrix und Obstruktion zweiter Ordnung

Daten (`points`, `edges`, `flex`, `stress`, `qData`, `rData`, `selected`,
`rightInverse`, `factor`, `selectedRows`) stammen aus `LeanPilot.JessenData`
(Export aus coordination/jessen-rigidity-20261009/result.json). Hier werden

* `rigidity` nach der Definition der Karte D aus `points` und `edges` gebaut
  und gegen `rData` geprueft,
* `qOf flex` nach q_e = Σ_d (u_i[d]-u_j[d])^2 gebaut und gegen `qData` geprueft,
* R u = 0, Rᵀ w = 0, w·q = -8 kernelgeprueft (`decide +kernel`, kein `native_decide`),
* rank R = 29 ueber zwei exakte Zertifikate (S·C = 1 fuer eine 29-Zeilen-Auswahl S,
  R = B·S) mit Mathlib-Ranglemmata hergeleitet,
* daraus: es gibt kein a mit R a = -q (Obstruktion zweiter Ordnung).

Nicht formalisiert: Differentiation einer Kurve, lokale Starrheit, Dynamik.
-/

namespace LeanPilot.Jessen
open Matrix

/-- Spaltenindex 3*i + d fuer Ecke i und Koordinate d. -/
def coord (i : Fin 12) (d : Fin 3) : Fin 36 := ⟨3 * i.val + d.val, by omega⟩

/-- Starrheitsmatrix nach Karte D:
R[e,3i+d] = p_i[d]-p_j[d], R[e,3j+d] = -(p_i[d]-p_j[d]), sonst 0, fuer Kante e = (i,j). -/
def rigidity : Matrix (Fin 30) (Fin 36) ℚ :=
  Matrix.of fun e c =>
    let i := (edges e).1
    let j := (edges e).2
    let k : Fin 12 := ⟨c.val / 3, by omega⟩
    let d : Fin 3 := ⟨c.val % 3, by omega⟩
    if k = i then points i d - points j d
    else if k = j then -(points i d - points j d) else 0

/-- q_e = Σ_{d<3} (u_i[d] - u_j[d])^2 fuer Kante e = (i,j). -/
def qOf (u : Fin 36 → ℚ) : Fin 30 → ℚ := fun e =>
  ∑ d : Fin 3, (u (coord (edges e).1 d) - u (coord (edges e).2 d)) ^ 2

/-- Zeilenauswahl: Zeile k ist die Einheitszeile zu `selectedRows k`. -/
def rowSelect : Matrix (Fin 29) (Fin 30) ℚ :=
  Matrix.of fun k e => if selectedRows k = e then 1 else 0

/-! ## Datenpruefung gegen die Definitionen -/

theorem rigidity_eq_data : rigidity = rData := by decide +kernel

theorem q_eq_data : qOf flex = qData := by decide +kernel

/-! ## Flex, Selbstspannung, Paarung -/

theorem rigidity_mulVec_flex : rigidity *ᵥ flex = 0 := by decide +kernel

theorem rigidity_transpose_mulVec_stress : rigidityᵀ *ᵥ stress = 0 := by decide +kernel

theorem stress_dot_q : stress ⬝ᵥ qOf flex = -8 := by decide +kernel

/-! ## Rangzertifikate -/

theorem rowSelect_mul_rigidity : rowSelect * rigidity = selected := by decide +kernel

theorem selected_mul_rightInverse : selected * rightInverse = 1 := by decide +kernel

theorem factor_mul_selected : factor * selected = rigidity := by decide +kernel

theorem rank_rigidity_le : rigidity.rank ≤ 29 := by
  calc rigidity.rank = (factor * selected).rank := by rw [factor_mul_selected]
    _ ≤ selected.rank := rank_mul_le_right _ _
    _ ≤ Fintype.card (Fin 29) := rank_le_card_height _
    _ = 29 := Fintype.card_fin _

theorem rank_rigidity_ge : 29 ≤ rigidity.rank := by
  calc (29 : ℕ) = Fintype.card (Fin 29) := (Fintype.card_fin _).symm
    _ = (1 : Matrix (Fin 29) (Fin 29) ℚ).rank := rank_one.symm
    _ = (selected * rightInverse).rank := by rw [selected_mul_rightInverse]
    _ ≤ selected.rank := rank_mul_le_left _ _
    _ = (rowSelect * rigidity).rank := by rw [rowSelect_mul_rigidity]
    _ ≤ rigidity.rank := rank_mul_le_right _ _

theorem rank_rigidity : rigidity.rank = 29 :=
  le_antisymm rank_rigidity_le rank_rigidity_ge

/-! ## Obstruktion zweiter Ordnung -/

/-- Es gibt kein a mit R a = -q: w liegt im Kokern von R, aber w·(-q) = 8 ≠ 0. -/
theorem no_second_order_acceleration :
    ¬ ∃ a : Fin 36 → ℚ, rigidity *ᵥ a = -(qOf flex) := by
  rintro ⟨a, ha⟩
  have h1 : stress ⬝ᵥ (rigidity *ᵥ a) = 0 := by
    rw [dotProduct_mulVec, ← mulVec_transpose, rigidity_transpose_mulVec_stress,
      zero_dotProduct]
  have h2 : stress ⬝ᵥ (rigidity *ᵥ a) = 8 := by
    rw [ha, dotProduct_neg, stress_dot_q]; norm_num
  rw [h1] at h2
  norm_num at h2

/-! ## Einbettung der rationalen Daten nach ℝ (nur die Obstruktion; der Rang bleibt ueber ℚ) -/

noncomputable def rigidityR : Matrix (Fin 30) (Fin 36) ℝ := rigidity.map (Rat.castHom ℝ)
noncomputable def stressR : Fin 30 → ℝ := (Rat.castHom ℝ) ∘ stress
noncomputable def qR : Fin 30 → ℝ := (Rat.castHom ℝ) ∘ qOf flex

theorem rigidityR_transpose_mulVec_stressR : rigidityRᵀ *ᵥ stressR = 0 := by
  funext c
  have h := congrArg (Rat.castHom ℝ) (congrFun rigidity_transpose_mulVec_stress c)
  rw [RingHom.map_mulVec] at h
  simpa [rigidityR, stressR, Matrix.transpose_map] using h

theorem stressR_dot_qR : stressR ⬝ᵥ qR = -8 := by
  have h := congrArg (Rat.castHom ℝ) stress_dot_q
  rw [RingHom.map_dotProduct] at h
  simpa [stressR, qR] using h

theorem no_second_order_acceleration_real :
    ¬ ∃ a : Fin 36 → ℝ, rigidityR *ᵥ a = -qR := by
  rintro ⟨a, ha⟩
  have h1 : stressR ⬝ᵥ (rigidityR *ᵥ a) = 0 := by
    rw [dotProduct_mulVec, ← mulVec_transpose, rigidityR_transpose_mulVec_stressR,
      zero_dotProduct]
  have h2 : stressR ⬝ᵥ (rigidityR *ᵥ a) = 8 := by
    rw [ha, dotProduct_neg, stressR_dot_qR]; norm_num
  rw [h1] at h2
  norm_num at h2

#print axioms rigidity_eq_data
#print axioms q_eq_data
#print axioms rigidity_mulVec_flex
#print axioms rigidity_transpose_mulVec_stress
#print axioms stress_dot_q
#print axioms rowSelect_mul_rigidity
#print axioms selected_mul_rightInverse
#print axioms factor_mul_selected
#print axioms rank_rigidity
#print axioms no_second_order_acceleration
#print axioms no_second_order_acceleration_real

end LeanPilot.Jessen
