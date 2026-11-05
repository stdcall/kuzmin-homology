"""Exact checks of Chapter 2, §§ 1-3 "Когомологии групп" (Sage).

Run from the project root: sage -python checks/sage/chapter-2a.py (plain
asserts; do not use -O).  The last line is "ok chapter-2a: N checks".

Book: Ю. В. Кузьмин, «Гомологическая теория групп» (Факториал Пресс, 2006),
printed pp. 61-91.  Pages are the printed pages; labels are those of
content/02-01-*.typ, 02-02-*.typ, 02-03-*.typ.  Modules are right modules,
as in the book; GAP multiplies permutations left to right, as the book
multiplies group elements.  Finite groups are multiplication tables built
from GAP (libgap); all arithmetic is over ZZ (Smith normal forms,
ranks, lattice quotients), no floats.

What is checked, by section, and where the expected values come from:

§ 1 (pp. 62-71).
  eq:cochain-coboundary and lem:coboundary-square-zero: delta delta f is
  expanded symbolically for n = 1..7 (arguments as products of consecutive
  g_i, the module action as one product): it has (n + 2)(n + 1) terms
  before cancellation (exc:coboundary-terms, printed answer), every term
  occurs exactly twice with opposite signs, the signs of the main type
  are the printed (-1)^(n+1-i)(-1)^(n-j) and (-1)^(n+1-j)(-1)^(n-(i-1)),
  f(g_3, ..., g_(n+1)) has the printed signs; the seven types of the
  proof have C(n-1, 2), n-1, n-1, n-1, 1, 1, 1 pairs, all seven occur
  first at n = 3, with 1, 2, 2, 2, 1, 1, 1 pairs (printed answer).
  delta^2 = 0 on the normalized cochain complexes of the groups below.
  prop:standard-complex-exact: the printed contracting homotopy
  s_n((g_1, ..., g_n) g) = (g_1, ..., g_n, g) satisfies
  eq:contracting-homotopy on every basis element of X_n (Z_2, Z_3, Z_2^2,
  S_3, n <= 3), and H_0 of eq:standard-complex is Z, not 0 (p. 66).
  prop:coinduced-cohomology: H^n(G, ZZ G) = 0 for n = 1, 2 (ZZ G is
  coinduced for finite G) and H^0(G, ZZ G) = Z (exc:coinduced-h0);
  the proof at n = 1 uses exactness at X_0, which holds for
  eq:standard-resolution (Ker epsilon = Im d_1, Im epsilon = Z free) but
  not for eq:standard-complex (the proof is corrected accordingly).
  prop:finite-group-exponent: every invariant of H^n(G, A) divides |G|
  (several groups and modules); lem:averaging-splitting for
  0 -> Delta -> ZZ G -> ZZ -> 0 (beta(s o sigma)(1) = m).
  exc:averaged-cochain: m f = (-1)^n delta(phi) for every cocycle of a
  Z-basis of Z^n (S_3, Z_4, Z_2^2; modules Z, sign, ZZ G; n <= 3).
  exc:homogeneous-resolution: the printed map (g_1, ..., g_n) g ->
  (g'_0, ..., g'_n) is a bijection of the free bases, G-equivariant and
  commutes with the differentials and epsilon (S_3, Z_4, n <= 3).
  exc:linearized-resolution and exc:tensor-unnormalized-resolution:
  (g_1 - 1) (x) ... (x) (g_n - 1) -> (g_1, ..., g_n) is a chain map, the
  map r_i -> r_i - epsilon(r_i) is a chain map of the tensor complex and
  is the identity on the linearized subcomplex (S_3, n <= 3).
  exc:cohomology-contravariant: corrected Hom_(G_1), Hom_(G_2) of the hint
  (C073): restriction along Z_4 -> Z_2 is a cochain map.

§ 2 (pp. 71-82).
  exc:unnormalized-standard-resolution: the printed homotopy is a
  contracting homotopy (S_3, n <= 3); exc:normalized-quotient-splitting
  (correction C103: (g_1, g_2), not (g_1 g_2)): the printed f' in
  dimensions 1 and 2 commutes with d and f f' = id; exc:non-homotopic-maps;
  exc:automorphism-action-on-cohomology and
  exc:inner-automorphism-on-cohomology: h -> h^* is a cochain map for an
  outer automorphism of Z_2^2 and the regular module, and for an inner
  automorphism f(g) = x^(-1) g x, phi(a) = a x (the book's convention,
  § 1.7) the printed map (g_1, ..., g_n) -> (x g_1 x^(-1), ...) x is a
  chain map over the identity, whose dual is h -> h^*; with
  f(g) = x g x^(-1) the identity phi(a g) = phi(a) f(g) fails (S_3).
  C084, C086-C089: chain-map and homotopy identities are checked through
  the constructions above (they use f_(n-1) d_n = d'_n f_n and
  s_(n-1) d_n + d_(n+1) s_n = id).

§ 3 (pp. 82-91).
  Free groups: eq:free-group-resolution gives H^1(F, Z) = Z^r, H^n = 0.
  Cyclic groups (eq:cyclic-group-resolution, p. 84): Ker epsilon = Im d,
  Ker d = Im sigma, Ker sigma = Im d in ZZ G (m <= 8); the printed
  formulas for H^(2k-1)(G, A), H^(2k)(G, A) agree with the normalized
  standard complex for A = Z, Z_2, Z_3, ZZ G and the sign module (m <= 6);
  H^(2k-1) G = 0, H^(2k) G = Z_m (printed).
  The Gruenberg resolution eq:gruenberg-tensor-resolution built from a
  map F -> G (Schreier transversal and free basis y_j of N, right Fox
  derivatives, the conjugation action of F on N/[N, N]) in the bases of
  p. 87: d^2 = 0 and exactness (as abelian groups, by ranks and
  elementary divisors) for Z_2, Z_3, Z_4, Z_2^2, S_3, Z_6, Q_8, D_8,
  A_4; the free ranks are r_(2k) = s^k, r_(2k+1) = r s^k with
  s = 1 + m(r - 1) (Schreier; exc:copresentation-chain-ranks); for cyclic
  groups the complex is eq:cyclic-group-resolution on the nose, with the
  printed generators e_(2k), e_(2k-1) and differentials.  H^n(G, Z) from
  it agrees with the normalized standard complex, with H^2 = (G^ab)^ and
  H^3 = M(G)^ (GAP: AbelianInvariants, AbelianInvariantsMultiplier); the
  relation module is generated by the relators (exc:one-cycles-
  generators); the Fox derivatives satisfy the fundamental formula.
  Standard presentation (pp. 87-89): the elements x_g x_h x_(gh)^(-1)
  generate N (GAP index computation, Z_3, Z_2^2, S_3) and their number
  (m - 1)^2 is the Schreier rank 1 + m(m - 2), so they are a free basis;
  identity eq:standard-generator-identity (all f, g, h) and
  eq:standard-differential-identity in ZZ F (all tuples, n <= 4; n = 5,
  6 for Z_2^2 and Z_3); the three missing terms of the proof (correction
  C119: (g_1, ..., g_(n-2) g_(n-1), g_n)), printed (g_(n-1) g_(n-2))
  refuted on S_3; the boundary of (f, g, h) (C118).
  p. 87, rank criterion: Schreier's formula for the normal subgroups met
  here; the trivial normal subgroup (rank 0, infinite index) refutes the
  printed criterion without «нетривиальной» (corrected).
  exc:cohomology-generators-bound (corrections C121, C122): for the
  standard and the Gruenberg resolutions k_n = rank Ker delta_n equals
  r_(n-1) - r_(n-2) + ... + (-1)^(n-1) r_0 + (-1)^n, with k_0 = 1 and
  i_0 = r_0 - 1; the printed initial condition k_0 = r_0 - 1 is refuted
  (k_0 = 1 while r_0 = 1); the number of invariants of H^n G is at most
  k_n.

What is NOT established: statements about all groups (only the listed
finite groups and degrees are computed; the general proofs are the book's);
infinite groups other than free groups; the correspondence of our text to
the printed page (checked by reading).
"""

import itertools
import random

from sage.all import ZZ, binomial, libgap, matrix

SCOPE = 'chapter-2a'
COUNT = [0]


