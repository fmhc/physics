import Mathlib.LinearAlgebra.QuadraticForm.Signature
import Mathlib.LinearAlgebra.QuadraticForm.Prod
import Mathlib.LinearAlgebra.QuadraticForm.IsometryEquiv
import Mathlib.LinearAlgebra.Matrix.SesquilinearForm
import Mathlib.LinearAlgebra.Matrix.NonsingularInverse
import Mathlib.LinearAlgebra.Matrix.Symmetric
import Mathlib.LinearAlgebra.FiniteDimensional.Lemmas
import Mathlib.LinearAlgebra.Matrix.Charpoly.Basic
import Mathlib.Algebra.Polynomial.Roots
import Mathlib.Algebra.Order.Star.Real

/-!
# C — Traegheitslemma (CLAUDE-S4, Abschnitt 4.2)

Quelle: coordination/liquid-marble-analysis-20261008/CLAUDE-S4.md, 4.2:

  neg(Zᵀ A⁻¹ Z) = neg(A) − 1 + [gᵀ A g > 0].

## Runde 2 (10.10.2026): Definition von `neg`

`neg M` ist der **negative Traegheitsindex** der quadratischen Form x ↦ xᵀ M x, also die
maximale Dimension eines Unterraums, auf dem die Form negativ definit ist
(Mathlib: `QuadraticForm.sigNeg`). Fuer reelle symmetrische Matrizen stimmt das mit der
Anzahl negativer Eigenwerte (mit Vielfachheit) ueberein (Spektralsatz); diese Gleichheit ist
hier **nicht** formalisiert. Die Karte nennt beide Lesarten als aequivalent; der datierte
NACHTRAG steht in ERGEBNIS.md.

Beweisweg (ausgefuehrt, ohne sorry):
* `neg_congruence` (Sylvester): Kongruenz Pᵀ M P mit invertierbarem P erhaelt `neg`
  (Mathlib `QuadraticMap.Equivalent.sigNeg_eq`).
* `neg_inv`: A⁻¹ = (A⁻¹)ᵀ A A⁻¹ ist zu A kongruent.
* `sigNeg_prod`: Additivitaet des Index ueber Produkte quadratischer Formen, ueber die
  Diagonalisierung `equivalent_weightedSumSquares` und `sigNeg_weightedSumSquares`.
* `neg_schur_restriction`: Zerlegung ℝⁿ = Bild(Z) ⊕ span(A g); sie ist A⁻¹-orthogonal
  (A⁻¹ (A g) = g ⊥ Bild(Z)), also ist die Form von A⁻¹ isometrisch zum Produkt der Form von
  Zᵀ A⁻¹ Z mit der eindimensionalen Form t ↦ (gᵀ A g) t². Daraus
  neg(A) = neg(A⁻¹) = neg(Zᵀ A⁻¹ Z) + [gᵀ A g < 0], und mit gᵀ A g ≠ 0 die Behauptung.

Haynsworth-Additivitaet fuer allgemeine Blockmatrizen wird fuer diesen Weg nicht benoetigt;
sie ist als Zusatz in `LeanPilot/Haynsworth.lean` (`neg_fromBlocks`) ebenfalls ohne sorry
bewiesen.

## Runde 1 (historisch)

`negCharpoly` ist die Definition aus Runde 1 (negative Nullstellen des charakteristischen
Polynoms mit Vielfachheit); sie bleibt nur mit dem 1x1-Fall `negCharpoly_fin_one` stehen.
-/

namespace LeanPilot.Inertia
open Matrix QuadraticMap QuadraticForm

/-! ## Quadratische Form einer Matrix und negativer Traegheitsindex -/

section Def
variable {m : Type*} [Fintype m] [DecidableEq m]

