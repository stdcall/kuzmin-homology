#import "../main-defs.typ": *
// After main-defs: its operator `cd` must not shadow the diagram helper.
#import "common.typ": grid-diagram

// Formula (2.13): a square of a chain map f: C → C'. The differentials d_n,
// d'_n are labelled above the rows, the vertical maps f_n, f_(n-1) on their
// right; the period after C'_(n-1) ends the sentence.
#let chain-map-square = grid-diagram(
  (
    ($C_n$, $C_(n-1)$),
    ($C'_n$, $C'_(n-1).$),
  ),
  across: ((label: $d_n$), (label: $d'_n$)),
  down: (((label: $f_n$), (label: $f_(n-1)$)),),
  gap: 9mm,
  row: 10mm,
)

// Formula (2.16): the chain map f: C → C' covers α: B → B'. The
// augmentations ε, ε' are labelled above the rows, the vertical maps f_0, α
// on their right.
#let covering-square = grid-diagram(
  (
    ($C_0$, $B$),
    ($C'_0$, $B'$),
  ),
  across: ((label: $epsilon$), (label: $epsilon'$)),
  down: (((label: $f_0$), (label: $alpha$)),),
  gap: 9mm,
  row: 10mm,
)
