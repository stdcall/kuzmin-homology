"""Exact checks of Chapter 5, §§ 1-4 "Гомологии расширений" (Sage).

Run from the project root: sage -python checks/sage/chapter-5a.py (plain
asserts; do not use -O).  The last line is "ok chapter-5a: N checks".

Book: Ю. В. Кузьмин, «Гомологическая теория групп» (Факториал Пресс, 2006),
printed pp. 243-270.  Pages are the printed pages; labels are those of
content/05-01-*.typ ... 05-04-*.typ.  Modules are right modules (a b =
b^-1 a b in a semidirect product B A); matrices act on row vectors; chain
complexes of free abelian groups are lists of integer matrices
d_n: C_n -> C_(n-1).  Homology is computed exactly with Sage's modules over
ZZ (kernels, images, quotients and their invariants); group data come from
GAP (libgap, GAP core only: AbelianInvariants, AbelianInvariantsMultiplier
of finite groups and of finitely presented groups).  Nothing here compares
our text with the printed book.

What is checked, by section, and where the expected values come from:

section_1 (pp. 243-250).
  th:kunneth on 40 pairs of random complexes of free abelian groups
  (lengths 3, ranks <= 3, torsion in the homology): the invariants of
  H_n(X (x) Y) equal those of (+) H_i(X) (x) H_j(Y) (+) (+) Tor(H_i(X),
  H_j(Y)) (i + j = n, resp. n - 1); the same for the cochain complexes
  Hom(X (x) Y, Z) with Tor in degree i + j = n + 1
  (th:direct-product-cohomology; the shift n - 1 of homology is refuted
  there), and Hom(X (x) Y, Z) = Hom(X, Z) (x) Hom(Y, Z) as complexes (the
  natural map; for X = Y = Z it is Z = Hom(Z (x) Z, Z) -> Hom(Z, Z) (x)
  Hom(Z, Z) = Z (x) Z, the isomorphism of p. 249).
  th:direct-product-homology and exc:two-cyclic-groups-product-homology:
  H_n(Z_m x Z_k) from the tensor product of the periodic complexes
  (m, k <= 6, n <= 7) is Z_m + Z_k + Z_d^((n-1)/2) for odd n and Z_d^(n/2)
  for even n > 0 (d = gcd), as the theorem gives; H^n of the same groups
  by th:direct-product-cohomology; for 36 direct products of finite groups
  (Z_2, Z_3, Z_4, Z_2^2, S_3, D_8, Q_8, A_4) H_1 and H_2 (GAP: abelian
  invariants, Schur multiplier) agree with the theorem (the formula of
  exc:direct-product-h2-relations).  Universal coefficients from the
  Kunneth theorem (p. 248, as corrected: the resolution W -> Z):
  H_n(X (x) Z_k) = H_n(X) (x) Z_k + Tor(H_(n-1)(X), Z_k) for the periodic
  complexes of Z_m (m, k <= 6) and the random complexes.
  exc:free-abelian-homology-rank: H_n(Z^r) has rank C_r^n (iterated
  Kunneth with zero differentials, r <= 6) and C_(r-1)^n + C_(r-1)^(n-1)
  = C_r^n.  exc:free-abelian-exterior-resolution: the tensor product of
  the resolutions X^(i) (indices as corrected) is the Koszul complex of
  p. 252 (bracket as corrected) after the change of basis
  u_I -> (-1)^(n(n-1)/2) e_I (r <= 4, all basis elements), and both have
  d d = 0.
section_2 (pp. 250-255).
  prop:semidirect-resolution for S_3 = Z_2 Z_3, D_8 = Z_2 Z_4, Z_2 Z_2^2,
  A_4 = Z_3 Z_2^2 and Z_6 = Z_2 x Z_3 with X the periodic resolution of B
  and Y = R(A): the action of p. 251 commutes with d (random elements);
  G acts freely on the Z-basis of X_i (x) Y_j (i, j <= 2); the homology of
  X (x)_B (R(A) (x)_A Z) in degrees 1, 2 equals GAP's abelian invariants
  and Schur multiplier, and in degree 3 equals the homology of the
  normalized bar complex of G (S_3, Z_6).  prop:invariant-basis-differential:
  the diagonal action commutes with the Koszul differential for B
  permuting a basis (swap on Z^2, 3-cycle on Z^3), and does not for
  b = -1 on Z or b = [[1, 1], [0, 1]] on Z^2 (box of exponents).
  prop:invariant-basis-homology: for Z wr Z_2 and Z wr Z_3 the formula
  gives H_1 = Z + Z_2, Z + Z_3 (GAP: abelian invariants of the presented
  groups).  prop:wreath-homology and lem:exterior-power-free need n >= 1,
  k >= 1: Lambda^0(P) = Z is not free over B != 1 and H_0 W = Z, while the
  printed formula gives Z^2 at n = 0 (refuted); B = Z acts freely on its
  nonempty finite subsets (in a window) and fixes the empty one.
  exc:exterior-power-group-ring (hint corrected: k-element subsets
  S of B): for all groups of order <= 8 and all k the stabilizer of a
  k-subset has order dividing k and acts on b_1 ^ ... ^ b_k by a
  character, nontrivial in some cases.  exc:infinite-dihedral-homology:
  with the action u (x) 1 -> -u (x) 1 on Delta/Delta^2 the total complex
  gives Z_2 + Z_2 (n odd) and 0 (n even > 0), n <= 9 (printed answer),
  the free product Z_2 * Z_2 gives the same (exc:semidirect-answers-check),
  GAP: H_1 = Z_2^2.  exc:inverted-cyclic-homology: the chain automorphism
  theta(u_2i) = (-1)^i u_2i, theta(u_(2i-1)) = (-1)^i u_(2i-1) y^-1 of the
  periodic resolution of Z_m is semilinear for y -> y^-1 (j <= 9, m <= 7),
  and H_n(Z Z_m) from the total complex is Z_m for n = 0, 3 mod 4, 0 for
  n = 1, 2 mod 4 (n > 1), m = 3, 5, 7, n <= 12 (printed answer); GAP: H_1.
section_3 (pp. 255-264).
  Spectral sequences of filtered complexes computed from the definitions
  (Z^r, B^r, E^r of pp. 257-258) on 30 random filtered complexes over Z
  (elementary pieces with torsion, mixed by filtration-preserving
  unimodular changes of basis) and on tensor bicomplexes: B^r inside Z^r,
  B^r = d(Z^(r-1)_(m+r-1)), the book's E^r equals Z^r/(B^r +
  Z^(r-1)_(m-1)), E^0 = F_m/F_(m-1), E^1 = H(F_m/F_(m-1)),
  th:filtered-complex-spectral-sequence (E^(r+1) = Ker d^r / Im d^r,
  with d^r computed as an induced map), stabilization by r = m + 1 and
  E^infinity = gr H(K); exm:two-step-filtration ((5.5) as corrected,
  as corrected); exm:bicomplex-e2 (E^2 = H'H''); prop:bicomplex-d2 with the
  corrected indices: d^2 cls(a) = cls(d' a_(m-1, k+1)) in
  E^2_(m-2, k+1); prop:d2-sequence-multiplication on X (x)_B Y,
  B = Z_2, Y: Z B -> Z B multiplication by 1 + b: E^2 = Z_2 at (m, 0),
  (m, 1) for even m, d^2 is an isomorphism from (m, 0), E^3 = E^inf = Z_2
  at (0, 0) only and H(K) = Z_2 in degree 0; exc:hom-bicomplex (the sign
  (-1)^m is needed).
section_4 (pp. 264-270).  The Euler characteristic of p. 268 (correction
  corrected: homology, not cohomology): for random complexes the alternating
  sums of ranks of chains, of homology and of the dimensions over F_2,
  F_3 agree; prop:extension-euler-characteristic: chi(E^2) for Z^r
  (r <= 6), the Klein bottle group and the Heisenberg group is 0, as is
  chi(A) chi(B); exc:nilpotent-euler-characteristic needs G != 1 (chi(1) =
  1; the exercise is corrected to G != 1); exc:nilpotent-group-dimension
  for the
  Heisenberg group: E^2_(1 2) = H_1(Z, Lambda^2 Z^2) = Z survives, so
  H_3 != 0, and 3 = 1 + 2 is the sum of the ranks of the factors of the
  upper central series (corrected: factors, not members).

What is NOT established: the general theorems are checked on the stated
random and explicit examples only; GAP's Schur multipliers are taken as
independent values; the statements about spectral sequences of extensions
of § 4 (existence, E^2 term, edge maps) are not computed here (they are
used, and tested on examples, in chapter-5b.py).
"""

