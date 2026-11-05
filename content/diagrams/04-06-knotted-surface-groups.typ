#import "../main-defs.typ": *
#import "@preview/cetz:0.5.2"

// Рис. 2–6, pp. 213–215: knots lying on a horizontal plane and loops coming
// down to them from a point O above the plane.
//
// A picture is built from curves in space. A point is (x, y, z): x goes to
// the right and y away from the reader in the plane, z is the height above
// it. The book draws the plane as a parallelogram, the oblique parallel
// projection below. Where two curves cross in the picture, the one farther
// from the reader is broken: a strand that passes under another one, a loop
// that passes under a strand, the far edge of the plane behind a loop (the
// book breaks the edge in Рис. 3, except at the second leg of the left loop,
// and at one loop of Рис. 5 only: `edge-gaps` in `breaks`). The strands of
// a knot are tubes (a double line), the loops and the plane are lines;
// arrowheads give the direction of a strand or of a loop.

// The sides of the plane lean to the right, its depth is shortened.
#let slant = 0.18
#let fore = 0.44
#let project(p) = (p.at(0) + slant * p.at(1), fore * p.at(1) + p.at(2))
// Of two points with one image, the one with the greater value lies in
// front of and above the other.
#let nearness(p) = slant * p.at(0) - p.at(1) + fore * p.at(2)
// The point at depth y (or on the plane at height z) that the picture shows
// at (sx, sy): the plane positions follow the book's figures; the depths
// are chosen.
#let at-depth(sx, sy, y) = (sx - slant * y, y, sy - fore * y)
#let on-plane(sx, sy, z: 0.1) = at-depth(sx, sy, (sy - z) / fore)

#let vsub(p, q) = p.zip(q).map(((a, b)) => a - b)
#let lerp(p, q, t) = p.zip(q).map(((a, b)) => a + (b - a) * t)
#let dist(p, q) = calc.sqrt(vsub(p, q).map(a => a * a).sum())
#let cross2(a, b) = a.at(0) * b.at(1) - a.at(1) * b.at(0)

// A smooth curve through the points (centripetal Catmull–Rom spline), `n`
// samples between two neighbouring points.
#let spline(points, n: 10, closed: false) = {
  let m = points.len()
  let ext = if closed {
    (points.last(), ..points, points.at(0), points.at(1))
  } else {
    (
      lerp(points.at(1), points.at(0), 2),
      ..points,
      lerp(points.at(m - 2), points.at(m - 1), 2),
    )
  }
  let gap(p, q) = calc.max(calc.sqrt(dist(p, q)), 1e-6)
  let out = ()
  for i in range(1, ext.len() - 2) {
    let (p0, p1, p2, p3) = ext.slice(i - 1, i + 3)
    let t1 = gap(p0, p1)
    let t2 = t1 + gap(p1, p2)
    let t3 = t2 + gap(p2, p3)
    for k in range(n) {
      let t = t1 + (t2 - t1) * k / n
      let a1 = lerp(p0, p1, t / t1)
      let a2 = lerp(p1, p2, (t - t1) / (t2 - t1))
      let a3 = lerp(p2, p3, (t - t2) / (t3 - t2))
      let b1 = lerp(a1, a2, t / t2)
      let b2 = lerp(a2, a3, (t - t1) / (t3 - t1))
      out.push(lerp(b1, b2, (t - t1) / (t2 - t1)))
    }
  }
  if not closed { out.push(points.last()) }
  out
}

// The point and the unit direction (in the plane) of a sampled curve at the
// fraction `at` of its samples.
#let along(points, at, closed: false) = {
  let n = points.len()
  let x = at * (if closed { n } else { n - 1 })
  let i = calc.min(int(calc.floor(x)), if closed { n - 1 } else { n - 2 })
  let p = points.at(i)
  let q = points.at(calc.rem(i + 1, n))
  let d = vsub(q, p).slice(0, 2)
  let l = calc.sqrt(d.map(a => a * a).sum())
  (lerp(p, q, x - i), d.map(a => a / l))
}

