// Commutative diagrams share the book's type and arrow style. Grid nodes
// and maps are supplied by each diagram; distinct arrowheads and dashed
// maps are specified at their edges.
#import "@preview/fletcher:0.5.8": diagram, edge, node

// `spacing` is the gap between neighbouring cells, each as wide as its
// widest node: wide nodes keep arrows of the same visible length.
// `size:` sets a diagram the book prints in smaller type: `0.85em`.
#let cd(spacing: 0pt, node-inset: 1mm, size: none, ..args) = {
  set text(top-edge: "bounds", bottom-edge: "bounds")
  set text(size: size) if size != none
  stack(diagram(
    spacing: spacing,
    node-shape: rect,
    node-inset: node-inset,
    edge-stroke: 0.45pt,
    label-size: 1em,
    label-sep: 0.25em,
    ..args,
  ))
}

// Two rows of maps joined by vertical maps, as in a morphism of exact
// sequences. `top` and `bottom` list the objects of the rows; `top-maps`
// and `bottom-maps` the labels of the arrows between consecutive objects
// (`[]` for an unlabelled arrow, `none` for no arrow); `down` the labels of
// the vertical maps under each column (`[]` unlabelled, `none` absent).
// Labels of the top row are above it, those of the bottom row below it, and
// those of the vertical maps on their left (`down-side: right`: on their
// right), as printed in the book.
// `dotted-down` and `dotted-bottom` list the columns or arrows printed dotted;
// `upward: true` turns the vertical maps upwards (a contravariant image).
// A wide ladder takes a smaller `gap` and node `inset` to fit the line.
#let ladder(
  top,
  bottom,
  down,
  top-maps: none,
  bottom-maps: none,
  dotted-down: (),
  dotted-bottom: (),
  upward: false,
  down-side: left,
  gap: 5mm,
  row: 9mm,
  inset: 1mm,
) = {
  let n = top.len()
  assert(bottom.len() == n and down.len() == n)
  let top-maps = if top-maps == none { range(n - 1).map(_ => []) } else {
    top-maps
  }
  let bottom-maps = if bottom-maps == none {
    range(n - 1).map(_ => [])
  } else { bottom-maps }
  let items = ()
  // `none` leaves a place of a row empty.
  for (x, object) in top.enumerate() {
    if object != none { items.push(node((x, 0), object)) }
  }
  for (x, object) in bottom.enumerate() {
    if object != none { items.push(node((x, 1), object)) }
  }
  for (x, label) in top-maps.enumerate() {
    if label != none { items.push(edge((x, 0), (x + 1, 0), label, "->")) }
  }
  for (x, label) in bottom-maps.enumerate() {
    if label != none {
      let style = if x in dotted-bottom { "..>" } else { "->" }
      items.push(edge((x, 1), (x + 1, 1), label, style, label-side: right))
    }
  }
  for (x, label) in down.enumerate() {
    if label != none {
      let style = if x in dotted-down { "..>" } else { "->" }
      // `down-side: right` prints the labels of the vertical maps on
      // their right, as some ladders of the book do.
      let side = if down-side == left { (left, right) } else { (right, left) }
      if upward {
        items.push(edge((x, 1), (x, 0), label, style, label-side: side.at(0)))
      } else {
        items.push(edge((x, 0), (x, 1), label, style, label-side: side.at(1)))
      }
    }
  }
  cd(spacing: (gap, row), node-inset: inset, ..items)
}

// Rows of objects joined by maps, as in a map of complexes. `rows` lists
// the objects of each row (`none` leaves a place empty); `across` the
// labels of the maps between consecutive objects of each row, printed above
// the arrows (`[]` unlabelled, `none` no arrow); `down` the labels of the
// maps from each row to the next, printed on the right of the arrows
// (`down-side: left`: on their left; `[]` unlabelled, `none` no arrow);
// `diagonal` the labels of the maps from each place down and to the left,
// printed on their upper left.
#let maps-grid(
  rows,
  across,
  down,
  diagonal: (),
  down-side: right,
  gap: 6mm,
  row: 11mm,
) = {
  let items = ()
  for (y, objects) in rows.enumerate() {
    for (x, object) in objects.enumerate() {
      if object != none { items.push(node((x, y), object)) }
    }
  }
  for (y, labels) in across.enumerate() {
    for (x, label) in labels.enumerate() {
      if label != none { items.push(edge((x, y), (x + 1, y), label, "->")) }
    }
  }
  for (y, labels) in down.enumerate() {
    for (x, label) in labels.enumerate() {
      if label != none {
        // Fletcher's sides follow the direction of the edge: for a map
        // downwards its left is the physical right.
        let side = if down-side == right { left } else { right }
        items.push(edge((x, y), (x, y + 1), label, "->", label-side: side))
      }
    }
  }
  for (y, labels) in diagonal.enumerate() {
    for (x, label) in labels.enumerate() {
      if label != none {
        items.push(edge(
          (x, y),
          (x - 1, y + 1),
          label,
          "->",
          label-side: right,
        ))
      }
    }
  }
  cd(spacing: (gap, row), ..items)
}

// Rows of objects on a grid joined by maps, as in a short exact sequence of
// chain complexes. `rows` lists the objects of each row; `none` leaves a
// place empty. `across` gives the maps along the rows: one entry for every
// row, or one entry for all of them. An entry is `none` (no maps), a style
// for every map between neighbouring objects of the row, or an array with
// one map for each gap of the row. `down` gives, for each two consecutive
// rows, the vertical maps by column. A map is `none`, a style ("->", "<-"
// upwards, "=" an equality) or a dictionary `(style: …, label: …)`; labels
// stand above the horizontal maps and on the right of the vertical ones.
// `extra` adds further edges, such as diagonal maps.
#let grid-diagram(
  rows,
  across: "->",
  down: (),
  extra: (),
  gap: 5mm,
  row: 5mm,
  inset: 1mm,
  // A diagram the book prints in smaller type to fit the line: `0.85em`.
  size: none,
) = {
  let items = ()
  for (y, objects) in rows.enumerate() {
    for (x, object) in objects.enumerate() {
      if object != none { items.push(node((x, y), object)) }
    }
  }
  let map(from, to, spec) = {
    if spec == none { return () }
    let (style, label) = if type(spec) == dictionary {
      (spec.at("style", default: "->"), spec.at("label", default: []))
    } else { (spec, []) }
    (edge(from, to, label, style, label-side: left),)
  }
  let row-maps = if type(across) == array { across } else {
    rows.map(_ => across)
  }
  for (y, objects) in rows.enumerate() {
    let maps = row-maps.at(y)
    if maps == none { continue }
    for x in range(objects.len() - 1) {
      if objects.at(x) == none or objects.at(x + 1) == none { continue }
      let spec = if type(maps) == array { maps.at(x) } else { maps }
      items += map((x, y), (x + 1, y), spec)
    }
  }
  for (y, columns) in down.enumerate() {
    for (x, spec) in columns.enumerate() {
      items += map((x, y), (x, y + 1), spec)
    }
  }
  let diagram = cd(spacing: (gap, row), node-inset: inset, ..items, ..extra)
  if size == none { diagram } else { text(size: size, diagram) }
}
