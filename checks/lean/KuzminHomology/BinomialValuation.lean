import Mathlib.NumberTheory.Padics.PadicVal.Basic

/-!
# Binomial coefficients modulo `p` in the sections of `R^n`

Chapter 6, § 5, pp. 327–330: the arithmetic of the binomial coefficients
`C_(n-k)^(i-k)` by which the projections `π^n_i` act on the factors of the
filtration of `R^n` (Lemma 5.4).

* Lemma 5.6 (p. 327), the criterion of Lucas: for `a = Σ a_α p^α`,
  `b = Σ b_β p^β` with digits `0 ≤ a_α, b_β ≤ p − 1`,
  `C_b^a ≢ 0 mod p ⟺ b_α ≥ a_α` for all `α`.
* Lemma 5.7 (p. 328): if `i − j = p^s` and `‖i‖_p, ‖n‖_p ≥ s`, the numbers
  `C_(n-k)^(i-k)`, `k = i, i − 1, …, j + 1`, are prime to `p` (the section
  `R^n_(i j+1)` is regular).
* Lemma 5.8 (p. 328): the same for `i − j = 2p^s`, `‖n‖_p = s`,
  `‖(i + j)/2‖_p > s`.
* Lemma 5.9 (p. 329): if `‖n‖_p = s`, the numbers `C_(n-k)^(p^s-k)`,
  `k = p^s, …, 1, 0`, are prime to `p`.
* Lemma 5.12 (p. 330), the step of its proof: if `‖n‖_p = s + 1`, that is
  `n = p^(s+1) m` with `(m, p) = 1`, then `C_n^(p^s)` is divisible by `p` but
  not by `p²`, so that `Coker π^n_(p^s) = ℤ_p`.  (The other step of that
  proof, that `π^n_(p^s)` maps `R^n_(p^s 1)` isomorphically onto `R^(p^s)_1`,
  is Lemma 5.7 with `i = p^s`, `j = 0`.)

Notation.  `C_b^a` is `b.choose a`; `p` is a prime (`Fact p.Prime`); the
digits of `a` are `a / p ^ α % p`.  `‖n‖_p ≥ s` is written `p ^ s ∣ n` (true
for `n = 0`, as `‖0‖_p = ∞` in the book) and `‖n‖_p = s` is
`p ^ s ∣ n ∧ ¬ p ^ (s + 1) ∣ n`; in Lemma 5.12 `‖n‖_p = s + 1` is
`padicValNat p n = s + 1` (which excludes `n = 0`, as the book's
convention does).  Natural subtraction is harmless: the statements assume
`i ≤ n` (sections of `R^n`) and `k ≤ i`.

The book proves Lemma 5.6 from the congruence `C_b^a ≡ ∏ C_(b_α)^(a_α)`
(formula (6.22)), comparing coefficients of `(1 + x)^b` in `ℤ_p[x]`.  Here
the criterion is derived instead from Kummer's theorem (mathlib's
`padicValNat_choose`: the `p`-adic valuation of `C_b^a` is the number of
carries in `a + (b − a)` in base `p`), through the intermediate form
`a mod p^t ≤ b mod p^t` for all `t`, which the later lemmas use directly.

* `mod_add_mod_lt_iff`: for `a ≤ b`, there is no carry modulo `q`
  (`a mod q + (b − a) mod q < q`) iff `a mod q ≤ b mod q`.
* `add_mod_of_dvd_left`, `add_mod_of_dvd`, `pow_dvd_or_dvd_pow`: remainders
  of `A + e` for `q ∣ A`, `e < q`, and comparability of powers of `p` under
  divisibility.
