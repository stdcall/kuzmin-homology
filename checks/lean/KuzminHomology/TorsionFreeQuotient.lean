import Mathlib.Algebra.Module.Submodule.Pointwise
import Mathlib.Algebra.Module.LinearMap.End
import Mathlib.LinearAlgebra.Quotient.Basic
import Mathlib.Algebra.Group.Torsion
import Mathlib.Data.Nat.Factorial.Basic

/-!
# Theorem 7.1 of Chapter 5: `s M / s t N ≅ M / t N` for a torsion-free `M`

Kuzmin, *Гомологическая теория групп* (Homological Group Theory), Chapter 5, § 7,
end of the proof of Theorem 7.1 (`th:abelian-kernel-d2`), printed p. 292.  With
`M = Λ^k ∧ P_G` and `N = Λ^(k+1)`, the book uses that `M` and `M / N` are
torsion-free to conclude that for any `s` and `t`
`s Λ^k ∧ P_G / s t Λ^(k+1) ≅ Λ^k ∧ P_G / t Λ^(k+1)`, and hence, for the module
`L_k = (1/2)(k+1)! L''_k = (1/2)(k+1)! Λ^k ∧ P_G / (k+1)! Λ^(k+1)` (with `L''_k`
of (`eq:pk0-sequence`)), that `L_k ≅ Λ^k ∧ P_G / 2 Λ^(k+1)`.  The isomorphism is
induced by multiplication by `s`.

Formalised here, for a module `M` over any ring `R` (abelian groups: `R = ℤ`;
`B`-modules: `R = ℤB`, the isomorphism is then one of `B`-modules), a submodule
`N` and integers `s, t`; `sM` is the pointwise multiple `s • ⊤` and `t N` is
`t • N`, and `s t N` is regarded as a submodule of `sM` (its preimage under the
inclusion `sM ⊆ M`):

* `smulTop`: the submodule `sM = s • ⊤` of `M`;
* `smulTopMap`: the `R`-linear map `M → sM`, `m ↦ s m`, and
  `smulTopMap_bijective`: it is bijective when multiplication by `s` is injective
  on `M` (`IsSMulRegular M s`);
* `map_smulTopMap`: it maps `t N` onto `s t N` (no hypothesis);
* `quotientEquiv`: the `R`-linear isomorphism `M / t N ≅ sM / s t N`, and
  `quotientEquiv_mk`: it sends the class of `m` to the class of `s m`;
* `isSMulRegular_of_ne_zero`: if `M` is torsion-free and `s ≠ 0`, multiplication
  by `s` is injective, so `quotientEquiv` applies;
* `factorial_div_two_mul_two` and `lkEquiv`: the case of the book,
  `s = (1/2)(k+1)!`, `t = 2`, `s t = (k+1)!` for `k ≥ 1`:
  `M / 2 N ≅ (1/2)(k+1)! M / (k+1)! N`;
* `smulTop_zero_counterexample`: for `s = 0` the statement fails
  (`M = N = ℤ`, `t = 2`: `0 · ℤ = 0`, while `ℤ / 2ℤ ≠ 0`), so "any `s`" means
  `s ≠ 0`.

Hypotheses: only the torsion-freeness of `M` (with `s ≠ 0`) is used, `t` is
arbitrary; the torsion-freeness of `M / N` is not needed for this isomorphism.

Not covered: the identification of `L_k` with `sM / s t N` for the modules of
the book (the embedding `Λ^(k+1) ⊆ Λ^k ∧ P_G`, the torsion-freeness of
`Λ^k ∧ P_G`, the exact sequence (`eq:pk0-sequence`)), the definition of `R^k`
and the commutativity of the last diagram of the proof; the ranks in that diagram
are checked numerically in `checks/sage/chapter-5b.py` (`section_7`).
-/

namespace KuzminHomology.TorsionFreeQuotient

open Pointwise

variable {R M : Type*} [Ring R] [AddCommGroup M] [Module R M]

variable (R M) in
/-- The submodule `sM = s • ⊤` of `M`. -/
abbrev smulTop (s : ℤ) : Submodule R M := s • (⊤ : Submodule R M)

/-- Multiplication by `s` as an `R`-linear map `M → sM`. -/
def smulTopMap (s : ℤ) : M →ₗ[R] smulTop R M s :=
  (DistribSMul.toLinearMap R M s).codRestrict (smulTop R M s)
    fun m => Submodule.smul_mem_pointwise_smul m s ⊤ Submodule.mem_top

@[simp]
theorem smulTopMap_apply (s : ℤ) (m : M) : (smulTopMap (R := R) s m : M) = s • m := rfl

/-- If multiplication by `s` is injective on `M`, then `m ↦ s m` is a bijection
`M → sM`. -/
theorem smulTopMap_bijective {s : ℤ} (hs : IsSMulRegular M s) :
    Function.Bijective (smulTopMap (R := R) (M := M) s) := by
  refine ⟨fun m₁ m₂ h => hs (congrArg Subtype.val h), ?_⟩
  rintro ⟨x, hx⟩
  obtain ⟨m, -, rfl⟩ := (Submodule.mem_smul_pointwise_iff_exists x s ⊤).mp hx
  exact ⟨m, rfl⟩

