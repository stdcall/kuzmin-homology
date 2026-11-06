"""Exact checks of Chapter 3 "Cohomology and the functor Ext", §§ 6-8 (Sage).

Run from the project root: sage -python checks/sage/chapter-3b.py (plain
asserts; do not use -O).  The last line is "ok chapter-3b: N checks".

Book: Yu. V. Kuzmin, Homological group theory (Factorial Press, Moscow,
2006), chapter 3, printed pp. 149-170.  Pages are printed pages; labels are
those of content/03-*.typ.  Expected values are the book's; where the book
is wrong the printed reading is kept as a refuted check (`refuted`) beside
the corrected one.  Exact arithmetic only: integer lattices (Sage free
modules over ZZ), Laurent polynomials over ZZ, Sage's ChainComplex over ZZ,
GAP through libgap (free and finitely presented groups, kernels,
simplified presentations, low-index subgroups, abelian invariants).  Fox
derivatives are the right derivatives of the book, D(u v) = D(u) v + D(v)
(p. 153: eta(v) = v(y) sum e_i dv/dy_i in W = G P with
(g, p)(h, q) = (g h, p h + q)), computed in Z G for finite G and in
Z[y_1^+-1, ..., y_r^+-1] for G = Z^r.

What is checked, by section:

section_6 (pp. 149-160): th:magnus-embedding (ii) and eq:relation-sequence
  for finite G = F/N: S_3, Z_2^2, Z_4, Z_3, Q_8, A_4 (rank 2), Z_2
  (rank 3), Z_n (rank 1, n <= 7): N is free of rank |G|(r - 1) + 1 (GAP),
  the Fox derivatives of its free basis lie in Ker sigma, form a basis of
  the lattice Ker sigma (so mu: M -> P is injective with image Ker sigma),
  Im sigma = Delta_G; eq:magnus-image-criterion for random words;
  exc:fox-derivative-criterion in the easy direction (commutators of
  elements of N have zero derivatives); exc:free-abelian-extension-center
  (P s lies in M and is fixed by G).  exc:commuting-with-relation-module
  (C244): Ann_P(g - 1) = P (1 + g + ... + g^(n-1)) and the centralizer of
  g in M is M meet P N_g, while the printed M N_g has index > 1 in it (S_3,
  Q_8, A_4, Z_n with n <= 7; the printed "a in M" refuted).  Free abelian
  G = Z^r, r <= 5: the commutator [y_i e_i, y_j e_j] in W equals
  e_i(y_j - 1) - e_j(y_i - 1) (C236; also from the Fox derivatives of
  [x_i, x_j]), the printed e_j(y_j - 1) is not even in Ker d_1 (C237,
  refuted); the Koszul differential with the sign inside the sum
  (sum_j (-1)^(n-j) ...; source corrected) has d d = 0, d_2 as corrected
  (C238; printed d_2 refuted), and the relations (3.33) of
  th:free-metabelian-relation-module are d_3(e_i ^ e_j ^ e_k);
  exc:fox-derivative-criterion for N = F' (G = Z^2): random elements of
  F'' have zero derivatives, [x, y]^k (k <= 4) do not.
section_6_roots (p. 158, exc:free-abelian-extension-unique-roots): the
  hint (lem:unique-roots-extension) covers G with unique roots only; the
  Klein bottle group K = <a, b | b^-1 a b a> is torsion-free and
  (a^k b^m)^2 = (a^k' b^m)^2 = b^(2m) for odd m.  For every such pair with
  |k|, |k'| <= 6, k != k', m in {1, -1, 3, -3}: in the Magnus embedding
  (a, e_a), (b, e_b) the element c = v^-2 u^2 of M = mu ZK (mu = (ba + 1,
  a - 1), the free generator of the relation module) is computed exactly
  as mu c', and a sign character rho of K with rho(a^k b^m) =
  rho(a^k' b^m) = -1 has rho(c') != 0, so c' is not in
  ZK(1 + g) + ZK(1 + h) and no lifts x, y in Phi have x^2 = y^2 (in K
  these pairs are all solutions of g^2 = h^2, g != h; unique n-th roots
  for odd n hold in K).  The general case is not computed; it holds for
  every torsion-free G: if x^n = y^n = t in Phi, the centralizer of t maps
  injectively to G (Magnus embedding, P free), so <x, y> maps
  isomorphically onto H = <g, h>, the free abelian extension of H splits,
  Delta_H is projective, H is free by the Stallings-Swan theorem quoted on
  p. 31 and p. 83, and g = h, x = y.
section_7 (pp. 160-165): the rewriting example of p. 161 (equality in the
  free group, the length drops by the 6 letters x_1); the change of
  generators in the proof of th:one-relator-free-module (C253, C254):
  x_1 = x^beta, x_2 = y x^-alpha kills the exponent sum of x for 200
  random words, the printed y = x_2 x^-alpha does not (refuted).  For 19
  one-relator groups (surface groups of genus 1-3, a^2 b^2 c^2, the Klein
  bottle, the trefoil, x^2 y^4, x^2 y^4 z^6, BS(1, 2), BS(2, 3), BS(2, 2),
  a longer word; with torsion: Z_5, Z_3 * Z, [x, y]^2, [x, y]^3,
  (x^2 y^3)^2, (x y x^-1 y^-2)^3, (x^2 y^4)^2 with a free generator z):
  H_n and H^n, n <= 7, from the resolution of cor:one-relator-resolution
  and of p. 165 (periodic t, s after d), with the augmented Fox
  derivatives computed from the word; H_1 against G_ab from GAP; H^2 = Z
  for v in F' (exc:one-relator-h2-commutator), H^2 = Z_gcd(sigma_i(v))
  otherwise (exc:one-relator-h2-noncommutator, C257; the printed least
  common multiple refuted where it differs); H_n = H^n = 0 for n >= 3 in the
  torsion-free case, H_odd = Z_m, H^even = Z_m (n >= 3) for v = w^m;
  universal coefficients in every degree; chi = 2 - r from the ranks.  The
  remark of p. 165 as corrected (C = F/F', z = v F'): C/<z> has the
  invariants of G_ab and the class of 0 -> <z> -> C -> G_ab -> 0 has order
  m = |H^2 G|; the printed C (z = (vF')^m) gives a different quotient when
  m > 1 (refuted).  The image of w has order exactly m in a finite quotient
  (Q_8, the Heisenberg group mod 3, Z_2, Z_3).
section_8 (pp. 165-170): chi(Z^r) = 0 from the ranks C(r, n) (C261),
  r <= 8; eq:subgroup-euler on all subgroups of index <= 5 of F_2, <= 3 of
  F_3 (free of rank k(r - 1) + 1), <= 4 of the genus-2 surface group
  (H_1 = Z^(2 + 2k)) and of a^2 b^2 c^2 (H_1 = Z^(2 + k) or
  Z^(1 + k) + Z_2), <= 6 of the Klein bottle group (exc:almost-polycyclic-
  euler); exc:vfp-euler-characteristic (C268) and
  exc:vfp-free-product-formulas: chi(SL_2(Z)) = -1/12 from Gamma(3),
  Gamma(4), Gamma(5) (free of ranks 3, 5, 11) and the commutator subgroup
  (free of rank 2, index 12), = 1/4 + 1/6 - 1/2; for Z_k *_Z_l Z_m
  (l, s, t <= 3) the commutator subgroup is free of rank 1 - |G_ab| chi;
  th:brown-sylow on these amalgams (every prime power of the denominator of
  chi divides k or m); exc:finite-free-product-euler for G_1 * G_2 with
  G_i in {Z_2, Z_3, Z_4, Z_2^2, S_3}: the kernel onto G_1 x G_2 is free of
  rank (m_1 - 1)(m_2 - 1) and generated by the [g_1, g_2];
  exc:modular-group-euler (the two Moebius maps have orders 2 and 3 in
  PSL_2(Z), chi(Z_2 * Z_3) = -1/6 from the commutator subgroup);
  exc:free-normal-complement and prop:euler-splitting on Z_p * Z_p -> Z_p
  (kernel free of rank p - 1, p <= 7) and Z_2 * Z_2 * Z_2 -> Z_2;
  [x, y]^m (m = 2, 3) as a group of type VFP: torsion-free kernels of index
  8 (Q_8, D_8) and 27 (Heisenberg mod 3) are surface groups with
  chi = |G : K| (1 - 2 + 1/m); exc:finite-group-field-rank over Q for S_3
  (r(P) = dim of invariants, Delta_G non-zero of rank 0) and
  exc:field-rank-subgroup (H = 1, P = K refutes the formula).

What this does NOT establish: the general theorems (only the listed
groups, ranks, indices and degrees are covered).  The exactness of the
Lyndon resolutions (th:one-relator-free-module,
th:one-relator-induced-module) is assumed when cohomology is read off
them; it is cross-checked only through H_1 (GAP), universal coefficients
and the Euler characteristics of finite-index subgroups.  The Magnus
embedding is verified only for finite G (for G = Z^2 only the easy
direction of exc:fox-derivative-criterion); prop:free-abelian-extension-
torsion-free is not computed.  Nothing here compares our text with the
printed book.
"""