def check(cond, what):
    assert bool(cond), 'FAILED: ' + what
    COUNT[0] += 1


def refuted(cond, what):
    assert not bool(cond), 'printed reading unexpectedly holds: ' + what
    COUNT[0] += 1


def gap(src):
    return libgap.eval(src)


# ---------------------------------------------------------------------------
# Finite groups as multiplication tables (GAP: product x*y = x, then y)
# ---------------------------------------------------------------------------

class TGroup:
    def __init__(self, G, name):
        if not G.IsPermGroup():
            G = G.IsomorphismPermGroup().Image()
        self.gap = G
        self.name = name
        deg = max(1, int(G.LargestMovedPoint()))
        self.deg = deg
        els = list(G.AsSSortedList())
        self.perms = [tuple(int(v) - 1 for v in libgap.ListPerm(x, deg))
                      for x in els]
        self.index = {p: i for i, p in enumerate(self.perms)}
        n = len(els)
        self.N = n
        self.mul = [[self.index[tuple(q[p[k]] for k in range(deg))]
                     for q in self.perms] for p in self.perms]
        self.e = self.index[tuple(range(deg))]
        self.inv = [next(j for j in range(n) if self.mul[i][j] == self.e)
                    for i in range(n)]
        self.nonid = [g for g in range(n) if g != self.e]

    def elt(self, x):
        return self.index[tuple(int(v) - 1
                                for v in libgap.ListPerm(x, self.deg))]

    def gens(self):
        return [self.elt(x) for x in self.gap.GeneratorsOfGroup()]

    def prod(self, *xs):
        r = self.e
        for x in xs:
            r = self.mul[r][x]
        return r


def group(src, name):
    return TGroup(gap(src), name)


def add(d, k, c):
    if c:
        v = d.get(k, 0) + c
        if v:
            d[k] = v
        else:
            del d[k]


# ---------------------------------------------------------------------------
# Modules: free abelian of rank k, right action a -> a rho[g] (row vectors)
# ---------------------------------------------------------------------------

def trivial_module(T):
    return [matrix(ZZ, [[1]]) for _ in range(T.N)]


def sign_module(T):
    rho = []
    for p in T.perms:
        s = libgap.SignPerm(libgap.PermList([v + 1 for v in p]))
        rho.append(matrix(ZZ, [[int(s)]]))
    return rho


def regular_module(T):
    """ZZ G with right multiplication: e_h g = e_(hg)."""
    rho = []
    for g in range(T.N):
        M = matrix(ZZ, T.N, T.N, sparse=True)
        for h in range(T.N):
            M[h, T.mul[h][g]] = 1
        rho.append(M)
    return rho


def augmentation_quotient_module(T):
    """ZZ G / ZZ sigma with basis e_h (h != 1) (e_1 = - sum of the others)."""
    rho = []
    others = T.nonid
    pos = {h: i for i, h in enumerate(others)}
    for g in range(T.N):
        M = matrix(ZZ, len(others), len(others), sparse=True)
        for h in others:
            t = T.mul[h][g]
            if t == T.e:
                for u in others:
                    M[pos[h], pos[u]] -= 1
            else:
                M[pos[h], pos[t]] += 1
        rho.append(M)
    return rho


# ---------------------------------------------------------------------------
# Normalized standard complex (p. 65): cochains f(g_1, ..., g_n), g_i != 1
# ---------------------------------------------------------------------------

def tuples(T, n):
    return list(itertools.product(T.nonid, repeat=n))


def coboundary_matrix(T, rho, n):
    """delta_n: F^n(G, A) -> F^(n+1)(G, A), column vectors, eq:cochain-
    coboundary: f(g_1..g_n) g_(n+1) + sum_(i=n)^1 (-1)^(n+1-i)
    f(.., g_i g_(i+1), ..) + (-1)^(n+1) f(g_2, .., g_(n+1))."""
    k = rho[0].nrows()
    src = {t: i for i, t in enumerate(tuples(T, n))}
    dst = tuples(T, n + 1)
    ent = {}

    def put(r, c, M):
        for a in range(k):
            for b in range(k):
                v = M[a, b]
                if v:
                    add(ent, (r * k + b, c * k + a), v)

    def put_scalar(r, c, s):
        for a in range(k):
            add(ent, (r * k + a, c * k + a), s)

    for r, t in enumerate(dst):
        put(r, src[t[:-1]], rho[t[-1]])  # value f(t[:-1]) rho[g_(n+1)]
        for i in range(1, n + 1):
            p = T.mul[t[i - 1]][t[i]]
            if p != T.e:
                u = t[:i - 1] + (p,) + t[i + 1:]
                put_scalar(r, src[u], (-1) ** (n + 1 - i))
        put_scalar(r, src[t[1:]], (-1) ** (n + 1))
    return matrix(ZZ, len(dst) * k, len(src) * k, ent, sparse=True)


def invariants_list(elem_divs, free_rank):
    tors = sorted(int(x) for x in elem_divs if x not in (0, 1))
    return tors + [0] * free_rank


def cohomology_from(Dprev, Dcur, dim):
    """Ker Dcur / Im Dprev for integer matrices (columns = cochains)."""
    rp = 0 if Dprev is None else Dprev.rank()
    rc = 0 if Dcur is None else Dcur.rank()
    ed = [] if Dprev is None else Dprev.elementary_divisors()
    return invariants_list(ed, dim - rc - rp)


def standard_cohomology(T, rho, top):
    """[H^0, ..., H^top] of G with coefficients rho (invariants, 0 = Z)."""
    k = rho[0].nrows()
    D = [coboundary_matrix(T, rho, n) for n in range(top + 1)]
    res = []
    for n in range(top + 1):
        dim = (T.N - 1) ** n * k
        res.append(cohomology_from(D[n - 1] if n else None, D[n], dim))
    return res, D


def cohomology_mod(Dprev, Dcur, dim, m):
    """H^n of the cochain complex tensored with Z_m (lattice computation,
    independent of universal coefficients)."""
    V = ZZ ** dim
    if Dcur is None or Dcur.nrows() == 0:
        K = V
    else:
        big = Dcur.augment(m * matrix.identity(ZZ, Dcur.nrows()))
        ker = big.right_kernel_matrix()
        K = V.submodule([row[:dim] for row in ker.rows()] +
                        [m * v for v in V.basis()])
    gensL = [m * v for v in V.basis()]
    if Dprev is not None:
        gensL += list(Dprev.columns())
    L = V.submodule(gensL)
    Q = K / L
    return sorted(int(x) for x in Q.invariants())


def same_group(a, b):
    """Compare abelian invariants lists (as abstract groups)."""
    def primary(lst):
        out = []
        for x in lst:
            if x == 0:
                out.append(0)
                continue
            for p, e in ZZ(x).factor():
                out.append(p ** e)
        return sorted(out)
    return primary(a) == primary(b)


# ---------------------------------------------------------------------------
# Free ZG-modules: elements are dicts {(key, h): coeff}
# ---------------------------------------------------------------------------

def bar_d(T, x):
    """d on the normalized bar resolution, p. 65."""
    out = {}
    for (t, h), c in x.items():
        n = len(t)
        if n == 0:
            continue
        add(out, (t[:-1], T.mul[t[-1]][h]), c)
        for i in range(1, n):
            p = T.mul[t[i - 1]][t[i]]
            if p != T.e:
                add(out, (t[:i - 1] + (p,) + t[i + 1:], h), (-1) ** (n - i) * c)
        add(out, (t[1:], h), (-1) ** n * c)
    return out


def bar_s(T, x):
    """s_n((g_1, ..., g_n) g) = (g_1, ..., g_n, g), zero if g = 1."""
    out = {}
    for (t, h), c in x.items():
        if h != T.e:
            add(out, (t + (h,), T.e), c)
    return out


def eps(x):
    return sum(c for (t, h), c in x.items() if len(t) == 0)


def basis_elems(T, n, normalized=True):
    src = T.nonid if normalized else range(T.N)
    for t in itertools.product(src, repeat=n):
        for h in range(T.N):
            yield {(t, h): 1}