/-- Multiplication by `s` maps `t N` onto `s t N` (as a submodule of `sM`). -/
theorem map_smulTopMap (s t : ℤ) (N : Submodule R M) :
    (t • N).map (smulTopMap (R := R) s) = ((s * t) • N).comap (smulTop R M s).subtype := by
  ext ⟨x, hx⟩
  simp only [Submodule.mem_map, Submodule.mem_comap, Submodule.subtype_apply]
  constructor
  · rintro ⟨m, hm, hmx⟩
    obtain ⟨n, hn, rfl⟩ := (Submodule.mem_smul_pointwise_iff_exists m t N).mp hm
    have hx' : s • t • n = x := congrArg Subtype.val hmx
    rw [← hx', ← mul_smul]
    exact Submodule.smul_mem_pointwise_smul n (s * t) N hn
  · intro h
    obtain ⟨n, hn, rfl⟩ := (Submodule.mem_smul_pointwise_iff_exists x (s * t) N).mp h
    refine ⟨t • n, Submodule.smul_mem_pointwise_smul n t N hn, ?_⟩
    apply Subtype.ext
    show s • t • n = (s * t) • n
    rw [mul_smul]

/-- The isomorphism of p. 292: `M / t N ≅ sM / s t N`, induced by multiplication
by `s`, when multiplication by `s` is injective on `M`. -/
noncomputable def quotientEquiv {s : ℤ} (hs : IsSMulRegular M s) (t : ℤ) (N : Submodule R M) :
    (M ⧸ t • N) ≃ₗ[R] smulTop R M s ⧸ ((s * t) • N).comap (smulTop R M s).subtype :=
  Submodule.Quotient.equiv (t • N) _ (LinearEquiv.ofBijective _ (smulTopMap_bijective hs))
    (map_smulTopMap s t N)

/-- `quotientEquiv` sends the class of `m` to the class of `s m`. -/
theorem quotientEquiv_mk {s : ℤ} (hs : IsSMulRegular M s) (t : ℤ) (N : Submodule R M)
    (m : M) :
    quotientEquiv (R := R) hs t N (Submodule.Quotient.mk m) =
      Submodule.Quotient.mk (smulTopMap s m) := rfl

/-- In a torsion-free `M` multiplication by a non-zero integer is injective. -/
theorem isSMulRegular_of_ne_zero [IsAddTorsionFree M] {s : ℤ} (hs : s ≠ 0) :
    IsSMulRegular M s :=
  zsmul_right_injective hs

/-- `(1/2)(k+1)! · 2 = (k+1)!` for `k ≥ 1`. -/
theorem factorial_div_two_mul_two {k : ℕ} (hk : 1 ≤ k) :
    (((k + 1).factorial / 2 : ℕ) : ℤ) * 2 = ((k + 1).factorial : ℕ) := by
  have h2 : 2 ∣ (k + 1).factorial := Nat.dvd_factorial two_pos (by omega)
  exact_mod_cast Nat.div_mul_cancel h2

/-- The case of the book (`k ≥ 1`): for a torsion-free `M`,
`M / 2 N ≅ (1/2)(k+1)! M / (k+1)! N`. -/
noncomputable def lkEquiv [IsAddTorsionFree M] (N : Submodule R M) {k : ℕ} (hk : 1 ≤ k) :
    (M ⧸ (2 : ℤ) • N) ≃ₗ[R]
      smulTop R M (((k + 1).factorial / 2 : ℕ) : ℤ) ⧸
        ((((k + 1).factorial : ℕ) : ℤ) • N).comap
          (smulTop R M (((k + 1).factorial / 2 : ℕ) : ℤ)).subtype :=
  (quotientEquiv (isSMulRegular_of_ne_zero (by
      have h2 : 2 ≤ (k + 1).factorial := by
        calc 2 = (1 + 1).factorial := rfl
          _ ≤ (k + 1).factorial := Nat.factorial_le (by omega)
      omega)) 2 N).trans
    (Submodule.quotEquivOfEq _ _ (by rw [factorial_div_two_mul_two hk]))

/-- `s ≠ 0` is needed: for `M = N = ℤ`, `t = 2`, `s = 0` the module `sM` is `0`,
while `M / t N = ℤ / 2ℤ` is not (the class of `1` is not zero). -/
theorem smulTop_zero_counterexample :
    smulTop ℤ ℤ 0 = ⊥ ∧
      (Submodule.Quotient.mk (1 : ℤ) : ℤ ⧸ (2 : ℤ) • (⊤ : Submodule ℤ ℤ)) ≠ 0 := by
  refine ⟨?_, ?_⟩
  · ext x
    rw [Submodule.mem_smul_pointwise_iff_exists, Submodule.mem_bot]
    constructor
    · rintro ⟨b, -, rfl⟩
      exact zero_smul ℤ b
    · rintro rfl
      exact ⟨0, Submodule.mem_top, zero_smul ℤ 0⟩
  · rw [Ne, Submodule.Quotient.mk_eq_zero, Submodule.mem_smul_pointwise_iff_exists]
    rintro ⟨b, -, hb⟩
    rw [smul_eq_mul] at hb
    omega

end KuzminHomology.TorsionFreeQuotient

#print axioms KuzminHomology.TorsionFreeQuotient.smulTop
#print axioms KuzminHomology.TorsionFreeQuotient.smulTopMap
#print axioms KuzminHomology.TorsionFreeQuotient.smulTopMap_apply
#print axioms KuzminHomology.TorsionFreeQuotient.smulTopMap_bijective
#print axioms KuzminHomology.TorsionFreeQuotient.map_smulTopMap
#print axioms KuzminHomology.TorsionFreeQuotient.quotientEquiv
#print axioms KuzminHomology.TorsionFreeQuotient.quotientEquiv_mk
#print axioms KuzminHomology.TorsionFreeQuotient.isSMulRegular_of_ne_zero
#print axioms KuzminHomology.TorsionFreeQuotient.factorial_div_two_mul_two
#print axioms KuzminHomology.TorsionFreeQuotient.lkEquiv
#print axioms KuzminHomology.TorsionFreeQuotient.smulTop_zero_counterexample
