import Mathlib.Algebra.BigOperators.GroupWithZero.Action
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Algebra.Group.Action.Opposite
import Mathlib.Data.Fintype.Card
import Mathlib.Tactic.Abel

/-!
# `|G|` kills the second cohomology of a finite group

Chapter 1, § 8, Proposition 8.5, p. 45: if `G` is a finite group of order
`n`, then for every `G`-module `A` the group `H²(G, A)` has finite exponent
dividing `n`.  The book works with the linear map `h : Δ_G ⊗ Δ_G → A` of
Proposition 8.1, puts `φ(t) = h(σ - n, t)` with `σ = ∑_(g ∈ G) g`, and uses
the identity (1.17) to get `δφ(r, t) = φ(r) t - φ(r t) = n h(r, t)`.  On
functions on the group this is the following: for `t = g - 1` and a
normalised cocycle, `φ(g - 1) = h(σ - n, g - 1) = ∑_(x ∈ G) h(x, g)`, and
`ψ(g) = ∑_(x ∈ G) h(x, g)` satisfies `δψ = n h` with the coboundary (1.13),
for every cocycle (1.12), normalised or not.  Corollary 8.6, p. 46: if one
can divide by `n` in `A` (in the sense of § 7: every `a ∈ A` is `n c` for
exactly one `c ∈ A`), then `H²(G, A) = 0`.

Notation.  The book's modules are right modules: `a ↦ a g` (`a^g` in the
multiplicative notation of the extension) is a right action of `G` on the
additive group `A` by additive maps.  Here it is a `DistribMulAction` of
the opposite group `Gᵐᵒᵖ` on an `AddCommGroup A`, written `a <• g`
(`MulOpposite.op g • a`, so that `a <• g₁ <• g₂ = a <• (g₁ * g₂)`).
A function `h : G × G → A` is the curried `h : G → G → A`, `h(g₁, g₂)` is
`h g₁ g₂`; `n = |G|` is `Fintype.card G`, acting on `A` by `n • a`.

* `IsCocycle`: the cocycle identity (1.12),
  `h(g₁, g₂) g₃ - h(g₁, g₂ g₃) + h(g₁ g₂, g₃) - h(g₂, g₃) = 0`.
* `coboundary`: the coboundary (1.13),
  `δφ(g₁, g₂) = φ(g₁) g₂ - φ(g₁ g₂) + φ(g₂)`.
* `isCocycle_coboundary`: every coboundary (1.13) satisfies (1.12); this
  uses that the action is a right action, as in the book.
* `psi`: `ψ(g) = ∑_(x ∈ G) h(x, g)`.
* `coboundary_psi`: `δψ = |G| h` for every cocycle `h`.
* `card_smul_eq_coboundary`: hence `|G| h` is a coboundary, i.e. `|G|`
  kills the class of every cocycle (Proposition 8.5).
* `exists_coboundary_eq_of_uniquelyDivisible`: if every `a ∈ A` is `|G| c`
  for exactly one `c`, every cocycle is a coboundary (Corollary 8.6).

Not covered: the groups `Z²(G, A)`, `B²(G, A)` and `H²(G, A)` themselves
(the statements are identities of functions `G → A`, `G → G → A`); the
dictionary of Proposition 8.1 between cocycles on `G` and linear maps
`Δ_G ⊗ Δ_G → A`, in which the book's proof is written (only its value
`φ(g - 1) = ∑_x h(x, g)` on normalised cocycles is used, in the comment
above); the splitting of extensions.  The identity `δφ = n h` is also
checked on generators of the normalised cocycles of twelve pairs `(G, A)`
in `checks/sage/chapter-1b.py` (section_8).
-/

namespace KuzminHomology.H2FiniteExponent

open Finset
open scoped RightActions

variable {G A : Type*} [Group G] [AddCommGroup A] [DistribMulAction Gᵐᵒᵖ A]

/-- The cocycle identity (1.12):
`h(g₁, g₂) g₃ - h(g₁, g₂ g₃) + h(g₁ g₂, g₃) - h(g₂, g₃) = 0`. -/
def IsCocycle (h : G → G → A) : Prop :=
  ∀ g₁ g₂ g₃ : G, h g₁ g₂ <• g₃ - h g₁ (g₂ * g₃) + h (g₁ * g₂) g₃ - h g₂ g₃ = 0