/-- Quadratische Form x ↦ x ⬝ᵥ (M *ᵥ x) der Matrix M. -/
noncomputable def qf (M : Matrix m m ℝ) : QuadraticForm ℝ (m → ℝ) :=
  LinearMap.BilinMap.toQuadraticMap
    (Matrix.toLinearMap₂' ℝ M : (m → ℝ) →ₗ[ℝ] (m → ℝ) →ₗ[ℝ] ℝ)

theorem qf_apply (M : Matrix m m ℝ) (x : m → ℝ) : qf M x = x ⬝ᵥ (M *ᵥ x) := by
  rw [qf, LinearMap.BilinMap.toQuadraticMap_apply, Matrix.toLinearMap₂'_apply']

/-- Negativer Traegheitsindex: maximale Dimension eines Unterraums, auf dem x ↦ xᵀ M x
negativ definit ist (Mathlib `QuadraticForm.sigNeg`). -/
noncomputable def neg (M : Matrix m m ℝ) : ℕ := sigNeg (qf M)

/-- Transport der Form entlang x ↦ P x (P darf rechteckig sein). -/
theorem qf_mulVec {k : Type*} [Fintype k] [DecidableEq k]
    (M : Matrix m m ℝ) (P : Matrix m k ℝ) (x : k → ℝ) :
    qf M (P *ᵥ x) = qf (Pᵀ * M * P) x := by
  simp only [qf_apply, ← mulVec_mulVec]
  rw [dotProduct_mulVec x Pᵀ, vecMul_transpose]

end Def

/-! ## Sylvester: Kongruenz erhaelt den Index; neg(A⁻¹) = neg(A) -/

section Congruence
variable {m : Type*} [Fintype m] [DecidableEq m]

/-- Sylvesters Traegheitssatz in der benoetigten Form: Kongruenz mit invertierbarem P. -/
theorem neg_congruence (M P : Matrix m m ℝ) (hP : IsUnit P.det) :
    neg (Pᵀ * M * P) = neg M := by
  have hPu : IsUnit P := (Matrix.isUnit_iff_isUnit_det P).mpr hP
  have hinj : Function.Injective P.mulVecLin := mulVec_injective_iff_isUnit.mpr hPu
  let e : (m → ℝ) ≃ₗ[ℝ] (m → ℝ) := P.mulVecLin.linearEquivOfInjective hinj rfl
  have key : ∀ x, qf M (e x) = qf (Pᵀ * M * P) x := fun x => by
    simp only [e, LinearMap.linearEquivOfInjective_apply, mulVecLin_apply]
    exact qf_mulVec M P x
  have hE : Equivalent (qf (Pᵀ * M * P)) (qf M) := ⟨e, key⟩
  exact hE.sigNeg_eq

/-- neg der Inversen einer invertierbaren symmetrischen Matrix. -/
theorem neg_inv (A : Matrix m m ℝ) (hA : A.IsSymm) (hdet : IsUnit A.det) :
    neg A⁻¹ = neg A := by
  have h : (A⁻¹)ᵀ * A * A⁻¹ = A⁻¹ := by
    rw [transpose_nonsing_inv, hA.eq, A.nonsing_inv_mul hdet, one_mul]
  calc neg A⁻¹ = neg ((A⁻¹)ᵀ * A * A⁻¹) := by rw [h]
    _ = neg A := neg_congruence A A⁻¹ (isUnit_nonsing_inv_det_iff.mpr hdet)

end Congruence

/-! ## Additivitaet des negativen Index ueber Produkte quadratischer Formen -/

section Prod

/-- Produkt zweier gewichteter Quadratsummen ist isometrisch zur gewichteten Quadratsumme
auf der disjunkten Vereinigung der Indexmengen. -/
theorem equivalent_prod_weightedSumSquares {ι κ : Type*} [Fintype ι] [Fintype κ]
    (w₁ : ι → ℝ) (w₂ : κ → ℝ) :
    Equivalent ((weightedSumSquares ℝ w₁).prod (weightedSumSquares ℝ w₂))
      (weightedSumSquares ℝ (Sum.elim w₁ w₂)) := by
  refine ⟨⟨(LinearEquiv.sumArrowLequivProdArrow ι κ ℝ ℝ).symm, fun x => ?_⟩⟩
  obtain ⟨f, g⟩ := x
  simp [weightedSumSquares_apply, Fintype.sum_sum_type]

theorem ncard_sum_elim_neg {ι κ : Type*} [Fintype ι] [Fintype κ] (w₁ : ι → ℝ) (w₂ : κ → ℝ) :
    {i | Sum.elim w₁ w₂ i < 0}.ncard = {i | w₁ i < 0}.ncard + {i | w₂ i < 0}.ncard := by
  rw [Set.ncard_eq_toFinset_card', Set.ncard_eq_toFinset_card', Set.ncard_eq_toFinset_card']
  simp only [Set.toFinset_ofPred, Finset.card_filter, Fintype.sum_sum_type, Sum.elim_inl,
    Sum.elim_inr]
  -- beide Seiten stimmen bis auf Entscheidbarkeitsinstanzen ueberein
  refine congrArg₂ (· + ·) ?_ ?_ <;> exact Finset.sum_congr rfl fun _ _ => by congr

/-- Der negative Index ist additiv ueber Produkte (Sylvester-Zaehlung nach Diagonalisierung). -/
theorem sigNeg_prod {M₁ M₂ : Type*} [AddCommGroup M₁] [Module ℝ M₁] [FiniteDimensional ℝ M₁]
    [AddCommGroup M₂] [Module ℝ M₂] [FiniteDimensional ℝ M₂]
    (Q₁ : QuadraticForm ℝ M₁) (Q₂ : QuadraticForm ℝ M₂) :
    sigNeg (Q₁.prod Q₂) = sigNeg Q₁ + sigNeg Q₂ := by
  have : Invertible (2 : ℝ) := invertibleOfNonzero two_ne_zero
  obtain ⟨w₁, e₁⟩ := Q₁.equivalent_weightedSumSquares
  obtain ⟨w₂, e₂⟩ := Q₂.equivalent_weightedSumSquares
  rw [(e₁.prod e₂).sigNeg_eq, e₁.sigNeg_eq, e₂.sigNeg_eq,
    (equivalent_prod_weightedSumSquares w₁ w₂).sigNeg_eq, sigNeg_weightedSumSquares,
    sigNeg_weightedSumSquares, sigNeg_weightedSumSquares, ncard_sum_elim_neg]

theorem ncard_unit_const (p : Prop) [Decidable p] :
    {_i : Unit | p}.ncard = if p then 1 else 0 := by
  split_ifs with h
  · simp [h]
  · simp [h]

end Prod

/-! ## Hauptsatz -/

/-- Traegheitslemma, allgemeine Form (CLAUDE-S4 4.2), in ℤ formuliert.
Annahmen: n ≥ 1, A reell symmetrisch invertierbar, g ≠ 0, die n-1 Spalten von Z linear
unabhaengig mit Bild genau ker(gᵀ), gᵀ A g ≠ 0 und Zᵀ A⁻¹ Z invertierbar
(die letzte Annahme wird im Beweis nicht gebraucht, ebenso g ≠ 0, das aus gᵀ A g ≠ 0 folgt). -/
theorem neg_schur_restriction {n : ℕ} (hn : 1 ≤ n)
    (A : Matrix (Fin n) (Fin n) ℝ) (hA : A.IsSymm) (hdet : IsUnit A.det)
    (g : Fin n → ℝ) (_hg : g ≠ 0)
    (Z : Matrix (Fin n) (Fin (n - 1)) ℝ)
    (hZ : LinearIndependent ℝ (fun j : Fin (n - 1) => fun i => Z i j))
    (hker : ∀ x : Fin n → ℝ, (∃ y, Z *ᵥ y = x) ↔ g ⬝ᵥ x = 0)
    (hgAg : g ⬝ᵥ (A *ᵥ g) ≠ 0)
    (_hZAZ : IsUnit (Zᵀ * A⁻¹ * Z).det) :
    (neg (Zᵀ * A⁻¹ * Z) : ℤ) = (neg A : ℤ) - 1 + (if 0 < g ⬝ᵥ (A *ᵥ g) then 1 else 0) := by
  -- Bezeichnungen
  set B := A⁻¹ with hB
  set v := A *ᵥ g with hv
  set c := g ⬝ᵥ (A *ᵥ g) with hc
  have hBv : B *ᵥ v = g := by
    rw [hB, hv, mulVec_mulVec, A.nonsing_inv_mul hdet, one_mulVec]
  have hBsymm : Bᵀ = B := by rw [hB, transpose_nonsing_inv, hA.eq]
  have hZg : ∀ y, g ⬝ᵥ (Z *ᵥ y) = 0 := fun y => (hker _).mp ⟨y, rfl⟩
  have hvg : v ⬝ᵥ g = c := by rw [hc, hv, dotProduct_comm]
  -- Injektivitaet von y ↦ Z y aus der linearen Unabhaengigkeit der Spalten
  have hZ' : LinearIndependent ℝ Zᵀ := hZ
  have hsum : ∀ y : Fin (n - 1) → ℝ, Z *ᵥ y = ∑ j, y j • Zᵀ j := by
    intro y; funext i
    simp [mulVec, dotProduct, Finset.sum_apply, mul_comm]
  have hZinj : ∀ y, Z *ᵥ y = 0 → y = 0 := by
    intro y hy
    have h := Fintype.linearIndependent_iff.mp hZ' y (by rw [← hsum, hy])
    funext j; exact h j
  -- Die Form von B auf Z y + s v
  have hexpand : ∀ (y : Fin (n - 1) → ℝ) (s : ℝ),
      qf B (Z *ᵥ y + s • v) = qf (Zᵀ * B * Z) y + c * (s * s) := by
    intro y s
    have h0 : (Z *ᵥ y) ⬝ᵥ (B *ᵥ (Z *ᵥ y)) = qf (Zᵀ * B * Z) y := by
      rw [← qf_apply, qf_mulVec]
    have h1 : (Z *ᵥ y) ⬝ᵥ g = 0 := by rw [dotProduct_comm]; exact hZg y
    have h2 : v ⬝ᵥ (B *ᵥ (Z *ᵥ y)) = 0 := by
      rw [dotProduct_mulVec, ← mulVec_transpose, hBsymm, hBv, hZg]
    calc qf B (Z *ᵥ y + s • v)
        = (Z *ᵥ y + s • v) ⬝ᵥ (B *ᵥ (Z *ᵥ y) + s • g) := by
          rw [qf_apply, mulVec_add, mulVec_smul, hBv]
      _ = (Z *ᵥ y) ⬝ᵥ (B *ᵥ (Z *ᵥ y)) + s * ((Z *ᵥ y) ⬝ᵥ g)
            + s * (v ⬝ᵥ (B *ᵥ (Z *ᵥ y))) + s * (s * (v ⬝ᵥ g)) := by
          simp only [add_dotProduct, dotProduct_add, smul_dotProduct, dotProduct_smul,
            smul_eq_mul]
          ring
      _ = qf (Zᵀ * B * Z) y + c * (s * s) := by rw [h0, h1, h2, hvg]; ring
  -- Die lineare Abbildung (y, t) ↦ Z y + t v und ihre Bijektivitaet
  let L : (Fin (n - 1) → ℝ) × (Unit → ℝ) →ₗ[ℝ] (Fin n → ℝ) :=
    Z.mulVecLin.comp (LinearMap.fst ℝ _ _) +
      (LinearMap.toSpanSingleton ℝ (Fin n → ℝ) v).comp
        ((LinearMap.proj () : (Unit → ℝ) →ₗ[ℝ] ℝ).comp (LinearMap.snd ℝ _ _))
  have hL : ∀ p, L p = Z *ᵥ p.1 + p.2 () • v := fun p => by
    simp [L]
  have hLinj : Function.Injective L := by
    rw [← LinearMap.ker_eq_bot, LinearMap.ker_eq_bot']
    intro p hp
    rw [hL] at hp
    have ht : p.2 () = 0 := by
      have h := congrArg (fun x => g ⬝ᵥ x) hp
      simp only [dotProduct_add, dotProduct_smul, hZg, dotProduct_zero, zero_add,
        smul_eq_mul] at h
      rw [← hc] at h
      exact (mul_eq_zero.mp h).resolve_right hgAg
    have hy : p.1 = 0 := by
      rw [ht, zero_smul, add_zero] at hp
      exact hZinj _ hp
    exact Prod.ext hy (funext fun _ => ht)
  have hdim : Module.finrank ℝ ((Fin (n - 1) → ℝ) × (Unit → ℝ)) = Module.finrank ℝ (Fin n → ℝ) := by
    simp [Module.finrank_prod]
    omega
  let e : ((Fin (n - 1) → ℝ) × (Unit → ℝ)) ≃ₗ[ℝ] (Fin n → ℝ) :=
    L.linearEquivOfInjective hLinj hdim
  -- Isometrie: Form von B ≅ Form von Zᵀ B Z × (c t²)
  have heq : Equivalent ((qf (Zᵀ * B * Z)).prod (weightedSumSquares ℝ (fun _ : Unit => c)))
      (qf B) := by
    refine ⟨e, fun p => ?_⟩
    show qf B (L p) = _
    rw [hL, hexpand, prod_apply, weightedSumSquares_apply]
    simp [smul_eq_mul]
  have hsig : neg B = neg (Zᵀ * B * Z) + (if c < 0 then 1 else 0) := by
    unfold neg
    rw [← heq.sigNeg_eq, sigNeg_prod, sigNeg_weightedSumSquares]
    congr 1
    exact ncard_unit_const (c < 0)
  rw [hB, neg_inv A hA hdet] at hsig
  -- Abschluss: c ≠ 0, also [c < 0] = 1 − [0 < c]
  rcases lt_trichotomy c 0 with h | h | h
  · simp only [h, ite_true] at hsig
    simp only [not_lt.mpr h.le, ite_false, hsig]
    push_cast; ring
  · exact absurd h hgAg
  · simp only [not_lt.mpr h.le, ite_false] at hsig
    simp only [h, ite_true, hsig]
    push_cast; ring

/-! ## Runde 1 (historisch): Zaehlung ueber das charakteristische Polynom -/

section Charpoly
open Polynomial
variable {m : Type*} [Fintype m] [DecidableEq m]

/-- Runde-1-Definition: negative Nullstellen des charakteristischen Polynoms mit
Vielfachheit. In Runde 2 nicht mehr verwendet; die Gleichheit mit `neg` fuer symmetrische
Matrizen ist nicht formalisiert. -/
noncomputable def negCharpoly (A : Matrix m m ℝ) : ℕ :=
  Multiset.card (A.charpoly.roots.filter (fun r : ℝ => r < 0))

/-- 1x1-Fall der Runde-1-Definition. -/
theorem negCharpoly_fin_one (c : ℝ) :
    negCharpoly (Matrix.of fun _ _ : Fin 1 => c) = if c < 0 then 1 else 0 := by
  unfold negCharpoly
  have hchar : (Matrix.of fun _ _ : Fin 1 => c).charpoly = X - C c := by
    rw [Matrix.charpoly, Matrix.det_fin_one, Matrix.charmatrix_apply_eq, Matrix.of_apply]
  rw [hchar, Polynomial.roots_X_sub_C, Multiset.filter_singleton]
  split_ifs <;> simp

end Charpoly

#print axioms qf_apply
#print axioms neg_congruence
#print axioms neg_inv
#print axioms sigNeg_prod
#print axioms neg_schur_restriction
#print axioms negCharpoly_fin_one

end LeanPilot.Inertia
