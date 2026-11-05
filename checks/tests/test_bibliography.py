"""The list of literature: the printed order, and data changes in the .bib
files reach the PDF without editing any Typst descriptions."""
import json
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import unittest

import pymupdf

ROOT = Path(__file__).resolve().parents[2]

# The printed list [1]–[83] in its order.
PRINTED = '''
Cassels1969 Andre1965 Artamonov1998 Atiyah2003 Atiyah1995 Baumslag1971
Baumslag1980 Bestvina1997 Bieri1980 Bieri1976 Brown1987 Bourbaki1987
Vinberg2001 Gilbert1995 Gordon1981 Gorenstein1985 Gruenberg1960
Gruenberg1970 Gupta1973 Dicks1999 Kargapolov1972 Kervaire1965 Klyachko1993
Knuth1966 Kovacs1991 Cohn1975 Kostrikin2000 Crowell1967 Kuzmin1972
Kuzmin1974 Kuzmin1975 Kuzmin1977 Kuzmin1978 Kuzmin1982 Kuzmin1984
Kuzmin1987 Kuzmin1989 Kuzmin1995 Kuzmin1996 Kuzmin1988 Kuzmin1993
Kulikov1994 Kulikov2004 Kulikova2005 Kurosh1967 Curtis1969 Lang1968
Lyndon1948 Lyndon1950 MacLane1966 Magnus1974 Maltsev1949 Milnor1974
Nouaze1967 Remeslennikov1970 Serre1969 Serre1971 Semenov1996 Stallings1968
Stallings1965 Swan1969 Swan1960 Wong1968 Faddeev1947 Hannebauer1989
Hartley1991 Hillman1989 Hilton1997 Hall1954 Hopf1942 Hochschild1953
Zerck1990 Charlap1966 Chunikhin1964 Shmelkin1964 Shmelkin1967
Stammbach1973 Stammbach1977 Stohr1984 Stohr1987 Evens1991 Eilenberg1947a
Eilenberg1947b
'''.split()


def records(text):
    """Key -> {field: value} of the braced one-line fields of a .bib file."""
    found = {}
    for key, body in re.findall(r'^@\w+\{(\w+),\n(.*?)^\}', text, re.M | re.S):
        found[key] = dict(re.findall(r'^  (\w+) = \{(.*)\},$', body, re.M))
    return found


