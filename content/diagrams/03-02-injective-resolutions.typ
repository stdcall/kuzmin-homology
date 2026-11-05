#import "../main-defs.typ": *
// After main-defs: its operator `cd` must not shadow the diagram helper.
#import "common.typ": grid-diagram

// Proof of Theorem 2.7: the cochain map f: Y → X extending id_A; the rows
// unlabelled and open to the right, the vertical maps id, f_0, f_n
// labelled on their right, none under the dots.
#let injective-comparison-diagram = grid-diagram(
  (
    ($0$, $A$, $Y_0$, $dots.c$, $Y_n$, $dots.c$),
    ($0$, $A$, $X_0$, $dots.c$, $X_n$, $dots.c$),
  ),
  down: (
    (none, (label: $id$), (label: $f_0$), none, (label: $f_n$), none),
  ),
  gap: 6mm,
  row: 9mm,
)

// P. 130: an exact sequence E of length n mapped into an injective
// resolution A → X; the rows unlabelled, the vertical maps id and f_n
// labelled on their right, those under B̄_0 and B̄_(n-1) unlabelled.
#let sequence-cocycle-diagram = grid-diagram(
  (
    ($0$, $A$, $overline(B)_0$, $dots.c$, $overline(B)_(n-1)$, $B$, $0$),
    ($0$, $A$, $X_0$, $dots.c$, $X_(n-1)$, $X_n$, $X_(n+1)$),
  ),
  down: (
    (none, (label: $id$), "->", none, "->", (label: $f_n$), none),
  ),
  gap: 6mm,
  row: 9mm,
)
