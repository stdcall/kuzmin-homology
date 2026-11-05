#import "../main-defs.typ": *
// After main-defs: its operator `cd` must not shadow the diagram helper.
#import "common.typ": grid-diagram

// Proof of Lemma 7.4, p. 288: the sequence σ_k above the sequence through
// D^k_0. Top row 0 → Λ^(k+1) →^2 Λ^(k+1) → D^k → Λ^k → 0, bottom row
// 0 → Λ^(k+1) →^2 Λ^k ∧ P_G → D^k_0 → Λ^k → 0,; the labels 2 above their
// arrows, the other arrows unlabelled. Vertical maps: equalities under
// Λ^(k+1) and Λ^k, unlabelled arrows down Λ^(k+1) → Λ^k ∧ P_G and
// D^k → D^k_0.
#let dk-inclusion-diagram = grid-diagram(
  (
    ($0$, $Lambda^(k+1)$, $Lambda^(k+1)$, $D^k$, $Lambda^k$, $0$),
    ($0$, $Lambda^(k+1)$, $Lambda^k and P_G$, $D^k_0$, $Lambda^k$, $0,$),
  ),
  across: (
    ("->", (label: $2$), "->", "->", "->"),
    ("->", (label: $2$), "->", "->", "->"),
  ),
  down: ((none, "=", "->", "->", "=", none),),
  gap: 6mm,
  row: 11mm,
)

// Proof of Lemma 7.4, p. 288: the sequence χ_k above the sequence through
// R^k_0. Top row 0 → Λ^(k+1) → Λ^k ∧ P_G → Λ^k ⊗ ZB → Λ^k → 0, all arrows
// unlabelled; bottom row 0 → Λ^(k+1) →^2 Λ^k ∧ P_G → R^k_0 → Λ^k → 0.,
// the label 2 above its arrow. Vertical maps: equalities under Λ^(k+1) and
// Λ^k, the arrow 2 down Λ^k ∧ P_G → Λ^k ∧ P_G with its label on the right,
// an unlabelled arrow Λ^k ⊗ ZB → R^k_0.
#let chi-r0-diagram = grid-diagram(
  (
    (
      $0$,
      $Lambda^(k+1)$,
      $Lambda^k and P_G$,
      $Lambda^k times.o ZZ B$,
      $Lambda^k$,
      $0$,
    ),
    ($0$, $Lambda^(k+1)$, $Lambda^k and P_G$, $R^k_0$, $Lambda^k$, $0.$),
  ),
  across: (
    "->",
    ("->", (label: $2$), "->", "->", "->"),
  ),
  down: ((none, "=", (label: $2$), "->", "=", none),),
  gap: 6mm,
  row: 11mm,
)

// Formula (5.38), p. 291: the sequence (5.36) with the exterior powers
// above the sequence through P^k. Top row 0 → Λ^(k+1) → Y_(k+1)/B_(k+1)
// →^d C_k → Λ^k → 0, bottom row 0 → Λ^(k+1) →^((k+1)!) Λ^(k+1)(P_G) →^ψ
// P^k → Λ^k → 0.; the labels d, (k+1)! and ψ above their arrows. Vertical
// maps: equalities under Λ^(k+1) and Λ^k, φ (curly phi) down
// Y_(k+1)/B_(k+1) → Λ^(k+1)(P_G) and ϕ (straight phi) down C_k → P^k, both
// labels on the right.
#let exterior-pg-diagram = grid-diagram(
  (
    ($0$, $Lambda^(k+1)$, $Y_(k+1) \/ B_(k+1)$, $C_k$, $Lambda^k$, $0$),
    ($0$, $Lambda^(k+1)$, $Lambda^(k+1)(P_G)$, $P^k$, $Lambda^k$, $0.$),
  ),
  across: (
    ("->", "->", (label: $d$), "->", "->"),
    ("->", (label: $(k+1)!$), (label: $psi$), "->", "->"),
  ),
  down: ((none, "=", (label: $phi$), (label: $phi.alt$), "=", none),),
  gap: 8mm,
  row: 11mm,
)

// End of the proof of Theorem 7.1, p. 292: the sequence through P^k above
// the sequence through P^k_0. Top row 0 → Λ^(k+1) →^((k+1)!) Λ^(k+1)(P_G)
// → P^k → Λ^k → 0, bottom row 0 → Λ^(k+1) →^((k+1)!) Λ^k ∧ P_G →^(ψ_0)
// P^k_0 → Λ^k → 0,; the labels (k+1)! and ψ_0 above their arrows.
// Vertical maps: equalities under Λ^(k+1) and Λ^k, unlabelled arrows up
// Λ^k ∧ P_G → Λ^(k+1)(P_G) and P^k_0 → P^k (the natural embeddings).
#let pk0-inclusion-diagram = grid-diagram(
  (
    ($0$, $Lambda^(k+1)$, $Lambda^(k+1)(P_G)$, $P^k$, $Lambda^k$, $0$),
    ($0$, $Lambda^(k+1)$, $Lambda^k and P_G$, $P^k_0$, $Lambda^k$, $0,$),
  ),
  across: (
    ("->", (label: $(k+1)!$), "->", "->", "->"),
    ("->", (label: $(k+1)!$), (label: $psi_0$), "->", "->"),
  ),
  down: ((none, "=", "<-", "<-", "=", none),),
  gap: 8mm,
  row: 11mm,
)

// End of the proof of Theorem 7.1, p. 292: the sequence through P^k_0
// above the sequence ρ_k. Top row 0 → Λ^(k+1) →^((k+1)!) Λ^k ∧ P_G →
// P^k_0 → Λ^k → 0 (the book prints Λ^(k+1)(P_G) as its second term;
// corrected), bottom row 0 → Λ^(k+1) →^2 Λ^k ∧ P_G → R^k → Λ^k → 0,;
// the labels (k+1)! and 2 above their arrows. Vertical maps: equalities
// under Λ^(k+1) and Λ^k, unlabelled arrows up Λ^k ∧ P_G → Λ^k ∧ P_G
// (multiplication by (1/2)(k+1)!) and R^k → P^k_0.
#let rk-pk0-diagram = grid-diagram(
  (
    ($0$, $Lambda^(k+1)$, $Lambda^k and P_G$, $P^k_0$, $Lambda^k$, $0$),
    ($0$, $Lambda^(k+1)$, $Lambda^k and P_G$, $R^k$, $Lambda^k$, $0,$),
  ),
  across: (
    ("->", (label: $(k+1)!$), "->", "->", "->"),
    ("->", (label: $2$), "->", "->", "->"),
  ),
  down: ((none, "=", "<-", "<-", "=", none),),
  gap: 8mm,
  row: 11mm,
)
