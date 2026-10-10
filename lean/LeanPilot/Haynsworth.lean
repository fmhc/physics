import LeanPilot.Inertia

/-!
# C (Zusatz) — Haynsworth: Traegheitsadditivitaet am Schur-Komplement

Fuer symmetrisches invertierbares B gilt
  neg [[B, C], [Cᵀ, D]] = neg B + neg (D − Cᵀ B⁻¹ C).
Beweis: Kongruenz mit T = [[1, −B⁻¹C], [0, 1]] (det T = 1) macht die Matrix blockdiagonal,
die blockdiagonale Form ist das Produkt der Blockformen, und `sigNeg_prod` zaehlt.
-/

namespace LeanPilot.Inertia
open Matrix QuadraticMap QuadraticForm

variable {p q : Type*} [Fintype p] [DecidableEq p] [Fintype q] [DecidableEq q]

/-- Blockdiagonale Form = Summe der Blockformen. -/
theorem qf_fromBlocks_diag (B : Matrix p p ℝ) (S : Matrix q q ℝ) (x : p → ℝ) (y : q → ℝ) :
    qf (fromBlocks B 0 0 S) (Sum.elim x y) = qf B x + qf S y := by
  simp only [qf_apply, fromBlocks_mulVec, Sum.elim_comp_inl, Sum.elim_comp_inr, zero_mulVec,
    add_zero, zero_add]
  simp [dotProduct, Fintype.sum_sum_type]

/-- Index einer blockdiagonalen Matrix ist additiv. -/
theorem neg_fromBlocks_diag (B : Matrix p p ℝ) (S : Matrix q q ℝ) :
    neg (fromBlocks B 0 0 S) = neg B + neg S := by
  have hE : Equivalent ((qf B).prod (qf S)) (qf (fromBlocks B 0 0 S)) := by
    refine ⟨(LinearEquiv.sumArrowLequivProdArrow p q ℝ ℝ).symm, fun z => ?_⟩
    obtain ⟨x, y⟩ := z
    show qf (fromBlocks B 0 0 S) (Sum.elim x y) = _
    rw [qf_fromBlocks_diag, prod_apply]
  unfold neg
  rw [← hE.sigNeg_eq, sigNeg_prod]

/-- Haynsworth: Traegheitsadditivitaet ueber das Schur-Komplement am invertierbaren,
symmetrischen Block B. -/
theorem neg_fromBlocks (B : Matrix p p ℝ) (C : Matrix p q ℝ) (D : Matrix q q ℝ)
    (hB : B.IsSymm) (hBu : IsUnit B.det) :
    neg (fromBlocks B C Cᵀ D) = neg B + neg (D - Cᵀ * B⁻¹ * C) := by
  set T : Matrix (p ⊕ q) (p ⊕ q) ℝ := fromBlocks 1 (-(B⁻¹ * C)) 0 1 with hT
  have hTdet : IsUnit T.det := by
    rw [hT, det_fromBlocks_zero₂₁, det_one, det_one, one_mul]; exact isUnit_one
  have hBinvT : (B⁻¹)ᵀ = B⁻¹ := by rw [transpose_nonsing_inv, hB.eq]
  have hBB : B⁻¹ * B = 1 := B.nonsing_inv_mul hBu
  have hBB' : B * B⁻¹ = 1 := B.mul_nonsing_inv hBu
  have hcong : Tᵀ * fromBlocks B C Cᵀ D * T = fromBlocks B 0 0 (D - Cᵀ * B⁻¹ * C) := by
    rw [hT, fromBlocks_transpose, fromBlocks_multiply, fromBlocks_multiply]
    simp only [transpose_one, transpose_zero, transpose_neg, transpose_mul, hBinvT,
      Matrix.one_mul, Matrix.mul_one, Matrix.zero_mul, Matrix.mul_zero, add_zero,
      Matrix.neg_mul, Matrix.mul_neg]
    congr 1
    -- Block (1,2): -(B B⁻¹ C) + C = 0
    · rw [← Matrix.mul_assoc, hBB', Matrix.one_mul, neg_add_cancel]
    -- Block (2,1): -(Cᵀ B⁻¹ B) + Cᵀ = 0
    · rw [Matrix.mul_assoc, hBB, Matrix.mul_one, neg_add_cancel]
    -- Block (2,2): (-(Cᵀ B⁻¹ B) + Cᵀ) = 0, Rest D - Cᵀ B⁻¹ C
    · rw [Matrix.mul_assoc Cᵀ B⁻¹ B, hBB, Matrix.mul_one, neg_add_cancel, Matrix.zero_mul,
        neg_zero, zero_add, sub_eq_neg_add]
  rw [← neg_congruence (fromBlocks B C Cᵀ D) T hTdet, hcong, neg_fromBlocks_diag]

#print axioms neg_fromBlocks_diag
#print axioms neg_fromBlocks

end LeanPilot.Inertia