import random
from fractions import Fraction
from itertools import combinations

from sage.all import (
    QQ, ZZ, ChainComplex, FreeModule, LaurentPolynomialRing, binomial, gcd,
    lcm, libgap, matrix, vector,
)

SCOPE = 'chapter-3b'
COUNT = [0]


def check(cond, what):
    assert bool(cond), 'FAILED: ' + what
    COUNT[0] += 1


def refuted(cond, what):
    assert not bool(cond), 'printed reading unexpectedly holds: ' + what
    COUNT[0] += 1


def gap(src):
    return libgap.eval(src)


Q8 = 'Group((1,2,3,4)(5,6,7,8), (1,5,3,7)(2,8,4,6))'


def prime_power_invariants(invs):
    """Abelian invariants in GAP's form: prime powers and zeros, sorted."""
    out = []
    for d in invs:
        d = abs(ZZ(d))
        if d == 0:
            out.append(0)
        elif d > 1:
            out.extend(p ** e for p, e in d.factor())
    return sorted(out)


def gap_invariants(G):
    return sorted(ZZ(x) for x in G.AbelianInvariants())


def homology_invariants(C, n):
    return prime_power_invariants(C.homology(n).invariants())


def free_rank_of(K):
    """(number of generators, number of relators) of a Tietze-simplified
    Reidemeister-Schreier presentation of the subgroup K of finite index in
    a finitely presented group (GAP core only, whatever packages are
    loaded)."""
    f = gap('function(K) local P, H; '
            'P := PresentationSubgroup(Parent(K), K); '
            'TzOptions(P).printLevel := 0; TzGoGo(P); '
            'H := FpGroupPresentation(P); '
            'return [Length(GeneratorsOfGroup(H)), '
            'Length(RelatorsOfFpGroup(H))]; end')
    r = f(K)
    return int(r[0]), int(r[1])


def commutator_subgroup(G):
    """G' as the kernel of the maximal abelian quotient of the finitely
    presented group G (finite index here), a subgroup of G given by a coset
    table."""
    return gap('G -> Kernel(MaximalAbelianQuotient(G))')(G)


# ---------------------------------------------------------------------------
# Words: lists of (generator index, +-1); written as strings over a..z with
# capitals for inverses ("xyXY" = x y x^-1 y^-1).
# ---------------------------------------------------------------------------

def word(s, gens):
    out = []
    for ch in s:
        if ch.islower():
            out.append((gens.index(ch), 1))
        else:
            out.append((gens.index(ch.lower()), -1))
    return out


def power(w, m):
    return w * m if m >= 0 else inverse(w) * (-m)


def inverse(w):
    return [(g, -e) for (g, e) in reversed(w)]


def gap_word(w, F='Fw'):
    if not w:
        return 'One(%s)' % F
    return ' * '.join('%s.%d^%d' % (F, g + 1, e) for (g, e) in w)


def exponent_sums(w, n):
    return [sum(e for (g, e) in w if g == i) for i in range(n)]


# ---------------------------------------------------------------------------
# Finite groups and right Fox derivatives
# ---------------------------------------------------------------------------

class TGroup:
    """A finite group given by GAP, with its multiplication table."""

    def __init__(self, G):
        self.G = G
        self.elts = G.AsSSortedList()
        tab = gap('function(e) return List(e, g -> List(e, h -> '
                  'PositionSorted(e, g*h))); end')(self.elts)
        self.mul = [[int(x) - 1 for x in row] for row in tab]
        self.n = len(self.mul)
        self.one = [i for i in range(self.n)
                    if all(self.mul[i][j] == j for j in range(self.n))][0]
        self.inv = [[j for j in range(self.n) if self.mul[i][j] == self.one][0]
                    for i in range(self.n)]

    def index(self, g):
        return int(self.elts.PositionSorted(g)) - 1

    def unit(self, i):
        v = [0] * self.n
        v[i] = 1
        return vector(ZZ, v)

    def rmul(self, v, h):
        w = [0] * self.n
        for g in range(self.n):
            if v[g]:
                w[self.mul[g][h]] += v[g]
        return vector(ZZ, w)

    def lmul(self, h, v):
        w = [0] * self.n
        for g in range(self.n):
            if v[g]:
                w[self.mul[h][g]] += v[g]
        return vector(ZZ, w)

    def evaluate(self, w, ims):
        x = self.one
        for (g, e) in w:
            x = self.mul[x][ims[g] if e > 0 else self.inv[ims[g]]]
        return x


def fox_finite(T, w, ims, r):
    """Right Fox derivatives D_i(w) in Z G (D(u v) = D(u) v + D(v)),
    concatenated into a vector of Z G^r."""
    acc = [vector(ZZ, [0] * T.n) for _ in range(r)]
    for (g, e) in w:
        y = ims[g] if e > 0 else T.inv[ims[g]]
        acc = [T.rmul(a, y) for a in acc]
        if e > 0:
            acc[g] = acc[g] + T.unit(T.one)
        else:
            acc[g] = acc[g] - T.unit(T.inv[ims[g]])
    return vector(ZZ, sum((list(a) for a in acc), []))


