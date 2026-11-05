#import "main-defs.typ": *
#import "statements.typ": *
#import "diagrams/06-01-rational-homology.typ": rational-e2-e3

#section[Гомологии с рациональными коэффициентами] <sec:rational-homology>

С рациональными гомологиями все обстоит просто, хотя и достаточно неожиданно.
Пусть $Lambda^(k)(M)$~— $k$-я внешняя степень модуля соотношений группы $B$ (мы
используем обозначения, введённые выше). Положим
$Lambda_(QQ)^(k)(M) = Lambda^(k)(M) times.o QQ$. При вычислении групп
$H_(k)(Phi, QQ)$ решающим является следующее утверждение.

#theorem[
  #source(295)Для любой группы $B$ и $k >= 2$ $Lambda_(QQ)^(k)(M)$~— плоский
  $B$-модуль.
] <th:rational-exterior-flat>

В теореме имеется в виду диагональное действие группы $B$ на внешней степени.
Определение плоских модулей обсуждалось в~§~@sec:tor-functors.

При $k = 1$ теорема неверна. Модуль $M times.o QQ$ может иметь любую
гомологическую размерность. Действительно, по теореме
редукции~@eq:mac-lane-reduction-h2
$ H_(n)(B, M times.o QQ) tilde.equiv H_(n+2)(B, QQ) quad (n > 0). $
Понятно, что для сколь угодно больших $n$ правая часть может быть отлична от
нуля.

Прежде чем доказывать теорему~@th:rational-exterior-flat, выведем из неё теорему
о гомологиях с рациональными коэффициентами. Вложение $M -> Phi$ индуцирует
гомоморфизм
$ H_(n)(M, QQ) times.o_B ZZ -> H_(n)(Phi, QQ) $
(подробнее см.~§~@sec:homology-definition). Так как $M$~— свободная абелева
группа, этот гомоморфизм можно переписать в виде
$ Lambda_(QQ)^(n)(M) times.o_B ZZ -> H_(n)(Phi, QQ). $

#theorem[
  Для любой группы $B$ при $n >= 2$ вложение $M -> Phi$ индуцирует изоморфизм
  $ H_(n)(Phi, QQ) tilde.equiv Lambda_(QQ)^(n)(M) times.o_B ZZ. $
] <th:rational-homology-exterior>

Отметим, что эта теорема носит отрицательный характер. Она утверждает, что кроме
очевидных циклов, связанных с внешней степенью, не существует циклов с
рациональными коэффициентами, которые бы присутствовали во всех расширениях
группы $B$ с абелевым ядром.

#proof(head: [Доказательство теоремы~@th:rational-homology-exterior.])[
  В спектральной последовательности свободного абелева расширения, сходящейся к
  $H_(n)(Phi, QQ)$,
  $
    E^2_(m thin k) = H_(m)(B, H_(k)(M, QQ)) = H_(m)(B, Lambda_(QQ)^(k)(M)).
  $
  Из теоремы~@th:rational-exterior-flat следует, что $E^2_(m thin k) = 0$ при
  $m > 0$, $k > 1$. По следствию~@cor:d2-base-characteristic-class
  гл.~@ch:extension-homology $d^2_(m thin 0)$ совпадает с умножением на
  характеристический класс~@eq:characteristic-class-sequence, а по
  предложению~@prop:free-extension-module-free главы~@ch:cohomology-ext для
  свободного абелева расширения модуль $P_G$
  из~@eq:characteristic-class-sequence свободен. Отсюда вытекает, что при
  $m > 2$ дифференциалы $d^2_(m thin 0)$~— изоморфизмы, а $d^2_(2 thin 0)$~—
  мономорфизм, следовательно, при $n >= 2$
  $
    H_(n)(Phi, QQ) = E^3_(0 thin n) = E^2_(0 thin n)
    = Lambda_(QQ)^(n)(M) times.o_B ZZ.
  $
]

#source(296)
#book-figure(
  rational-e2-e3,
  caption: [$E^2$ и $E^3$ с рациональными коэффициентами.],
) <fig:rational-e2-e3>

