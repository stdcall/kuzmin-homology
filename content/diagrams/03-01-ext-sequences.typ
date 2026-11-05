#import "../main-defs.typ": *
// After main-defs: its operator `cd` must not shadow the diagram helper.
#import "common.typ": edge, grid-diagram

// `n` unlabelled arrows of a row; a row labelled «E:» begins with `none`,
// no arrow from the label to the next object.
#let plain(n) = range(n).map(_ => "->")

// §1, p. 118: the extensions E and E' of B by A are equivalent. The rows
// are labelled E: and E': on the left; the vertical maps id, f, id have
// their labels on the right.
#let equivalence-diagram = grid-diagram(
  (
    ($E:$, $0$, $A$, $overline(B)$, $B$, $0$),
    ($E':$, $0$, $A$, $overline(B)'$, $B$, $0$),
  ),
  across: ((none, ..plain(4)), (none, ..plain(4))),
  down: (
    (none, none, (label: $id$), (label: $f$), (label: $id$), none),
  ),
  gap: 6mm,
  row: 9mm,
)

// Formula (3.5): the chain map f: X → E over id_B. The top row begins with
// an arrow into X_2 from nothing; the differentials d_2, d_1, ε and the
// maps μ, σ are labelled above the rows, the vertical maps f_1, f_0, id
// on their right, the map X_2 → 0 unlabelled.
#let extension-cocycle-diagram = grid-diagram(
  (
    (none, $X_2$, $X_1$, $X_0$, $B$, $0$),
    (none, $0$, $A$, $overline(B)$, $B$, $0.$),
  ),
  across: (
    (none, (label: $d_2$), (label: $d_1$), (label: $epsilon$), "->"),
    (none, "->", (label: $mu$), (label: $sigma$), "->"),
  ),
  down: ((none, "->", (label: $f_1$), (label: $f_0$), (label: $id$), none),),
  extra: (edge((0, 0), (1, 0), "->"),),
  gap: 6mm,
  row: 11mm,
)

// Proof of Proposition 1.1, p. 121: the chain map into the coamalgam
// sequence (3.4); unlabelled rows, the vertical maps f_1, f_0, id
// labelled on their right, X_2 → 0 unlabelled.
#let coamalgam-cocycle-diagram = grid-diagram(
  (
    ($X_2$, $X_1$, $X_0$, $B$, $0$),
    ($0$, $A plus.o A$, $hat(B)$, $B$, $0.$),
  ),
  down: (("->", (label: $f_1$), (label: $f_0$), (label: $id$), none),),
  gap: 6mm,
  row: 9mm,
)

// Proof of Proposition 1.1, p. 121: the extension built from a cocycle
// f_1; d_2, d_1, ε above the top row, the bottom row unlabelled, the
// vertical maps f_1, f_0, id labelled on their right, X_2 → 0 unlabelled.
#let cocycle-extension-diagram = grid-diagram(
  (
    ($X_2$, $X_1$, $X_0$, $B$, $0$),
    ($0$, $X_1 \/ Ker f_1$, $X_0 \/ d_1(Ker f_1)$, $B$, $0.$),
  ),
  across: (
    ((label: $d_2$), (label: $d_1$), (label: $epsilon$), "->"),
    "->",
  ),
  down: (("->", (label: $f_1$), (label: $f_0$), (label: $id$), none),),
  gap: 6mm,
  row: 9mm,
)

// Formula (3.7): a morphism f: E → E' of exact sequences of length n. The
// rows are labelled E: and E': on the left; μ, σ_(n-1), σ_0 and their
// primed versions above the arrows; the vertical maps id, f_(n-1), f_0,
// id labelled on their right; the column of dots has no vertical map.
#let sequence-morphism-diagram = grid-diagram(
  (
    ($E:$, $0$, $A$, $B_(n-1)$, $dots.c$, $B_0$, $B$, $0$),
    ($E':$, $0$, $A$, $B'_(n-1)$, $dots.c$, $B'_0$, $B$, $0.$),
  ),
  across: (
    (
      none,
      "->",
      (label: $mu$),
      (label: $sigma_(n-1)$),
      "->",
      (label: $sigma_0$),
      "->",
    ),
    (
      none,
      "->",
      (label: $mu'$),
      (label: $sigma'_(n-1)$),
      "->",
      (label: $sigma'_0$),
      "->",
    ),
  ),
  down: (
    (
      none,
      none,
      (label: $id$),
      (label: $f_(n-1)$),
      none,
      (label: $f_0$),
      (label: $id$),
      none,
    ),
  ),
  gap: 6mm,
  row: 12mm,
)

// P. 122: the chain map f: X → E over id_B for a sequence E of length n;
// unlabelled rows, the vertical maps f_n, f_(n-1), f_0, id labelled on
// their right, X_(n+1) → 0 unlabelled, none under the dots.
#let n-cocycle-diagram = grid-diagram(
  (
    ($X_(n+1)$, $X_n$, $X_(n-1)$, $dots.c$, $X_0$, $B$, $0$),
    ($0$, $A$, $B_(n-1)$, $dots.c$, $B_0$, $B$, $0$),
  ),
  down: (
    (
      "->",
      (label: $f_n$),
      (label: $f_(n-1)$),
      none,
      (label: $f_0$),
      (label: $id$),
      none,
    ),
  ),
  gap: 5mm,
  row: 9mm,
)

// Exercise 3: a chain map between two resolutions of the Z-module Z_2; a
// number k beside an arrow is the map 1 → k. The labels 2, 1 stand above
// the rows, the vertical maps 1 on their right, 0 → Z unlabelled.
#let two-resolutions-diagram = grid-diagram(
  (
    ($0$, $0$, $ZZ$, $ZZ$, $ZZ_2$, $0$),
    ($0$, $ZZ$, $ZZ$, $ZZ_4$, $ZZ_2$, $0$),
  ),
  across: (
    ("->", "->", (label: $2$), (label: $1$), "->"),
    ("->", (label: $2$), (label: $2$), (label: $1$), "->"),
  ),
  down: ((none, "->", (label: $1$), (label: $1$), (label: $1$), none),),
  gap: 6mm,
  row: 9mm,
)

// Exercise 3: the morphism f: E → E' with R = Z, A = Z, B = Z_2; the rows
// labelled E: and E': on the left, all maps unlabelled; the comma after
// the last 0 belongs to the sentence.
#let non-isomorphic-morphism-diagram = grid-diagram(
  (
    ($E:$, $0$, $ZZ$, $ZZ plus.o ZZ$, $ZZ$, $ZZ_2$, $0$),
    ($E':$, $0$, $ZZ$, $ZZ$, $ZZ_4$, $ZZ_2$, $0,$),
  ),
  across: ((none, ..plain(5)), (none, ..plain(5))),
  down: ((none, none, "->", "->", "->", "->", none),),
  gap: 6mm,
  row: 9mm,
)