def unbar_d(T, x):
    """Unnormalized standard resolution (exc:unnormalized-standard-
    resolution): the same formulas, entries equal to 1 allowed."""
    out = {}
    for (t, h), c in x.items():
        n = len(t)
        if n == 0:
            continue
        add(out, (t[:-1], T.mul[t[-1]][h]), c)
        for i in range(1, n):
            p = T.mul[t[i - 1]][t[i]]
            add(out, (t[:i - 1] + (p,) + t[i + 1:], h), (-1) ** (n - i) * c)
        add(out, (t[1:], h), (-1) ** n * c)
    return out


def unbar_s(T, x):
    out = {}
    for (t, h), c in x.items():
        add(out, (t + (h,), T.e), c)
    return out


# ---------------------------------------------------------------------------
# Section 1
# ---------------------------------------------------------------------------

def symbolic_delta_squared():
    """Terms of delta(delta f), f in F^(n-1) (eq:cochain-coboundary): an
    argument is an interval (a, b) meaning g_a ... g_b, the action an
    interval or None.  Each term remembers the outer index i of
    (-1)^(n+1-i) delta f(.., g_i g_(i+1), ..) ('first', 'last' otherwise)."""
    for n in range(1, 8):
        g = [(i, i) for i in range(1, n + 2)]
        outer = [(1, tuple(g[:-1]), (n + 1, n + 1), 'first')]
        for i in range(n, 0, -1):
            a = tuple(g[:i - 1]) + ((i, i + 1),) + tuple(g[i + 1:])
            outer.append(((-1) ** (n + 1 - i), a, None, i))
        outer.append(((-1) ** (n + 1), tuple(g[1:]), None, 'last'))
        terms = []
        for s0, h, act, oi in outer:
            inner = [(1, h[:-1], h[-1])]
            for k in range(n - 1, 0, -1):
                a = h[:k - 1] + ((h[k - 1][0], h[k][1]),) + h[k + 1:]
                inner.append(((-1) ** (n - k), a, None))
            inner.append(((-1) ** n, h[1:], None))
            for s1, a, act1 in inner:
                if act1 is None:
                    tot = act
                elif act is None:
                    tot = act1
                else:
                    assert act1[1] + 1 == act[0]
                    tot = (act1[0], act[1])
                terms.append((s0 * s1, a, tot, oi))
        check(len(terms) == (n + 2) * (n + 1),
              'exc:coboundary-terms: (n+2)(n+1) terms, n = %d' % n)
        groups = {}
        for s, a, act, oi in terms:
            groups.setdefault((a, act), []).append(s)
        check(all(len(v) == 2 and sum(v) == 0 for v in groups.values()),
              'lem:coboundary-square-zero: every term twice, opposite signs, '
              'n = %d' % n)

        def typ(a, act):
            lens = [b - a0 + 1 for a0, b in a]
            start = a[0][0] if a else None
            if act is None:
                if start == 1 and 3 in lens:
                    return 2
                if start == 1 and lens.count(2) == 2:
                    return 1
                if start == 2 and lens.count(2) == 1:
                    return 4
                if start == 3 or (not a and n == 1):
                    return 7
            elif act == (n + 1, n + 1):
                if a and start == 1 and lens.count(2) == 1:
                    return 3
                if (a and start == 2) or (not a and n == 1):
                    return 6
            elif act == (n, n + 1):
                return 5
            return None

        count = {t: 0 for t in range(1, 8)}
        known = True
        for (a, act) in groups:
            t = typ(a, act)
            known = known and t is not None
            if t is not None:
                count[t] += 1
        check(known, 'every term is of a type of the proof, n = %d' % n)
        expect = {1: binomial(n - 1, 2), 2: n - 1, 3: n - 1, 4: n - 1,
                  5: 1, 6: 1, 7: 1}
        check(count == expect, 'pairs per type %s, n = %d' % (count, n))
        if n == 3:
            check([count[t] for t in range(1, 8)] == [1, 2, 2, 2, 1, 1, 1],
                  'exc:coboundary-terms: 1, 2, 2, 2, 1, 1, 1 pairs at n = 3')
        check(all(count[t] > 0 for t in range(1, 8)) == (n >= 3),
              'all seven types occur iff n >= 3 (n = %d)' % n)
        ok7 = ok1 = True
        for s, a, act, oi in terms:
            if typ(a, act) == 7 and n >= 2:
                ok7 = ok7 and ((oi == 'last' and s == -1) or
                               (oi == 1 and s == 1))
            if typ(a, act) == 1:
                j, i = [a0 for a0, b in a if b == a0 + 1]
                if oi == i:
                    ok1 = ok1 and s == (-1) ** (n + 1 - i) * (-1) ** (n - j)
                else:
                    ok1 = ok1 and oi == j and \
                        s == (-1) ** (n + 1 - j) * (-1) ** (n - (i - 1))
        check(ok7, 'f(g_3, .., g_(n+1)): sign - from the last term, + from '
              'i = 1 (p. 64), n = %d' % n)
        check(ok1, 'main type: signs (-1)^(n+1-i)(-1)^(n-j) and '
              '(-1)^(n+1-j)(-1)^(n-(i-1)) (p. 63-64), n = %d' % n)


def check_contracting_homotopy(T, top):
    """eq:contracting-homotopy on every basis element (g_1..g_n) h of X_n;
    at n = 0 with d_0 = epsilon and s_(-1)(1) = (), i.e. for the augmented
    eq:standard-resolution."""
    for n in range(0, top + 1):
        ok = True
        for b in basis_elems(T, n):
            if n == 0:
                lhs = {((), T.e): eps(b)}  # s_(-1) epsilon
            else:
                lhs = bar_s(T, bar_d(T, b))
            for k, c in bar_d(T, bar_s(T, b)).items():
                add(lhs, k, c)
            ok = ok and lhs == b
        check(ok, 'prop:standard-complex-exact: the printed s_n satisfies '
              'd s + s d = id on X_%d, %s' % (n, T.name))