import random
from itertools import combinations, permutations, product

from sage.all import (ZZ, binomial, gcd, identity_matrix, libgap, matrix,
                      vector)

SCOPE = 'chapter-5a'
COUNT = [0]


def check(cond, what):
    assert bool(cond), 'FAILED: ' + what
    COUNT[0] += 1


def refuted(cond, what):
    assert not bool(cond), 'printed reading unexpectedly holds: ' + what
    COUNT[0] += 1


def gap(src):
    return libgap.eval(src)


def addto(d, k, c):
    if c:
        v = d.get(k, 0) + c
        if v:
            d[k] = v
        else:
            del d[k]


def dadd(d, e, s=1):
    for k, v in e.items():
        addto(d, k, s * v)


def vadd(x, y):
    return tuple(a + b for a, b in zip(x, y))


def perm_sign(p):
    s = 1
    p = list(p)
    for i in range(len(p)):
        for j in range(i + 1, len(p)):
            if p[i] > p[j]:
                s = -s
    return s


# ---------------------------------------------------------------------------
# Finitely generated abelian groups: (free rank, sorted prime powers)
# ---------------------------------------------------------------------------

def normal_form(invs):
    free = 0
    tors = []
    for m in invs:
        m = int(m)
        if m == 0:
            free += 1
        elif m > 1:
            for pp, e in ZZ(m).factor():
                tors.append(int(pp) ** int(e))
    return (free, tuple(sorted(tors)))


def ab_sum(*gs):
    free = sum(g[0] for g in gs)
    tors = []
    for g in gs:
        tors += list(g[1])
    return (free, tuple(sorted(tors)))


def ab_tensor(g, h):
    free = g[0] * h[0]
    tors = []
    for _ in range(g[0]):
        tors += list(h[1])
    for _ in range(h[0]):
        tors += list(g[1])
    for a in g[1]:
        for b in h[1]:
            d = int(gcd(a, b))
            if d > 1:
                tors.append(d)
    return normal_form([0] * free + tors)


def ab_tor(g, h):
    tors = []
    for a in g[1]:
        for b in h[1]:
            d = int(gcd(a, b))
            if d > 1:
                tors.append(d)
    return normal_form(tors)


ZERO = (0, ())


# ---------------------------------------------------------------------------
# Chain complexes of free abelian groups: ranks and matrices d_n (rows)
# ---------------------------------------------------------------------------

class Complex:
    """C_0, ..., C_top with d[n]: C_n -> C_(n-1) (row convention)."""

    def __init__(self, ranks, d):
        self.ranks = list(ranks)
        self.d = dict(d)
        for n in range(1, len(self.ranks)):
            if n not in self.d:
                self.d[n] = matrix(ZZ, self.ranks[n], self.ranks[n - 1])
        for n in range(2, len(self.ranks)):
            assert (self.d[n] * self.d[n - 1]).is_zero()

    def top(self):
        return len(self.ranks) - 1

    def H(self, n):
        V = ZZ ** self.ranks[n]
        Z = V.span(self.d[n].left_kernel().basis()) if n > 0 else V
        if n + 1 <= self.top():
            Bd = V.span(self.d[n + 1].rows())
        else:
            Bd = V.span([])
        return normal_form((Z / Bd).invariants())

    def H_mod(self, n, k):
        """H_n(C (x) Z_k)."""
        V = ZZ ** self.ranks[n]
        if n > 0:
            D = self.d[n]
            big = D.stack(k * identity_matrix(ZZ, self.ranks[n - 1])) \
                if self.ranks[n - 1] else D
            K = big.left_kernel()
            Z = V.span([v[:self.ranks[n]] for v in K.basis()])
        else:
            Z = V
        rows = [k * v for v in V.basis()]
        if n + 1 <= self.top():
            rows += list(self.d[n + 1].rows())
        return normal_form((Z / V.span(rows)).invariants())

    def cohom(self, n):
        """H^n(Hom(C, Z)), n < top."""
        V = ZZ ** self.ranks[n]
        dT = self.d[n + 1].transpose()          # C^n -> C^(n+1)
        Z = V.span(dT.left_kernel().basis())
        Bd = V.span(self.d[n].transpose().rows()) if n > 0 else V.span([])
        return normal_form((Z / Bd).invariants())


def tensor(X, Y):
    top = min(X.top(), Y.top())
    ranks = []
    offs = []
    for n in range(top + 1):
        off = {}
        tot = 0
        for i in range(n + 1):
            j = n - i
            off[i] = tot
            tot += X.ranks[i] * Y.ranks[j]
        ranks.append(tot)
        offs.append(off)
    d = {}
    for n in range(1, top + 1):
        D = matrix(ZZ, ranks[n], ranks[n - 1])
        for i in range(n + 1):
            j = n - i
            if i >= 1:
                blk = X.d[i].tensor_product(identity_matrix(ZZ, Y.ranks[j]))
                D.set_block(offs[n][i], offs[n - 1][i - 1], blk)
            if j >= 1:
                blk = (-1) ** i * identity_matrix(ZZ, X.ranks[i]) \
                    .tensor_product(Y.d[j])
                D.set_block(offs[n][i], offs[n - 1][i], blk)
        d[n] = D
    return Complex(ranks, d)


def periodic(m, top):
    """X (x)_(Z_m) Z for the periodic resolution: Z <-0- Z <-m- Z ..."""
    d = {}
    for n in range(1, top + 1):
        d[n] = matrix(ZZ, [[0 if n % 2 else m]])
    return Complex([1] * (top + 1), d)


def random_complex(top, rng):
    ranks = [rng.randint(1, 3) for _ in range(top + 1)]
    d = {}
    for n in range(1, top + 1):
        if n == 1:
            K = (ZZ ** ranks[0]).basis()
        else:
            K = d[n - 1].left_kernel().basis()
        rows = []
        for _ in range(ranks[n]):
            if K and rng.random() < 0.85:
                v = sum(rng.randint(-2, 2) * kv for kv in K)
                v = rng.choice([1, 1, 2, 3]) * v
                rows.append(list(v) if hasattr(v, '__iter__')
                            else [0] * ranks[n - 1])
            else:
                rows.append([0] * ranks[n - 1])
        d[n] = matrix(ZZ, ranks[n], ranks[n - 1], rows)
    return Complex(ranks, d)


# ---------------------------------------------------------------------------
# Section 1
# ---------------------------------------------------------------------------

def kunneth_expected(X, Y, n):
    parts = []
    for i in range(n + 1):
        parts.append(ab_tensor(X.H(i), Y.H(n - i)))
    for i in range(n):
        parts.append(ab_tor(X.H(i), Y.H(n - 1 - i)))
    return ab_sum(*parts)


def cokunneth_expected(X, Y, n, shift=1):
    parts = []
    for i in range(n + 1):
        parts.append(ab_tensor(X.cohom(i), Y.cohom(n - i)))
    for i in range(n + shift + 1):
        j = n + shift - i
        if 0 <= j:
            parts.append(ab_tor(X.cohom(i), Y.cohom(j)))
    return ab_sum(*parts)


