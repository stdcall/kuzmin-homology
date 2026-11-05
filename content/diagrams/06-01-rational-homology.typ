#import "../main-defs.typ": *
#import "@preview/cetz:0.5.2"

// The lattice of a spectral sequence, as in Рис. 8–10: the point (m, k)
// stands for the group E_(m k); a dot marks a term that may be non-zero.
// The axes start at the origin, heavier than other lines and with
// arrowheads; `origin` places the panel in the canvas, `width` and
// `height` are the lengths of the axes, `terms` lists the dotted points.
#let point-radius = 0.09
#let lattice-panel(origin, width, height, terms) = cetz.draw.group({
  import cetz.draw: *
  let (x0, y0) = origin
  // The style of the axes stays inside the group of the panel.
  set-style(line: (
    stroke: 1pt,
    mark: (end: "stealth", fill: black, scale: 0.8),
  ))
  line((x0, y0), (x0 + width, y0))
  line((x0, y0), (x0, y0 + height))
  for (m, k) in terms {
    circle((x0 + m, y0 + k), radius: point-radius, fill: black, stroke: none)
  }
})

// Рис. 8, p. 296: E² and E³ with rational coefficients, two panels side by
// side, axes 7 units long, no labels; the book draws the terms with
// m, k ≤ 5. Left, E²: by theorem 1.1, E²_(m k) = 0 for m > 0, k > 1, so the
// column m = 0 and the rows k = 0, 1 remain. Right, E³: the differentials
// d²_(m 0) are isomorphisms for m > 2 and a monomorphism for m = 2, so only
// the column m = 0 and E³_(1 0) remain.
#let rational-e2-e3 = cetz.canvas(length: 5mm, {
  let last = 5
  let lattice = range(last + 1)
    .map(m => range(last + 1).map(k => (m, k)))
    .flatten()
    .chunks(2)
  let e2 = lattice.filter(((m, k)) => m == 0 or k <= 1)
  let e3 = e2.filter(((m, k)) => m == 0 or (m == 1 and k == 0))
  lattice-panel((0, 0), 7, 7, e2)
  lattice-panel((8.1, 0), 7, 7, e3)
})