// A loop round a strand: from the point `from` down the first leg, round
// the tip on the plane in front of the strand, up the second leg to `to`.
// The strand is a sampled curve; the loop goes round it at the fraction
// `at`. `first-over`: the first leg passes above the strand, the second
// under it (false: the other way round); `side` (1 or -1) puts the first
// leg after or before the tip along the strand. `reach` is how far the tip
// lies in front of the strand, `half` half the width of the loop. `via1`
// and `via2` shape the legs: points of the picture that the legs pass on
// their way from and to the base point, at the depth of the strand (or
// nearer or farther by a third number).
#let finger(
  strand,
  at,
  from,
  to,
  closed: false,
  first-over: true,
  side: 1,
  reach: 0.9,
  half: 0.3,
  rise: 0.4,
  via1: (),
  via2: (),
) = {
  let (p, t) = along(strand, at, closed: closed)
  // The tip lies straight below the strand in the picture.
  let n = (slant, -1).map(a => a / calc.sqrt(1 + slant * slant))
  // u along the strand, v toward the reader, height z.
  let place(u, v, z) = (
    p.at(0) + u * t.at(0) + v * n.at(0),
    p.at(1) + u * t.at(1) + v * n.at(1),
    z,
  )
  let low = 0.02
  let over-leg(s) = (place(s * half, -0.1, rise), place(s * half, reach, low))
  let under-leg(s) = (
    place(s * half, -0.55, rise),
    place(s * half, -0.4, low),
    place(s * half, reach, low),
  )
  let (down, up) = if first-over {
    (over-leg(side), under-leg(-side).rev())
  } else { (under-leg(side), over-leg(-side).rev()) }
  // A third number moves the point toward the reader (negative) or away.
  let via(points) = points.map(q => at-depth(
    q.at(0),
    q.at(1),
    p.at(1) + q.at(2, default: 0),
  ))
  spline(
    (
      from,
      ..via(via1),
      ..down,
      place(0, reach + half, low),
      ..up,
      ..via(via2),
      to,
    ),
    n: 8,
  )
}

// The lines of the pictures.
#let unit = 7.6mm
#let tube-width = 2.1pt
#let tube-core = 0.8pt
#let line-width = 0.75pt
#let clearance = 1.4pt
#let widths = (tube: tube-width, thread: line-width, edge: line-width)

#let prepare(curve) = {
  let flat = curve.points.map(project)
  let n = flat.len()
  let closed = curve.at("closed", default: false)
  let segs = if closed { n } else { n - 1 }
  let cum = (0.0,)
  for i in range(segs) {
    cum.push(cum.last() + dist(flat.at(i), flat.at(calc.rem(i + 1, n))))
  }
  (..curve, closed: closed, flat: flat, n: n, segs: segs, cum: cum)
}

// Boxes round runs of segments, to skip pairs of segments far apart.
#let chunk = 8
#let boxes(c) = range(0, c.segs, step: chunk).map(s => {
  let e = calc.min(s + chunk, c.segs)
  let pts = range(s, e + 1).map(i => c.flat.at(calc.rem(i, c.n)))
  let xs = pts.map(p => p.at(0))
  let ys = pts.map(p => p.at(1))
  (
    s: s,
    e: e,
    x0: calc.min(..xs),
    x1: calc.max(..xs),
    y0: calc.min(..ys),
    y1: calc.max(..ys),
  )
})