def section_1(groups):
    symbolic_delta_squared()
    S3 = groups['S3']
    Z4 = groups['Z4']
    V4 = groups['Z2^2']
    for name in ('Z2', 'Z3', 'Z4', 'Z2^2', 'S3'):
        check_contracting_homotopy(groups[name], 3)
    # p. 66: in X_0 the complex (2.6) is not exact: Ker d_0 / Im d_1 = Z
    for T in (S3, Z4):
        D1 = matrix(ZZ, T.N, (T.N - 1) * T.N, sparse=True)
        col = 0
        for g in T.nonid:
            for h in range(T.N):
                D1[T.mul[g][h], col] += 1
                D1[h, col] -= 1
                col += 1
        ed = D1.elementary_divisors()
        check(D1.rank() == T.N - 1 and all(x in (0, 1) for x in ed),
              'p. 66: H_0 of (2.6) is Z (Im d_1 = Delta_G of rank m - 1, '
              'saturated), %s' % T.name)
    # delta^2 = 0 and cohomology of the trivial module
    tops = {'Z2': 6, 'Z3': 6, 'Z4': 4, 'Z2^2': 4, 'Z5': 3, 'Z6': 3, 'S3': 3}
    std = {}
    for name, top in tops.items():
        T = groups[name]
        H, D = standard_cohomology(T, trivial_module(T), top)
        for n in range(top):
            check((D[n + 1] * D[n]).is_zero(),
                  'lem:coboundary-square-zero: delta^2 = 0, %s, n = %d'
                  % (name, n))
        check(H[0] == [0], 'H^0(G, Z) = Z, %s' % name)
        for n in range(1, top + 1):
            check(all(T.N % x == 0 for x in H[n] if x),
                  'prop:finite-group-exponent: exponent of H^%d(%s, Z) '
                  'divides |G|' % (n, name))
            check(0 not in H[n], 'H^%d(%s, Z) finite' % (n, name))
        std[name] = (H, D)
    # prop:coinduced-cohomology: H^n(G, ZZ G) = 0, n = 1, 2; H^0 = Z
    for name, top in (('Z2', 4), ('Z3', 3), ('Z4', 2), ('Z2^2', 2), ('S3', 2)):
        T = groups[name]
        H, D = standard_cohomology(T, regular_module(T), top)
        check(H[0] == [0], 'exc:coinduced-h0: H^0(G, ZZ G) = Z, %s' % name)
        check(all(H[n] == [] for n in range(1, top + 1)),
              'prop:coinduced-cohomology: H^n(%s, ZZ G) = 0, 1 <= n <= %d'
              % (name, top))
        for n in range(top):
            check((D[n + 1] * D[n]).is_zero(), 'delta^2 = 0, ZZ G')
    # prop:finite-group-exponent with other modules
    for name, rho_f, top in (('S3', sign_module, 3), ('Z4', None, 3),
                             ('S3', augmentation_quotient_module, 2),
                             ('Z2^2', augmentation_quotient_module, 2)):
        T = groups[name]
        if rho_f is None:  # Z_4 acting on Z^2 by rotation through 90 deg
            g = T.gens()[0]
            R = matrix(ZZ, [[0, 1], [-1, 0]])
            rho = [None] * T.N
            x = T.e
            for k in range(4):
                rho[x] = R ** k
                x = T.mul[x][g]
        else:
            rho = rho_f(T)
        H, D = standard_cohomology(T, rho, top)
        for n in range(1, top + 1):
            check(all(T.N % x == 0 for x in H[n] if x) and 0 not in H[n],
                  'prop:finite-group-exponent, %s, nontrivial module, n = %d'
                  % (name, n))
    # lem:averaging-splitting for 0 -> Delta -> ZZ G -> ZZ -> 0, s(1) = 1
    for T in (S3, V4):
        # (s o g)(x) = s(x g^-1) g; s(1) = 1 in ZZ G; sum over G
        img = {}
        for g in range(T.N):
            add(img, g, 1)  # s(1 g^-1) g = 1 * g
        check(sum(img.values()) == T.N and len(img) == T.N,
              'lem:averaging-splitting: (s o sigma)(1) = sigma, beta = m')
    # exc:averaged-cochain: m f = (-1)^n delta(phi), phi = sum_g f(g, ...)
    for name, rho_f, top in (('S3', trivial_module, 3), ('S3', sign_module, 3),
                             ('Z4', trivial_module, 3),
                             ('Z2^2', regular_module, 2)):
        T = groups[name]
        rho = rho_f(T)
        k = rho[0].nrows()
        for n in range(1, top + 1):
            Dn = coboundary_matrix(T, rho, n)
            Dm = coboundary_matrix(T, rho, n - 1)
            ker = Dn.right_kernel_matrix()
            src = {t: i for i, t in enumerate(tuples(T, n - 1))}
            ok = True
            for f in ker.rows():
                phi = [0] * (len(src) * k)
                for i, t in enumerate(tuples(T, n)):
                    j = src[t[1:]]
                    for a in range(k):
                        phi[j * k + a] += f[i * k + a]
                lhs = T.N * f
                rhs = (-1) ** n * (Dm * matrix(ZZ, len(phi), 1, phi)).column(0)
                ok = ok and lhs == rhs
            check(ok, 'exc:averaged-cochain: m f = (-1)^n delta(phi) on a '
                  'basis of Z^%d, %s (%d cocycles)' % (n, name, ker.nrows()))
    # exc:homogeneous-resolution
    for T in (S3, Z4):
        for n in range(0, 4):
            def Phi(x):
                out = {}
                for (t, h), c in x.items():
                    q = len(t)
                    gp = [None] * (q + 1)
                    gp[q] = h
                    for k in range(q, 0, -1):
                        gp[k - 1] = T.mul[t[k - 1]][gp[k]]
                    add(out, tuple(gp), c)
                return out

            def hom_d(y):
                out = {}
                for t, c in y.items():
                    m = len(t) - 1
                    for i in range(m + 1):
                        u = t[:i] + t[i + 1:]
                        if any(u[j] == u[j + 1] for j in range(len(u) - 1)):
                            continue
                        add(out, u, (-1) ** (m - i) * c)
                return out
            imgs = set()
            adj = chain = equi = True
            for b in basis_elems(T, n):
                y = Phi(b)
                (key,) = y.keys()
                adj = adj and all(key[j] != key[j + 1] for j in range(n))
                imgs.add(key)
                if n:
                    chain = chain and Phi(bar_d(T, b)) == hom_d(y)
                else:
                    chain = chain and sum(y.values()) == eps(b)
                # G-equivariance: Phi(b g) = Phi(b) g (diagonal action)
                ((t, h),) = b.keys()
                for g in range(T.N):
                    yb = Phi({(t, T.mul[h][g]): 1})
                    equi = equi and \
                        yb == {tuple(T.mul[v][g] for v in key): 1}
            check(adj and len(imgs) == (T.N - 1) ** n * T.N,
                  'exc:homogeneous-resolution: bijection of the free bases '
                  '(adjacent entries distinct), %s, n = %d' % (T.name, n))
            check(chain, 'exc:homogeneous-resolution: d Phi = Phi d '
                  '(epsilon at n = 0), %s, n = %d' % (T.name, n))
            check(equi, 'exc:homogeneous-resolution: Phi is G-equivariant '
                  '(diagonal action), %s, n = %d' % (T.name, n))
    # exc:linearized-resolution, exc:tensor-unnormalized-resolution
    for T in (S3, V4):
        def tens_d(x):
            """Tensor form of the unnormalized resolution: on
            g_1 x .. x g_n x h as on (g_1, .., g_n) h."""
            return unbar_d(T, x)

        def lin(x):
            out = {}
            for (t, h), c in x.items():
                for signs in itertools.product((0, 1), repeat=len(t)):
                    u = tuple(t[i] if signs[i] else T.e for i in range(len(t)))
                    add(out, (u, h), c * (-1) ** (len(t) - sum(signs)))
            return out

        def fmap(x):  # r_i -> r_i - epsilon(r_i) on pure tensors g_i
            return lin(x)
        for n in range(1, 4):
            ok1 = ok2 = ok3 = True
            for b in basis_elems(T, n):
                ok1 = ok1 and lin(bar_d(T, b)) == tens_d(lin(b))
                ok2 = ok2 and fmap(lin(b)) == lin(b)
            for b in basis_elems(T, n, normalized=False):
                ok3 = ok3 and fmap(tens_d(b)) == tens_d(fmap(b))
            check(ok1, 'exc:linearized-resolution: (g_1 - 1) (x) .. (x) '
                  '(g_n - 1) -> (g_1, .., g_n) is a chain map, %s, n = %d'
                  % (T.name, n))
            check(ok2, 'exc:tensor-unnormalized-resolution: f = id on the '
                  'linearized subcomplex, %s, n = %d' % (T.name, n))
            check(ok3, 'exc:tensor-unnormalized-resolution: f is a chain '
                  'map, %s, n = %d' % (T.name, n))
    # exc:cohomology-contravariant (C073): Z_4 -> Z_2, restriction of
    # cochains along alpha commutes with delta (A = Z with sign of Z_2)
    Z2 = groups['Z2']
    gen4 = Z4.gens()[0]
    gen2 = Z2.gens()[0]
    alpha = {}
    x, y = Z4.e, Z2.e
    for k in range(4):
        alpha[x] = y
        x, y = Z4.mul[x][gen4], Z2.mul[y][gen2]
    rho2 = [matrix(ZZ, [[1]]) if g == Z2.e else matrix(ZZ, [[-1]])
            for g in range(2)]
    rho4 = [rho2[alpha[g]] for g in range(4)]
    for n in range(0, 4):
        D2 = coboundary_matrix(Z2, rho2, n)
        D4 = coboundary_matrix(Z4, rho4, n)

        def pull(m_):
            src = {t: i for i, t in enumerate(tuples(Z2, m_))}
            tt = tuples(Z4, m_)
            P = matrix(ZZ, len(tt), len(src), sparse=True)
            for i, t in enumerate(tt):
                u = tuple(alpha[v] for v in t)
                if Z2.e not in u:
                    P[i, src[u]] = 1
            return P
        check(D4 * pull(n) == pull(n + 1) * D2,
              'exc:cohomology-contravariant: alpha^* commutes with delta, '
              'n = %d' % n)
    return std


# ---------------------------------------------------------------------------
# Section 2
# ---------------------------------------------------------------------------