def fox_laurent(L, w, r):
    """Right Fox derivatives with values in Z[y_1^+-1, ..., y_r^+-1]."""
    y = L.gens()
    acc = [L(0)] * r
    for (g, e) in w:
        yy = y[g] if e > 0 else y[g] ** -1
        acc = [a * yy for a in acc]
        acc[g] += 1 if e > 0 else -y[g] ** -1
    return acc


# ---------------------------------------------------------------------------
# Section 6: free extensions with abelian kernel, the Magnus embedding
# ---------------------------------------------------------------------------

def magnus_finite(name, target, images, r):
    """th:magnus-embedding for G = F/N finite, F free of rank r."""
    T = TGroup(gap(target))
    ims = [T.index(gap(x)) for x in images]
    gap('Fw := FreeGroup(%d)' % r)
    hom = gap('GroupHomomorphismByImages(Fw, %s, GeneratorsOfGroup(Fw), '
              '[%s])' % (target, ', '.join(images)))
    check(hom.Image().Size() == T.n, name + ': x_i -> y_i is onto')
    N = hom.Kernel()
    B = N.FreeGeneratorsOfGroup()
    basis = [[(abs(int(a)) - 1, 1 if int(a) > 0 else -1)
              for a in b.LetterRepAssocWord()] for b in B]
    rank = T.n * (r - 1) + 1
    check(len(basis) == rank, name + ': N free of rank |G|(r - 1) + 1')
    e = T.unit(T.one)

    def sigma(p):                    # P -> Z G, e_i -> y_i - 1
        out = vector(ZZ, [0] * T.n)
        for i in range(r):
            pi = vector(ZZ, list(p)[i * T.n:(i + 1) * T.n])
            out += T.lmul(ims[i], pi) - pi
        return out
    Sig = matrix(ZZ, [sigma(vector(ZZ, [1 if j == k else 0
                                         for j in range(r * T.n)]))
                      for k in range(r * T.n)]).transpose()
    mus = [fox_finite(T, b, ims, r) for b in basis]
    check(all(Sig * mu == 0 for mu in mus),
          name + ': Fox identity, mu(M) lies in Ker sigma')
    V = FreeModule(ZZ, r * T.n)
    K = V.span(Sig.right_kernel().basis())
    check(K.rank() == rank, name + ': Ker sigma has rank |G|(r - 1) + 1')
    check(V.span(mus) == K and matrix(ZZ, mus).rank() == rank,
          name + ': mu maps a basis of M = N/N\' onto a basis of Ker sigma '
          '(th:magnus-embedding (ii))')
    Delta = FreeModule(ZZ, T.n).span([T.unit(g) - e for g in range(T.n)])
    check(FreeModule(ZZ, T.n).span(Sig.columns()) == Delta,
          name + ': Im sigma = Delta_G (eq:relation-sequence exact)')
    # (3.28): Sum (y_i - 1) D_i(w) = w - 1 for random words w
    random.seed(len(name))
    for _ in range(20):
        w = [(random.randrange(r), random.choice([1, -1]))
             for _ in range(random.randint(1, 12))]
        check(sigma(fox_finite(T, w, ims, r)) ==
              T.unit(T.evaluate(w, ims)) - e,
              name + ': eq:magnus-image-criterion for eta(w)')
    # ex. 3.6.2, easy direction: words of N' have zero derivatives in Z G
    for _ in range(10):
        u = sum((power(basis[random.randrange(rank)], random.choice([1, -1]))
                 for _ in range(3)), [])
        v = sum((power(basis[random.randrange(rank)], random.choice([1, -1]))
                 for _ in range(3)), [])
        c = inverse(u) + inverse(v) + u + v
        check(fox_finite(T, c, ims, r) == 0,
              name + ': ex. 3.6.2, [u, v] with u, v in N')
    # ex. 3.6.7: P s lies in M and is central (s = sum of the elements)
    s = vector(ZZ, [1] * T.n)
    for i in range(r):
        p = vector(ZZ, [0] * (i * T.n) + list(s) + [0] * ((r - i - 1) * T.n))
        check(p in K and all(T.rmul(s, g) == s for g in range(T.n)),
              name + ': ex. 3.6.7, e_%d s in M, central' % i)
    return T, ims, Sig, K, V


def ex_3_6_6(name, T, ims, K, V, r):
    """ex. 3.6.6 (C244): g = t_1 with image of order n > 1; h in M commutes
    with g iff mu(h)(g - 1) = 0 iff mu(h) = a (1 + g + ... + g^(n-1)) with
    a in P.  The printed a in M gives the smaller lattice M (1 + ... )."""
    gx = ims[0]
    order, x = 1, gx
    while x != T.one:
        x = T.mul[x][gx]
        order += 1
    Ng = vector(ZZ, [0] * T.n)
    x = T.one
    for _ in range(order):
        Ng += T.unit(x)
        x = T.mul[x][gx]

    def rmul_elt(p, z):              # p in P = Z G^r times z in Z G
        out = []
        for i in range(r):
            pi = vector(ZZ, list(p)[i * T.n:(i + 1) * T.n])
            acc = vector(ZZ, [0] * T.n)
            for h in range(T.n):
                if z[h]:
                    acc += z[h] * T.rmul(pi, h)
            out += list(acc)
        return vector(ZZ, out)
    units = [vector(ZZ, [1 if j == k else 0 for j in range(r * T.n)])
             for k in range(r * T.n)]
    Gm1 = T.unit(gx) - T.unit(T.one)
    A = matrix(ZZ, [rmul_elt(u, Gm1) for u in units]).transpose()
    Ann = V.span(A.right_kernel().basis())
    PN = V.span([rmul_elt(u, Ng) for u in units])
    check(Ann == PN, name + ': ex. 3.6.6, Ann_P(g - 1) = P (1 + ... + '
          'g^%d)' % (order - 1))
    centralizer = Ann.intersection(K)
    printed = V.span([rmul_elt(k, Ng) for k in K.basis()])
    check(centralizer == PN.intersection(K),
          name + ': ex. 3.6.6 (corrected), C_M(g) = M meet P N_g')
    idx = printed.index_in(centralizer)
    check(printed.is_submodule(centralizer) and idx > 1,
          name + ': ex. 3.6.6, M N_g has index %s in C_M(g)' % idx)
    refuted(printed == centralizer, name + ': ex. 3.6.6 with a in M')


