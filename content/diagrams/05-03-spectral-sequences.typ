#import "../main-defs.typ": *
// After main-defs: its operator `cd` must not shadow the diagram helper.
#import "common.typ": cd, edge, grid-diagram, node
#import "@preview/cetz:0.5.2"

// Рис. 7, p. 257: the filtration of the tensor product K = X ⊗_R Y. The point
// (i, j) of the lattice stands for X_i ⊗_R Y_j; F_m K sums the points on and
// to the left of the vertical line x = m, and the n-dimensional chains K_n
// lie on the line x + y = n. The book draws the lattice 0 ≤ i ≤ 6,
// 0 ≤ j ≤ 5 with m = 3 and n = 5, the axes beyond the lattice, the label
// x = m above the vertical line and x + y = n on a curved leader from the
// foot of the diagonal.
#let filtration-lattice = cetz.canvas(length: 5mm, {
  import cetz.draw: *
  let (columns, rows, m, n) = (6, 5, 3, 5)
  assert(m < n and n <= columns and n <= rows)
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
  // The vertical line x = m through the whole lattice and its label above.
  line((m, 0), (m, rows))
  content((m, rows + 0.75), $x = m$)
  line((0, n), (n, 0))
  // The leader leaves the foot of the line horizontally and reaches the
  // label horizontally.
  let from = (n + 0.1, 0.3)
  let to = (n + 2, 0.95)
  bezier(from, to, (n + 1, 0.3), (n + 1.1, 0.95))
  content(to, $x + y = n$, anchor: "west", padding: 0.15)
})

// Scheme (5.8), p. 262: the path of the computation of d²_(m k) for a
// bicomplex. The rows are a staircase: d′a_(m-1 k+1) ← a_(m-1 k+1) above,
// d′a_(m k) ← a_(m k) below, d′a_(m k) under a_(m-1 k+1) with an arrow up
// to it. All three arrows are plain and unlabelled.
#let d2-path = cd(
  spacing: (11mm, 4.5mm),
  node-inset: 1.8mm,
  node((0, 0), $d' a_(m-1 thin k+1)$),
  node((1, 0), $a_(m-1 thin k+1)$),
  node((1, 1), $d' a_(m thin k)$),
  node((2, 1), $a_(m thin k)$),
  edge((1, 0), (0, 0), "->"),
  edge((1, 1), (1, 0), "->"),
  edge((2, 1), (1, 1), "->"),
)

// Proof of Proposition 3.3, p. 263: the sequence (5.10) multiplied by X.
// The columns are X_(m-2), X_(m-1), X_m, the rows ⊗_B H_(k+1)(Y),
// ⊗_B Y_(k+1)/B_(k+1), ⊗_B C_k, ⊗_B H_k(Y). The rows map to the left, the
// columns down; the path of the computation is marked by double arrows: on
// the right of the plain arrow down, a double arrow up (↓⇑) in column 0
// between rows 0 and 1, in column 1 between rows 1 and 2, in column 2
// between rows 2 and 3; above the plain arrow to the left, a double arrow to
// the left in row 1 between columns 0 and 1 and in row 2 between columns 1
// and 2. No labels.
#let pair-gap = 3.5pt
#let up-pair(x, y) = (
  edge((x, y), (x, y + 1), "->", shift: -pair-gap),
  edge((x, y + 1), (x, y), "=>", shift: -pair-gap),
)
#let left-pair(x, y) = (
  edge((x + 1, y), (x, y), "=>", shift: -pair-gap),
  edge((x + 1, y), (x, y), "->", shift: pair-gap),
)
#let d2-connecting-path = grid-diagram(
  (
    (
      $X_(m-2) times.o_B H_(k+1)(Y)$,
      $X_(m-1) times.o_B H_(k+1)(Y)$,
      $X_m times.o_B H_(k+1)(Y)$,
    ),
    (
      $X_(m-2) times.o_B Y_(k+1) \/ B_(k+1)$,
      $X_(m-1) times.o_B Y_(k+1) \/ B_(k+1)$,
      $X_m times.o_B Y_(k+1) \/ B_(k+1)$,
    ),
    (
      $X_(m-2) times.o_B C_k$,
      $X_(m-1) times.o_B C_k$,
      $X_m times.o_B C_k$,
    ),
    (
      $X_(m-2) times.o_B H_(k)(Y)$,
      $X_(m-1) times.o_B H_(k)(Y)$,
      $X_m times.o_B H_(k)(Y)$,
    ),
  ),
  across: ("<-", (none, "<-"), ("<-", none), "<-"),
  down: (
    (none, "->", "->"),
    ("->", none, "->"),
    ("->", "->", none),
  ),
  extra: (
    ..up-pair(0, 0),
    ..up-pair(1, 1),
    ..up-pair(2, 2),
    ..left-pair(0, 1),
    ..left-pair(1, 2),
  ),
  gap: 7mm,
  row: 5mm,
)