def section_2(groups):
    S3 = groups['S3']
    V4 = groups['Z2^2']
    # exc:unnormalized-standard-resolution: contracting homotopy
    for T in (S3, V4):
        for n in range(0, 3):
            ok = True
            for b in basis_elems(T, n, normalized=False):
                lhs = unbar_s(T, unbar_d(T, b)) if n else \
                    {((), T.e): eps(b)}
                for k, c in unbar_d(T, unbar_s(T, b)).items():
                    add(lhs, k, c)
                ok = ok and lhs == b
            check(ok, 'exc:unnormalized-standard-resolution: the printed '
                  's satisfies d s + s d = id on X_%d, %s' % (n, T.name))
    # exc:normalized-quotient-splitting (C103)
    for T in (S3, V4):
        e = T.e

        def f1(g, h):  # f'((g) h + Y_1) = ((g) - (1)) h
            return {((g,), h): 1, ((e,), h): -1}

        def f2(g1, g2, h):
            return {((g1, g2), h): 1, ((g1, e), h): -1, ((e, g2), h): -1,
                    ((e, e), h): 1}

        def fp(x):  # f' on normalized chains of degree 1, 2
            out = {}
            for (t, h), c in x.items():
                y = f1(t[0], h) if len(t) == 1 else (
                    f2(t[0], t[1], h) if len(t) == 2 else {(t, h): 1})
                for k, v in y.items():
                    add(out, k, c * v)
            return out

        def proj(x):  # f: X -> X / Y
            out = {}
            for (t, h), c in x.items():
                if e not in t:
                    add(out, (t, h), c)
            return out
        for n in (1, 2):
            ok1 = all(unbar_d(T, fp(b)) == fp(bar_d(T, b))
                      for b in basis_elems(T, n))
            ok2 = all(proj(fp(b)) == b for b in basis_elems(T, n))
            check(ok1, "exc:normalized-quotient-splitting (C103): d f' = "
                  "f' d, %s, n = %d" % (T.name, n))
            check(ok2, "exc:normalized-quotient-splitting: f f' = id, %s, "
                  "n = %d" % (T.name, n))
    # exc:non-homotopic-maps: Hom(Z_n, Z) = 0, so no s_0 with id = d_1 s_0
    for nn in range(2, 7):
        check(all((nn * c) % nn == 0 for c in range(nn)),
              'exc:non-homotopic-maps: a map Z_%d -> Z is zero' % nn)
    # exc:automorphism-action-on-cohomology: f swaps the generators of
    # Z_2^2, phi(e_h) = e_(f(h)) on ZZ G; h -> h^* commutes with delta
    a, b = V4.gens()
    fmap = {V4.e: V4.e, a: b, b: a, V4.mul[a][b]: V4.mul[a][b]}
    rho = regular_module(V4)
    Phi = matrix(ZZ, 4, 4, {(h, fmap[h]): 1 for h in range(4)})
    check(all(Phi * rho[fmap[g]] == rho[g] * Phi for g in range(4)),
          'eq:semilinear-automorphism: phi(a g) = phi(a) f(g), Z_2^2')
    finv = {v: k for k, v in fmap.items()}

    def star(n, k):
        src = {t: i for i, t in enumerate(tuples(V4, n))}
        tt = tuples(V4, n)
        P = matrix(ZZ, len(tt) * k, len(tt) * k, sparse=True)
        for i, t in enumerate(tt):
            j = src[tuple(finv[v] for v in t)]
            for p in range(k):
                for q in range(k):
                    if Phi[q, p]:
                        P[i * k + p, j * k + q] = Phi[q, p]
        return P
    for n in range(0, 3):
        D = coboundary_matrix(V4, rho, n)
        check(D * star(n, 4) == star(n + 1, 4) * D,
              'exc:automorphism-action-on-cohomology: delta(h^*) = '
              '(delta h)^*, n = %d' % n)
    # exc:inner-automorphism-on-cohomology on S_3
    T = S3
    rho_s = sign_module(T)
    Dsg = [coboundary_matrix(T, rho_s, n) for n in range(4)]
    Dtr = [coboundary_matrix(T, trivial_module(T), n) for n in range(4)]
    check(standard_cohomology(T, rho_s, 3)[0][1:] == [[2], [3], [2]],
          'H^1, H^2, H^3 of S_3 with the sign module: Z_2, Z_3, Z_2 '
          '(nonzero, so the next check is not vacuous)')
    for x in T.nonid:
        xi = T.inv[x]

        def Phi_x(z):
            out = {}
            for (t, h), c in z.items():
                add(out, (tuple(T.prod(x, v, xi) for v in t),
                          T.mul[x][h]), c)
            return out
        for n in range(0, 4):
            if n:
                ok = all(bar_d(T, Phi_x(bb)) == Phi_x(bar_d(T, bb))
                         for bb in basis_elems(T, n))
            else:
                ok = all(eps(Phi_x(bb)) == eps(bb) for bb in basis_elems(T, 0))
            check(ok, 'exc:inner-automorphism-on-cohomology: the printed map '
                  'is a chain map over id_Z, S_3, n = %d' % n)
        # on cohomology: h^* - h is a coboundary for every cocycle h,
        # h^*(g_1, .., g_n) = h(x g_1 x^-1, ..) x; H^2(S_3, Z) = Z_2 and
        # H^n(S_3, sign), n = 1, 2, 3, are nonzero
        for mname, rr, Dl in (('Z', trivial_module(T), Dtr),
                              ('sign', rho_s, Dsg)):
            for n in (1, 2, 3):
                tt = tuples(T, n)
                pos = {t: i for i, t in enumerate(tt)}
                sx = rr[x][0, 0]
                V = ZZ ** len(tt)
                B = V.submodule(Dl[n - 1].columns())
                ok = True
                for f in Dl[n].right_kernel_matrix().rows():
                    hs = V([sx * f[pos[tuple(T.prod(x, v, xi) for v in t)]]
                            for t in tt])
                    ok = ok and (hs - f) in B
                check(ok, 'exc:inner-automorphism-on-cohomology: alpha_x^* '
                      '= id on H^%d(S_3, %s)' % (n, mname))
        # phi(a) = a x satisfies phi(a g) = phi(a) f(g) for f(g) = x^-1 g x
        # (alpha_x of § 1.7), not for f(g) = x g x^-1 (regular module)
        ok = all(T.mul[T.mul[h][g]][x] == T.mul[T.mul[h][x]][T.prod(xi, g, x)]
                 for h in range(T.N) for g in range(T.N))
        check(ok, 'phi(a g) = phi(a) f(g) with f(g) = x^-1 g x')
        bad = all(T.mul[T.mul[h][g]][x] ==
                  T.mul[T.mul[h][x]][T.prod(x, g, xi)]
                  for h in range(T.N) for g in range(T.N))
        if not all(T.prod(x, g, xi) == T.prod(xi, g, x) for g in range(T.N)):
            refuted(bad, 'with f(g) = x g x^-1 the identity '
                    'eq:semilinear-automorphism holds')


# ---------------------------------------------------------------------------
# Section 3: free groups, cyclic groups, Gruenberg resolution
# ---------------------------------------------------------------------------

def cyclic_formula(T, rho, n):
    """The printed H^(2k-1), H^(2k) of p. 84 for G = <g>, A = rho:
    Ker sigma / A(g - 1) and Ker(g - 1) / A sigma (row vectors)."""
    g = T.gens()[0]
    k = rho[0].nrows()
    I = matrix.identity(ZZ, k)
    dmat = rho[g] - I
    smat = sum(rho[h] for h in range(T.N))
    if n == 0:
        Kmat = dmat
        return invariants_list([], k - Kmat.rank())
    if n % 2 == 1:
        Kmat, Imat = smat, dmat
    else:
        Kmat, Imat = dmat, smat
    # a -> a Kmat, kernel mod image of a -> a Imat (column form: transpose)
    return cohomology_from(Imat.transpose(), Kmat.transpose(), k)


