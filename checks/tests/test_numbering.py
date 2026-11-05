"""Compile the shared styles and inspect the actual numbered records."""
import json
from pathlib import Path
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[2]


class Numbering(unittest.TestCase):
    def test_book_scheme(self):
        # Statements share one counter in a section (2.1, 2.2), formulas count
        # through a chapter ((1.1), (1.2)), exercises restart in a section; a
        # section of another chapter is cited as chapter.section.
        source = '''#import "/content/book-style.typ": book-style
#import "/content/main-defs.typ": *
#import "/content/statements.typ": *
#show: book-style
#chapter[Первая] <ch:first>
#section[Первый] <sec:first>
$ a = a $ <eq:first>
#exercises[
  #exercise[Задание.] <exc:first>
  #exercise[Задание.] <exc:second>
]
#section[Второй] <sec:second>
#proposition[Утверждение.] <prop:first>
#corollary[Следствие.] <cor:first>
#lemma[Лемма.] <lem:first>
$ b = b $ <eq:second>
#exercises[
  #exercise[Задание.] <exc:third>
]
Ссылки: @prop:first, @lem:first, @eq:second, @exc:second, §~@sec:first.
#chapter[Вторая] <ch:second>
#section[Первый] <sec:third>
#theorem[Теорема.] <th:first>
$ c = c $ <eq:third>
Ссылки: @cor:first главы @ch:first, @eq:first, §~@sec:second,
§~@sec:second[] гл.~@ch:first, §~@sec:third.
'''
        with tempfile.TemporaryDirectory(prefix='kuzmin-', dir='/tmp') as d:
            driver = Path(d) / 'driver.typ'
            driver.write_text(source)
            result = subprocess.run([
                'typst', 'eval', '--root', str(ROOT),
                '--font-path', str(ROOT / 'assets/fonts'),
                '--ignore-system-fonts',
                'query(metadata).map(it => it.value)',
                '--in', '-', '--format', 'json',
            ], input=source, capture_output=True, text=True, cwd=ROOT)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(result.stderr, '')
            records = json.loads(result.stdout)
            numbered = [(r['family'], r['number']) for r in records
                        if r.get('kind') == 'numbered']
            self.assertEqual([n for f, n in numbered if f == 'eq'],
                             [[1, 1], [1, 2], [2, 1]])
            self.assertEqual([n for f, n in numbered if f == 'exc'],
                             [[1, 1, 1], [1, 1, 2], [1, 2, 1]])
            self.assertIn(('prop', [1, 2, 1]), numbered)
            self.assertIn(('cor', [1, 2, 2]), numbered)
            self.assertIn(('lem', [1, 2, 3]), numbered)
            self.assertIn(('th', [2, 1, 1]), numbered)
            refs = [r for r in records if r.get('kind') == 'cross-reference']
            self.assertEqual([r['printed'] for r in refs],
                             ['2.1', '2.3', '1.2', '2', '1',
                              '2.2', '1', '1.1', '1.2', '2', '1', '1'])
            self.assertTrue(all(r['resolved'] for r in refs))


if __name__ == '__main__':
    unittest.main()
