#import "../main-defs.typ": *
// After main-defs: its operator `cd` must not shadow the diagram helper.
#import "common.typ": cd, edge, grid-diagram, node

// p. 149: a morphism of the category of extensions with abelian kernel
// over a fixed group G. Unlabelled rows; the vertical maps A_1 → A_2 and
// overline(G)_1 → overline(G)_2 unlabelled, G → G labelled id on its right.
#let extension-morphism-diagram = grid-diagram(
  (
    ($1$, $A_1$, $overline(G)_1$, $G$, $1$),
    ($1$, $A_2$, $overline(G)_2$, $G$, $1.$),
  ),
  down: ((none, "->", "->", (label: $id$), none),),
  gap: 6mm,
  row: 9mm,
)

// Definition 6.1, p. 150: the unique morphism of the free extension with
// abelian kernel into an extension E. Unlabelled rows; M → A unlabelled,
// f and id labelled on the right of their vertical maps.
#let free-extension-morphism-diagram = grid-diagram(
  (
    ($1$, $M$, $Phi$, $G$, $1$),
    ($1$, $A$, $overline(G)$, $G$, $1,$),
  ),
  down: ((none, "->", (label: $f$), (label: $id$), none),),
  gap: 6mm,
  row: 9mm,
)

// p. 150: the absolutely free extension maps into any extension. Unlabelled
// rows; N → A unlabelled, φ and id labelled on the right of their vertical
// maps.
#let free-presentation-morphism-diagram = grid-diagram(
  (
    ($1$, $N$, $F$, $G$, $1$),
    ($1$, $A$, $overline(G)$, $G$, $1.$),
  ),
  down: ((none, "->", (label: $phi$), (label: $id$), none),),
  gap: 6mm,
  row: 9mm,
)

// Proof of Proposition 6.3, p. 152: α: Φ → GP factors through the
// embedding ν: Φ → GA. Φ on the left; the arrow up to GA labelled ν on its
// upper left, the arrow down to GP labelled α on its lower left, β: GA → GP
// downwards labelled on its right.
#let magnus-factorization-diagram = cd(
  spacing: (8mm, 7mm),
  node((0, 1), $Phi$),
  node((1, 0), $G A$),
  node((1, 2), $G P.$),
  edge((0, 1), (1, 0), $nu$, "->", label-side: left),
  edge((1, 0), (1, 2), $beta$, "->", label-side: left),
  edge((0, 1), (1, 2), $alpha$, "->", label-side: right),
)

// Exercise 11, p. 159: the relation module of an amalgamated free product.
// The top row maps the induced free modules onto the induced fundamental
// ideals; the left vertical map between the top left module and P has
// heads at both ends (an isomorphism), the right one goes down to Δ_G; the
// bottom row P → Δ_G. No labels.
#let amalgam-relation-diagram = grid-diagram(
  (
    (
      $(P_1 times.o_(G_1) ZZ G) plus.o (P_2 times.o_(G_2) ZZ G)$,
      $(Delta_(G_1) times.o_(G_1) ZZ G)
      plus.o (Delta_(G_2) times.o_(G_2) ZZ G)$,
    ),
    ($P$, $Delta_G$),
  ),
  down: (("<->", "->"),),
  gap: 6mm,
  row: 9mm,
)
