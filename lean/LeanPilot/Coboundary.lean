import LeanPilot.NetData
import LeanPilot.Positive

/-!
# B — Spezialisierung D = d1 des Positivsatzes auf die Zelle aus A

`d1Matrix` ist die 116x68-Matrix des Korandes d1 (Dreieck = [01]+[12]-[02] ueber
`faceEdges`), als reelle Matrix. `d1Matrix_mulVec` zeigt, dass sie dieselbe Abbildung
wie `d1` in NetTopology ist (dort ueber Z). `d1_weighted_posSemidef` ist der allgemeine
Satz aus Positive.lean fuer D = d1.
-/

namespace LeanPilot.Net
open Matrix

def d1Matrix : Matrix (Fin 116) (Fin 68) ℝ :=
  Matrix.of fun f e =>
    (if e = (faceEdges f).1 then 1 else 0) + (if e = (faceEdges f).2.1 then 1 else 0)
      - (if e = (faceEdges f).2.2 then 1 else 0)

theorem d1Matrix_mulVec (y : Fin 68 → ℝ) :
    d1Matrix *ᵥ y = fun f => y (faceEdges f).1 + y (faceEdges f).2.1 - y (faceEdges f).2.2 := by
  funext f
  simp [d1Matrix, mulVec, dotProduct, add_mul, sub_mul, Finset.sum_add_distrib,
    Finset.sum_sub_distrib, ite_mul]

theorem d1_weighted_posSemidef (w : Fin 116 → ℝ) (hw : ∀ i, 0 < w i) :
    (d1Matrixᵀ * Matrix.diagonal w * d1Matrix).PosSemidef :=
  LeanPilot.positive_weights_posSemidef d1Matrix w hw

#print axioms d1Matrix_mulVec
#print axioms d1_weighted_posSemidef

end LeanPilot.Net