class Bibliography(unittest.TestCase):
    def test_original_list_and_text_references(self):
        bib = ((ROOT / 'references.bib').read_text() +
               (ROOT / 'editorial.bib').read_text())
        keys = re.findall(r'^@\w+\{([^,]+),', bib, re.M)
        listed = re.findall(r'<bib:([^>]+)>',
                            (ROOT / 'content/80-bibliography.typ').read_text())
        self.assertEqual(len(PRINTED), 83)
        self.assertEqual(listed, PRINTED)
        self.assertEqual(len(keys), len(set(keys)))
        self.assertTrue(set(listed).issubset(keys))
        related = set()
        for key in re.findall(r'^  related = \{([^}]+)\}', bib, re.M):
            related.update(key.split(','))
        self.assertTrue(related.issubset(keys))
        self.assertEqual(set(keys), set(listed) | related)
        fields = records(bib)
        self.assertEqual(set(fields), set(keys))
        for key, record in fields.items():
            with self.subTest(key=key):
                self.assertIn(record.get('language'),
                              {'russian', 'english', 'french', 'german'})
                if key in listed:
                    self.assertIn('annotation', record)
                    # Foreign names print with their Russian transcription.
                    if record['language'] != 'russian':
                        self.assertIn('{nameaddon}', record['annotation'])
                if 'doi' in record:
                    self.assertRegex(record['doi'], r'^10\.\d{4,5}/\S+$')

    def test_mutation_and_backlinks_ignore_the_bibliography_itself(self):
        with tempfile.TemporaryDirectory(prefix='kuzmin-bib-', dir='/tmp') as d:
            root = Path(d)
            shutil.copytree(ROOT / 'content', root / 'content')
            shutil.copytree(ROOT / 'assets/fonts', root / 'assets/fonts')
            original = (ROOT / 'references.bib').read_text()
            (root / 'references.bib').write_text(original)
            shutil.copy(ROOT / 'editorial.bib', root / 'editorial.bib')
            # Two mentions of Swan1960 on pages 1 and 2, a reference to it
            # inside the bibliography, and a record without mentions.
            (root / 'sample.typ').write_text('''
#import "content/book-style.typ": book-style
#import "content/main-defs.typ": *
#import "content/statements.typ": bib-entry
#import "content/bibliography-style.typ": bib-description
#show: book-style
Упоминание [@bib:Swan1960].
#pagebreak()
Ещё одно упоминание [@bib:Swan1960, с.~3].
#pagebreak()
#metadata(none) <bibliography-start>
#bib-entry[#bib-description("Swan1960")] <bib:Swan1960>
#bib-entry[#bib-description("Hopf1942")] <bib:Hopf1942>
Ссылка между записями: [@bib:Swan1960].
#metadata(none) <bibliography-end>
''')

            def compile(name):
                result = subprocess.run([
                    'typst', 'compile', '--ignore-system-fonts',
                    '--font-path', str(root / 'assets/fonts'),
                    '--root', str(root), str(root / 'sample.typ'),
                    str(root / name),
                ], capture_output=True, text=True)
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertEqual(result.stderr, '')
                with pymupdf.open(root / name) as pdf:
                    text = ' '.join(' '.join(p.get_text().split()) for p in pdf)
                    # The shared line-breaking rule keeps a text hyphen with
                    # its preceding inline formula; it adds no visible glyph.
                    text = text.replace('⁠', '')
                    links = {a['uri'] for p in pdf for a in p.get_links()
                             if 'uri' in a}
                    italic = {s['text'].strip() for p in pdf
                              for b in p.get_text('dict')['blocks']
                              for line in b.get('lines', [])
                              for s in line['spans']
                              if 'Italic' in s['font']}
                query = subprocess.run([
                    'typst', 'eval', '--root', str(root),
                    '--font-path', str(root / 'assets/fonts'),
                    '--ignore-system-fonts',
                    'query(metadata).map(it => it.value)',
                    '--in', str(root / 'sample.typ'), '--format', 'json',
                ], capture_output=True, text=True)
                self.assertEqual(query.returncode, 0, query.stderr)
                values = [x for x in json.loads(query.stdout)
                          if isinstance(x, dict)]
                mentions = [x for x in values
                            if x.get('target') == 'bib-mention:bib:Swan1960']
                self.assertEqual([m['description'] for m in mentions],
                                 ['1', '2'])
                self.assertFalse([x for x in values if x.get('target') ==
                                  'bib-mention:bib:Hopf1942'])
                return text, links, italic

            before, links, italic = compile('before.pdf')
            self.assertIn(
                '[1] Суон (Swan R. G.) Induced representations and projective '
                'modules // Ann. Math. — 1960. — v. 71. — p. 552–578. '
                '(Русский перевод: Математика. — 1964. — т. 8, № 1. — '
                'с. 3–28.) DOI: 10.2307/1969944 [1, 2]', before)
            self.assertIn('[2] Хопф (Hopf H.) Fundamentalgruppe', before)
            self.assertIn('https://doi.org/10.2307/1969944', links)
            self.assertIn('Суон', italic)
            self.assertNotIn('Swan R. G.', italic)

            def mutate(text, key, old, new):
                head = text.index('{' + key + ',')
                end = text.index('\n}\n', head)
                record = text[head:end]
                self.assertIn(old, record)
                return text[:head] + record.replace(old, new, 1) + text[end:]

            changed = original
            for key, old, new in [
                ('Swan1960', 'title = {Induced representations and projective '
                 'modules}', 'title = {Bibliography mutation probe}'),
                ('Swan1960', 'author = {Swan, R. G.}',
                 'author = {Changedauthor, R. G.}'),
                ('Swan1960', 'nameaddon = {Суон}', 'nameaddon = {Мутация}'),
                ('Swan1960', 'userb = {Ann. Math.}', 'userb = {Mutation J.}'),
                ('Swan1960', 'doi = {10.2307/1969944}',
                 'doi = {10.1234/mutation-probe}'),
                ('Swan1960', 'pages = {552--578}', 'pages = {9001--9002}'),
                ('Swan1964', 'pages = {3--28}', 'pages = {7001--7002}'),
            ]:
                changed = mutate(changed, key, old, new)
            (root / 'references.bib').write_text(changed)
            after, links, italic = compile('after.pdf')
            self.assertIn(
                '[1] Мутация (Changedauthor R. G.) Bibliography mutation probe '
                '// Mutation J. — 1960. — v. 71. — p. 9001–9002. '
                '(Русский перевод: Математика. — 1964. — т. 8, № 1. — '
                'с. 7001–7002.) DOI: 10.1234/mutation-probe [1, 2]', after)
            self.assertNotIn('Induced representations', after)
            self.assertIn('https://doi.org/10.1234/mutation-probe', links)
            self.assertIn('Мутация', italic)


if __name__ == '__main__':
    unittest.main()