/-- The coboundary (1.13): `δφ(g₁, g₂) = φ(g₁) g₂ - φ(g₁ g₂) + φ(g₂)`. -/
def coboundary (φ : G → A) (g₁ g₂ : G) : A :=
  φ g₁ <• g₂ - φ (g₁ * g₂) + φ g₂

/-- Coboundaries are cocycles (the right action makes (1.12) and (1.13) fit). -/
theorem isCocycle_coboundary (φ : G → A) : IsCocycle (coboundary φ) := by
  intro g₁ g₂ g₃
  simp only [coboundary, smul_add, smul_sub, op_smul_op_smul, mul_assoc]
  abel

variable [Fintype G]

/-- `ψ(g) = ∑_(x ∈ G) h(x, g)`, the function `t ↦ h(σ - n, t)` of the proof of
Proposition 8.5 at `t = g - 1` for a normalised cocycle `h`. -/
def psi (h : G → G → A) (g : G) : A :=
  ∑ x, h x g

/-- `δψ = |G| h` for every cocycle `h` (the computation of Proposition 8.5). -/
theorem coboundary_psi (h : G → G → A) (hh : IsCocycle h) (g₁ g₂ : G) :
    coboundary (psi h) g₁ g₂ = Fintype.card G • h g₁ g₂ := by
  have key : ∀ x : G, h x g₁ <• g₂ - h x (g₁ * g₂) = h g₁ g₂ - h (x * g₁) g₂ := by
    intro x
    rw [← sub_eq_zero, ← hh x g₁ g₂]
    abel
  have shift : ∑ x : G, h (x * g₁) g₂ = ∑ x : G, h x g₂ :=
    Equiv.sum_comp (Equiv.mulRight g₁) (fun x => h x g₂)
  unfold coboundary psi
  rw [Finset.smul_sum, ← Finset.sum_sub_distrib, Finset.sum_congr rfl (fun x _ => key x),
    Finset.sum_sub_distrib, shift, Finset.sum_const, Finset.card_univ]
  abel

/-- Proposition 8.5: `|G| h` is a coboundary for every cocycle `h`. -/
theorem card_smul_eq_coboundary (h : G → G → A) (hh : IsCocycle h) :
    ∃ φ : G → A, ∀ g₁ g₂ : G, Fintype.card G • h g₁ g₂ = coboundary φ g₁ g₂ :=
  ⟨psi h, fun g₁ g₂ => (coboundary_psi h hh g₁ g₂).symm⟩

/-- Corollary 8.6: if one can divide by `n = |G|` in `A` (every `a` is `n c` for
exactly one `c`), every cocycle is a coboundary. -/
theorem exists_coboundary_eq_of_uniquelyDivisible
    (hdiv : ∀ a : A, ∃! c : A, Fintype.card G • c = a)
    (h : G → G → A) (hh : IsCocycle h) :
    ∃ φ : G → A, ∀ g₁ g₂ : G, h g₁ g₂ = coboundary φ g₁ g₂ := by
  choose d hd hu using hdiv
  have inj : ∀ x y : A, Fintype.card G • x = Fintype.card G • y → x = y :=
    fun x y hxy => (hu _ x hxy).trans (hu _ y rfl).symm
  refine ⟨fun g => d (psi h g), fun g₁ g₂ => inj _ _ ?_⟩
  rw [← coboundary_psi h hh]
  simp only [coboundary, smul_add, smul_sub, smul_comm (Fintype.card G) (MulOpposite.op g₂), hd]

end KuzminHomology.H2FiniteExponent

#print axioms KuzminHomology.H2FiniteExponent.isCocycle_coboundary
#print axioms KuzminHomology.H2FiniteExponent.coboundary_psi
#print axioms KuzminHomology.H2FiniteExponent.card_smul_eq_coboundary
#print axioms KuzminHomology.H2FiniteExponent.exists_coboundary_eq_of_uniquelyDivisible