class FreeData:
    """F = F(x_1..x_r) -> G, x_i -> gens[i]; Schreier transversal, free basis
    of N, right Fox derivatives in ZZ G, conjugation action on N/[N,N]."""

    def __init__(self, T, gens):
        self.T = T
        self.gens = gens
        r = len(gens)
        self.r = r
        word = {T.e: ()}
        queue = [T.e]
        while queue:
            c = queue.pop(0)
            for i in range(r):
                for s in (1, -1):
                    d = T.mul[c][gens[i] if s == 1 else T.inv[gens[i]]]
                    if d not in word:
                        word[d] = word[c] + ((i, s),)
                        queue.append(d)
        self.word = word
        ygens = []
        yindex = {}
        for c in range(T.N):
            for i in range(r):
                d = T.mul[c][gens[i]]
                if word[d] == word[c] + ((i, 1),) or \
                        word[c] == word[d] + ((i, -1),):
                    continue
                yindex[(c, i)] = len(ygens)
                ygens.append(reduce(word[c] + ((i, 1),) + inverse(word[d])))
        self.ygens = ygens
        self.yindex = yindex
        self.s = len(ygens)
        # conjugation matrices M(g)[j, l] = exp. sum of y_l in t y_j t^-1
        self.M = {}
        for g in range(T.N):
            t = word[g]
            self.M[g] = matrix(ZZ, [self.expsum(t + y + inverse(t))
                                    for y in ygens])
        # Fox Jacobian J[j][i] in ZZ G (dicts)
        self.J = [[self.fox(y, i) for i in range(r)] for y in ygens]

    def image(self, w):
        T = self.T
        c = T.e
        for i, s in w:
            c = T.mul[c][self.gens[i] if s == 1 else T.inv[self.gens[i]]]
        return c

    def expsum(self, w):
        T = self.T
        v = [0] * self.s
        c = T.e
        for i, s in w:
            if s == 1:
                j = self.yindex.get((c, i))
                if j is not None:
                    v[j] += 1
                c = T.mul[c][self.gens[i]]
            else:
                c = T.mul[c][T.inv[self.gens[i]]]
                j = self.yindex.get((c, i))
                if j is not None:
                    v[j] -= 1
        assert c == T.e, 'word not in N'
        return v

    def fox(self, w, i):
        """Right Fox derivative D_i(w) mapped to ZZ G:
        w - 1 = sum_i (x_i - 1) D_i(w), D_i(uv) = D_i(u) v + D_i(v)."""
        T = self.T
        out = {}
        suf = T.e
        for (j, s) in reversed(w):
            gj = self.gens[j]
            if j == i:
                if s == 1:
                    add(out, suf, 1)
                else:
                    add(out, T.mul[T.inv[gj]][suf], -1)
            suf = T.mul[gj if s == 1 else T.inv[gj]][suf]
        return out


def reduce(w):
    out = []
    for a in w:
        if out and out[-1][0] == a[0] and out[-1][1] == -a[1]:
            out.pop()
        else:
            out.append(a)
    return tuple(out)


def inverse(w):
    return tuple((i, -s) for i, s in reversed(w))


def gruenberg_basis(FD, n):
    k = n // 2
    if n % 2 == 0:
        return list(itertools.product(range(FD.s), repeat=k))
    return [(i,) + j for i in range(FD.r)
            for j in itertools.product(range(FD.s), repeat=k)]


def kron_entry(M, js, ls):
    v = 1
    for a, b in zip(js, ls):
        v *= M[a, b]
        if not v:
            return 0
    return v


def gruenberg_d(FD, n, b):
    """d_n on a basis element b of C_n (dict {(key, h): c}), p. 87."""
    T = FD.T
    out = {}
    if n == 1:
        (i,) = b
        add(out, ((), FD.gens[i]), 1)
        add(out, ((), T.e), -1)
        return out
    k = n // 2
    if n % 2 == 1:
        i, js = b[0], b[1:]
        gi = FD.gens[i]
        M = FD.M[gi]
        for ls in itertools.product(range(FD.s), repeat=k):
            c = kron_entry(M, js, ls)
            if c:
                add(out, (ls, gi), c)
        add(out, (js, T.e), -1)
        return out
    j1, rest = b[0], b[1:]
    for i in range(FD.r):
        for g, c in FD.J[j1][i].items():
            M = FD.M[g]
            for ls in itertools.product(range(FD.s), repeat=k - 1):
                v = kron_entry(M, rest, ls)
                if v:
                    add(out, ((i,) + ls, g), c * v)
    return out


def gruenberg_abelian_matrix(FD, n):
    """d_n as an integer matrix C_n -> C_(n-1) on the Z-bases (key, h)."""
    T = FD.T
    src = gruenberg_basis(FD, n)
    dst = gruenberg_basis(FD, n - 1)
    dpos = {b: i for i, b in enumerate(dst)}
    ent = {}
    for ci, b in enumerate(src):
        img = gruenberg_d(FD, n, b)
        for g in range(T.N):
            for (key, h), c in img.items():
                add(ent, (dpos[key] * T.N + T.mul[h][g], ci * T.N + g), c)
    return matrix(ZZ, len(dst) * T.N, len(src) * T.N, ent, sparse=True)


def gruenberg_cochain_matrix(FD, n):
    """delta_n: Hom_G(C_n, Z) -> Hom_G(C_(n+1), Z), trivial module Z."""
    src = gruenberg_basis(FD, n)
    dst = gruenberg_basis(FD, n + 1)
    spos = {b: i for i, b in enumerate(src)}
    ent = {}
    for r, b in enumerate(dst):
        for (key, h), c in gruenberg_d(FD, n + 1, b).items():
            add(ent, (r, spos[key]), c)
    return matrix(ZZ, len(dst), len(src), ent, sparse=True)


def exact_at(Din, Dout, dim):
    """H = Ker Dout / Im Din = 0 for integer matrices (columns = chains)."""
    rin = 0 if Din is None else Din.rank()
    rout = 0 if Dout is None else Dout.rank()
    if rin + rout != dim:
        return False
    return Din is None or all(x in (0, 1) for x in Din.elementary_divisors())