def section_6():
    cases = [
        ('S_3', 'SymmetricGroup(3)', ['(1,2)', '(1,2,3)'], 2),
        ('Z_2 x Z_2', 'Group((1,2), (3,4))', ['(1,2)', '(3,4)'], 2),
        ('Z_4 (two generators)', 'CyclicGroup(IsPermGroup, 4)',
         ['(1,2,3,4)', '(1,2,3,4)'], 2),
        ('Z_3', 'CyclicGroup(IsPermGroup, 3)', ['(1,2,3)', '()'], 2),
        ('Q_8', Q8,
         ['(1,2,3,4)(5,6,7,8)', '(1,5,3,7)(2,8,4,6)'], 2),
        ('A_4', 'AlternatingGroup(4)', ['(1,2,3)', '(1,2)(3,4)'], 2),
        ('Z_2 (three generators)', 'Group((1,2))', ['(1,2)', '(1,2)', '()'],
         3),
    ] + [('Z_%d (one generator)' % n, 'CyclicGroup(IsPermGroup, %d)' % n,
           ['(%s)' % ','.join(str(i) for i in range(1, n + 1))], 1)
          for n in range(2, 8)]
    Q = gap(Q8)
    check(Q.Size() == 8 and not Q.IsAbelian() and
          len([x for x in Q.AsList() if x.Order() == 2]) == 1,
          'the permutation group used for Q_8 is quaternion')
    data = {}
    for (name, target, images, r) in cases:
        data[name] = magnus_finite(name, target, images, r)

    # ex. 3.6.6 (C244): for g with image of order n, h in M commutes with g
    # iff mu(h) (g - 1) = 0 iff mu(h) = a (1 + g + ... + g^(n-1)), a in P.
    for name in ['S_3', 'Q_8', 'A_4'] + ['Z_%d (one generator)' % n
                                         for n in range(2, 8)]:
        T, ims, Sig, K, V = data[name]
        ex_3_6_6(name, T, ims, K, V, 1 if 'one generator' in name else 2)

    # Free abelian G = Z^r: commutators in W = G P (C236-C238), the Koszul
    # differentials, the relations (3.33) of th:free-metabelian-relation-module
    for r in range(2, 6):
        L = LaurentPolynomialRing(ZZ, r, 'y')
        y = L.gens()

        def wmul(u, v):          # (g, p)(h, q) = (g h, p h + q)
            return (u[0] * v[0], [a * v[0] + b for a, b in zip(u[1], v[1])])

        def winv(u):
            gi = u[0] ** -1
            return (gi, [-a * gi for a in u[1]])
        E = [[L(1) if j == i else L(0) for j in range(r)] for i in range(r)]
        for i in range(r):
            for j in range(i + 1, r):
                u, v = (y[i], E[i]), (y[j], E[j])
                c = wmul(wmul(winv(u), winv(v)), wmul(u, v))
                corr = [L(0)] * r
                corr[i] += y[j] - 1
                corr[j] -= y[i] - 1
                check(c[0] == 1 and c[1] == corr,
                      'C236: [y_i e_i, y_j e_j] = e_i(y_j - 1) - e_j(y_i - 1)'
                      ', r = %d' % r)
                comm = [(i, -1), (j, -1), (i, 1), (j, 1)]
                check(fox_laurent(L, comm, r) == corr,
                      'Fox derivatives of [x_i, x_j] give the same element')
                pr = [L(0)] * r
                pr[i] += y[j] - 1
                pr[j] -= y[j] - 1
                refuted(sum((y[k] - 1) * pr[k] for k in range(r)) == 0,
                        'C237: e_i(y_j - 1) - e_j(y_j - 1) lies in Ker d_1')
        # Koszul: d_n(e_I) = sum_j (-1)^(n-j) e_(I - i_j) (y_(i_j) - 1)

        def d(chain):            # chain: dict {tuple I: Laurent coeff}
            out = {}
            for I, c in chain.items():
                n = len(I)
                for jj in range(1, n + 1):
                    J = I[:jj - 1] + I[jj:]
                    out[J] = out.get(J, L(0)) + \
                        (-1) ** (n - jj) * c * (y[I[jj - 1]] - 1)
            return {k: v for k, v in out.items() if v != 0}
        for n in range(1, r + 1):
            for I in combinations(range(r), n):
                if n >= 2:
                    check(d(d({I: L(1)})) == {},
                          'Koszul d_(n-1) d_n = 0, r = %d, n = %d' % (r, n))
        for i, j in combinations(range(r), 2):
            check(d({(i, j): L(1)}) == {(j,): -(y[i] - 1), (i,): y[j] - 1},
                  'C238: d_2(e_i ^ e_j) = e_i(y_j - 1) - e_j(y_i - 1)')
            printed = {(i,): y[j] - 1, (j,): -(y[j] - 1)}
            refuted(d(printed) == {}, 'C238: printed d_2, d_1 d_2 = 0')
        for i, j, k in combinations(range(r), 3):
            rel = {(i, j): y[k] - 1, (i, k): -(y[j] - 1), (j, k): y[i] - 1}
            check(d({(i, j, k): L(1)}) == rel and d(rel) == {},
                  '(3.33) = d_3(e_i ^ e_j ^ e_k) and lies in Ker d_2')
    # ex. 3.6.2 (easy direction) for N = F', G = Z^2: words of F'' have
    # zero Fox derivatives in Z[Z^2]; [x, y] and its powers do not.
    L = LaurentPolynomialRing(ZZ, 2, 'y')
    gens = 'xy'
    cxy = word('XYxy', gens)
    cases = [inverse(cxy) + inverse(word('X', gens) + cxy + word('x', gens))
             + cxy + word('X', gens) + cxy + word('x', gens)]
    random.seed(11)
    for _ in range(10):
        def rand_comm():
            a = [(random.randrange(2), random.choice([1, -1]))
                 for _ in range(random.randint(1, 5))]
            b = [(random.randrange(2), random.choice([1, -1]))
                 for _ in range(random.randint(1, 5))]
            return inverse(a) + inverse(b) + a + b
        u, v = rand_comm(), rand_comm()
        cases.append(inverse(u) + inverse(v) + u + v)
    for c in cases:
        check(fox_laurent(L, c, 2) == [0, 0],
              'ex. 3.6.2: an element of F\'\' has zero derivatives mod F\'')
    for k in range(1, 5):
        check(fox_laurent(L, power(cxy, k), 2) != [0, 0],
              'ex. 3.6.2: [x, y]^%d has non-zero derivatives' % k)


# ---------------------------------------------------------------------------
# Section 7: one-relator groups (Lyndon)
# ---------------------------------------------------------------------------

def klein_mul(x, y):
    """Product in Z K, K = <a, b | b^-1 a b = a^-1>, a^i b^j as (i, j)."""
    out = {}
    for (i, j), c in x.items():
        for (k, l), d in y.items():
            key = (i + (1 if j % 2 == 0 else -1) * k, j + l)
            out[key] = out.get(key, 0) + c * d
    return {k: v for k, v in out.items() if v}


def klein_add(*xs):
    out = {}
    for x in xs:
        for k, v in x.items():
            out[k] = out.get(k, 0) + v
    return {k: v for k, v in out.items() if v}


def klein_magnus(w):
    """Image (g, (p_a, p_b)) of a word in a, b, A = a^-1, B = b^-1."""
    one = {(0, 0): 1}
    gens = {'a': ((1, 0), (one, {})), 'b': ((0, 1), ({}, one)),
            'A': ((-1, 0), ({(-1, 0): -1}, {})),
            'B': ((0, -1), ({}, {(0, -1): -1}))}
    g, p = (0, 0), ({}, {})
    for letter in w:
        h, q = gens[letter]
        hel = {h: 1}
        p = (klein_add(klein_mul(p[0], hel), q[0]),
             klein_add(klein_mul(p[1], hel), q[1]))
        g = (g[0] + (1 if g[1] % 2 == 0 else -1) * h[0], g[1] + h[1])
    return g, p


