#import "../main-defs.typ": source

// The EAN-13 symbol of the ISBN, drawn from its digits: the first digit
// selects the parity pattern of the left half; guard bars run longer.
#let ean13(digits) = {
  let l-codes = (
    "0001101",
    "0011001",
    "0010011",
    "0111101",
    "0100011",
    "0110001",
    "0101111",
    "0111011",
    "0110111",
    "0001011",
  )
  // R codes are the complements of L codes, G codes the R codes reversed.
  let r-code(d) = l-codes
    .at(d)
    .clusters()
    .map(b => if b == "0" { "1" } else {
      "0"
    })
    .join()
  let g-code(d) = r-code(d).rev()
  let parity = (
    "LLLLLL",
    "LLGLGG",
    "LLGGLG",
    "LLGGGL",
    "LGLLGG",
    "LGGLLG",
    "LGGGLL",
    "LGLGLG",
    "LGLGGL",
    "LGGLGL",
  )
  let d = digits.clusters().map(int)
  let total = range(12)
    .map(i => d.at(i) * if calc.odd(i) { 3 } else { 1 })
    .sum()
  assert(
    calc.rem(10 - calc.rem(total, 10), 10) == d.at(12),
    message: "EAN-13 check digit",
  )
  // (pattern, guard) pieces from left to right.
  let pieces = (("101", true),)
  for i in range(6) {
    let side = parity.at(d.at(0)).at(i)
    let digit = d.at(i + 1)
    pieces.push((
      if side == "L" { l-codes.at(digit) } else { g-code(digit) },
      false,
    ))
  }
  pieces.push(("01010", true))
  for i in range(6) { pieces.push((r-code(d.at(i + 7)), false)) }
  pieces.push(("101", true))
  let module = 0.33mm
  let height = 18mm
  let x = 0
  let bars = ()
  for (pattern, guard) in pieces {
    for bit in pattern.clusters() {
      if bit == "1" {
        bars.push(place(left + top, dx: 11 * module + x * module, rect(
          width: module,
          height: if guard { height + 1.6mm } else { height },
          fill: black,
          stroke: none,
        )))
      }
      x += 1
    }
  }
  let label(body, dx, width) = place(
    left + top,
    dx: dx,
    dy: height + 0.2mm,
    box(
      width: width,
      align(center, text(size: 7.5pt, body)),
    ),
  )
  box(width: (x + 18) * module, height: height + 3.6mm, {
    bars.join()
    place(left + top, dy: height + 0.2mm, text(size: 7.5pt, str(d.at(0))))
    label(d.slice(1, 7).map(str).join(), 14 * module, 42 * module)
    label(d.slice(7, 13).map(str).join(), 61 * module, 42 * module)
  })
}

// Page 4: the bibliographic record and the imprint.
#let publication-page() = page(header: none, footer: none)[
  #source(4)
  #set text(size: 9.5pt)
  #set par(first-line-indent: 0pt, leading: 0.5em, spacing: 0.7em)
  УДК 512\
  ББК 22.14\
  #h(2em)К 89
  #v(5mm)
  #grid(
    columns: (13mm, 1fr),
    row-gutter: 0.6em,
    [], [*Кузьмин Ю. В.*],
    [К 89],
    par(justify: true, first-line-indent: 2em)[Гомологическая теория групп / Ю.
      В. Кузьмин. — М.: Изд-во «Факториал Пресс», 2006. — 352 с. — (Advanced
      Studies in Mathematics and Mechanics; Вып. 1).],

    [], [#h(2em)ISBN 5-88688-079-8],
  )
  #v(2mm)
  #pad(left: 13mm, {
    set text(size: 8.5pt)
    set par(justify: true, first-line-indent: (amount: 1.5em, all: true))
    [В книге дается систематическое изложение теории гомологий групп. Не
      предполагается глубоких знаний в смежных дисциплинах (теории колец и
      модулей, топологии). В помощь читателю подобрано большое количество
      упражнений. Упор сделан на различные приложения в теории групп.
      Значительная часть книги, около трети объема, посвящена материалу, который
      ранее не излагался в монографиях.]
    parbreak()
    [Книга рассчитана на студентов старших курсов университетов, аспирантов и
      научных работников.]
  })
  #align(right)[УДК 512\ ББК 22.14#h(4mm)]
  #align(center)[
    _Серия_\
    ADVANCED STUDIES IN MATHEMATICS AND MECHANICS\
    _Выпуск_ 1
  ]
  _Научное издание_\
  _Юрий Викторович Кузьмин_\
  #text(size: 11pt)[ГОМОЛОГИЧЕСКАЯ ТЕОРИЯ ГРУПП]
  #line(length: 100%, stroke: 0.4pt)
  #set text(size: 8.5pt)
  #par(justify: true)[Формат 70 × 100/16. Усл. печ. л. 27. Бумага офсетная №1.
    Гарнитура литературная. Подписано к печати 10.01.2006. Тираж 400 экз. Заказ
    № 2532.]

  #par(justify: true)[Издательство «Факториал Пресс», 117449, Москва, а/я 331;
    ЛР ИД № 00316 от 22.10.99.]
  #align(center)[e-mail: factorialco\@mail.ru]

  #par(justify: true)[Отпечатано с готовых диапозитивов издательства «Факториал
    Пресс» в ППП типографии «Наука» Академиздатцентра «Наука» РАН. 121099,
    Москва Г-99, Шубинский пер., 6.]
  #line(length: 100%, stroke: 0.4pt)
  #grid(
    columns: (1fr, 1fr),
    align: (left + bottom, left + bottom),
    [#h(5mm)ISBN 5-88688-079-8\ #ean13("9785886880793")],
    text(size: 10pt)[© Факториал Пресс, 2006.\ Все права защищены.],
  )
]