* `not_dvd_choose_iff_mod`: for `a ≤ b`, `p ∤ C_b^a` iff
  `a mod p^t ≤ b mod p^t` for all `t` (from Kummer's theorem).
* `forall_mod_le_iff_digits`: `a mod p^t ≤ b mod p^t` for all `t` iff
  `a_α ≤ b_α` for all `α`.
* `lucas_criterion`: Lemma 5.6, for all `a, b` (for `a > b` both sides fail).
* `not_dvd_choose_add`: `p ∤ C_(A+e)^e` if `p^s ∣ A` and `e < p^s`.
* `not_dvd_choose_add_pow`: `p ∤ C_(A+e)^(p^s+e)` if `‖A‖_p = s` and
  `e < p^s` (the digit `s` of `A` is not zero).
* `regular_section_single`: Lemma 5.7.
* `regular_section_double`: Lemma 5.8 (the hypotheses `‖i‖_p = ‖j‖_p = s`
  follow from the others and are not needed).
* `regular_section_top`: Lemma 5.9.
* `padicValNat_choose_pow`: `v_p(C_n^(p^s)) = 1` if `v_p(n) = s + 1`, from
  `n C_(n-1)^(p^s-1) = p^s C_n^(p^s)` and `p ∤ C_(n-1)^(p^s-1)`.
* `dvd_choose_pow_and_not_sq`: the same in the book's words, `p ∣ C_n^(p^s)`
  and `p² ∤ C_n^(p^s)`.
* `padicValNat_choose_pow_of_eq_mul`: the same for `n = p^(s+1) m`,
  `p ∤ m`.

Not covered: the congruence (6.22) itself; Lemma 5.4 (that `π^n_i` acts on
the factor `Δ^k` as multiplication by `C_(n-k)^(i-k)`), Corollary 5.5 and
the passage from these numbers to the modules: the regularity of the
sections, the isomorphisms induced by the projections, `Coker π^n_(p^s) =
ℤ_p` and the homology of Lemma 5.12.  These, and the numerical statements
above for `p = 3, 5` and `n ≤ 3p³` resp. `2p³`, are checked in
`checks/sage/chapter-6b.py` (`section_5_projections`, `section_5_lucas`,
`section_5_sections`).
-/

namespace KuzminHomology.BinomialValuation

open Nat

/-- For `a ≤ b`: no carry modulo `q` in `a + (b − a)` iff `a mod q ≤ b mod q`. -/
theorem mod_add_mod_lt_iff {a b q : ℕ} (hab : a ≤ b) (hq : 0 < q) :
    a % q + (b - a) % q < q ↔ a % q ≤ b % q := by
  have hb : b % q = (a % q + (b - a) % q) % q := by
    conv_lhs => rw [← Nat.add_sub_of_le hab]
    exact Nat.add_mod _ _ _
  have h1 := Nat.mod_lt a hq
  have h2 := Nat.mod_lt (b - a) hq
  generalize a % q = x at *
  generalize (b - a) % q = y at *
  generalize b % q = z at *
  subst hb
  constructor
  · intro h
    rw [Nat.mod_eq_of_lt h]
    omega
  · intro h
    by_contra h'
    push Not at h'
    rw [Nat.mod_eq_sub_mod h', Nat.mod_eq_of_lt (by omega)] at h
    omega

/-- `(A + e) mod q = e mod q` if `q ∣ A`. -/
theorem add_mod_of_dvd_left {q A e : ℕ} (hA : q ∣ A) : (A + e) % q = e % q := by
  rw [Nat.add_mod, Nat.mod_eq_zero_of_dvd hA, zero_add, Nat.mod_mod]

/-- `(A + e) mod Q = A mod Q + e` if `q ∣ Q`, `q ∣ A` and `e < q`. -/
theorem add_mod_of_dvd {q Q A e : ℕ} (hqQ : q ∣ Q) (hQ : 0 < Q) (hA : q ∣ A) (he : e < q) :
    (A + e) % Q = A % Q + e := by
  obtain ⟨w, rfl⟩ := hqQ
  obtain ⟨u, hu⟩ : q ∣ A % (q * w) := (Nat.dvd_mod_iff (Dvd.intro w rfl)).mpr hA
  have hlt : A % (q * w) < q * w := Nat.mod_lt _ hQ
  rw [hu] at hlt
  have huw : u < w := Nat.lt_of_mul_lt_mul_left hlt
  have h1 : q * (u + 1) ≤ q * w := Nat.mul_le_mul_left _ huw
  rw [Nat.mul_add, Nat.mul_one] at h1
  rw [Nat.add_mod, Nat.mod_eq_of_lt (show e < q * w by omega), hu,
    Nat.mod_eq_of_lt (by omega)]

/-- `p^t ∣ p^s`, or `s < t` and `p^s ∣ p^t`. -/
theorem pow_dvd_or_dvd_pow (p s t : ℕ) : p ^ t ∣ p ^ s ∨ (s < t ∧ p ^ s ∣ p ^ t) := by
  rcases le_or_gt t s with h | h
  · exact Or.inl (Nat.pow_dvd_pow p h)
  · exact Or.inr ⟨h, Nat.pow_dvd_pow p h.le⟩

variable {p : ℕ} [hp : Fact p.Prime]

/-- Kummer's theorem without carries: for `a ≤ b`, `p ∤ C_b^a` iff
`a mod p^t ≤ b mod p^t` for every `t`. -/
theorem not_dvd_choose_iff_mod {a b : ℕ} (hab : a ≤ b) :
    ¬ p ∣ b.choose a ↔ ∀ t, a % p ^ t ≤ b % p ^ t := by
  have hp1 := hp.out.one_lt
  have hC : b.choose a ≠ 0 := (Nat.choose_pos hab).ne'
  have hv : ¬ p ∣ b.choose a ↔ padicValNat p (b.choose a) = 0 :=
    ⟨padicValNat.eq_zero_of_not_dvd, fun h hd => by
      have := one_le_padicValNat_of_dvd hC hd
      omega⟩
  rw [hv, padicValNat_choose hab (Nat.lt_succ_self (log p b)), Finset.card_eq_zero,
    Finset.filter_eq_empty_iff]
  have hpt : ∀ t, 0 < p ^ t := fun t => Nat.pow_pos hp.out.pos
  constructor
  · intro h t
    rcases Nat.eq_zero_or_pos t with rfl | ht
    · simp only [pow_zero, Nat.mod_one, le_refl]
    by_cases htb : t < (log p b).succ
    · exact (mod_add_mod_lt_iff hab (hpt t)).mp
        (Nat.lt_of_not_le (h (Finset.mem_Ico.mpr ⟨ht, htb⟩)))
    · have hbt : b < p ^ t :=
        lt_of_lt_of_le (Nat.lt_pow_succ_log_self hp1 b)
          (Nat.pow_le_pow_right hp.out.pos (by omega))
      rw [Nat.mod_eq_of_lt hbt, Nat.mod_eq_of_lt (lt_of_le_of_lt hab hbt)]
      exact hab
  · intro h t _
    exact Nat.not_le_of_lt ((mod_add_mod_lt_iff hab (hpt t)).mpr (h t))

/-- `a mod p^t ≤ b mod p^t` for all `t` iff the base-`p` digits satisfy
`a_α ≤ b_α` for all `α`. -/
theorem forall_mod_le_iff_digits {a b : ℕ} :
    (∀ t, a % p ^ t ≤ b % p ^ t) ↔ ∀ t, a / p ^ t % p ≤ b / p ^ t % p := by
  constructor
  · intro h t
    have ht := h (t + 1)
    rw [Nat.mod_pow_succ, Nat.mod_pow_succ] at ht
    by_contra hlt
    push Not at hlt
    have h1 : p ^ t * (b / p ^ t % p + 1) ≤ p ^ t * (a / p ^ t % p) :=
      Nat.mul_le_mul_left _ hlt
    have h2 := Nat.mod_lt b (Nat.pow_pos (n := t) hp.out.pos)
    rw [Nat.mul_add, Nat.mul_one] at h1
    generalize a % p ^ t = x at *
    generalize b % p ^ t = y at *
    generalize p ^ t * (a / p ^ t % p) = u at *
    generalize p ^ t * (b / p ^ t % p) = v at *
    omega
  · intro h t
    induction t with
    | zero => simp only [pow_zero, Nat.mod_one, le_refl]
    | succ t ih =>
      rw [Nat.mod_pow_succ, Nat.mod_pow_succ]
      exact Nat.add_le_add ih (Nat.mul_le_mul_left _ (h t))

/-- Lemma 5.6: `C_b^a ≢ 0 mod p` iff `b_α ≥ a_α` for all digits. -/
theorem lucas_criterion (a b : ℕ) :
    ¬ p ∣ b.choose a ↔ ∀ α, a / p ^ α % p ≤ b / p ^ α % p := by
  rcases le_or_gt a b with hab | hba
  · rw [not_dvd_choose_iff_mod hab, forall_mod_le_iff_digits]
  · rw [Nat.choose_eq_zero_of_lt hba]
    simp only [dvd_zero, not_true_eq_false, false_iff, not_forall, not_le]
    by_contra hall
    push Not at hall
    have h := forall_mod_le_iff_digits.mpr hall a
    have hap : a < p ^ a := Nat.lt_pow_self hp.out.one_lt
    rw [Nat.mod_eq_of_lt hap, Nat.mod_eq_of_lt (by omega)] at h
    omega

/-- `p ∤ C_(A+e)^e` if `p^s ∣ A` and `e < p^s`. -/
theorem not_dvd_choose_add {s A e : ℕ} (hA : p ^ s ∣ A) (he : e < p ^ s) :
    ¬ p ∣ (A + e).choose e := by
  rw [not_dvd_choose_iff_mod (Nat.le_add_left e A)]
  intro t
  rcases pow_dvd_or_dvd_pow p s t with h | ⟨_, h⟩
  · rw [add_mod_of_dvd_left (h.trans hA)]
  · have hpt : 0 < p ^ t := Nat.pow_pos hp.out.pos
    rw [add_mod_of_dvd h hpt hA he, Nat.mod_eq_of_lt (lt_of_lt_of_le he (Nat.le_of_dvd hpt h))]
    exact Nat.le_add_left e _

/-- `p ∤ C_(A+e)^(p^s+e)` if `‖A‖_p = s` and `e < p^s`. -/
theorem not_dvd_choose_add_pow {s A e : ℕ} (hA : p ^ s ∣ A) (hA' : ¬ p ^ (s + 1) ∣ A)
    (he : e < p ^ s) : ¬ p ∣ (A + e).choose (p ^ s + e) := by
  have hA0 : A ≠ 0 := by rintro rfl; exact hA' (dvd_zero _)
  have hsA : p ^ s ≤ A := Nat.le_of_dvd (Nat.pos_of_ne_zero hA0) hA
  rw [not_dvd_choose_iff_mod (by omega)]
  intro t
  rcases pow_dvd_or_dvd_pow p s t with h | ⟨hst, h⟩
  · rw [add_mod_of_dvd_left (h.trans hA), add_comm (p ^ s) e, Nat.add_mod,
      Nat.mod_eq_zero_of_dvd h, add_zero, Nat.mod_mod]
  · have hpt : 0 < p ^ t := Nat.pow_pos hp.out.pos
    have h2 : p ^ s + e < p ^ t := by
      have h3 : 2 * p ^ s ≤ p * p ^ s := Nat.mul_le_mul_right _ hp.out.two_le
      have h4 : p ^ (s + 1) ≤ p ^ t := Nat.pow_le_pow_right hp.out.pos hst
      rw [pow_succ, mul_comm] at h4
      omega
    have h5 : p ^ s ≤ A % p ^ t := by
      have hd : p ^ s ∣ A % p ^ t := (Nat.dvd_mod_iff h).mpr hA
      have hne : A % p ^ t ≠ 0 := fun h0 =>
        hA' ((Nat.pow_dvd_pow p hst).trans (Nat.dvd_of_mod_eq_zero h0))
      exact Nat.le_of_dvd (Nat.pos_of_ne_zero hne) hd
    rw [add_mod_of_dvd h hpt hA he, Nat.mod_eq_of_lt h2]
    exact Nat.add_le_add_right h5 e

/-- Lemma 5.7: if `i − j = p^s` and `‖i‖_p, ‖n‖_p ≥ s`, then
`p ∤ C_(n-k)^(i-k)` for `k = i, i − 1, …, j + 1`. -/
theorem regular_section_single {s n i j k : ℕ} (hi : p ^ s ∣ i) (hn : p ^ s ∣ n) (hin : i ≤ n)
    (hij : j + p ^ s = i) (hjk : j < k) (hki : k ≤ i) :
    ¬ p ∣ (n - k).choose (i - k) := by
  have e : n - k = (n - i) + (i - k) := by omega
  rw [e]
  exact not_dvd_choose_add (Nat.dvd_sub hn hi) (by omega)

/-- Lemma 5.8: if `i − j = 2p^s`, `‖n‖_p = s` and `‖(i + j)/2‖_p > s`, then
`p ∤ C_(n-k)^(i-k)` for `k = i, i − 1, …, j + 1`. -/
theorem regular_section_double {s n i j k : ℕ} (hn : p ^ s ∣ n) (hn' : ¬ p ^ (s + 1) ∣ n)
    (hm : p ^ (s + 1) ∣ (i + j) / 2) (hin : i ≤ n) (hij : j + 2 * p ^ s = i)
    (hjk : j < k) (hki : k ≤ i) :
    ¬ p ∣ (n - k).choose (i - k) := by
  have hm_eq : (i + j) / 2 = j + p ^ s := by omega
  rw [hm_eq] at hm
  have hms : p ^ s ∣ j + p ^ s := (Nat.pow_dvd_pow p (Nat.le_succ s)).trans hm
  rcases lt_or_ge (j + p ^ s) k with hk | hk
  · have hi : p ^ s ∣ i := by
      have : i = (j + p ^ s) + p ^ s := by omega
      rw [this]
      exact Nat.dvd_add hms (dvd_refl _)
    exact regular_section_single hi hn hin (by omega) hk hki
  · have hA : p ^ s ∣ n - (j + p ^ s) := Nat.dvd_sub hn hms
    have hA' : ¬ p ^ (s + 1) ∣ n - (j + p ^ s) := fun h => hn' (by
      have : n = (n - (j + p ^ s)) + (j + p ^ s) := by omega
      rw [this]
      exact Nat.dvd_add h hm)
    have e1 : n - k = (n - (j + p ^ s)) + (j + p ^ s - k) := by omega
    have e2 : i - k = p ^ s + (j + p ^ s - k) := by omega
    rw [e1, e2]
    exact not_dvd_choose_add_pow hA hA' (by omega)

/-- Lemma 5.9: if `‖n‖_p = s`, then `p ∤ C_(n-k)^(p^s-k)` for
`k = p^s, …, 1, 0`. -/
theorem regular_section_top {s n k : ℕ} (hn : p ^ s ∣ n) (hn' : ¬ p ^ (s + 1) ∣ n)
    (hk : k ≤ p ^ s) : ¬ p ∣ (n - k).choose (p ^ s - k) := by
  rcases Nat.eq_zero_or_pos k with rfl | hk0
  · simpa using not_dvd_choose_add_pow (e := 0) hn hn' (Nat.pow_pos hp.out.pos)
  · have hn0 : n ≠ 0 := by rintro rfl; exact hn' (dvd_zero _)
    exact regular_section_single (j := 0) (dvd_refl _) hn
      (Nat.le_of_dvd (Nat.pos_of_ne_zero hn0) hn) (zero_add _) hk0 hk

/-- Lemma 5.12, step of the proof: `v_p(C_n^(p^s)) = 1` if `v_p(n) = s + 1`. -/
theorem padicValNat_choose_pow {s n : ℕ} (hn : padicValNat p n = s + 1) :
    padicValNat p (n.choose (p ^ s)) = 1 := by
  have hn0 : n ≠ 0 := by rintro rfl; simp at hn
  have hdvd : p ^ s ∣ n := by
    have h := pow_padicValNat_dvd (p := p) (n := n)
    rw [hn] at h
    exact (Nat.pow_dvd_pow p (Nat.le_succ s)).trans h
  have hps : 0 < p ^ s := Nat.pow_pos hp.out.pos
  have hsn : p ^ s ≤ n := Nat.le_of_dvd (Nat.pos_of_ne_zero hn0) hdvd
  have hC' : ¬ p ∣ (n - 1).choose (p ^ s - 1) := by
    have e : n - 1 = (n - p ^ s) + (p ^ s - 1) := by omega
    rw [e]
    exact not_dvd_choose_add (Nat.dvd_sub hdvd (dvd_refl _)) (by omega)
  have key : n * (n - 1).choose (p ^ s - 1) = n.choose (p ^ s) * p ^ s := by
    have := Nat.add_one_mul_choose_eq (n - 1) (p ^ s - 1)
    rwa [Nat.sub_add_cancel (Nat.pos_of_ne_zero hn0), Nat.sub_add_cancel hps] at this
  have hc0 : (n - 1).choose (p ^ s - 1) ≠ 0 := (Nat.choose_pos (by omega)).ne'
  have hC0 : n.choose (p ^ s) ≠ 0 := (Nat.choose_pos hsn).ne'
  have hv := congrArg (padicValNat p) key
  rw [padicValNat.mul hn0 hc0, padicValNat.mul hC0 hps.ne', padicValNat.prime_pow, hn,
    padicValNat.eq_zero_of_not_dvd hC'] at hv
  omega

/-- Lemma 5.12, step of the proof: if `‖n‖_p = s + 1`, then `C_n^(p^s)` is
divisible by `p` but not by `p²`. -/
theorem dvd_choose_pow_and_not_sq {s n : ℕ} (hn : padicValNat p n = s + 1) :
    p ∣ n.choose (p ^ s) ∧ ¬ p ^ 2 ∣ n.choose (p ^ s) := by
  have hv := padicValNat_choose_pow hn
  have hC0 : n.choose (p ^ s) ≠ 0 := by
    intro h0
    rw [h0, padicValNat_zero_right] at hv
    exact zero_ne_one hv
  refine ⟨?_, ?_⟩
  · have h := (padicValNat_dvd_iff_le (p := p) (n := 1) hC0).mpr hv.ge
    rwa [pow_one] at h
  · rw [padicValNat_dvd_iff_le hC0, hv]
    omega

/-- Lemma 5.12, step of the proof, for `n = p^(s+1) m` with `(m, p) = 1`. -/
theorem padicValNat_choose_pow_of_eq_mul {s m : ℕ} (hm : ¬ p ∣ m) :
    padicValNat p ((p ^ (s + 1) * m).choose (p ^ s)) = 1 := by
  have hm0 : m ≠ 0 := by rintro rfl; exact hm (dvd_zero _)
  apply padicValNat_choose_pow
  rw [padicValNat.mul (pow_ne_zero _ hp.out.ne_zero) hm0, padicValNat.prime_pow,
    padicValNat.eq_zero_of_not_dvd hm, add_zero]

end KuzminHomology.BinomialValuation

#print axioms KuzminHomology.BinomialValuation.mod_add_mod_lt_iff
#print axioms KuzminHomology.BinomialValuation.add_mod_of_dvd_left
#print axioms KuzminHomology.BinomialValuation.add_mod_of_dvd
#print axioms KuzminHomology.BinomialValuation.pow_dvd_or_dvd_pow
#print axioms KuzminHomology.BinomialValuation.not_dvd_choose_iff_mod
#print axioms KuzminHomology.BinomialValuation.forall_mod_le_iff_digits
#print axioms KuzminHomology.BinomialValuation.lucas_criterion
#print axioms KuzminHomology.BinomialValuation.not_dvd_choose_add
#print axioms KuzminHomology.BinomialValuation.not_dvd_choose_add_pow
#print axioms KuzminHomology.BinomialValuation.regular_section_single
#print axioms KuzminHomology.BinomialValuation.regular_section_double
#print axioms KuzminHomology.BinomialValuation.regular_section_top
#print axioms KuzminHomology.BinomialValuation.padicValNat_choose_pow
#print axioms KuzminHomology.BinomialValuation.dvd_choose_pow_and_not_sq
#print axioms KuzminHomology.BinomialValuation.padicValNat_choose_pow_of_eq_mul