def section_1():
    rng = random.Random(1)
    for trial in range(40):
        X = random_complex(3, rng)
        Y = random_complex(3, rng)
        T = tensor(X, Y)
        for n in range(3):
            check(T.H(n) == kunneth_expected(X, Y, n),
                  'th:kunneth (random complexes, n = %d)' % n)
        for n in range(2):
            check(T.cohom(n) == cokunneth_expected(X, Y, n),
                  'th:direct-product-cohomology form (random, n = %d)' % n)
        # universal coefficients (Y = Z_k in degree 0)
        for k in (2, 3, 4):
            for n in range(1, 3):
                check(X.H_mod(n, k) == ab_sum(
                    ab_tensor(X.H(n), normal_form([k])),
                    ab_tor(X.H(n - 1), normal_form([k]))),
                    'universal coefficients from th:kunneth (n = %d)' % n)
    # Hom(X (x) Y, Z) = Hom(X, Z) (x) Hom(Y, Z) as cochain complexes: with
    # f (x) g evaluated on x (x) y as f(x) g(y), the cochain differential
    # (transpose of d_(X (x) Y)) is d f (x) g + (-1)^i f (x) d g
    X = random_complex(3, rng)
    Y = random_complex(3, rng)
    T = tensor(X, Y)
    for n in range(0, 3):
        # degree n of Hom(X, Z) (x) Hom(Y, Z): pieces (i, n - i), the same
        # order and bases as T_n; its differential to degree n + 1
        D = matrix(ZZ, T.ranks[n], T.ranks[n + 1])
        roff = 0
        for i in range(n + 1):
            j = n - i
            coff = 0
            for i2 in range(n + 2):
                j2 = n + 1 - i2
                if i2 == i + 1:
                    D.set_block(roff, coff, X.d[i + 1].transpose()
                                .tensor_product(identity_matrix(ZZ,
                                                                Y.ranks[j])))
                if i2 == i and j2 == j + 1:
                    D.set_block(roff, coff, (-1) ** i * identity_matrix(
                        ZZ, X.ranks[i]).tensor_product(Y.d[j + 1]
                                                       .transpose()))
                coff += X.ranks[i2] * Y.ranks[j2]
            roff += X.ranks[i] * Y.ranks[j]
        check(D == T.d[n + 1].transpose(),
              'Hom(X (x) Y, Z) = Hom(X, Z) (x) Hom(Y, Z) as complexes '
              '(degree %d)' % n)
    check(matrix(ZZ, [[1]]).tensor_product(matrix(ZZ, [[1]])).det() == 1,
          'p. 249: Hom(Z (x) Z, Z) = Z -> Hom(Z, Z) (x) Hom(Z, Z) = Z (x) Z '
          'is an isomorphism')
    # cyclic groups: exc:two-cyclic-groups-product-homology
    for m in range(1, 7):
        for k in range(1, 7):
            X = periodic(m, 8)
            Y = periodic(k, 8)
            T = tensor(X, Y)
            dd = int(gcd(m, k))
            for n in range(1, 8):
                if n % 2:
                    want = normal_form([m, k] + [dd] * ((n - 1) // 2))
                else:
                    want = normal_form([dd] * (n // 2))
                got = T.H(n)
                check(got == want, 'H_%d(Z_%d x Z_%d) = %s' % (n, m, k, want))
                check(got == kunneth_expected(X, Y, n),
                      'th:direct-product-homology Z_%d x Z_%d, n = %d'
                      % (m, k, n))
            for n in range(0, 7):
                check(T.cohom(n) == cokunneth_expected(X, Y, n),
                      'th:direct-product-cohomology Z_%d x Z_%d, n = %d'
                      % (m, k, n))
            if m > 1 and k > 1 and dd > 1:
                refuted(all(T.cohom(n) == cokunneth_expected(X, Y, n, -1)
                            for n in range(1, 6)),
                        'H^n with Tor over i + j = n - 1, Z_%d x Z_%d'
                        % (m, k))
            for kk in (2, 3, 4):
                for n in range(1, 7):
                    check(X.H_mod(n, kk) == ab_sum(
                        ab_tensor(X.H(n), normal_form([kk])),
                        ab_tor(X.H(n - 1), normal_form([kk]))),
                        'H_n(Z_%d, Z_%d) by universal coefficients' % (m, kk))
    # direct products of finite groups, n = 1, 2 (GAP)
    names = ['CyclicGroup(2)', 'CyclicGroup(3)', 'CyclicGroup(4)',
             'DirectProduct(CyclicGroup(2), CyclicGroup(2))',
             'SymmetricGroup(3)', 'DihedralGroup(8)', 'QuaternionGroup(8)',
             'AlternatingGroup(4)']
    groups = [gap(nm) for nm in names]
    groups = [G.IsomorphismPermGroup().Image() for G in groups]
    h1 = [normal_form(G.AbelianInvariants()) for G in groups]
    h2 = [normal_form(G.AbelianInvariantsMultiplier()) for G in groups]
    for i in range(len(groups)):
        for j in range(i, len(groups)):
            P = libgap.DirectProduct(groups[i], groups[j])
            check(normal_form(P.AbelianInvariants())
                  == ab_sum(h1[i], h1[j]),
                  'th:direct-product-homology, H_1(%s x %s)'
                  % (names[i], names[j]))
            check(normal_form(P.AbelianInvariantsMultiplier())
                  == ab_sum(h2[i], h2[j], ab_tensor(h1[i], h1[j])),
                  'exc:direct-product-h2-relations, H_2(%s x %s)'
                  % (names[i], names[j]))
    # exc:free-abelian-homology-rank
    factor = Complex([1, 1, 0, 0, 0, 0, 0], {})     # X^(i) (x)_(G_i) Z
    T = factor
    for r in range(2, 7):
        T = tensor(T, factor)
        for n in range(r + 1):
            check(T.H(n) == (int(binomial(r, n)), ()),
                  'H_%d(Z^%d) free of rank C_%d^%d' % (n, r, r, n))
            check(binomial(r - 1, n) + binomial(r - 1, n - 1)
                  == binomial(r, n),
                  'C_(r-1)^n + C_(r-1)^(n-1) = C_r^n')
    # exc:free-abelian-exterior-resolution: tensor product = Koszul complex
    for r in range(1, 5):
        def koszul_d(I, sgn_tensor):
            out = {}
            n = len(I)
            for pos, j in enumerate(I):
                rest = I[:pos] + I[pos + 1:]
                s = (-1) ** pos if sgn_tensor else (-1) ** (n - 1 - pos)
                # (... ) (x) (x_j - 1)
                addto(out, (rest, j), s)
                addto(out, (rest, None), -s)
            return out
        for n in range(1, r + 1):
            for I in combinations(range(r), n):
                eps_n = (-1) ** (n * (n - 1) // 2)
                eps_n1 = (-1) ** ((n - 1) * (n - 2) // 2)
                t = koszul_d(I, True)
                k = koszul_d(I, False)
                check({key: eps_n * v for key, v in t.items()}
                      == {key: eps_n1 * v for key, v in k.items()},
                      'exc:free-abelian-exterior-resolution, r=%d, I=%s'
                      % (r, I))
        # d d = 0 for the Koszul differential (Laurent monomials)
        for n in range(2, r + 1):
            for I in combinations(range(r), n):
                tot = {}
                for (rest, j), c in koszul_d(I, False).items():
                    shift = tuple(1 if (j is not None and t == j) else 0
                                  for t in range(r))
                    for (rest2, j2), c2 in koszul_d(rest, False).items():
                        sh2 = tuple(1 if (j2 is not None and t == j2) else 0
                                    for t in range(r))
                        addto(tot, (rest2, vadd(shift, sh2)), c * c2)
                check(tot == {}, 'Koszul d d = 0, r=%d, n=%d' % (r, n))


# ---------------------------------------------------------------------------
# Section 2: semidirect products
# ---------------------------------------------------------------------------

class SemiFinite:
    """G = B A with B = Z_n cyclic acting on a finite abelian group
    A = Z_a1 x ... by an automorphism phi (b: a -> a phi)."""

    def __init__(self, nb, mods, phi):
        self.nb = nb
        self.mods = mods
        self.A = [tuple(v) for v in product(*[range(m) for m in mods])]
        self.phi = phi

    def add(self, a, c):
        return tuple((x + y) % m for x, y, m in zip(a, c, self.mods))

    def act(self, a, t):
        for _ in range(t % self.nb):
            a = self.phi(a)
        return a


def total_semidirect(S, top):
    """X (x)_B (R(A) (x)_A Z), X periodic for B = Z_nb; total complex up to
    degree top."""
    A = S.A
    tuples = {k: list(product(A, repeat=k)) for k in range(top + 1)}
    tidx = {k: {t: i for i, t in enumerate(tuples[k])} for k in tuples}

    def dY(k):
        D = matrix(ZZ, len(tuples[k]), len(tuples[k - 1]), sparse=True)
        for i, t in enumerate(tuples[k]):
            D[i, tidx[k - 1][t[:-1]]] += 1
            for j in range(k - 1):
                nt = t[:j] + (S.add(t[j], t[j + 1]),) + t[j + 2:]
                D[i, tidx[k - 1][nt]] += (-1) ** (k - 1 - j)
            D[i, tidx[k - 1][t[1:]]] += (-1) ** k
        return D

    def actB(k, s):
        D = matrix(ZZ, len(tuples[k]), len(tuples[k]), sparse=True)
        for i, t in enumerate(tuples[k]):
            D[i, tidx[k][tuple(S.act(a, s) for a in t)]] = 1
        return D
    dYs = {k: dY(k) for k in range(1, top + 1)}
    acts = {(k, s): actB(k, s) for k in range(top + 1) for s in range(S.nb)}
    ranks = []
    offs = []
    for n in range(top + 1):
        off = {}
        tot = 0
        for m in range(n + 1):
            off[m] = tot
            tot += len(tuples[n - m])
        ranks.append(tot)
        offs.append(off)
    d = {}
    for n in range(1, top + 1):
        D = matrix(ZZ, ranks[n], ranks[n - 1], sparse=True)
        for m in range(n + 1):
            k = n - m
            if m >= 1:
                if m % 2:
                    blk = acts[(k, S.nb - 1)] - identity_matrix(
                        ZZ, len(tuples[k]), sparse=True)
                else:
                    blk = sum(acts[(k, s)] for s in range(S.nb))
                D.set_block(offs[n][m], offs[n - 1][m - 1], blk)
            if k >= 1:
                D.set_block(offs[n][m], offs[n - 1][m], (-1) ** m * dYs[k])
        d[n] = D
    return Complex(ranks, {n: d[n].dense_matrix() for n in d})


def bar_complex(G, top):
    """Normalized bar complex of a finite group (GAP) tensored with Z."""
    els = list(G.AsSSortedList())
    e = G.Identity()
    nonid = [x for x in els if x != e]
    idx = {x: i for i, x in enumerate(nonid)}
    tuples = {k: list(product(range(len(nonid)), repeat=k))
              for k in range(top + 1)}
    tidx = {k: {t: i for i, t in enumerate(tuples[k])} for k in tuples}
    mul = {}
    for i, x in enumerate(nonid):
        for j, y in enumerate(nonid):
            z = x * y
            mul[(i, j)] = idx[z] if z != e else None
    d = {}
    for k in range(1, top + 1):
        D = matrix(ZZ, len(tuples[k]), len(tuples[k - 1]), sparse=True)
        for i, t in enumerate(tuples[k]):
            D[i, tidx[k - 1][t[1:]]] += 1
            for j in range(k - 1):
                z = mul[(t[j], t[j + 1])]
                if z is not None:
                    nt = t[:j] + (z,) + t[j + 2:]
                    D[i, tidx[k - 1][nt]] += (-1) ** (j + 1)
            D[i, tidx[k - 1][t[:-1]]] += (-1) ** k
        d[k] = D.dense_matrix()
    return Complex([len(tuples[k]) for k in range(top + 1)], d)


def fp_group(gens, rels):
    names = [g.strip() for g in gens.split(',')]
    body = ''.join('%s := F.%d; ' % (g, i + 1) for i, g in enumerate(names))
    src = ('CallFuncList(function() local F, %s; F := FreeGroup(%s); %s'
           'return F / [%s]; end, [])'
           % (', '.join(names), ', '.join('"%s"' % g for g in names), body,
              rels))
    return libgap.eval(src)


def section_2():
    rng = random.Random(2)
    cases = [
        ('S_3 = Z_2 Z_3', SemiFinite(2, [3], lambda a: ((-a[0]) % 3,)),
         'SymmetricGroup(3)', True),
        ('D_8 = Z_2 Z_4', SemiFinite(2, [4], lambda a: ((-a[0]) % 4,)),
         'DihedralGroup(8)', False),
        ('D_8 = Z_2 Z_2^2', SemiFinite(2, [2, 2], lambda a: (a[1], a[0])),
         'DihedralGroup(8)', False),
        ('A_4 = Z_3 Z_2^2', SemiFinite(3, [2, 2],
                                       lambda a: (a[1], (a[0] + a[1]) % 2)),
         'AlternatingGroup(4)', False),
        ('Z_6 = Z_2 x Z_3', SemiFinite(2, [3], lambda a: a),
         'CyclicGroup(6)', True),
    ]
    for name, S, gname, deg3 in cases:
        # phi is an automorphism of order dividing nb
        for a in S.A:
            check(S.act(a, S.nb) == a, '%s: phi^nb = 1' % name)
            for c in S.A:
                check(S.phi(S.add(a, c)) == S.add(S.phi(a), S.phi(c)),
                      '%s: phi additive' % name)
        # the action of p. 251 commutes with d in R(A) = V (x) Z A:
        # ((a_1..a_n) r) b = (a_1 b, ..., a_n b)(r b)
        def dR(y):
            out = {}
            for (t, g), c in y.items():
                n = len(t)
                addto(out, (t[:-1], S.add(t[-1], g)), c)
                for j in range(n - 1):
                    addto(out, (t[:j] + (S.add(t[j], t[j + 1]),) + t[j + 2:],
                                g), c * (-1) ** (n - 1 - j))
                addto(out, (t[1:], g), c * (-1) ** n)
            return out

        def actR(y):
            out = {}
            for (t, g), c in y.items():
                addto(out, (tuple(S.phi(a) for a in t), S.phi(g)), c)
            return out
        for _ in range(30):
            n = rng.randint(1, 3)
            y = {(tuple(rng.choice(S.A) for _ in range(n)),
                  rng.choice(S.A)): 1}
            check(dR(actR(y)) == actR(dR(y)),
                  '%s: action of p. 251 commutes with d' % name)
        # G acts freely on the basis of X_i (x) Y_j: basis (b', (t), g)
        # with (b, a) acting as b then translation by a
        nA = len(S.A)
        for j in range(3):
            basis = [(bp, t, g) for bp in range(S.nb)
                     for t in product(S.A, repeat=j) for g in S.A]
            seen = set()
            orbits = 0
            for x in basis:
                if x in seen:
                    continue
                orbits += 1
                orb = set()
                for b in range(S.nb):
                    for a in S.A:
                        bp, t, g = x
                        y = ((bp + b) % S.nb, tuple(S.act(c, b) for c in t),
                             S.add(S.act(g, b), a))
                        orb.add(y)
                check(len(orb) == S.nb * nA,
                      '%s: free orbit on X_i (x) Y_%d' % (name, j))
                seen |= orb
            check(orbits == len(S.A) ** j,
                  '%s: rank of X_i (x) Y_%d over G' % (name, j))
        top = 4 if deg3 else 3
        T = total_semidirect(S, top)
        G = gap(gname)
        check(T.H(0) == (1, ()), '%s: H_0 = Z' % name)
        check(T.H(1) == normal_form(G.AbelianInvariants()),
              'prop:semidirect-resolution %s: H_1 (GAP)' % name)
        check(T.H(2) == normal_form(G.AbelianInvariantsMultiplier()),
              'prop:semidirect-resolution %s: H_2 (GAP multiplier)' % name)
        if deg3:
            Bc = bar_complex(G, 4)
            check(T.H(3) == Bc.H(3),
                  'prop:semidirect-resolution %s: H_3 = %s (bar complex)'
                  % (name, T.H(3)))
    # prop:invariant-basis-differential: Koszul complex of Z^r with the
    # diagonal action (e_I (x) x^v) b = (e_I b) (x) x^(v b)
    def koszul_d(y):
        out = {}
        for (I, v), c in y.items():
            n = len(I)
            for pos, j in enumerate(I):
                rest = I[:pos] + I[pos + 1:]
                s = (-1) ** (n - 1 - pos)
                ej = tuple(1 if t == j else 0 for t in range(len(v)))
                addto(out, (rest, vadd(v, ej)), c * s)
                addto(out, (rest, v), -c * s)
        return out

    def wedge_act(I, M):
        # (e_i1 M) ^ ... ^ (e_in M) in the basis e_J
        r = M.nrows()
        out = {}
        rows = M.matrix_from_rows(list(I))
        for J in combinations(range(r), len(I)):
            v = rows.matrix_from_columns(list(J)).det() if I else 1
            if v:
                out[J] = v
        return out

    def actK(y, M):
        out = {}
        for (I, v), c in y.items():
            vb = tuple(int(x) for x in vector(ZZ, v) * M)
            for J, w in wedge_act(I, M).items():
                addto(out, (J, vb), c * w)
        return out
    for nm, M, ok in [('swap on Z^2', matrix(ZZ, [[0, 1], [1, 0]]), True),
                      ('3-cycle on Z^3', matrix(ZZ, [[0, 1, 0], [0, 0, 1],
                                                     [1, 0, 0]]), True),
                      ('-1 on Z', matrix(ZZ, [[-1]]), False),
                      ('[[1,1],[0,1]] on Z^2', matrix(ZZ, [[1, 1], [0, 1]]),
                       False)]:
        r = M.nrows()
        good = True
        for n in range(0, r + 1):
            for I in combinations(range(r), n):
                for v in product(range(-1, 2), repeat=r):
                    y = {(I, tuple(v)): 1}
                    good = good and koszul_d(actK(y, M)) == actK(koszul_d(y),
                                                                  M)
        if ok:
            check(good, 'prop:invariant-basis-differential: %s commutes' % nm)
        else:
            refuted(good, 'diagonal action commutes with d for %s' % nm)
    # prop:invariant-basis-homology: H_1 of Z wr Z_2, Z wr Z_3 (GAP)
    for nb, gens, rels, want in [
            (2, 'a, b, t', 't^2, Comm(a, b), t^-1*a*t*b^-1, t^-1*b*t*a^-1',
             normal_form([0, 2])),
            (3, 'a, b, c, t', 't^3, Comm(a, b), Comm(b, c), Comm(a, c), '
                't^-1*a*t*b^-1, t^-1*b*t*c^-1, t^-1*c*t*a^-1',
             normal_form([0, 3]))]:
        Gp = fp_group(gens, rels)
        # formula: H_1 = H_1(Z_nb) + H_0(Z_nb, Z[Z_nb]) = Z_nb + Z
        check(normal_form(Gp.AbelianInvariants()) == want,
              'prop:invariant-basis-homology: H_1(Z wr Z_%d) = Z + Z_%d (GAP)'
              % (nb, nb))
    # prop:wreath-homology / lem:exterior-power-free: n >= 1, k >= 1
    refuted((2, ()) == (1, ()), 'p. 254 printed: H_0 W = Lambda^0(P) (x)_B '
            'Z + H_0 B = Z^2')
    window = range(-3, 4)
    for k in range(0, 4):
        for Sset in combinations(window, k):
            for b in range(1, 3):
                moved = tuple(sorted(s + b for s in Sset))
                if k == 0:
                    check(moved == Sset, 'B = Z fixes the empty subset')
                else:
                    check(moved != Sset, 'B = Z acts freely on nonempty '
                          'finite subsets (k = %d)' % k)
    # exc:exterior-power-group-ring: stabilizers of k-subsets divide k
    nontriv = False
    for order in range(2, 9):
        for G in libgap.AllSmallGroups(order):
            els = list(G.AsSSortedList())
            idx = {x: i for i, x in enumerate(els)}
            tab = [[idx[x * y] for y in els] for x in els]
            for k in range(1, order + 1):
                ok = True
                for Sset in combinations(range(order), k):
                    stab = [c for c in range(order)
                            if sorted(tab[s][c] for s in Sset) == list(Sset)]
                    ok = ok and k % len(stab) == 0
                    # the character: sign of the permutation of S by c
                    for c in stab:
                        img = [Sset.index(tab[s][c]) for s in Sset]
                        if perm_sign(img) == -1:
                            nontriv = True
                check(ok, 'exc:exterior-power-group-ring: |Stab(S)| divides '
                      'k = %d (order %d)' % (k, order))
    check(nontriv, 'exc:exterior-power-group-ring: a nontrivial character '
          'occurs')
    # exc:infinite-dihedral-homology
    # Y (x)_A Z = Z_- (degree 1) + Z (degree 0), zero differential
    top = 10
    ranks = [1] + [2] * (top)
    d = {}
    for n in range(1, top + 1):
        # basis of K_n: (m = n, k = 0), (m = n - 1, k = 1)
        # d' on (m, 0): x^-1 - 1 = 0 (m odd), N = 2 (m even)
        # d' on (m, 1): -1 - 1 = -2 (m odd), N = 0 (m even)
        m0 = n
        a = 0 if m0 % 2 else 2
        if n == 1:
            D = matrix(ZZ, [[0], [0]])
        else:
            m1 = n - 1
            c = -2 if m1 % 2 else 0
            D = matrix(ZZ, [[a, 0], [0, c]])
        d[n] = D
    K = Complex(ranks, d)
    for n in range(1, top):
        want = normal_form([2, 2]) if n % 2 else ZERO
        check(K.H(n) == want, 'exc:infinite-dihedral-homology: H_%d = %s'
              % (n, want))
        Z2 = normal_form([2]) if n % 2 else ZERO
        check(K.H(n) == ab_sum(Z2, Z2), 'exc:semidirect-answers-check: '
              'Z_2 * Z_2, n = %d' % n)
    check(normal_form(fp_group('x, y', 'x^2, x*y*x*y').AbelianInvariants())
          == normal_form([2, 2]), 'infinite dihedral group: H_1 (GAP)')
    # the action on Delta: (y - 1) x = y^-1 - 1 = -(y - 1) y^-1, so on
    # Delta / Delta^2 = Z it is -1 (Laurent polynomials in y)
    from sage.all import LaurentPolynomialRing
    Ly = LaurentPolynomialRing(ZZ, 'y')
    yy = Ly.gen()
    check(yy ** -1 - 1 == -(yy - 1) * yy ** -1,
          'exc:infinite-dihedral-homology: (y - 1) x = -(y - 1) y^-1')
    # exc:inverted-cyclic-homology
    for m in range(2, 8):
        # Z[y]/(y^m - 1): dict exponent -> coeff
        def mulR(a, b):
            out = {}
            for i, c in a.items():
                for j, e in b.items():
                    addto(out, (i + j) % m, c * e)
            return out

        def inv_auto(a):
            return {(-i) % m: c for i, c in a.items()}
        N = {j: 1 for j in range(m)}
        y1 = {1: 1, 0: -1}

        def dcoef(j):
            return y1 if j % 2 else N

        def theta(j):
            i = (j + 1) // 2
            s = (-1) ** i
            return {0: s} if j % 2 == 0 else {(-1) % m: s}
        for j in range(1, 10):
            # d theta(u_j) = theta(d u_j): u_(j-1) c_(j-1->...)
            lhs = mulR(dcoef(j), theta(j))
            rhs = mulR(theta(j - 1), inv_auto(dcoef(j)))
            check(lhs == rhs, 'exc:inverted-cyclic-homology: theta semilinear '
                  'chain map, m=%d, j=%d' % (m, j))
        top = 13
        ranks = [1] + [2] * top
        d = {}
        for n in range(1, top + 1):
            # K_n basis: (0, n), (1, n - 1); d'' = (-1)^m d_Y on Y (x)_A Z,
            # d_Y(u_j) = 0 (j odd), m (j even); d'(1, j) = theta - 1
            def dy(j):
                return 0 if j % 2 else m
            sgn = {0: 1, 1: -1}

            def th(j):
                return (-1) ** ((j + 1) // 2)
            if n == 1:
                D = matrix(ZZ, [[dy(1)], [th(0) - 1]])
            else:
                D = matrix(ZZ, [[dy(n), 0],
                                [th(n - 1) - 1, sgn[1] * dy(n - 1)]])
            d[n] = D
        K = Complex(ranks, d)
        for n in range(2, top):
            if m % 2:
                want = normal_form([m]) if n % 4 in (0, 3) else ZERO
                check(K.H(n) == want, 'exc:inverted-cyclic-homology: '
                      'H_%d(Z Z_%d) = %s' % (n, m, want))
        Gp = fp_group('x, y', 'x^-1*y*x*y, y^%d' % m)
        check(K.H(1) == normal_form(Gp.AbelianInvariants()),
              'Z Z_%d: H_1 (GAP)' % m)


# ---------------------------------------------------------------------------
# Section 3: spectral sequences of filtered complexes
# ---------------------------------------------------------------------------

class Filtered:
    """K_n = Z^(rank_n) with basis vectors of filtration degree deg[n][i]
    (sorted increasingly) and d[n]: K_n -> K_(n-1) not raising it."""

    def __init__(self, ranks, deg, d):
        self.ranks, self.deg, self.d = ranks, deg, d
        self.top = len(ranks) - 1
        for n in range(1, self.top + 1):
            D = d[n]
            for i in range(ranks[n]):
                for j in range(ranks[n - 1]):
                    if D[i, j]:
                        assert deg[n - 1][j] <= deg[n][i]
        for n in range(2, self.top + 1):
            assert (d[n] * d[n - 1]).is_zero()
        self.maxdeg = max([max(x) if x else 0 for x in deg.values()] + [0])

    def V(self, n):
        return ZZ ** self.ranks[n]

    def F(self, m, n):
        V = self.V(n)
        return V.span([V.gen(i) for i in range(self.ranks[n])
                       if self.deg[n][i] <= m])

    def dimg(self, n, S):
        """d(S) in K_(n-1), S a submodule of K_n."""
        V1 = self.V(n - 1)
        if n == 0 or self.ranks[n - 1] == 0:
            return V1.span([])
        return V1.span([v * self.d[n] for v in S.basis()])

    def preimage(self, n, S, T):
        """{x in S : d x in T} (T a submodule of K_(n-1))."""
        if n == 0:
            return S
        if not S.basis():
            return S
        Smat = matrix(ZZ, S.basis())
        img = Smat * self.d[n]
        Tb = T.basis()
        big = img.stack(matrix(ZZ, Tb)) if Tb else img
        K = big.left_kernel()
        k = len(S.basis())
        return self.V(n).span([vector(ZZ, v[:k]) * Smat for v in K.basis()])

    def Zr(self, r, m, n):
        return self.preimage(n, self.F(m, n), self.F(m - r, n - 1)
                             if n > 0 else None)

    def Br(self, r, m, n):
        if n + 1 > self.top:
            return self.V(n).span([])
        return self.dimg(n + 1, self.F(m + r - 1, n + 1)).intersection(
            self.F(m, n))

    def E(self, r, m, n):
        Z = self.Zr(r, m, n)
        W = self.Br(r, m, n) + self.Zr(r - 1, m - 1, n) if r >= 1 else \
            self.Br(r, m, n) + self.F(m - 1, n)
        return Z, W


def random_filtered(rng, top=4, maxdeg=3):
    """Direct sum of elementary pieces Z u -> c Z v (filtration of u >=
    that of v), mixed by filtration-preserving unimodular changes of basis."""
    pieces = {n: [] for n in range(top + 1)}
    elems = []
    for _ in range(rng.randint(4, 8)):
        n = rng.randint(1, top)
        p = rng.randint(0, maxdeg)
        q = rng.randint(0, p)
        c = rng.choice([1, 1, 2, 3, 4, 0])
        elems.append((n, p, q, c))
    for _ in range(rng.randint(0, 3)):
        elems.append((rng.randint(0, top), rng.randint(0, maxdeg), None, 0))
    deg = {n: [] for n in range(top + 1)}
    for e in elems:
        n, p, q, c = e
        deg[n].append(p)
        if q is not None:
            deg[n - 1].append(q)
    # order bases by degree
    pos = {n: [] for n in range(top + 1)}
    for n in range(top + 1):
        order = sorted(range(len(deg[n])), key=lambda i: deg[n][i])
        pos[n] = {old: new for new, old in enumerate(order)}
        deg[n] = [deg[n][i] for i in order]
    ranks = [len(deg[n]) for n in range(top + 1)]
    cnt = {n: 0 for n in range(top + 1)}
    d = {n: matrix(ZZ, ranks[n], ranks[n - 1]) for n in range(1, top + 1)}
    for e in elems:
        n, p, q, c = e
        iu = pos[n][cnt[n]]
        cnt[n] += 1
        if q is not None:
            iv = pos[n - 1][cnt[n - 1]]
            cnt[n - 1] += 1
            d[n][iu, iv] = c
    # mix: P_n lower unitriangular w.r.t. degrees (x -> x P_n)
    P = {}
    for n in range(top + 1):
        M = identity_matrix(ZZ, ranks[n])
        for i in range(ranks[n]):
            for j in range(ranks[n]):
                if i != j and deg[n][j] <= deg[n][i] and rng.random() < 0.5:
                    M[i, j] = rng.randint(-2, 2)
        # make it unimodular: keep only entries with j < i (triangular)
        for i in range(ranks[n]):
            for j in range(i, ranks[n]):
                M[i, j] = 1 if i == j else 0
        P[n] = M
    newd = {}
    for n in range(1, top + 1):
        newd[n] = P[n] * d[n] * P[n - 1].inverse().change_ring(ZZ)
    return Filtered(ranks, deg, newd)


def tensor_filtered(X, Y, top):
    ranks, deg, offs = [], {}, []
    for n in range(top + 1):
        off = {}
        tot = 0
        dg = []
        for i in range(n + 1):
            j = n - i
            if i > X.top() or j > Y.top():
                off[i] = tot
                continue
            off[i] = tot
            tot += X.ranks[i] * Y.ranks[j]
            dg += [i] * (X.ranks[i] * Y.ranks[j])
        ranks.append(tot)
        deg[n] = dg
        offs.append(off)
    d = {}
    for n in range(1, top + 1):
        D = matrix(ZZ, ranks[n], ranks[n - 1])
        for i in range(n + 1):
            j = n - i
            if i > X.top() or j > Y.top():
                continue
            if i >= 1 and j <= Y.top():
                blk = X.d[i].tensor_product(identity_matrix(ZZ, Y.ranks[j]))
                D.set_block(offs[n][i], offs[n - 1][i - 1], blk)
            if j >= 1:
                blk = (-1) ** i * identity_matrix(ZZ, X.ranks[i]) \
                    .tensor_product(Y.d[j])
                D.set_block(offs[n][i], offs[n - 1][i], blk)
        d[n] = D
    return Filtered(ranks, deg, d)


def inv(M):
    return normal_form(M.invariants())


def check_filtered(K, name):
    top = K.top
    R = K.maxdeg + 2
    for n in range(top):
        for m in range(0, K.maxdeg + 1):
            k = n - m
            Fm, Fm1 = K.F(m, n), K.F(m - 1, n)
            for r in range(0, R + 1):
                Z = K.Zr(r, m, n)
                B = K.Br(r, m, n)
                check(B.is_submodule(Z), '%s: B^r in Z^r' % name)
                if r >= 1:
                    # p. 258: B^r = d(Z^(r-1)_(m+r-1 ...))
                    check(B == K.dimg(n + 1, K.Zr(r - 1, m + r - 1, n + 1))
                          if n + 1 <= top else True,
                          '%s: B^r = d(Z^(r-1)_(m+r-1, k-r+2))' % name)
                    # book's E^r = (Z^r + F_(m-1))/(B^r + F_(m-1)) equals
                    # Z^r/(B^r + Z^(r-1)_(m-1))
                    check(Z.intersection(B + Fm1)
                          == B + K.Zr(r - 1, m - 1, n),
                          '%s: Z^r meet (B^r + F_(m-1)) = B^r + '
                          'Z^(r-1)_(m-1)' % name)
                    check(inv((Z + Fm1) / (B + Fm1))
                          == inv(Z / (B + K.Zr(r - 1, m - 1, n))),
                          '%s: two forms of E^r' % name)
            # E^0 and E^1
            Z0 = K.Zr(0, m, n)
            check(Z0 == Fm, '%s: Z^0 = F_m K_n' % name)
            E0 = (Z0 + Fm1) / (K.Br(0, m, n) + Fm1)
            check(inv(E0) == inv(Fm / Fm1), '%s: E^0 = F_m/F_(m-1)' % name)
            # E^1 = H_n(F_m / F_(m-1))
            Zq = K.preimage(n, Fm, K.F(m - 1, n - 1) if n > 0 else None) \
                if n > 0 else Fm
            Bq = (K.dimg(n + 1, K.F(m, n + 1)) + Fm1) if n + 1 <= top \
                else Fm1
            Z1, B1 = K.Zr(1, m, n), K.Br(1, m, n)
            check(inv((Z1 + Fm1) / (B1 + Fm1)) == inv((Zq + Fm1) / Bq),
                  '%s: E^1 = H(F_m/F_(m-1))' % name)
            # stabilization and E^infinity = gr H
            Zinf = K.preimage(n, Fm, K.V(n - 1).span([])) if n > 0 else Fm
            check(K.Zr(m + 1, m, n) == Zinf, '%s: Z^(m+1) = Z^infinity'
                  % name)
            Bd = K.dimg(n + 1, K.V(n + 1)) if n + 1 <= top else \
                K.V(n).span([])
            Zinf1 = K.preimage(n, Fm1, K.V(n - 1).span([])) if n > 0 \
                else Fm1
            Binf = Bd.intersection(Fm)
            Einf = inv((Zinf + Fm1) / (Binf + Fm1))
            check(Einf == inv((Zinf + Bd) / (Zinf1 + Bd)),
                  '%s: E^infinity = F_m H / F_(m-1) H' % name)
            check(inv((K.Zr(R, m, n) + Fm1) / (K.Br(R, m, n) + Fm1)) == Einf
                  if n + 1 <= top - 1 else True,
                  '%s: E^r = E^infinity for large r' % name)
    # th:filtered-complex-spectral-sequence: E^(r+1) = Ker d^r / Im d^r
    for r in range(0, R):
        for n in range(1, top - 1):
            for m in range(0, K.maxdeg + 1):
                Z, W = K.E(r, m, n)
                Q = Z / W
                # d^r: E^r_(m, n) -> E^r_(m - r, n - 1)
                Zt, Wt = K.E(r, m - r, n - 1)
                Qt = Zt / Wt
                phi = Q.hom([Qt(g.lift() * K.d[n]) for g in Q.gens()], Qt)
                # incoming d^r: E^r_(m + r, n + 1) -> E^r_(m, n)
                Zs, Ws = K.E(r, m + r, n + 1)
                Qs = Zs / Ws
                psi = Qs.hom([Q(g.lift() * K.d[n + 1]) for g in Qs.gens()], Q)
                ker = phi.kernel()
                im = psi.image()
                check(im.V().is_submodule(ker.V()), '%s: d^r d^r = 0' % name)
                Zn, Wn = K.E(r + 1, m, n)
                check(inv(ker.V() / im.V()) == inv(Zn / Wn),
                      'th:filtered-complex-spectral-sequence %s r=%d m=%d '
                      'n=%d' % (name, r, m, n))


def section_3():
    rng = random.Random(3)
    for t in range(30):
        K = random_filtered(rng)
        check_filtered(K, 'random filtered complex %d' % t)
    # tensor bicomplexes: Example 2 (E^2 = H'H''), prop:bicomplex-d2
    for t in range(6):
        X = random_complex(3, rng)
        Y = random_complex(3, rng)
        K = tensor_filtered(X, Y, 3)
        check_filtered(K, 'tensor bicomplex %d' % t)
        # E^2_(m k) = H'_m H''_k: H''_(m k) = X_m (x) H_k(Y) (X free),
        # H' = homology of X (x) H_k(Y)
        for n in range(3):
            for m in range(n + 1):
                k = n - m
                Z, W = K.E(2, m, n)
                # H'_m H''_k for a tensor bicomplex: H_m(X (x) H_k(Y))
                Hk = Y.H(k)
                # build X (x) H_k(Y) via a free presentation of H_k(Y)
                tors = list(Hk[1])
                free = Hk[0]
                parts = []
                # H_m(X (x) Z^free) + H_m(X (x) Z_t)
                for _ in range(free):
                    parts.append(X.H(m))
                for tt in tors:
                    parts.append(X.H_mod(m, tt))
                check(inv(Z / W) == ab_sum(*parts) if parts else
                      inv(Z / W) == ZERO,
                      'exm:bicomplex-e2 (E^2 = H\'H\'\'), m=%d k=%d' % (m, k))
        # prop:bicomplex-d2 with the corrected indices
        for n in range(2, 3):
            for m in range(2, n + 1):
                k = n - m
                Z, W = K.E(2, m, n)
                Q = Z / W
                Zt, Wt = K.E(2, m - 2, n - 1)
                Qt = Zt / Wt
                for g in Q.gens():
                    a = g.lift()
                    # components by filtration degree
                    a_mk = vector(ZZ, [a[i] if K.deg[n][i] == m else 0
                                       for i in range(K.ranks[n])])
                    a_m1 = vector(ZZ, [a[i] if K.deg[n][i] == m - 1 else 0
                                       for i in range(K.ranks[n])])
                    trunc = a_mk + a_m1
                    check(trunc in Z, 'a_(mk) + a_(m-1,k+1) in Z^2')
                    dd = a_m1 * K.d[n]
                    dprime = vector(ZZ, [dd[i] if K.deg[n - 1][i] == m - 2
                                         else 0
                                         for i in range(K.ranks[n - 1])])
                    check(dprime in Zt, 'd\' a_(m-1,k+1) in Z^2_(m-2, k+1)')
                    check(Qt(dprime) == Qt(a * K.d[n]),
                          'prop:bicomplex-d2: d^2 cls(a) = cls(d\' '
                          'a_(m-1,k+1)) in E^2_(m-2,k+1)')
    # exm:two-step-filtration
    for t in range(10):
        K = random_filtered(rng, top=4, maxdeg=1)
        for k in range(0, 3):
            # delta_(k+1): H_(k+1)(K'') -> H_k(K'), K' = F_0, K'' = K/F_0
            n = k + 1
            F0n, F0k = K.F(0, n), K.F(0, k)
            Zq = K.preimage(n, K.V(n), F0k)
            Bq = (K.dimg(n + 1, K.V(n + 1)) if n + 1 <= K.top
                  else K.V(n).span([])) + F0n
            Hq = (Zq + F0n) / Bq
            Zp = K.preimage(k, F0k, K.V(k - 1).span([])) if k > 0 else F0k
            Bp = K.dimg(k + 1, F0n)
            Hp = Zp / Bp
            delta = Hq.hom([Hp(g.lift() * K.d[n]) for g in Hq.gens()], Hp)
            Z, W = K.E(2, 0, k)
            coker = Hp.V() / (delta.image().V())
            check(inv(Z / W) == inv(coker), '(5.5): E^2_(0 k) = Coker '
                  'delta_(k+1)')
            Z1, W1 = K.E(2, 1, k + 1)
            check(inv(Z1 / W1) == inv(delta.kernel()),
                  '(5.5): E^2_(1 k) = Ker delta_(k+1)')
    # prop:d2-sequence-multiplication: B = Z_2, X periodic, Y: Z B -(1+b)->
    # Z B in degrees 1 -> 0.  K_(m k) = X_m (x)_B Y_k = Y_k (rank 2).
    top = 7
    bmat = matrix(ZZ, [[0, 1], [1, 0]])
    one = identity_matrix(ZZ, 2)
    Yd = one + bmat                       # (1 + b), right multiplication
    ranks, deg, offs = [], {}, []
    for n in range(top + 1):
        ranks.append(2 * (2 if n >= 1 else 1))
        deg[n] = ([n, n] + ([n - 1, n - 1] if n >= 1 else []))
    d = {}
    for n in range(1, top + 1):
        D = matrix(ZZ, ranks[n], ranks[n - 1])
        # block (m = n, k = 0) -> (m = n - 1, k = 0): d' with X differential
        def dX(m):
            return (bmat - one) if m % 2 else (one + bmat)
        D.set_block(0, 0, dX(n))
        # block (m = n - 1, k = 1): d' -> (n - 2, 1); d'' -> (n - 1, 0)
        if n >= 2:
            D.set_block(2, 2, dX(n - 1))
        D.set_block(2, 0, (-1) ** (n - 1) * Yd)
        d[n] = D
    K = Filtered(ranks, deg, d)
    for m in range(0, 6):
        for k in (0, 1):
            n = m + k
            if n >= top - 1:
                continue
            Z, W = K.E(2, m, n)
            want = normal_form([2]) if m % 2 == 0 else ZERO
            check(inv(Z / W) == want, 'E^2_(%d %d) = H_m(Z_2, Z_-)' % (m, k))
            Z3, W3 = K.E(3, m, n)
            want3 = normal_form([2]) if (m, k) == (0, 0) else ZERO
            check(inv(Z3 / W3) == want3,
                  'prop:d2-sequence-multiplication: E^3_(%d %d) = %s'
                  % (m, k, want3))
    Kc = Complex(ranks, {n: K.d[n] for n in K.d})
    for n in range(0, top - 1):
        check(Kc.H(n) == (normal_form([2]) if n == 0 else ZERO),
              'H_n(X (x)_B Y) = H_n(Y_B)')
    # exc:hom-bicomplex: K^(m k) = Hom(X_m, Y^k), f -> d' f = d_X f,
    # d'' f = (-1)^m f delta_Y; d'd'' + d''d' = 0 needs the sign
    X = random_complex(3, rng)
    Y = random_complex(3, rng)
    for m in range(0, 2):
        for k in range(0, 2):
            delta = Y.d[k + 1].transpose()        # Y^k -> Y^(k+1)
            for _ in range(5):
                f = matrix(ZZ, X.ranks[m], Y.ranks[k],
                           lambda i, j: rng.randint(-2, 2))
                both = X.d[m + 1] * ((-1) ** m * f * delta) \
                    + (-1) ** (m + 1) * (X.d[m + 1] * f) * delta
                check(both.is_zero(), "exc:hom-bicomplex: d'd'' + d''d' = 0")
    # without the sign: X, Y the periodic complexes of Z_2, Z_3, m = k = 1
    X, Y = periodic(2, 3), periodic(3, 3)
    f = matrix(ZZ, [[1]])
    delta = Y.d[2].transpose()
    nosign = X.d[2] * (f * delta) + (X.d[2] * f) * delta
    refuted(nosign.is_zero(), "exc:hom-bicomplex without the sign (-1)^m")


# ---------------------------------------------------------------------------
# Section 4
# ---------------------------------------------------------------------------

def section_4():
    rng = random.Random(4)
    for t in range(20):
        X = random_complex(4, rng)
        # make it a finite complex: top = 4, H computed up to 4 with
        # d_5 = 0
        chi_chains = sum((-1) ** n * X.ranks[n] for n in range(5))
        chi_h = sum((-1) ** n * X.H(n)[0] for n in range(5))
        check(chi_chains == chi_h,
              'chi(K) = sum (-1)^n r(H_n(K)) (homology, as corrected)')
        for p in (2, 3):
            dims = 0
            for n in range(5):
                h = X.H_mod(n, p)
                dims += (-1) ** n * (h[0] + len(h[1]))
            check(dims == chi_h, '(5.11): chi = sum (-1)^n dim H_n(K, Z_%d)'
                  % p)
    # chi(Z^r) = sum (-1)^n C_r^n
    for r in range(0, 7):
        chi = sum((-1) ** n * binomial(r, n) for n in range(r + 1))
        check(chi == (1 if r == 0 else 0), 'chi(Z^%d) = %d' % (r, chi))
    refuted(sum((-1) ** n * binomial(0, n) for n in range(1)) == 0,
            'exc:nilpotent-euler-characteristic for G = 1 (chi(1) = 1)')
    # Heisenberg group: B = Z acting on A = Z^2 by u = [[1, 1], [0, 1]];
    # E^2_(m k) = H_m(Z, Lambda^k A): m = 0 coinvariants, m = 1 invariants
    u = matrix(ZZ, [[1, 1], [0, 1]])
    lam = {0: matrix(ZZ, [[1]]), 1: u, 2: matrix(ZZ, [[u.det()]])}
    chi = 0
    for k in (0, 1, 2):
        Mk = lam[k] - identity_matrix(ZZ, lam[k].nrows())
        V = ZZ ** lam[k].nrows()
        coinv = normal_form((V / V.span(Mk.rows())).invariants())
        inv_ = Mk.left_kernel().rank()
        chi += (-1) ** k * coinv[0] - (-1) ** k * inv_
        if k == 2:
            check(inv_ == 1, 'exc:nilpotent-group-dimension: E^2_(1 2) = '
                  'H_1(Z, Lambda^2 Z^2) = Z, so H_3 != 0')
    check(chi == 0, 'prop:extension-euler-characteristic: chi(Heisenberg) '
          '= chi(E^2) = 0')
    # Klein bottle group: A = Z + Z_-, B = Z_2; chi(E^2) from ranks of
    # coinvariants (m = 0; H_m(Z_2, -) is finite for m > 0)
    ranks0 = [1, 1, 0]           # Lambda^0, Lambda^1 = Z + Z_-, Lambda^2 = Z_-
    chiK = sum((-1) ** k * ranks0[k] for k in range(3))
    check(chiK == 0 and chiK == 0 * 1, '(5.13) for the Klein bottle group: '
          'chi = chi(Z^2) chi(Z_2) = 0')


def main():
    section_1()
    section_2()
    section_3()
    section_4()
    print('ok %s: %d checks' % (SCOPE, COUNT[0]))


if __name__ == '__main__':
    main()