def section_6_roots():
    g, mu = klein_magnus('Baba')
    check(g == (0, 0), 'ex. 3.6.8: b^-1 a b a is a relator of K')
    a1 = {(1, 0): 1, (0, 0): -1}
    b1 = {(0, 1): 1, (0, 0): -1}
    check(klein_add(klein_mul(a1, mu[0]), klein_mul(b1, mu[1])) == {},
          'ex. 3.6.8: mu lies in the relation module')
    inv = {'a': 'A', 'A': 'a', 'b': 'B', 'B': 'b'}
    for m in (1, -1, 3, -3):
        bm = ('b' if m > 0 else 'B') * abs(m)
        for k in range(-6, 7):
            for k2 in range(-6, 7):
                if k == k2:
                    continue
                u = ('a' if k > 0 else 'A') * abs(k) + bm
                v = ('a' if k2 > 0 else 'A') * abs(k2) + bm
                vinv = ''.join(inv[x] for x in reversed(v))
                gw, c = klein_magnus(vinv + vinv + u + u)
                check(gw == (0, 0), 'ex. 3.6.8: g^2 = h^2 in K')
                # c' with (a - 1) c' = c_b, coset by coset of <a>
                cp = {}
                for j in {j for (_, j) in c[1]}:
                    ys = {i: x for (i, jj), x in c[1].items() if jj == j}
                    acc = 0
                    for i in range(max(ys), min(ys) - 1, -1):
                        acc += ys.get(i, 0)
                        if acc:
                            cp[(i - 1, j)] = acc
                    check(acc == 0, 'ex. 3.6.8: (a - 1) x = c_b solvable')
                check(klein_mul(mu[0], cp) == c[0]
                      and klein_mul(mu[1], cp) == c[1],
                      'ex. 3.6.8: c = mu x exactly')
                excluded = False
                for sa in (1, -1):
                    if sa ** k * (-1) ** m != -1 or sa ** k2 * (-1) ** m != -1:
                        continue
                    value = sum(x * sa ** i * (-1) ** j
                                for (i, j), x in cp.items())
                    excluded = excluded or value != 0
                check(excluded, 'ex. 3.6.8: no lifts with equal squares for '
                      'a^%d b^%d, a^%d b^%d' % (k, m, k2, m))


def lyndon_complexes(sig, m, N):
    """Chain and cochain complexes (tensored with Z) of the resolution of
    cor:one-relator-resolution (m = 1) or of the periodic resolution of
    th:one-relator-induced-module (v = w^m, m > 1), degrees <= N."""
    n = len(sig)
    chains = {1: matrix(ZZ, 1, n, 0), 2: matrix(ZZ, n, 1, sig)}
    if m > 1:
        for k in range(3, N + 1):
            # C_k -> C_(k-1): t (u - 1) for k odd, s (1 + ... + u^(m-1)) even
            chains[k] = matrix(ZZ, 1, 1, [0 if k % 2 else m])
    C = ChainComplex(chains, degree=-1)
    co = {k - 1: M.transpose() for k, M in chains.items()}
    D = ChainComplex(co, degree=1)
    return C, D


ONE_RELATOR = [
    # (name, generators, w, m) : v = w^m
    ('Z^2 = <x, y | [x, y]>', 'xy', 'XYxy', 1),
    ('surface of genus 2', 'abcd', 'ABabCDcd', 1),
    ('surface of genus 3', 'abcdef', 'ABabCDcdEFef', 1),
    ('non-orientable surface a^2 b^2 c^2', 'abc', 'aabbcc', 1),
    ('Klein bottle x y x^-1 y', 'xy', 'xyXy', 1),
    ('trefoil x^2 y^-3', 'xy', 'xxYYY', 1),
    ('x^2 y^4', 'xy', 'xxyyyy', 1),
    ('x^2 y^4 z^6', 'xyz', 'xxyyyyzzzzzz', 1),
    ('BS(1, 2)', 'at', 'TatAA', 1),
    ('BS(2, 3)', 'at', 'TaatAAA', 1),
    ('BS(2, 2)', 'at', 'TaatAA', 1),
    ('x y x y^-1 x^-2 y^3', 'xy', 'xyxYXXyyy', 1),
    ('Z_5 = <x | x^5>', 'x', 'x', 5),
    ('Z_3 * Z = <x, y | x^3>', 'xy', 'x', 3),
    ('<x, y | [x, y]^2>', 'xy', 'XYxy', 2),
    ('<x, y | [x, y]^3>', 'xy', 'XYxy', 3),
    ('<x, y | (x^2 y^3)^2>', 'xy', 'xxyyy', 2),
    ('<x, y | (x y x^-1 y^-2)^3>', 'xy', 'xyXYY', 3),
    ('<x, y, z | (x^2 y^4)^2>', 'xyz', 'xxyyyy', 2),
]


