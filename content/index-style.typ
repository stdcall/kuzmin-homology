#import "main-defs.typ": *
#import "main-defs.typ" as defs

// The list of notation, generated from the marks beside the places that
// introduce each notation, in the order of these places: "ZG — групповое
// кольцо с. 13".
#let notation-entries = context {
  let entries = (:)
  let order = ()
  for mark in query(<notation-mark>) {
    let name = mark.value.notation
    if name not in entries {
      order.push(name)
      entries.insert(name, (meaning: mark.value.meaning, at: ()))
    }
    let entry = entries.at(name)
    assert(
      entry.meaning == mark.value.meaning,
      message: "Conflicting explanations of notation " + name,
    )
    let folio = counter(page).at(mark.location()).first()
    if entry.at.all(l => counter(page).at(l).first() != folio) {
      entry.at.push(mark.location())
    }
    entries.insert(name, entry)
  }
  set par(first-line-indent: 0pt, justify: false, hanging-indent: 1.5em)
  for name in order {
    let entry = entries.at(name)
    let pages = entry.at.map(l => box({
      metadata((
        kind: "cross-reference",
        target: "notation-mark",
        resolved: true,
        position: here().position(),
        target-position: l.position(),
      ))
      link(l, [с.~#counter(page).at(l).first()])
    }))
    block(width: 100%, above: 0pt, below: 0.45em, par[
      #eval(name, mode: "markup", scope: dictionary(defs)) —
      #eval(entry.meaning, mode: "markup", scope: dictionary(defs))
      #pages.join([, ])
    ])
  }
}

// The subject index as the author prints it: a heading on its own line
// with its pages, its subentries «—диагональное 14», a subentry that
// shares its first word with the one above continues indented
// («—свободная нильпотентная 23» / «разрешимая 23»), a third level is
// indented. The first heading of each letter begins with a capital, the
// others with a small letter. Pages and links are computed from the marks.

// Sorting: lower case, the parts of a path joined by a separator below any
// letter, so that a heading precedes its subentries.
#let sort-key(path) = {
  let key = lower(path.join("\u{1}"))
  key = key.replace(regex("\s*\([^)]*\)"), "")
  key = key.replace(regex("[,’'.$]"), "")
  key = key.replace("ё", "е")
  // «$C$-группа» stands under С, as in the author's index; other Latin
  // letters after the Cyrillic ones («HNN-расширения»).
  key = key.replace(regex("\\bc-"), "с-")
  key.replace(regex("[a-z]"), m => "\u{4ff}" + m.text)
}

#let locator(location) = box(context {
  metadata((
    kind: "cross-reference",
    target: "index-mark",
    resolved: true,
    position: here().position(),
    target-position: location.position(),
  ))
  link(location, str(counter(page).at(location).first()))
})

// The first letter of a heading in the case of its place in the letter
// group; a heading that begins with a formula or a Latin capital
// («C-группа», «HNN-расширение») keeps its form.
#let with-case(term, first) = {
  let head = term.clusters().first()
  if head.match(regex("^\p{Cyrillic}$")) == none { return term }
  (if first { upper(head) } else { lower(head) }) + term.slice(head.len())
}

#let markup(term) = eval(term, mode: "markup", scope: dictionary(defs))

#let index-entries = context {
  let entries = (:)
  for mark in query(<index-mark>) {
    let path = mark.value.path
    // Headings without pages of their own still head their subentries.
    for depth in range(1, path.len()) {
      let parent = path.slice(0, depth)
      let key = parent.join("\u{1f}")
      if key not in entries { entries.insert(key, (path: parent, at: ())) }
    }
    let key = path.join("\u{1f}")
    let record = entries.at(key, default: (path: path, at: ()))
    let target = mark.value.at("target", default: none)
    let location = if target == none { mark.location() } else {
      let found = query(target)
      assert(found.len() == 1, message: "Index target must exist uniquely")
      found.first().location()
    }
    let number = counter(page).at(location).first()
    if record.at.all(l => counter(page).at(l).first() != number) {
      record.at.push(location)
    }
    entries.insert(key, record)
  }
  // Headings that differ only in the case of their first letter are one.
  let merged = (:)
  for entry in entries.values() {
    let key = sort-key(entry.path)
    if key in merged {
      let found = merged.at(key)
      found.at += entry.at
      merged.insert(key, found)
    } else { merged.insert(key, entry) }
  }
  let sorted = merged.values().sorted(key: e => sort-key(e.path))
  // A heading without pages of its own takes its first subentry into its
  // line, as the author prints «теорема Кюннета 245» / «—сравнения 76».
  let joined = ()
  let skip = false
  for (i, entry) in sorted.enumerate() {
    if skip {
      skip = false
      continue
    }
    let next = sorted.at(i + 1, default: none)
    if (
      entry.path.len() == 1
        and entry.at.len() == 0
        and next != none
        and next.path.len() == 2
        and sort-key(next.path.slice(0, 1)) == sort-key(entry.path)
    ) {
      joined.push((
        path: (entry.path.first() + " " + next.path.last(),),
        at: next.at,
        children-of: entry.path.first(),
      ))
      skip = true
    } else { joined.push(entry) }
  }
  let sorted = joined
  let initial = none
  let sibling = none
  for entry in sorted {
    let depth = entry.path.len()
    let letter = upper(sort-key(entry.path).clusters().first())
    let first = letter != initial
    if first {
      if initial != none { v(0.9em, weak: true) }
      initial = letter
    }
    let term = entry.path.last()
    let pages = entry
      .at
      .sorted(key: l => counter(page).at(l).first())
      .map(locator)
      .join([, ])
    let words = term.split(" ")
    let line = if depth == 1 {
      sibling = none
      [#markup(with-case(term, first)) #pages]
    } else if depth == 2 {
      let continues = (
        sibling != none and words.len() > 1 and sibling == words.first()
      )
      sibling = words.first()
      if continues {
        [#h(1.5em)#markup(words.slice(1).join(" ")) #pages]
      } else [—#markup(term) #pages]
    } else [#h(1.5em)#markup(term) #pages]
    block(width: 100%, above: 0pt, below: 0.3em, par(
      hanging-indent: 2.5em,
      line,
    ))
  }
}
