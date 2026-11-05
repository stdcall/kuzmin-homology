#import "../main-defs.typ": *
// After main-defs: its operator `cd` must not shadow the diagram helper.
#import "common.typ": cd, edge, grid-diagram, node

// Proof of Theorem 6.4, p. 282: the sequence (5.24) above the sequence with
// the unknown term «?». Top row 0 → Λ^(k+1) → Y_(k+1)/B_(k+1) →^d C_k → Λ^k
// → 0, bottom row 0 → Λ^(k+1) →^((k+1)!) Λ^(k+1) → ? → Λ^k → 0.; the labels
// d and (k+1)! above their arrows, the other arrows unlabelled. Vertical
// maps: equalities under Λ^(k+1) and Λ^k, φ (curly phi) under
// Y_(k+1)/B_(k+1) with its label on the right, no map under C_k. The book
// prints Λ_k in the fifth column (corrected to Λ^k, as in (5.25)).
#let quotient-question-diagram = grid-diagram(
  (
    ($0$, $Lambda^(k+1)$, $Y_(k+1) \/ B_(k+1)$, $C_k$, $Lambda^k$, $0$),
    ($0$, $Lambda^(k+1)$, $Lambda^(k+1)$, $?$, $Lambda^k$, $0.$),
  ),
  across: (
    ("->", "->", (label: $d$), "->", "->"),
    ("->", (label: $(k+1)!$), "->", "->", "->"),
  ),
  down: ((none, "=", (label: $phi$), none, "=", none),),
  gap: 6mm,
  row: 11mm,
)

// Formula (5.25), p. 282: the same top row; bottom row 0 → Λ^(k+1)
// →^((k+1)!) Λ^(k+1) →^ψ P^k → Λ^k → 0,; the labels d, (k+1)! and ψ above
// their arrows. Vertical maps: equalities under Λ^(k+1) and Λ^k, φ (curly
// phi) under Y_(k+1)/B_(k+1) and ϕ (straight phi) under C_k, both labels on
// the right.
#let pk-diagram = grid-diagram(
  (
    ($0$, $Lambda^(k+1)$, $Y_(k+1) \/ B_(k+1)$, $C_k$, $Lambda^k$, $0$),
    ($0$, $Lambda^(k+1)$, $Lambda^(k+1)$, $P^k$, $Lambda^k$, $0,$),
  ),
  across: (
    ("->", "->", (label: $d$), "->", "->"),
    ("->", (label: $(k+1)!$), (label: $psi$), "->", "->"),
  ),
  down: ((none, "=", (label: $phi$), (label: $phi.alt$), "=", none),),
  gap: 6mm,
  row: 11mm,
)

// End of the proof of Theorem 6.4, p. 283: the sequence (5.22) above the
// sequence (5.26). Top row 0 → Λ^(k+1) →^2 Λ^(k+1) → D^k → Λ^k → 0, bottom
// row 0 → Λ^(k+1) →^((k+1)!) Λ^(k+1) → P^k → Λ^k → 0,; the labels 2 and
// (k+1)! above their arrows. Vertical maps: equalities under Λ^(k+1) and
// Λ^k, α under the middle Λ^(k+1) with its label on the right, an
// unlabelled arrow D^k → P^k. The book prints Λ_k in the fifth column
// (corrected to Λ^k).
#let dk-pk-diagram = grid-diagram(
  (
    ($0$, $Lambda^(k+1)$, $Lambda^(k+1)$, $D^k$, $Lambda^k$, $0$),
    ($0$, $Lambda^(k+1)$, $Lambda^(k+1)$, $P^k$, $Lambda^k$, $0,$),
  ),
  across: (
    ("->", (label: $2$), "->", "->", "->"),
    ("->", (label: $(k+1)!$), "->", "->", "->"),
  ),
  down: ((none, "=", (label: $alpha$), "->", "=", none),),
  gap: 9mm,
  row: 11mm,
)
