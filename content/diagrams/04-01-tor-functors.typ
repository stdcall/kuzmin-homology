#import "../main-defs.typ": *
// After main-defs: its operator `cd` must not shadow the diagram helper.
#import "common.typ": edge, grid-diagram
#import "@preview/cetz:0.5.2"

// Рис. 1, p. 176: the chains of the tensor product X ⊗_R Y. The point (i, j)
// of the lattice stands for X_i ⊗_R Y_j, the line i + j = n carries the
// n-dimensional chains, and the two arrows from a point (i, j) of the line
// show where the summands of the differential (4.5) go: to (i - 1, j) and to
// (i, j - 1). The book draws the lattice 0 ≤ i ≤ 6, 0 ≤ j ≤ 5 with n = 5,
// the arrows from (2, 3), the axes beyond the lattice and the label i + j = n
// on a curved leader from the foot of the line.
#let tensor-lattice = cetz.canvas(length: 5mm, {
  import cetz.draw: *
  let (columns, rows, n) = (6, 5, 5)
  let (i, j) = (2, 3)
  assert(i + j == n and i > 0 and j > 0)
  let dot = 0.075
  let head = (end: "stealth", fill: black, scale: 0.8)
  set-style(stroke: 0.5pt)
  // The axes, drawn beyond the lattice, in heavier lines.
  line((0, 0), (columns + 3, 0), stroke: 1pt, mark: head)
  line((0, 0), (0, rows + 2), stroke: 1pt, mark: head)
  for x in range(columns + 1) {
    for y in range(rows + 1) {
      circle((x, y), radius: dot, fill: black, stroke: none)
    }
  }
  line((0, n), (n, 0))
  // The summands of d(x ⊗ y): to (i - 1, j) and to (i, j - 1); the heads
  // stop at the dots.
  line((i, j), (i - 1 + dot, j), stroke: 0.8pt, mark: head)
  line((i, j), (i, j - 1 + dot), stroke: 0.8pt, mark: head)
  // The leader leaves the foot of the line horizontally and reaches the
  // label horizontally.
  let from = (n + 0.1, 0.3)
  let to = (n + 2, 0.95)
  bezier(from, to, (n + 1, 0.3), (n + 1.1, 0.95))
  content(to, $i + j = n$, anchor: "west", padding: 0.15)
})

// Proof of Lemma 1.2, p. 177: the exact sequences of complexes
// 0 → S_(k-1) → S_k → X ⊗_R Y_k → 0 and 0 → T_(k-1) → T_k → B ⊗_R Y_k → 0;
// the vertical maps f_(k-1), f_k, p_k (restrictions of f and ε ⊗ 1) are
// labelled on their right, the rows unlabelled.
#let filtration-sequences = grid-diagram(
  (
    ($0$, $S_(k-1)$, $S_k$, $X times.o_R Y_k$, $0$),
    ($0$, $T_(k-1)$, $T_k$, $B times.o_R Y_k$, $0.$),
  ),
  down: (
    (
      none,
      (label: $f_(k-1)$),
      (label: $f_k$),
      (label: $p_k$),
      none,
    ),
  ),
  gap: 6mm,
  row: 9mm,
)

// Proof of Lemma 1.2, p. 177: the long exact sequences of the two rows of
// `filtration-sequences`. Each row begins with an arrow from nothing and ends
// with the arrow ∂_n to nothing; ∂_(n+1) and ∂_n are labelled above the rows,
// the vertical maps p_(k n+1), f_(k-1 n), f_(k n), p_(k n) on their right.
#let filtration-homology = grid-diagram(
  (
    (
      none,
      $H_(n+1)(X times.o_R Y_k)$,
      $H_(n)(S_(k-1))$,
      $H_(n)(S_k)$,
      $H_(n)(X times.o_R Y_k)$,
      none,
    ),
    (
      none,
      $H_(n+1)(B times.o_R Y_k)$,
      $H_(n)(T_(k-1))$,
      $H_(n)(T_k)$,
      $H_(n)(B times.o_R Y_k)$,
      none,
    ),
  ),
  across: (
    (none, (label: $partial_(n+1)$), "->", "->", none),
    (none, (label: $partial_(n+1)$), "->", "->", none),
  ),
  down: (
    (
      none,
      (label: $p_(k n+1)$),
      (label: $f_(k-1 n)$),
      (label: $f_(k n)$),
      (label: $p_(k n)$),
      none,
    ),
  ),
  extra: (
    edge((0, 0), (1, 0), "->"),
    edge((0, 1), (1, 1), "->"),
    edge((4, 0), (5, 0), $partial_n$, "->", label-side: left),
    edge((4, 1), (5, 1), $partial_n$, "->", label-side: left),
  ),
  gap: 6mm,
  row: 9mm,
)