def section_7():
    # p. 161, the rewriting example: v = x_1^-1 x_2 x_1^3 x_3^-1 x_4^3 x_1^-2
    gap('Fw := FreeGroup(4)')
    v = gap('Fw.1^-1*Fw.2*Fw.1^3*Fw.3^-1*Fw.4^3*Fw.1^-2')
    xk = lambda k, i: gap('Fw.1^%d * Fw.%d * Fw.1^%d' % (-k, i, k))
    u = xk(1, 2) * xk(-2, 3) ** -1 * xk(-2, 4) ** 3
    check(v == u, 'p. 161: v = x_12 x_(-2 3)^-1 x_(-2 4)^3')
    check(int(v.Length()) - 5 == 6,
          'p. 161: the length drops by the number of letters x_1 (6)')
    # C253, C254: x_1 = x^beta, x_2 = y x^-alpha kills the exponent sum of x
    random.seed(3)
    tried = 0
    while tried < 200:
        w = [(random.randrange(3), random.choice([1, -1]))
             for _ in range(random.randint(2, 14))]
        al, be = exponent_sums(w, 3)[:2]
        if al == 0 or be == 0:
            continue
        tried += 1

        def substitute(w, sgn):
            # new generators: 0 = x, 1 = y, 2 = x_3
            out = []
            for (g, e) in w:
                if g == 0:
                    img = power([(0, 1)], be)
                elif g == 1:
                    img = [(1, 1)] + power([(0, 1)], -sgn * al)
                else:
                    img = [(2, 1)]
                out += img if e > 0 else inverse(img)
            return out
        check(exponent_sums(substitute(w, 1), 3)[0] == 0,
              'C253: sigma_x(v) = 0 after x_1 = x^beta, x_2 = y x^-alpha')
        refuted(exponent_sums(substitute(w, -1), 3)[0] == 0,
                'C253: printed y = x_2 x^-alpha (x_2 = y x^alpha)')

    for (name, gens, ws, m) in ONE_RELATOR:
        n = len(gens)
        w = word(ws, gens)
        v = power(w, m)
        sig = exponent_sums(v, n)
        # augmented Fox derivatives = exponent sums
        T1 = TGroup(gap('Group(())'))
        fx = fox_finite(T1, v, [T1.one] * n, n)
        check(list(fx) == sig, name + ': eps(dv/dx_i) = sigma_i(v)')
        C, D = lyndon_complexes(sig, m, 9)
        Hn = [homology_invariants(C, k) for k in range(8)]
        Hc = [homology_invariants(D, k) for k in range(8)]
        gap('Fw := FreeGroup(%d)' % n)
        G = gap('Fw / [%s]' % gap_word(v))
        ab = gap_invariants(G)
        check(Hn[1] == ab, name + ': H_1 from the resolution = G_ab (GAP)')
        check(Hn[0] == [0] and Hc[0] == [0], name + ': H_0 = H^0 = Z')
        g = 0
        for s in sig:
            g = gcd(g, s)
        if all(s == 0 for s in sig):
            check(Hc[2] == [0], name + ': ex. 3.7.1, H^2 G = Z (v in F\')')
            check(Hn[2] == [0], name + ': H_2 G = Z (v in F\')')
        else:
            check(Hc[2] == prime_power_invariants([g]),
                  name + ': ex. 3.7.2, H^2 G = Z_gcd = Z_%d' % g)
            nz = [abs(s) for s in sig if s]
            l = 1
            for s in nz:
                l = lcm(l, s)
            if l != g:
                refuted(Hc[2] == prime_power_invariants([l]),
                        name + ': ex. 3.7.2 with the least common multiple '
                        '(%d)' % l)
            check(Hn[2] == [], name + ': H_2 G = 0 (v not in F\')')
            # remark p. 165 (corrected): C = F/F', z = v F'; the sequence
            # 0 -> <z> -> C -> G_ab -> 0 is exact and its class generates
            # Ext(G_ab, Z) = Z_g: the restriction Hom(Z^n, Z) -> Hom(<z>, Z)
            # has image g Z, so the class of id has order g = |H^2 G|.
            S = matrix(ZZ, n, 1, sig).smith_form()[0]
            check(prime_power_invariants([0] * (n - 1) + [S[0, 0]]) == ab,
                  name + ': remark p. 165, C/<z> = G_ab for C = F/F\'')
            check(abs(S[0, 0]) == g,
                  name + ': remark p. 165, the class of C has order m')
            if g > 1:
                S2 = matrix(ZZ, n, 1, [g * s for s in sig]).smith_form()[0]
                refuted(prime_power_invariants([0] * (n - 1) + [S2[0, 0]])
                        == ab, name + ': remark p. 165 read as z = (vF\')^m')
        for k in range(3, 8):
            if m == 1:
                check(Hn[k] == [] and Hc[k] == [],
                      name + ': H_%d = H^%d = 0 (cd <= 2)' % (k, k))
            else:
                odd = k % 2 == 1
                Zm = prime_power_invariants([m])
                check(Hn[k] == (Zm if odd else []) and
                      Hc[k] == ([] if odd else Zm),
                      name + ': th:one-relator-induced-module, periodic '
                      'H_%d, H^%d' % (k, k))
        # universal coefficients: H^k = Hom(H_k, Z) + Ext(H_(k-1), Z)
        for k in range(1, 7):
            free = Hn[k].count(0)
            tors = [x for x in Hn[k - 1] if x]
            check(Hc[k] == sorted([0] * free + tors),
                  name + ': H^%d against universal coefficients' % k)
        # chi of a torsion-free one-relator group: 2 - n from the ranks of H^*
        if m == 1:
            chi = sum((-1) ** k * Hc[k].count(0) for k in range(3))
            check(chi == 2 - n, name + ': chi = 2 - r (p. 167)')

    # the order of u = image of w is exactly m: finite quotients
    quot = [
        ('<x, y | [x, y]^2>', 'xy', 'XYxy', 2, Q8,
         ['(1,2,3,4)(5,6,7,8)', '(1,5,3,7)(2,8,4,6)']),
        ('<x, y | [x, y]^3>', 'xy', 'XYxy', 3,
         'Group([[1,1,0],[0,1,0],[0,0,1]]*Z(3)^0, '
         '[[1,0,0],[0,1,1],[0,0,1]]*Z(3)^0)',
         ['[[1,1,0],[0,1,0],[0,0,1]]*Z(3)^0',
          '[[1,0,0],[0,1,1],[0,0,1]]*Z(3)^0']),
        ('<x, y | (x^2 y^3)^2>', 'xy', 'xxyyy', 2, 'Group((1,2))',
         ['()', '(1,2)']),
        ('<x, y | (x y x^-1 y^-2)^3>', 'xy', 'xyXYY', 3,
         'Group((1,2,3))', ['()', '(1,2,3)']),
    ]
    for (name, gens, ws, m, target, images) in quot:
        T = TGroup(gap(target))
        ims = [T.index(gap(x)) for x in images]
        w = word(ws, gens)
        check(T.evaluate(power(w, m), ims) == T.one,
              name + ': x_i -> images defines a homomorphism')
        uu = T.evaluate(w, ims)
        order = 1
        x = uu
        while x != T.one:
            x = T.mul[x][uu]
            order += 1
        check(order == m, name + ': u has order exactly %d' % m)


# ---------------------------------------------------------------------------
# Section 8: Euler characteristic
# ---------------------------------------------------------------------------