// For every curve, the places (arc length in the picture, half-length) where
// it passes behind another curve or behind itself and is broken.
#let breaks(curves) = {
  let cuts = curves.map(_ => ())
  let all-boxes = curves.map(boxes)
  for a in range(curves.len()) {
    for b in range(a, curves.len()) {
      let (ca, cb) = (curves.at(a), curves.at(b))
      for ba in all-boxes.at(a) {
        for bb in all-boxes.at(b) {
          if a == b and bb.e <= ba.s { continue }
          if (
            ba.x1 < bb.x0 or bb.x1 < ba.x0 or ba.y1 < bb.y0 or bb.y1 < ba.y0
          ) { continue }
          for i in range(ba.s, ba.e) {
            for j in range(bb.s, bb.e) {
              if (
                a == b
                  and (
                    j <= i + 1 or (ca.closed and i == 0 and j == ca.segs - 1)
                  )
              ) { continue }
              let p = ca.flat.at(i)
              let r = vsub(ca.flat.at(calc.rem(i + 1, ca.n)), p)
              let q = cb.flat.at(j)
              let w = vsub(cb.flat.at(calc.rem(j + 1, cb.n)), q)
              let den = cross2(r, w)
              if calc.abs(den) < 1e-12 { continue }
              let d = vsub(q, p)
              let u = cross2(d, w) / den
              let v = cross2(d, r) / den
              if u < 0 or u >= 1 or v < 0 or v >= 1 { continue }
              // Curves that only meet at their ends (loops at O).
              if (
                (u < 1e-9 or u > 1 - 1e-9) and (v < 1e-9 or v > 1 - 1e-9)
              ) { continue }
              let pa = lerp(
                ca.points.at(i),
                ca.points.at(calc.rem(i + 1, ca.n)),
                u,
              )
              let pb = lerp(
                cb.points.at(j),
                cb.points.at(calc.rem(j + 1, cb.n)),
                v,
              )
              let a-behind = nearness(pa) < nearness(pb)
              let (lo, hi, k, x, rl) = if a-behind { (a, b, i, u, r) } else {
                (b, a, j, v, w)
              }
              // The far edge of the plane is broken only where the book
              // breaks it: `edge-gaps` of a loop is `none` (the loop is drawn
              // across the edge) or the part (fractions of its samples) whose
              // crossings break it.
              if curves.at(lo).kind == "edge" {
                let gaps = curves.at(hi).at("edge-gaps", default: (0, 1))
                let s = (if a-behind { j } else { i }) / curves.at(hi).segs
                if gaps == none or s < gaps.at(0) or s > gaps.at(1) { continue }
              }
              let len-r = calc.sqrt(r.map(z => z * z).sum())
              let len-w = calc.sqrt(w.map(z => z * z).sum())
              let sin = calc.max(calc.abs(den) / (len-r * len-w), 0.25)
              let cos = (
                calc.abs(r.at(0) * w.at(0) + r.at(1) * w.at(1))
                  / (
                    len-r * len-w
                  )
              )
              let upper = widths.at(curves.at(hi).kind)
              let lower = widths.at(curves.at(lo).kind)
              let half = (
                (
                  (upper / 2 + clearance) / sin + lower / 2 * cos / sin
                )
                  / unit
              )
              let lrl = calc.sqrt(rl.map(z => z * z).sum())
              cuts.at(lo).push((curves.at(lo).cum.at(k) + x * lrl, half))
            }
          }
        }
      }
    }
  }
  cuts
}

// The point of the picture at arc length s of a curve.
#let point-at(c, s) = {
  let total = c.cum.last()
  let s = if c.closed { calc.rem-euclid(s, total) } else {
    calc.clamp(s, 0, total)
  }
  let i = 0
  while i < c.segs - 1 and c.cum.at(i + 1) < s { i += 1 }
  let len = c.cum.at(i + 1) - c.cum.at(i)
  let t = if len > 0 { (s - c.cum.at(i)) / len } else { 0 }
  lerp(c.flat.at(i), c.flat.at(calc.rem(i + 1, c.n)), t)
}

// The part of a curve between arc lengths a < b (b may pass the start of a
// closed curve).
#let piece(c, a, b) = {
  let total = c.cum.last()
  let pts = (point-at(c, a),)
  for k in range(if c.closed { 2 } else { 1 }) {
    for i in range(c.n) {
      let s = c.cum.at(i) + k * total
      if s > a and s < b { pts.push(c.flat.at(i)) }
    }
  }
  pts.push(point-at(c, b))
  pts
}