#proof(head: [Доказательство теоремы~@th:rational-exterior-flat.])[
  Воспользуемся индукцией по $k$. При $k = 2$ нужное утверждение следует из
  результатов §~@sec:free-quotient-groups. Действительно, пусть для краткости
  $R = ZZ B$. В~§~@sec:free-quotient-groups были указаны точные
  последовательности~@eq:spliced-sequence и~@eq:augmentation-symmetric-sequence.
  Если их срастить и домножить тензорно на $QQ$, получится точная
  последовательность
  $
    0 -> Lambda_(QQ)^(2)(M) -> (P times.o M) times.o QQ
    -> (P compose P) times.o QQ -> (R compose R) times.o QQ
    -> R times.o QQ -> 0.
  $
  Модули $R$ и $P times.o M$ свободны. По
  лемме~@lem:symmetric-square-free-cyclic и замечанию, которое ей предшествует,
  $R compose R$ и $P compose P$ можно представить в виде прямой суммы свободного
  модуля и модулей, индуцированных с подгрупп порядка 2. Отсюда, очевидно,
  следует, что они становятся плоскими $B$-модулями уже при тензорном домножении
  на $ZZ[1\/2]$~— кольцо двоично-рациональных чисел. Используя выписанную
  последовательность и сдвиг размерности, заключаем, что $Lambda_(QQ)^(2)(M)$~—
  плоский $B$-модуль.

  Чтобы сделать шаг индукции, рассмотрим альтернирование $alpha_k$
  $ alpha_k: Lambda_(QQ)^(k)(M) -> Lambda_(QQ)^(k-1)(M) times.o M. $
  По определению,
  $
    alpha_(k)(m_1 and dots and m_k) = sum_(i=1)^k (-1)^(k-i)
    m_1 and dots and hat(m)_i and dots and m_k times.o m_i
  $
  ($hat(m)_i$~— пропуск $m_i$). Легко видеть, что правая часть равенства
  кососимметрична, поэтому это отображение продолжается до линейного
  отображения. Рассмотрим также естественное отображение
  $ beta_k: Lambda_(QQ)^(k-1)(M) times.o M -> Lambda_(QQ)^(k)(M). $
  #source(297)Композиция $alpha_k$ и $beta_k$ совпадает с умножением на $k$,
  следовательно, это же верно для композиции индуцированных отображений
  $
    alpha_k^m & : Tor_(m)^(B)(L, Lambda_(QQ)^(k)(M))
                -> Tor_(m)^(B)(L, Lambda_(QQ)^(k-1)(M) times.o M), \
     beta_k^m & : Tor_(m)^(B)(L, Lambda_(QQ)^(k-1)(M) times.o M)
                -> Tor_(m)^(B)(L, Lambda_(QQ)^(k)(M))
  $
  (здесь $L$~— произвольный $B$-модуль). Так как мы присоединили рациональные
  коэффициенты, умножение на $k$ обратимо, поэтому $alpha_k^m$~— вложение. Таким
  образом, достаточно доказать, что плоским является модуль
  $Lambda_(QQ)^(k-1)(M) times.o M$. Используя
  предложение~@prop:tor-diagonal-shift главы~@ch:homology-tor и теорему
  редукции, имеем
  $
    Tor_(m)^(B)(L, Lambda_(QQ)^(k-1)(M) times.o M)
    tilde.equiv Tor_(m)^(B)(L times.o Lambda_(QQ)^(k-1)(M), M) tilde.equiv \
    tilde.equiv Tor_(m+2)^(B)(L times.o Lambda_(QQ)^(k-1)(M), ZZ)
    tilde.equiv Tor_(m+2)^(B)(L, Lambda_(QQ)^(k-1)(M)) = 0
  $
  — последнее равенство по предположению индукции.
]

Теоремы~@th:rational-exterior-flat и~@th:rational-homology-exterior были
доказаны автором в работе [@bib:Kuzmin1988]. В работе [@bib:Zerck1990] Церк
вычислил размерности групп $H_(n)(Phi, QQ)$ для случая, когда расширяемая группа
$B$ конечна.

#exercises[
  #exercise[
    Как описать $H_(1)(Phi, QQ)$? (Ответ: пространство, размерность которого
    равна числу свободных образующих.)
  ] <exc:rational-first-homology>

  #exercise[
    Пусть $T_(QQ)^(r)(M)$~— тензорная степень над $QQ$ модуля соотношений
    произвольной группы $B$. Докажите, что при $k >= 2$ $B$-модули
    $Lambda_(QQ)^(k)(M) times.o T_(QQ)^(r)(M)$ плоские (доказательство мало
    отличается от доказательства теоремы~@th:rational-exterior-flat). Верно ли
    это при $k = 1$?
  ] <exc:rational-exterior-tensor-flat>

  #exercise[
    Сформулируйте и докажите аналог теоремы~@th:rational-homology-exterior для
    когомологий. (Указание: надо рассмотреть отображение ограничения
    $ H^(n)(Phi, QQ) -> Hom_(B)(ZZ, H^(n)(M, QQ)).) $
  ] <exc:rational-cohomology-analog>
]
