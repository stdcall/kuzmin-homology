#import "numbering.typ": (
  numbered-record, place-key, printed-number, record-number,
)

// The page of the file is the printed page of the book.
#let printed-offset = 0

#let source(n, printed: none) = context {
  let printed = if printed == none { str(n - printed-offset) } else {
    printed
  }
  [#metadata((
    kind: "source",
    file-page: n,
    printed-page: printed,
    position: here().position(),
  ))]
}

// Numbers are semibold, but never lighter than a bold heading around them.
#let number-text(body) = context {
  let weight = text.weight
  let heavy = (
    weight in ("bold", "extrabold", "black")
      or (type(weight) == int and weight > 600)
  )
  text(weight: if heavy { weight } else { "semibold" }, style: "normal", body)
}

// Keep a reference's invisible position with its first visible word.
// Descriptive references may wrap over several lines.
#let caption-link(body, destination) = {
  if type(body) == str { body = text(body) }
  if body.func() in ([ ].func(), linebreak, parbreak, h, v, metadata) {
    return body
  }
  if body.func() == text and body.has("text") {
    let visible = body.text.match(regex("\\S(?:[\\s\\S]*\\S)?"))
    if visible == none { return body }
    return [#body.text.slice(0, visible.start)#link(
        destination,
        body.text.slice(visible.start, visible.end),
      )#body.text.slice(visible.end)]
  }
  if body.func() == [].func() {
    return body.children.map(it => caption-link(it, destination)).join()
  }
  if body.func() in (emph, strong) {
    let fields = body.fields()
    let inner = fields.remove("body")
    return body.func()(caption-link(inner, destination), ..fields)
  }
  if body.func() == link { body } else { link(destination, body) }
}
#let anchor-caption(body, marker, destination) = {
  if body.func() in ([ ].func(), linebreak, parbreak, h, v, metadata) {
    return (false, body)
  }
  if body.func() == text and body.has("text") {
    let word = body.text.match(regex("\\S+"))
    if word == none { return (false, body) }
    return (
      true,
      [#body.text.slice(0, word.start)#box[
          #marker#link(destination, body.text.slice(word.start, word.end))
        ]#caption-link(body.text.slice(word.end), destination)],
    )
  }
  if body.func() == [].func() {
    let done = false
    let parts = ()
    for child in body.children {
      if done { parts.push(caption-link(child, destination)) } else {
        let (found, content) = anchor-caption(child, marker, destination)
        done = found
        parts.push(content)
      }
    }
    return (done, parts.join())
  }
  if body.func() in (emph, strong, link) {
    let fields = body.fields()
    let (found, content) = anchor-caption(
      fields.remove("body"),
      marker,
      destination,
    )
    return (found, body.func()(content, ..fields))
  }
  (true, box[#marker#link(destination, body)])
}

#let reference-body(it, caption, trace: true) = context {
  let target = str(it.target)
  let prefix = target.split(":").first()
  let record = if it.element != none { numbered-record(it.target) }
  let number = if prefix in ("pg", "front") and it.element != none {
    (counter(page).at(it.element.location()).first(),)
  } else if record != none { record-number(record) }
  let pending = number == none
  // A section of another chapter is cited as chapter.section (§4.6), of
  // the same chapter by its number (§2); `@sec:…[]` gives the number only
  // (§4 гл. 1).
  let printed = if pending { "?" } else if (
    prefix in ("bib", "ch", "pg", "front") or it.supplement == []
  ) { str(number.last()) } else if prefix == "sec" {
    if number.first() == place-key(here()).first() {
      str(number.last())
    } else { number.map(str).join(".") }
  } else { printed-number(prefix, number) }
  if prefix == "eq" and it.supplement == [′] { printed += "′" }
  let body = if caption { it.supplement } else if prefix in ("eq", "ax") {
    let letter = printed.match(regex("^[A-Z]$")) != none
    text(
      style: "normal",
    )[(#number-text(if letter { emph(printed) } else { printed }))]
  } else { number-text(printed) }
  if not trace { return body }
  let destination = if pending { none } else if (
    prefix in ("pg", "front") or it.element.func() == math.equation
  ) { it.element.location() } else { record.location() }
  let marker = {
    metadata((
      kind: "cross-reference",
      target: target,
      resolved: not pending,
      printed: printed,
      target-position: if not pending { destination.position() },
    ))
    if prefix == "bib" {
      [#metadata((kind: "bibliography-mention", target: target))
        <bibliography-mention>]
    }
  }
  if caption and not pending {
    return anchor-caption(body, marker, destination).last()
  }
  let anchored = [#marker#body]
  if pending { anchored } else { link(destination, anchored) }
}

#let reference-rules(body, trace: true) = {
  show ref: it => {
    let caption = it.supplement not in (auto, none, [], [°], [′])
    let shown = reference-body(it, caption, trace: trace)
    if caption { shown } else { box(shown) }
  }
  body
}

#let idx(target: none, ..path) = {
  assert(path.named().len() == 0 and path.pos().len() > 0)
  [#metadata((
    kind: "index-mark",
    path: path.pos(),
    target: target,
  ))<index-mark>]
}

