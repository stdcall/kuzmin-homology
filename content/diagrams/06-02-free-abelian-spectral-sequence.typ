#import "../main-defs.typ": *
// After main-defs: its operator `cd` must not shadow the diagram helper.
#import "common.typ": cd, edge, node
#import "06-01-rational-homology.typ": lattice-panel
#import "@preview/cetz:0.5.2"

// Scheme after theorem 2.2, p. 299: three terms E² on a staircase going
// down to the right, each the direct sum of two torsion parts; in the
// book the summands are split as below. The arrows are the differentials
// d²_(m k) (from t_k E²_(m k) to t_k E²_(m-2 k+1)) and d²_(m+2 k-1) (from
// t_(k-1) E²_(m+2 k-1) to t_(k-1) E²_(m k)): plain arrows up and to the
// left, from the first summand of the lower term to the second summand of
// the term above, no labels.
#let staircase-terms = (
  ($t_(k+1) E^2_(m-2 thin k+1)$, $t_k E^2_(m-2 thin k+1)$),
  ($t_k E^2_(m thin k)$, $t_(k-1) E^2_(m thin k)$),
  ($t_(k-1) E^2_(m+2 thin k-1)$, $t_(k-2) E^2_(m+2 thin k-1)$),
)
// The summands stand at the usual distance from ⊕; the arrows keep clear of
// their indices (`outset`).
#let d2-staircase = cd(
  spacing: (0pt, 7mm),
  node-inset: 0.5mm,
  ..staircase-terms
    .enumerate()
    .map(((row, (first, second))) => (
      node((3 * row, row), first, outset: 1.2mm),
      node((3 * row + 1, row), $plus.o$),
      node((3 * row + 2, row), second, outset: 1.2mm),
    ))
    .flatten(),
  ..range(1, staircase-terms.len()).map(row => edge(
    (3 * row, row),
    (3 * row - 1, row - 1),
    "->",
  )),
)

// Рис. 9, p. 300: E³ with coefficients in Z[1/2] (theorem 2.2), one panel,
// vertical axis 7 units, horizontal 9. Non-zero terms lie on the columns
// m = 0 (all k) and m = 1 (k = 0 and k ≥ 2: E³_(1 1) = 0); the book draws
// k ≤ 5. The dashed diagonal m + k = n runs from (0, n) for n = 4 down to
// the right past (1, n − 1); labels: tE³_(0 n) = t_n E²_(0 n) to the left of
// (0, n), E³_(1 n-1) = t_(n-1) E²_(1 n-1) to the right of (1, n − 1), and
// m + k = n beyond the end of the diagonal.
#let half-coefficients-e3 = cetz.canvas(length: 5mm, {
  import cetz.draw: *
  let last = 5
  let total = 4
  let terms = (
    range(last + 1).map(k => (0, k))
      + range(last + 1).filter(k => k != 1).map(k => (1, k))
  )
  lattice-panel((0, 0), 9, 7, terms)
  set-style(content: (
    padding: 0.15,
    wrap: text.with(top-edge: "bounds", bottom-edge: "bounds"),
  ))
  line(
    (0, total),
    (2.5, total - 2.5),
    stroke: (thickness: 0.5pt, dash: "dashed"),
    name: "diagonal",
  )
  content(
    (-0.45, total),
    $t E^3_(0 thin n) = t_n E^2_(0 thin n)$,
    anchor: "east",
  )
  content(
    (1.6, total - 1.15),
    $E^3_(1 thin n-1) = t_(n-1) E^2_(1 thin n-1)$,
    anchor: "west",
  )
  content((rel: (0.35, 0), to: "diagonal.end"), $m + k = n$, anchor: "west")
})

// Рис. 10, p. 306: E² and E³ with coefficients in Z_(p) for p = 5
// (theorem 2.11), two panels, vertical axes 14 units, horizontal 8; the book
// draws m ≤ 6, k ≤ 12 and labels the rows p and 2p left of the axis. Left,
// E²: for m > 0 only the rows k ≡ 0, 1 mod p remain (the row k = 0 too).
// Right, E³: the column m = 0, E³_(1 0) and the terms E³_(1 k) for k ≡ 0
// mod p, k > 0.
#let local-e2-e3 = cetz.canvas(length: 5mm, {
  import cetz.draw: *
  let prime = 5
  let (columns, rows) = (6, 12)
  let lattice = range(columns + 1)
    .map(m => range(rows + 1).map(k => (m, k)))
    .flatten()
    .chunks(2)
  let e2 = lattice.filter(((m, k)) => m == 0 or calc.rem(k, prime) <= 1)
  let e3 = e2.filter(((m, k)) => (
    m == 0 or (m == 1 and calc.rem(k, prime) == 0)
  ))
  let right = 10.1
  for (x, terms) in ((0, e2), (right, e3)) {
    lattice-panel((x, 0), 8, 14, terms)
    content((x - 0.95, prime), $p$)
    content((x - 0.95, 2 * prime), $2p$)
  }
})