// The visible parts of a curve with the given breaks; a scrap between two
// breaks shorter than `shortest` is left out.
#let shortest = 0.15
#let visible(c, cuts) = {
  let total = c.cum.last()
  if cuts.len() == 0 { return none }
  let merged = ()
  for (x0, x1) in cuts
    .map(((s, h)) => (s - h, s + h))
    .sorted(key: x => x.at(0)) {
    if merged.len() > 0 and x0 <= merged.at(-1).at(1) {
      merged.at(-1) = (merged.at(-1).at(0), calc.max(merged.at(-1).at(1), x1))
    } else { merged.push((x0, x1)) }
  }
  if c.closed {
    if merged.len() > 1 and merged.at(-1).at(1) - total >= merged.at(0).at(0) {
      let last = merged.pop()
      merged.at(0) = (
        last.at(0) - total,
        calc.max(merged.at(0).at(1), last.at(1) - total),
      )
    }
    let m = merged.len()
    range(m)
      .map(k => (
        merged.at(k).at(1),
        if k + 1 < m { merged.at(k + 1).at(0) } else {
          merged.at(0).at(0) + total
        },
      ))
      .filter(((a, b)) => b - a > shortest)
      .map(((a, b)) => piece(c, a, b))
  } else {
    let ends = ((none, 0), ..merged, (total, none))
    range(ends.len() - 1)
      .map(k => (ends.at(k).at(1), ends.at(k + 1).at(0)))
      .filter(((a, b)) => b - a > shortest)
      .map(((a, b)) => piece(c, a, b))
  }
}

// A filled arrowhead at the fraction `at` of the samples of a curve, in its
// direction (`back: true`: against it).
#let arrowhead(c, at, size: 1, back: false) = {
  import cetz.draw: line
  let x = at * c.segs
  let i = calc.min(int(calc.floor(x)), c.segs - 1)
  let s = c.cum.at(i) + (x - i) * (c.cum.at(i + 1) - c.cum.at(i))
  let p = point-at(c, s)
  let d = vsub(point-at(c, s + 0.05), point-at(c, s - 0.05))
  let l = calc.sqrt(d.map(a => a * a).sum())
  let d = d.map(a => a / l * (if back { -1 } else { 1 }))
  let e = (-d.at(1), d.at(0))
  let (len, wide) = (0.3 * size, 0.09 * size)
  let at-p(f, g) = (
    p.at(0) + f * d.at(0) + g * e.at(0),
    p.at(1) + f * d.at(1) + g * e.at(1),
  )
  line(
    at-p(len / 2, 0),
    at-p(-len / 2, wide),
    at-p(-len / 4, 0),
    at-p(-len / 2, -wide),
    close: true,
    fill: black,
    stroke: none,
  )
}

// A picture: the curves (kind "edge", "tube" or "thread"; points in space;
// `closed`), arrowheads (`on` the curve with this index, at the fraction
// `pos` of its samples; `size`, `back`) and labels (a point of the picture,
// the label, its anchor).
#let scene(curves, arrows: (), labels: ()) = cetz.canvas(length: unit, {
  import cetz.draw: *
  let curves = curves.map(prepare)
  let cuts = breaks(curves)
  let styles = (
    edge: ((paint: black, thickness: line-width, cap: "butt", join: "miter"),),
    thread: (
      (paint: black, thickness: line-width, cap: "butt", join: "round"),
    ),
    tube: (
      (paint: black, thickness: tube-width, cap: "butt", join: "round"),
      (paint: white, thickness: tube-core, cap: "butt", join: "round"),
    ),
  )
  for kind in ("edge", "tube", "thread") {
    for (c, cut) in curves.zip(cuts) {
      if c.kind != kind { continue }
      let parts = visible(c, cut)
      for stroke in styles.at(kind) {
        if parts == none {
          line(..c.flat, close: c.closed, stroke: stroke)
        } else {
          for part in parts { line(..part, stroke: stroke) }
        }
      }
    }
  }
  for a in arrows {
    arrowhead(
      curves.at(a.on),
      a.pos,
      size: a.at("size", default: 1),
      back: a.at("back", default: false),
    )
  }
  for (at, body, anchor) in labels {
    content(at, body, anchor: anchor)
  }
})

// The plane: the parallelogram of all pictures, 10 by 10.
#let plane = (
  kind: "edge",
  closed: true,
  points: ((0, 0, 0), (10, 0, 0), (10, 10, 0), (0, 10, 0)),
)

