# Гомологическая теория групп

Ю. В. Кузьмин.

Москва: Факториал Пресс, 2006. Серия Advanced Studies in Mathematics and
Mechanics, выпуск 1. ISBN 5-88688-079-8.

Систематическое изложение теории гомологий групп: расширения с абелевым
ядром, когомологии групп и функтор Ext, гомологии и функтор Tor,
спектральная последовательность расширения, гомологии свободных абелевых
расширений. Каждый параграф заканчивается упражнениями.

В [релизах](https://github.com/stdcall/kuzmin-homology/releases) —
книга с редакционными примечаниями, отдельный список исправлений
опечаток и ошибок оригинала и контрольные суммы SHA-256.

Для сборки нужны Typst 0.15.1, Typstyle 0.15.1, Tinymist 0.15.10,
Python 3.14, uv и just. Шрифты и их лицензии включены в `assets/fonts`.

```sh
just build
just check
just corrections
just check-sage   # точные вычисления, SageMath
just check-lean   # Lean 4 и mathlib
```

Результаты записываются в `build/`. Математические проверки описаны
в [checks/README.md](checks/README.md), соглашения исходников —
в [CONTRIBUTING.md](CONTRIBUTING.md).
