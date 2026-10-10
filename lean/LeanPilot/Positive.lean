import Mathlib.LinearAlgebra.Matrix.PosDef
import Mathlib.Algebra.Order.Star.Real

namespace LeanPilot
open Matrix

/-- Finite-dimensional Gram form with nonnegative diagonal weights. -/
theorem weighted_coboundary_posSemidef
    {m n : Type*} [Fintype m] [Fintype n] [DecidableEq m]
    (D : Matrix m n ℝ) (w : m → ℝ) (hw : ∀ i, 0 ≤ w i) :
    (D.transpose * Matrix.diagonal w * D).PosSemidef := by
  simpa using (Matrix.PosSemidef.diagonal hw).conjTranspose_mul_mul_same D

theorem positive_weights_posSemidef
    {m n : Type*} [Fintype m] [Fintype n] [DecidableEq m]
    (D : Matrix m n ℝ) (w : m → ℝ) (hw : ∀ i, 0 < w i) :
    (D.transpose * Matrix.diagonal w * D).PosSemidef :=
  weighted_coboundary_posSemidef D w (fun i => (hw i).le)

#print axioms positive_weights_posSemidef
end LeanPilot