// The trefoil on the plane as the book draws it: points of its picture in
// order along the knot (the left lobe, the lower strand, the ring at the
// back, the right lobe, the upper strand) and their heights. A crossing is
// decided by the heights of its two strands: 0.2 above, 0.04 below. The two
// strands of a crossing must not share a point: a crossing at the end of a
// segment is taken for curves meeting at their ends and left unbroken.
#let trefoil = spline(
  (
    (2.94, 2.98, 0.12),
    (2.23, 2.84, 0.12),
    (1.87, 2.41, 0.12),
    (2.10, 1.93, 0.12),
    (2.74, 1.47, 0.12),
    (3.71, 1.19, 0.12),
    (4.68, 1.24, 0.2),
    (5.77, 1.41, 0.12),
    (6.74, 1.68, 0.12),
    (7.39, 2.14, 0.12),
    (7.60, 2.66, 0.12),
    (7.53, 3.11, 0.04),
    (7.23, 3.45, 0.12),
    (6.42, 3.61, 0.12),
    (5.52, 3.54, 0.12),
    (4.74, 3.30, 0.12),
    (4.23, 2.90, 0.12),
    (4.10, 2.66, 0.2),
    (4.06, 2.11, 0.12),
    (4.35, 1.56, 0.12),
    (4.58, 1.27, 0.04),
    (5.26, 1.01, 0.12),
    (6.29, 0.84, 0.12),
    (7.39, 0.86, 0.12),
    (8.35, 1.04, 0.12),
    (9.06, 1.50, 0.12),
    (9.35, 2.23, 0.12),
    (9.19, 2.90, 0.12),
    (8.61, 3.18, 0.12),
    (7.52, 3.15, 0.2),
    (6.42, 2.87, 0.12),
    (5.45, 2.60, 0.12),
    (4.81, 2.54, 0.12),
    (4.13, 2.71, 0.04),
    (3.52, 2.87, 0.12),
  ).map(((sx, sy, z)) => on-plane(sx, sy, z: z)),
  closed: true,
  n: 10,
)
#let trefoil-tube = (kind: "tube", closed: true, points: trefoil)

// Рис. 2, p. 213: the projection of the trefoil.
#let trefoil-projection = scene((plane, trefoil-tube))

// Рис. 3, p. 214: the generators of the trefoil group, a loop from O round
// each of its three arcs. The book breaks the far edge of the plane at the
// first (outer) leg of the left loop only.
#let trefoil-o = at-depth(5.4, 5.9, 6.5)
#let trefoil-generators = scene(
  (
    plane,
    trefoil-tube,
    ..((0.986, 1, (0, 0.5)), (0.386, 1, (0, 1)), (0.807, -1, (0, 1))).map((
      (at, side, gaps),
    ) => (
      kind: "thread",
      points: finger(
        trefoil,
        at,
        trefoil-o,
        trefoil-o,
        closed: true,
        side: side,
      ),
      edge-gaps: gaps,
    )),
  ),
  labels: ((project(trefoil-o), $O$, "south-east"),),
)

// A strand through points of its picture, at the height z.
#let strand(points, z) = spline(points.map(((sx, sy)) => on-plane(
  sx,
  sy,
  z: z,
)))