#let editorial-note-counter = counter("editorial-note")
#let ed-note(body) = {
  editorial-note-counter.step()
  context {
    // «*1)» in the text and in the note, a space before the note's text.
    let mark = "*" + str(editorial-note-counter.get().first()) + ")"
    footnote(numbering: _ => mark)[#h(0.3em)#body~— _Прим. ред._]
    counter(footnote).update(n => n - 1)
  }
}


#import "numbering.typ": exercise-numbers, formulas, series-counter, statements
// A chapter restarts the formulas, a section the statements and exercises.
#let chapter(title) = {
  formulas.update(0)
  statements.update(0)
  exercise-numbers.update(0)
  heading(level: 1, title)
}
#let section(title) = {
  statements.update(0)
  exercise-numbers.update(0)
  series-counter.update(0)
  heading(level: 2, title)
}
// A subheading inside a section («Редукция к симметрическим степеням…»):
// centred, bold, without a number, not in the contents; its formulas keep
// their normal weight, as printed.
#let subheading(body) = block(
  width: 100%,
  above: 1.8em,
  below: 1.1em,
  sticky: true,
  align(center, text(weight: "bold", body)),
)

// Preface, bibliography, lists: chapter-like openings without a number.
#let unnumbered-chapter(title, outlined: true) = heading(
  level: 1,
  numbering: none,
  outlined: outlined,
  title,
)
#let editorial-bibliography = []

#let subject-index(body) = {
  set par(first-line-indent: 0pt, justify: false, leading: 0.45em)
  set text(size: 9pt)
  columns(2, gutter: 5mm, body)
}

// A citation range «[32]–[40]»: both ends are native references, and the
// records between them in the order of the list also count this place as
// a mention.
#let bib-order = {
  read("80-bibliography.typ")
    .matches(regex("<bib:([A-Za-z0-9]+)>"))
    .map(m => m.captures.first())
}
#let cite-range(first, last) = {
  let key(it) = str(it.target).slice(4)
  let a = bib-order.position(k => k == key(first))
  let b = bib-order.position(k => k == key(last))
  assert(a != none and b != none and a < b, message: "cite-range: ends")
  [\[#first\]–\[#last\]]
  for k in bib-order.slice(a + 1, b) {
    let mention = (kind: "bibliography-mention", target: "bib:" + k)
    [#metadata(mention)<bibliography-mention>]
  }
}

// The letters and operators of the book. The integers, the rationals and
// the group ring are bold upright as printed: ZG, Q, Z_n.
#let ZZ = $bold(upright(Z))$
#let QQ = $bold(upright(Q))$
#let RR = $bold(upright(R))$
#let CC = $bold(upright(C))$
#let Hom = math.op("Hom")
#let Ext = math.op("Ext")
#let Tor = math.op("Tor")
#let Der = math.op("Der")
#let Aut = math.op("Aut")
#let Inn = math.op("Inn")
#let Out = math.op("Out")
#let End = math.op("End")
#let Ker = math.op("Ker")
#let Im = math.op("Im")
#let Coker = math.op("Coker")
#let Ann = math.op("Ann")
// «id» is italic in the book (id_A), also inside italic statements.
#let id = $i d$.body
#let cls = math.op("cls")
#let ext = math.op("ext")
#let alt = math.op("alt")
#let sign = math.op("sign")
#let Res = math.op("Res")
#let Cor = math.op("Cor")
#let res = math.op("res")
#let cor = math.op("cor")
#let tor = math.op("tor")
#let Inf = math.op("Inf")
// Delimiters that grow with their contents, where the book prints them so
// (the style keeps delimiters at text size, as TeX does).
#let grow(body) = math.lr(body, size: 100%)
#let wr = math.op("wr")
#let Wr = math.op("Wr")
#let cd = math.op("cd")
#let hd = math.op("hd")
#let rk = math.op("rk")

// A letterspaced run-in head inside the text («Т о ч н о с т ь в …»).
#let spaced(body) = text(tracking: 0.22em, body)

// The place and date of a preface on the left, the author on the right.
#let signature(where, name) = block(above: 2.6em, grid(
  columns: (1fr, auto),
  where, emph(name),
))

// An entry of the list of notation, beside the place that introduces the
// notation: the notation and its explanation as markup strings. The list
// gives the page of each place.
#let nidx(notation, meaning) = {
  assert(type(notation) == str and type(meaning) == str)
  [#metadata((
    kind: "notation-mark",
    notation: notation,
    meaning: meaning,
  ))<notation-mark>]
}