def section_3(groups, std):
    # free groups: (2.20) gives H^0 = Z, H^1 = Z^r, H^n = 0
    for r in range(1, 5):
        # Hom_F(ZZ F, Z) = Z -> Hom_F(Delta_F, Z) = Z^r, f_a(x_i) = a(x_i-1)
        delta0 = matrix(ZZ, r, 1, [0] * r)
        check(cohomology_from(None, delta0, 1) == [0] and
              cohomology_from(delta0, None, r) == [0] * r,
              'H^0 F = Z, H^1 F = Z^%d (p. 83)' % r)
    # cyclic groups, p. 84
    for m in range(2, 9):
        T = TGroup(gap('CyclicGroup(IsPermGroup, %d)' % m), 'Z%d' % m)
        g = T.gens()[0]
        R = regular_module(T)
        dmat = R[g] - matrix.identity(ZZ, m)
        smat = sum(R[h] for h in range(m))
        epsm = matrix(ZZ, m, 1, [1] * m)
        # row-vector maps a -> a dmat etc.; exactness of
        # ... -> ZZ G -(sigma)-> ZZ G -(d)-> ZZ G -(eps)-> Z
        check(exact_at(dmat.transpose(), epsm.transpose(), m),
              'Ker epsilon = Im d, Z_%d' % m)
        check(exact_at(smat.transpose(), dmat.transpose(), m),
              'Ker d = Im sigma, Z_%d' % m)
        check(exact_at(dmat.transpose(), smat.transpose(), m),
              'Ker sigma = Im d = Delta_G, Z_%d' % m)
        check(epsm.transpose().rank() == 1 and all(
            x == 1 for x in epsm.transpose().elementary_divisors()),
            'epsilon onto Z')
    for m in range(2, 7):
        T = TGroup(gap('CyclicGroup(IsPermGroup, %d)' % m), 'Z%d' % m)
        top = 5 if m <= 3 else (4 if m <= 4 else 3)
        mods = [('Z', trivial_module(T)), ('ZG', regular_module(T))]
        for q in (2, 3):
            # Z_q as a trivial module is not free abelian; use Z with the
            # mod q comparison below instead
            pass
        if m % 2 == 0:
            gg = T.gens()[0]
            rho = [None] * m
            x = T.e
            for k in range(m):
                rho[x] = matrix(ZZ, [[(-1) ** k]])
                x = T.mul[x][gg]
            mods.append(('sign', rho))
        for mname, rho in mods:
            if mname == 'ZG' and m > 4:
                continue
            tp = min(top, 3) if mname == 'ZG' else top
            H, D = standard_cohomology(T, rho, tp)
            for n in range(0, tp + 1):
                check(same_group(H[n], cyclic_formula(T, rho, n)),
                      'p. 84: H^%d(Z_%d, %s) by the printed formula'
                      % (n, m, mname))
            if mname == 'Z':
                for n in range(1, tp + 1):
                    check(H[n] == ([] if n % 2 else [m]),
                          'H^%d(Z_%d) = %s (p. 84)'
                          % (n, m, '0' if n % 2 else 'Z_%d' % m))
            # Z_q coefficients by the printed formula, q = 2, 3
            for q in (2, 3):
                for n in range(0, tp + 1):
                    Hq = cohomology_mod(D[n - 1] if n else None, D[n],
                                        (m - 1) ** n * rho[0].nrows(), q)
                    # printed formula with A tensored by Z_q
                    g0 = T.gens()[0]
                    k = rho[0].nrows()
                    dm = rho[g0] - matrix.identity(ZZ, k)
                    sm = sum(rho[h] for h in range(m))
                    if n == 0:
                        Km, Im_ = dm, None
                    elif n % 2:
                        Km, Im_ = sm, dm
                    else:
                        Km, Im_ = dm, sm
                    Hf = cohomology_mod(None if Im_ is None else
                                        Im_.transpose(), Km.transpose(), k, q)
                    check(Hf == Hq, 'p. 84 with A = %s (x) Z_%d, Z_%d, n = %d'
                          % (mname, q, m, n))
    # Gruenberg resolution
    specs = [('Z2', None), ('Z3', None), ('Z4', None), ('Z2^2', None),
             ('S3', None), ('Z6', 'gens2'), ('Q8', None), ('D8', None),
             ('A4', None)]
    exact_top = {'Z2': 5, 'Z3': 5, 'Z4': 5, 'Z2^2': 4, 'S3': 4, 'Z6': 3,
                 'Q8': 3, 'D8': 3, 'A4': 2}
    coh_top = {'Z2': 6, 'Z3': 6, 'Z4': 6, 'Z2^2': 5, 'S3': 5, 'Z6': 5,
               'Q8': 5, 'D8': 4, 'A4': 4}
    for name, _ in specs:
        T = groups[name]
        if name == 'Z6':
            # two generators: x of order 2 and y of order 3
            x = next(g for g in T.nonid if T.mul[g][g] == T.e)
            y = next(g for g in T.nonid if T.prod(g, g, g) == T.e)
            gens = [x, y]
        else:
            gens = T.gens()
        FD = FreeData(T, gens)
        m, r = T.N, len(gens)
        s = 1 + m * (r - 1)
        check(FD.s == s, 'Schreier: rank N = 1 + m(r - 1) = %d, %s'
              % (s, name))
        # Fox fundamental formula on the free generators of N
        ok = True
        for j, y in enumerate(FD.ygens):
            tot = {}
            for i in range(r):
                for g, c in FD.J[j][i].items():
                    add(tot, T.mul[gens[i]][g], c)
                    add(tot, g, -c)
            ok = ok and tot == {}
        check(ok, 'Fox: 0 = g_y - 1 = sum (g_i - 1) D_i(y) for the %d free '
              'generators y of N, %s' % (s, name))
        # relation module generated by the relators (exc:one-cycles-gen.)
        rels = [tuple(rr) for rr in relators(T, name, gens)]
        vecs = []
        for w in rels:
            v = FD.expsum(w)
            for g in range(T.N):
                vecs.append(list(matrix(ZZ, [v]) * FD.M[g])[0])
        Mv = matrix(ZZ, vecs)
        check(Mv.rank() == s and all(x == 1 for x in
                                     Mv.elementary_divisors()[:s]),
              'exc:one-cycles-generators: images of v_i - 1 generate '
              'Delta_N / Delta_F Delta_N as a G-module, %s' % name)
        # ranks of the chain modules
        for n in range(0, 6):
            k = n // 2
            rn = s ** k if n % 2 == 0 else r * s ** k
            check(len(gruenberg_basis(FD, n)) == rn,
                  'exc:copresentation-chain-ranks: r_%d = %d, %s'
                  % (n, rn, name))
        # d^2 = 0 and exactness (as abelian groups)
        et = exact_top[name]
        Dab = {n: gruenberg_abelian_matrix(FD, n) for n in range(1, et + 2)}
        epsm = matrix(ZZ, 1, m, [1] * m)
        check((epsm * Dab[1]).is_zero(), 'epsilon d_1 = 0')
        for n in range(1, et + 1):
            check((Dab[n] * Dab[n + 1]).is_zero(),
                  'Gruenberg d^2 = 0, %s, n = %d' % (name, n))
        check(exact_at(Dab[1], epsm, m), 'exact at C_0, %s' % name)
        for n in range(1, et + 1):
            check(exact_at(Dab[n + 1], Dab[n], Dab[n].ncols()),
                  'eq:gruenberg-tensor-resolution exact at C_%d, %s'
                  % (n, name))
        # cohomology with trivial coefficients
        ct = coh_top[name]
        Dc = [gruenberg_cochain_matrix(FD, n) for n in range(ct + 1)]
        Hg = []
        for n in range(ct + 1):
            Hg.append(cohomology_from(Dc[n - 1] if n else None, Dc[n],
                                      len(gruenberg_basis(FD, n))))
        check(Hg[0] == [0] and Hg[1] == [], 'H^0 = Z, H^1 = 0, %s' % name)
        ab = sorted(int(v) for v in T.gap.AbelianInvariants())
        mult = sorted(int(v) for v in T.gap.AbelianInvariantsMultiplier())
        check(same_group(Hg[2], ab), 'H^2(%s, Z) = (G^ab)^ = %s'
              % (name, ab))
        check(same_group(Hg[3], mult), 'H^3(%s, Z) = M(G)^ = %s'
              % (name, mult))
        if name in std:
            H, _ = std[name]
            for n in range(min(len(H), ct + 1)):
                check(same_group(H[n], Hg[n]),
                      'standard and Gruenberg resolutions agree: '
                      'H^%d(%s, Z)' % (n, name))
        if r == 1:
            # cyclic: the complex is (2.21): d_(2k) = sigma, d_(2k+1) = g - 1
            g = gens[0]
            for n in range(1, 6):
                ((b),) = [gruenberg_basis(FD, n)[0]]
                img = gruenberg_d(FD, n, b)
                key = gruenberg_basis(FD, n - 1)[0]
                if n % 2 == 0:
                    expect = {(key, h): 1 for h in range(m)}
                else:
                    expect = {(key, g): 1, (key, T.e): -1}
                check(img == expect, 'p. 85: e_%d -> e_%d %s, Z_%d'
                      % (n, n - 1, 'sigma' if n % 2 == 0 else '(g - 1)', m))
            check(FD.ygens == [((0, 1),) * m],
                  'N = <x^%d> freely generated by x^%d' % (m, m))
        # exc:cohomology-generators-bound with the Gruenberg ranks
        rk = [len(gruenberg_basis(FD, n)) for n in range(ct + 1)]
        bound_check(rk, Dc, Hg, name + ' (Gruenberg)')
    for name in ('Z2', 'Z3', 'Z4', 'Z2^2', 'S3'):
        H, D = std[name]
        rk = [(groups[name].N - 1) ** n for n in range(len(D))]
        bound_check(rk, D, H, name + ' (standard)')


def relators(T, name, gens):
    """Words in the generators with trivial image, generating N normally:
    the relators of a presentation found by GAP for these generators."""
    G = T.gap
    imgs = libgap([libgap.PermList([v + 1 for v in T.perms[g]])
                   for g in gens])
    rels = libgap.RelatorsOfFpGroup(libgap.Image(
        libgap.IsomorphismFpGroupByGenerators(G, imgs)))
    out = []
    for rel in rels:
        letters = libgap.LetterRepAssocWord(rel)
        w = tuple((abs(int(a)) - 1, 1 if int(a) > 0 else -1) for a in letters)
        out.append(w)
    return out