// Рис. 4, p. 214: a crossing of the knot, where the arc i goes on as the arc
// j under the arc k, and the loops x_i, x_j, x_k round the three arcs, each
// passing above its arc on the way down (the arrows). The book draws the
// loops across the far edge of the plane.
#let crossing-ij = strand(
  (
    (2.33, 3.91),
    (3.17, 3.86),
    (4.33, 3.61),
    (5.03, 3.36),
    (5.49, 3.11),
    (5.90, 2.86),
    (6.95, 2.25),
    (7.70, 1.89),
    (9.56, 1.41),
  ),
  0.08,
)
#let crossing-k = strand(
  (
    (2.24, 0.75),
    (2.70, 1.25),
    (3.75, 2.19),
    (5.49, 2.97),
    (7.24, 3.25),
    (
      10.00,
      3.77,
    ),
  ),
  0.2,
)
// A point of a loop shown at (sx, sy), above the plane and behind the
// strands.
#let above(sx, sy) = at-depth(sx, sy, 7.5)
#let crossing-o = above(7.06, 6.74)
#let crossing-loops = scene(
  (
    plane,
    (kind: "tube", points: crossing-ij),
    (kind: "tube", points: crossing-k),
    (
      kind: "thread",
      points: finger(
        crossing-ij,
        0.296,
        crossing-o,
        crossing-o,
        side: -1,
        reach: 1,
        half: 0.33,
        via1: ((4.68, 4.58),),
        via2: ((5.23, 4.40),),
      ),
      edge-gaps: none,
    ),
    (
      kind: "thread",
      points: finger(
        crossing-k,
        0.584,
        crossing-o,
        crossing-o,
        reach: 1,
        half: 0.22,
        via1: ((6.25, 4.58),),
        via2: ((5.67, 4.40),),
      ),
      edge-gaps: none,
    ),
    (
      kind: "thread",
      points: finger(
        crossing-ij,
        0.733,
        crossing-o,
        crossing-o,
        reach: 1,
        half: 0.27,
        via1: ((7.79, 5.80), (7.79, 4.97)),
        via2: ((7.15, 4.40),),
      ),
      edge-gaps: none,
    ),
  ),
  arrows: (
    (on: 1, pos: 0.108, size: 1.2),
    (on: 1, pos: 0.875, size: 1.2),
    (on: 2, pos: 0.2, size: 1.2),
    (on: 3, pos: 1 / 9),
    (on: 4, pos: 1 / 9),
    (on: 5, pos: 1 / 10),
  ),
  labels: (
    ((7.56, 6.58), $O$, "center"),
    ((5.09, 5.74), $x_i$, "center"),
    ((6.72, 4.72), $x_k$, "center"),
    ((8.37, 5.35), $x_j$, "center"),
    ((2.97, 3.36), $i$, "center"),
    ((8.08, 2.19), $j$, "center"),
    ((3.20, 1.25), $k$, "center"),
  ),
)

// Рис. 5, p. 215: the loop x_k^(-1) x_j x_k at the same crossing: x_k
// backwards round the arc k left of the crossing (passing under k on the
// way down), x_j round the arc j, then x_k round the arc k right of the
// crossing. The three loops meet at two corners below O.
#let product-ij = strand(
  (
    (2.11, 3.15),
    (3.33, 3.05),
    (4.50, 2.74),
    (5.09, 2.40),
    (5.38, 2.19),
    (6.70, 1.37),
    (8.30, 0.99),
    (9.62, 1.06),
  ),
  0.08,
)
#let product-k = strand(
  ((2.74, 0.72), (3.71, 1.40), (5.09, 2.26), (7.33, 3.22), (9.62, 3.74)),
  0.2,
)
#let product-o = above(6.38, 7.74)
#let product-corners = (above(6.38, 7.16), above(6.89, 6.89))
#let product-parts = (
  finger(
    product-k,
    0.43,
    product-o,
    product-corners.at(0),
    first-over: false,
    side: -1,
    reach: 1,
    half: 0.3,
    via1: ((4.69, 5.69), (4.31, 4.45), (4.25, 3.63)),
    via2: ((5.03, 4.32), (5.44, 5.48)),
  ),
  finger(
    product-ij,
    0.679,
    ..product-corners,
    side: -1,
    reach: 1,
    half: 0.3,
    via1: ((6.70, 5.83), (6.89, 4.32)),
    via2: ((7.58, 4.04), (7.55, 4.80), (7.33, 5.62)),
  ),
  finger(
    product-k,
    0.894,
    product-corners.at(1),
    product-o,
    reach: 1,
    half: 0.3,
    via1: ((8.33, 5.28, -1),),
    via2: (
      (8.08, 4.59),
      (8.11, 5.28),
      (8.21, 6.10),
      (7.83, 7.13),
      (
        7.01,
        7.71,
      ),
    ),
  ),
)
// The samples where the parts begin on the whole loop.
#let product-starts = (
  0,
  product-parts.at(0).len() - 1,
  product-parts.at(0).len() + product-parts.at(1).len() - 2,
)
#let product-loop = (
  product-parts.at(0)
    + product-parts.at(1).slice(1)
    + product-parts.at(2).slice(1)
)
// An arrow at a defining point of a part (a loop has 8 samples between two
// of its points).
#let product-arrow(part, point) = (
  (product-starts.at(part) + 8 * point) / (product-loop.len() - 1)
)
#let product-loop-picture = scene(
  (
    plane,
    (kind: "tube", points: product-ij),
    (kind: "tube", points: product-k),
    // The book breaks the far edge of the plane at the legs of x_k only.
    (
      kind: "thread",
      points: product-loop,
      edge-gaps: (product-starts.at(2) / (product-loop.len() - 1), 1),
    ),
  ),
  arrows: (
    (on: 1, pos: 1 / 7, size: 1.2),
    (on: 1, pos: 6 / 7, size: 1.2),
    (on: 2, pos: 1 / 4, size: 1.2),
    (on: 3, pos: product-arrow(0, 1)),
    (on: 3, pos: product-arrow(1, 2)),
    (on: 3, pos: product-arrow(2, 1)),
  ),
  labels: (
    ((5.82, 7.88), $O$, "center"),
    ((4.12, 5.52), $x_k^(-1)$, "center"),
    ((6.35, 3.91), $x_j$, "center"),
    ((8.84, 4.97), $x_k$, "center"),
    ((3.35, 2.57), $i$, "center"),
    ((8.35, 1.40), $j$, "center"),
    ((3.84, 0.93), $k$, "center"),
  ),
)