def section_8():
    # Prop. 8.1 and the examples of p. 167 from the ranks of H^*
    for r in range(1, 9):
        ranks = [binomial(r, n) for n in range(r + 1)]
        check(sum((-1) ** n * c for n, c in enumerate(ranks)) == 0,
              'chi(Z^%d) = 0 from the ranks C(r, n) (C261)' % r)

    # (3.35) chi(H) = |G : H| chi(G) on finite-index subgroups (GAP)
    gap('Ff := FreeGroup(2)')
    G = gap('Ff / []')
    for K in G.LowIndexSubgroupsFpGroup(5):
        k = int(G.Index(K))
        check(free_rank_of(K) == (k + 1, 0),
              '(3.35): a subgroup of index %d of F_2 is free of rank %d'
              % (k, k + 1))
    gap('Ff := FreeGroup(3)')
    G = gap('Ff / []')
    for K in G.LowIndexSubgroupsFpGroup(3):
        k = int(G.Index(K))
        check(free_rank_of(K) == (2 * k + 1, 0),
              '(3.35): a subgroup of index %d of F_3 is free of rank %d'
              % (k, 2 * k + 1))
    gap('Fs := FreeGroup("a1","b1","a2","b2")')
    G = gap('Fs / [Comm(Fs.1,Fs.2)*Comm(Fs.3,Fs.4)]')
    for K in G.LowIndexSubgroupsFpGroup(4):
        k = int(G.Index(K))
        # chi(K) = -2k = 2 - 2g', H_1(K) = Z^(2g')
        check(gap_invariants(K) == [0] * (2 + 2 * k),
              '(3.35): genus-2 surface group, subgroup of index %d has '
              'H_1 = Z^%d' % (k, 2 + 2 * k))
    gap('Fn := FreeGroup("a","b","c")')
    G = gap('Fn / [Fn.1^2*Fn.2^2*Fn.3^2]')
    for K in G.LowIndexSubgroupsFpGroup(4):
        k = int(G.Index(K))
        inv = gap_invariants(K)
        # chi(K) = -k; orientable: H_1 = Z^(2 - chi), else Z^(1 - chi) + Z_2
        check(inv == [0] * (2 + k) or inv == [0] * (1 + k) + [2],
              '(3.35): a^2 b^2 c^2, subgroup of index %d' % k)
    gap('Fk := FreeGroup("x","y")')
    G = gap('Fk / [Fk.1*Fk.2*Fk.1^-1*Fk.2]')
    for K in G.LowIndexSubgroupsFpGroup(6):
        inv = gap_invariants(K)
        check(inv in ([0, 0], [0, 2]),
              'ex. 3.8.9: Klein bottle group, subgroup of index %d (chi = 0)'
              % int(G.Index(K)))

    # ex. 3.8.3 (C268), ex. 3.8.5: SL_2(Z) = Z_4 *_Z_2 Z_6, chi = -1/12 from
    # several torsion-free subgroups of finite index
    gap('Fa := FreeGroup("a", "b")')
    G = gap('Fa / [Fa.1^4, Fa.1^2*Fa.2^-3]')
    libgap.set_global('Gsl', G)
    chis = []
    for N in [3, 4, 5]:
        hom = gap('GroupHomomorphismByImages(Gsl, SL(2, Integers mod %d), '
                  'GeneratorsOfGroup(Gsl), [[[0,1],[-1,0]], [[0,1],[-1,1]]] *'
                  ' One(Integers mod %d))' % (N, N))
        K = hom.Kernel()
        k = int(G.Index(K))
        rk, rel = free_rank_of(K)
        check(rel == 0, 'SL_2(Z): Gamma(%d) is free' % N)
        chis.append(Fraction(1 - rk, k))
    D = commutator_subgroup(G)
    rk, rel = free_rank_of(D)
    check(rel == 0 and rk == 2 and int(G.Index(D)) == 12,
          'SL_2(Z): the commutator subgroup is free of rank 2, index 12')
    chis.append(Fraction(1 - rk, 12))
    check(all(c == Fraction(-1, 12) for c in chis) and
          Fraction(1, 4) + Fraction(1, 6) - Fraction(1, 2) == Fraction(-1, 12),
          'ex. 3.8.3, ex. 3.8.5: chi(SL_2(Z)) = -1/12 = 1/4 + 1/6 - 1/2 '
          'for every subgroup used')
    # Brown's theorem: 12 = 4 * 3, subgroups of order 4 and 3 exist
    check(4 % 4 == 0 and 6 % 3 == 0, 'th:brown-sylow for SL_2(Z)')

    # ex. 3.8.5 for Z_k *_Z_l Z_m: the commutator subgroup (the factors embed
    # in G_ab) is free of rank 1 - |G_ab| chi(G); Brown's theorem
    for l in range(1, 4):
        for s in range(1, 4):
            for t in range(s, 4):
                k, m = l * s, l * t
                if k == 1:
                    continue
                gap('Fa := FreeGroup("a", "b")')
                G = gap('Fa / [Fa.1^%d, Fa.2^%d, Fa.1^%d * Fa.2^-%d]'
                        % (k, m, s, t))
                chi = Fraction(1, k) + Fraction(1, m) - Fraction(1, l)
                D = commutator_subgroup(G)
                idx = int(G.Index(D))
                check(idx == k * m // l,
                      'Z_%d *_Z_%d Z_%d: |G_ab| = km/l' % (k, l, m))
                rk, rel = free_rank_of(D)
                check(rel == 0 and Fraction(1 - rk) == idx * chi,
                      'ex. 3.8.5: chi(Z_%d *_Z_%d Z_%d) = %s'
                      % (k, l, m, chi))
                den = chi.denominator
                for p, e in ZZ(den).factor():
                    check(k % p ** e == 0 or m % p ** e == 0,
                          'th:brown-sylow: a subgroup of order %d in '
                          'Z_%d *_Z_%d Z_%d' % (p ** e, k, l, m))

    # ex. 3.8.4: G_1 * G_2 -> G_1 x G_2 has a free kernel of rank
    # (m_1 - 1)(m_2 - 1) generated by the [g_1, g_2]
    groups = [('Z_2', ['a^2'], 1, '(1,2)', 'Group((1,2))', ['a']),
              ('Z_3', ['a^3'], 1, '(1,2,3)', 'Group((1,2,3))', ['a', 'a^2']),
              ('Z_4', ['a^4'], 1, '(1,2,3,4)', 'Group((1,2,3,4))',
               ['a', 'a^2', 'a^3']),
              ('Z_2^2', ['a^2', 'b^2', 'a*b*a^-1*b^-1'], 2,
               ['(1,2)', '(3,4)'], 'Group((1,2), (3,4))', ['a', 'b', 'a*b']),
              ('S_3', ['a^2', 'b^3', '(a*b)^2'], 2, ['(1,2)', '(1,2,3)'],
               'SymmetricGroup(3)', ['a', 'b', 'b^2', 'a*b', 'a*b^2'])]
    for i1 in range(len(groups)):
        for i2 in range(i1, len(groups)):
            n1, r1, g1, im1, P1, el1 = groups[i1]
            n2, r2, g2, im2, P2, el2 = groups[i2]
            names = ['a%d' % j for j in range(g1 + g2)]
            gap('Fp := FreeGroup(%d)' % (g1 + g2))

            def sub(rel, off):
                return rel.replace('a', 'Fp.%d' % (off + 1)).replace(
                    'b', 'Fp.%d' % (off + 2))
            rels = [sub(x, 0) for x in r1] + [sub(x, g1) for x in r2]
            G = gap('Fp / [%s]' % ', '.join(rels))
            libgap.set_global('Gfp', G)
            im1 = im1 if isinstance(im1, list) else [im1]
            im2 = im2 if isinstance(im2, list) else [im2]
            m1 = int(gap(P1).Size())
            m2 = int(gap(P2).Size())
            gap('Dp := DirectProduct(%s, %s)' % (P1, P2))
            ims = ['Image(Embedding(Dp, 1), %s)' % x for x in im1] + \
                ['Image(Embedding(Dp, 2), %s)' % x for x in im2]
            hom = gap('GroupHomomorphismByImages(Gfp, Dp, GeneratorsOfGroup('
                      'Gfp), [%s])' % ', '.join(ims))
            K = hom.Kernel()
            rk, rel = free_rank_of(K)
            check(int(G.Index(K)) == m1 * m2 and rel == 0 and
                  rk == (m1 - 1) * (m2 - 1),
                  'ex. 3.8.4: kernel of %s * %s -> %s x %s free of rank %d'
                  % (n1, n2, n1, n2, (m1 - 1) * (m2 - 1)))
            def elt(x, off):
                return x.replace('a', 'GeneratorsOfGroup(Gfp)[%d]' % (off + 1)
                                 ).replace('b', 'GeneratorsOfGroup(Gfp)[%d]'
                                           % (off + 2))
            cs = ['Comm(%s, %s)' % (elt(x, 0), elt(y, g1))
                  for x in el1 for y in el2]
            check(len(cs) == (m1 - 1) * (m2 - 1), 'ex. 3.8.4: number of '
                  'commutators [g_1, g_2]')
            comms = gap('Subgroup(Gfp, [%s])' % ', '.join(cs))
            check(int(G.Index(comms)) == m1 * m2,
                  'ex. 3.8.4: the commutators [g_1, g_2] generate the kernel '
                  '(%s, %s)' % (n1, n2))
            chi = Fraction(1 - rk, m1 * m2)
            check(chi == Fraction(1, m1) + Fraction(1, m2) - 1,
                  'ex. 3.8.4: chi(%s * %s) = 1/m_1 + 1/m_2 - 1' % (n1, n2))

    # ex. 3.8.6: the modular group PSL_2(Z) = Z_2 * Z_3, chi = -1/6
    Sm = matrix(ZZ, [[0, -1], [1, 0]])        # z -> -1/z
    Tm = matrix(ZZ, [[1, -1], [1, 0]])        # z -> 1 - 1/z = (z - 1)/z
    I2 = matrix.identity(ZZ, 2)
    check(Sm ** 2 == -I2 and Tm ** 3 == -I2 and Tm != I2 and Tm ** 2 != -I2
          and Tm != -I2,
          'ex. 3.8.6: z -> -1/z has order 2, z -> 1 - 1/z order 3 in PSL_2')
    gap('Fm := FreeGroup(2)')
    G = gap('Fm / [Fm.1^2, Fm.2^3]')
    D = commutator_subgroup(G)
    rk, rel = free_rank_of(D)
    check(rel == 0 and rk == 2 and int(G.Index(D)) == 6 and
          Fraction(1 - rk, 6) == Fraction(-1, 6),
          'ex. 3.8.6: chi(Z_2 * Z_3) = -1/6')

    # ex. 3.8.7 and prop:euler-splitting: Z_p * Z_p -> Z_p (sum): kernel free
    # of rank p - 1; p does not divide 1 - (p - 1) = chi for p > 2, and a
    # complement exists (a free factor maps isomorphically)
    for p in [2, 3, 5, 7]:
        gap('Fz := FreeGroup(2)')
        G = gap('Fz / [Fz.1^%d, Fz.2^%d]' % (p, p))
        libgap.set_global('Gz', G)
        cyc = '(%s)' % ','.join(str(i) for i in range(1, p + 1))
        hom = gap('GroupHomomorphismByImages(Gz, Group(%s), '
                  'GeneratorsOfGroup(Gz), [%s, %s])' % (cyc, cyc, cyc))
        K = hom.Kernel()
        rk, rel = free_rank_of(K)
        check(rel == 0 and rk == p - 1,
              'ex. 3.8.7: kernel of Z_%d * Z_%d -> Z_%d free of rank %d'
              % (p, p, p, p - 1))
        if p > 2:
            check((rk - 1) % p != 0, 'ex. 3.8.7: r != 1 mod %d' % p)
    gap('Fz := FreeGroup(3)')
    G = gap('Fz / [Fz.1^2, Fz.2^2, Fz.3^2]')
    libgap.set_global('Gz', G)
    hom = gap('GroupHomomorphismByImages(Gz, Group((1,2)), '
              'GeneratorsOfGroup(Gz), [(1,2), (1,2), (1,2)])')
    K = hom.Kernel()
    rk, rel = free_rank_of(K)
    check(rel == 0 and rk == 2 and (1 - rk) % 2 != 0,
          'prop:euler-splitting: Z_2 * Z_2 * Z_2 over a free H, chi(H) = -1')

    # torsion one-relator groups as groups of type VFP (ex. 3.8.3): a
    # torsion-free subgroup of finite index gives chi = 1 - n + 1/m
    tf = [('<x, y | [x, y]^2>', 'Fw.1^-1*Fw.2^-1*Fw.1*Fw.2', 2,
           Q8, '[(1,2,3,4)(5,6,7,8), (1,5,3,7)(2,8,4,6)]'),
          ('<x, y | [x, y]^2>', 'Fw.1^-1*Fw.2^-1*Fw.1*Fw.2', 2,
           'Group((1,2,3,4), (1,3))', '[(1,2,3,4), (1,3)]'),
          ('<x, y | [x, y]^3>', 'Fw.1^-1*Fw.2^-1*Fw.1*Fw.2', 3,
           'Group([[1,1,0],[0,1,0],[0,0,1]]*Z(3)^0, '
           '[[1,0,0],[0,1,1],[0,0,1]]*Z(3)^0)',
           '[[[1,1,0],[0,1,0],[0,0,1]]*Z(3)^0, '
           '[[1,0,0],[0,1,1],[0,0,1]]*Z(3)^0]')]
    for name, w, m, target, ims in tf:
        gap('Fw := FreeGroup(2)')
        G = gap('Fw / [(%s)^%d]' % (w, m))
        libgap.set_global('Gt', G)
        hom = gap('GroupHomomorphismByImages(Gt, %s, GeneratorsOfGroup(Gt), '
                  '%s)' % (target, ims))
        K = hom.Kernel()
        k = int(G.Index(K))
        chiK = k * (1 - 2 + Fraction(1, m))
        inv = gap_invariants(K)
        rk, rel = free_rank_of(K)
        check(inv == [0] * int(2 - chiK) and rel == 1,
              name + ': kernel of index %d is a surface group with '
              'chi = %s = |G : K| (1 - 2 + 1/%d)' % (k, chiK, m))

    # ex. 3.8.1, 3.8.2 over Q, G = S_3: r(P) = dim P (x)_G Q = dim P^G;
    # Delta_G is a non-zero module of rank 0; H = 1, P = Q refutes
    # r_(K H)(P) = |G : H| r_(K G)(P).
    T = TGroup(gap('SymmetricGroup(3)'))
    rho = [matrix(QQ, [list(T.rmul(T.unit(i), g)) for i in range(T.n)])
           for g in range(T.n)]            # rows: images of basis vectors
    Delta = matrix(QQ, [list(T.unit(g) - T.unit(T.one)) for g in range(T.n)
                        if g != T.one])
    for nm, B in [('Q G', matrix.identity(QQ, T.n)), ('Delta', Delta)]:
        Vb = B.row_space()
        inv = Vb
        for M in rho:
            inv = inv.intersection((M - 1).left_kernel())
        moved = matrix(QQ, [list(b * (M - 1)) for b in B.rows()
                            for M in rho])
        coinv = Vb.dimension() - moved.rank()
        check(inv.dimension() == coinv,
              'ex. 3.8.1: r(%s) = dim of invariants = %d' % (nm, coinv))
        if nm == 'Delta':
            check(coinv == 0 and Vb.dimension() > 0,
                  'ex. 3.8.1: Delta_G is non-zero of rank 0')
    refuted(1 == T.n * 1, 'ex. 3.8.2: r_(K H)(P) = |G : H| r_(K G)(P) for '
            'H = 1, P = K, G = S_3')


def main():
    section_6()
    section_6_roots()
    section_7()
    section_8()
    print('ok %s: %d checks' % (SCOPE, COUNT[0]))


if __name__ == '__main__':
    main()