def bound_check(rk, D, H, name):
    """exc:cohomology-generators-bound (corrections C121, C122)."""
    top = len(D) - 1
    k = [rk[n] - D[n].rank() for n in range(top + 1)]
    i = [D[n].rank() for n in range(top + 1)]
    check(k[0] == 1 and i[0] == rk[0] - 1,
          'k_0 = 1, i_0 = r_0 - 1 (corrected), %s' % name)
    refuted(k[0] == rk[0] - 1,
            'printed initial condition k_0 = r_0 - 1, %s' % name)
    for n in range(1, top + 1):
        check(k[n] == i[n - 1], 'k_n = i_(n-1) (H^n finite), %s' % name)
        formula = sum((-1) ** (n - 1 - j) * rk[j] for j in range(n)) + \
            (-1) ** n
        check(k[n] == formula, 'k_%d = r_(n-1) - ... + (-1)^n = %d, %s'
              % (n, formula, name))
        check(len(H[n]) <= k[n], 'number of generators of H^%d <= k_%d, %s'
              % (n, n, name))


# ---------------------------------------------------------------------------
# Standard presentation (pp. 87-89): identities in ZZ F, F free on x_g
# ---------------------------------------------------------------------------

def standard_presentation(groups):
    for name in ('Z2', 'Z3', 'Z2^2', 'S3'):
        T = groups[name]
        e = T.e

        def xg(g):
            return {(): 1} if g == e else {(g,): 1}

        def mulz(a, b):
            out = {}
            for u, c in a.items():
                for v, d in b.items():
                    add(out, u + v, c * d)
            return out

        def plus(*terms):
            out = {}
            for s, a in terms:
                for k, c in a.items():
                    add(out, k, s * c)
            return out

        def br(*gs):
            n = len(gs)
            if n == 1:
                return plus((1, xg(gs[0])), (-1, xg(e)))
            if n == 2:
                return plus((1, mulz(xg(gs[0]), xg(gs[1]))),
                            (-1, xg(T.mul[gs[0]][gs[1]])))
            if n % 2:
                return mulz(br(gs[0]), br(*gs[1:]))
            return mulz(br(gs[0], gs[1]), br(*gs[2:]))
        # (2.28): x_f (g, h) = (f, g) x_h - (f, gh) + (fg, h)
        check(all(mulz(xg(f), br(g, h)) ==
                  plus((1, mulz(br(f, g), xg(h))), (-1, br(f, T.mul[g][h])),
                       (1, br(T.mul[f][g], h)))
                  for f, g, h in itertools.product(range(T.N), repeat=3)),
              'eq:standard-generator-identity in ZZ F, all f, g, h, %s'
              % name)
        # (2.29) for n <= 4 (all tuples), n = 5, 6 for small groups
        maxn = 6 if T.N <= 4 else 4
        for n in range(2, maxn + 1):
            ok = True
            for gs in itertools.product(range(T.N), repeat=n):
                rhs = [(1, mulz(br(*gs[:-1]), xg(gs[-1])))]
                for i in range(n - 1, 0, -1):
                    u = gs[:i - 1] + (T.mul[gs[i - 1]][gs[i]],) + gs[i + 1:]
                    rhs.append(((-1) ** (n - i), br(*u)))
                rhs.append(((-1) ** n, br(*gs[1:])))
                ok = ok and br(*gs) == plus(*rhs)
            check(ok, 'eq:standard-differential-identity in ZZ F, %s, n = %d '
                  '(all %d tuples)' % (name, n, T.N ** n))
        # the three missing terms of the proof (C119) on S_3, n = 4 (all
        # tuples) and n = 5 (300 random tuples)
        if name == 'S3':
            good = bad = True
            rnd = random.Random(5)
            cases = [(4, gs) for gs in itertools.product(T.nonid, repeat=4)]
            cases += [(5, tuple(rnd.choice(T.nonid) for _ in range(5)))
                      for _ in range(300)]
            for n, gs in cases:
                first = mulz(mulz(br(*gs[:n - 3]), xg(gs[n - 3])),
                             br(gs[n - 2], gs[n - 1]))
                three = plus(
                    (1, mulz(br(*gs[:n - 1]), xg(gs[n - 1]))),
                    (-1, br(*(gs[:n - 2] + (T.mul[gs[n - 2]][gs[n - 1]],)))),
                    (1, br(*(gs[:n - 3] + (T.mul[gs[n - 3]][gs[n - 2]],
                                           gs[n - 1])))))
                printed = plus(
                    (1, mulz(br(*gs[:n - 1]), xg(gs[n - 1]))),
                    (-1, br(*(gs[:n - 2] + (T.mul[gs[n - 2]][gs[n - 1]],)))),
                    (1, br(*(gs[:n - 3] + (T.mul[gs[n - 2]][gs[n - 3]],
                                           gs[n - 1])))))
                good = good and first == three
                bad = bad and first == printed
            check(good, 'C119: (2.30) equals the three terms with '
                  '(g_1, .., g_(n-2) g_(n-1), g_n), S_3, n = 4, 5')
            refuted(bad, 'printed (g_1, .., g_(n-1) g_(n-2), g_n), S_3')
        # C118: (f, g, h) = (f)(g, h) lies in Delta_F Delta_N; boundary
        check(all(br(f, g, h) ==
                  plus((1, mulz(br(f, g), xg(h))), (-1, br(f, T.mul[g][h])),
                       (1, br(T.mul[f][g], h)), (-1, br(g, h)))
                  for f, g, h in itertools.product(T.nonid, repeat=3)),
              'C118: (f, g, h) = (f, g) x_h - (f, gh) + (fg, h) - (g, h), %s'
              % name)
        # x_g x_h x_(gh)^-1 generate N (index m) and are (m-1)^2 = rank N
        if T.N <= 6:
            r = T.N - 1
            F = gap('FreeGroup(%d)' % r)
            fg = list(F.GeneratorsOfGroup())
            pos = {g: i for i, g in enumerate(T.nonid)}

            def xw(g):
                return F.One() if g == e else fg[pos[g]]
            zs = [xw(g) * xw(h) * xw(T.mul[g][h]) ** -1
                  for g in T.nonid for h in T.nonid]
            H = libgap.Subgroup(F, zs)
            check(int(libgap.Index(F, H)) == T.N,
                  'p. 88: x_g x_h x_(gh)^-1 generate a subgroup of index '
                  '%d, %s' % (T.N, name))
            check(len(zs) == 1 + T.N * (r - 1) == (T.N - 1) ** 2,
                  '(m - 1)^2 = 1 + m(m - 2): a free basis of N, %s' % name)
    # p. 87: rank criterion needs N != 1: the trivial subgroup of F_2 has
    # rank 0 and infinite index; nontrivial normal subgroups of finite
    # index have rank 1 + j(r - 1) (Schreier)
    F = gap('FreeGroup(2)')
    one = libgap.TrivialSubgroup(F)
    rank_finite = len(libgap.GeneratorsOfGroup(one)) == 0
    index_finite = libgap.Index(F, one) != libgap.infinity
    check(rank_finite and not index_finite,
          'N = 1 in F_2: rank 0, infinite index')
    refuted(rank_finite == index_finite,
            'p. 87 as printed: rank of a normal subgroup of F_2 finite iff '
            'its index finite (N = 1)')


def main():
    random.seed(1)
    srcs = {
        'Z2': 'CyclicGroup(IsPermGroup, 2)',
        'Z3': 'CyclicGroup(IsPermGroup, 3)',
        'Z4': 'CyclicGroup(IsPermGroup, 4)',
        'Z5': 'CyclicGroup(IsPermGroup, 5)',
        'Z6': 'CyclicGroup(IsPermGroup, 6)',
        'Z2^2': 'Group((1,2), (3,4))',
        'S3': 'SymmetricGroup(3)',
        'Q8': 'Image(IsomorphismPermGroup(SmallGroup(8, 4)))',
        'D8': 'DihedralGroup(IsPermGroup, 8)',
        'A4': 'AlternatingGroup(4)',
    }
    groups = {k: group(v, k) for k, v in srcs.items()}
    std = section_1(groups)
    section_2(groups)
    section_3(groups, std)
    standard_presentation(groups)
    print('ok %s: %d checks' % (SCOPE, COUNT[0]))


if __name__ == '__main__':
    main()