// Рис. 6, p. 215: a moment of the deformation of x_k^(-1) x_j x_k into x_i.
// The loop comes down above the arc i, runs on the plane under the arcs k,
// j and again k round the crossing and goes back up to O. Its points: the
// picture, then the depth above the plane or `none` on the plane.
#let deformation-ij = strand(
  (
    (2.54, 3.66),
    (3.44, 3.41),
    (4.34, 3.08),
    (4.99, 2.70),
    (5.45, 2.37),
    (5.74, 2.15),
    (6.56, 1.76),
    (7.38, 1.51),
    (8.66, 1.42),
  ),
  0.08,
)
#let deformation-k = strand(
  ((2.94, 1.29), (4.02, 1.81), (5.39, 2.30), (7.14, 2.70), (8.66, 2.97)),
  0.2,
)
#let deformation-loop = spline(
  (
    (6.50, 6.44, 7.0),
    (6.27, 5.78, 6.8),
    (5.98, 5.23, 6.6),
    (5.39, 4.67, 6.3),
    (5.10, 4.40, 6.1),
    (4.69, 4.04, 5.9),
    (4.40, 3.58, 5.7),
    (4.31, 3.08, 5.5),
    (4.29, 2.75, 5.2),
    (4.37, 2.37, 5.0),
    (4.46, 2.15, none),
    (4.64, 1.81, none),
    (4.99, 1.51, none),
    (5.39, 1.40, none),
    (5.86, 1.49, none),
    (6.27, 1.68, none),
    (6.62, 1.81, none),
    (6.91, 2.20, none),
    (7.03, 2.64, none),
    (7.14, 2.86, none),
    (7.17, 3.19, 6.8),
    (7.14, 3.52, 7.0),
    (6.97, 4.07, 7.1),
    (6.85, 4.40, 7.2),
    (6.68, 4.95, 7.2),
    (6.56, 5.67, 7.1),
    (6.50, 6.44, 7.0),
  ).map(((sx, sy, y)) => if y == none { on-plane(sx, sy, z: 0.02) } else {
    at-depth(sx, sy, y)
  }),
)
#let deformation-picture = scene(
  (
    plane,
    (kind: "tube", points: deformation-ij),
    (kind: "tube", points: deformation-k),
    // The book draws the loop across the far edge of the plane.
    (kind: "thread", points: deformation-loop, edge-gaps: none),
  ),
  arrows: (
    (on: 1, pos: 1 / 8, size: 1.2),
    (on: 1, pos: 7 / 8, size: 1.2),
    (on: 2, pos: 0.24, size: 1.2),
    (on: 3, pos: 2 / 26),
  ),
  labels: (
    ((7.03, 6.21), $O$, "center"),
    ((5.45, 5.33), $x_i$, "center"),
    ((3.58, 2.98), $i$, "center"),
    ((7.29, 1.10), $j$, "center"),
    ((3.97, 1.21), $k$, "center"),
  ),
)
