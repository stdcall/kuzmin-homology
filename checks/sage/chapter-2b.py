"""Exact checks of Chapter 2, §§ 4-7 "Когомологии групп" (Sage).

Run from the project root: sage -python checks/sage/chapter-2b.py (plain
asserts; do not use -O).  The last line is "ok chapter-2b: N checks".

Book: Ю. В. Кузьмин, «Гомологическая теория групп» (Факториал Пресс, 2006),
printed pp. 91-116.  Pages are the printed pages; labels are those of
content/02-04-*.typ ... 02-07-*.typ.  Modules are right modules, as in the
book; GAP multiplies left to right, as the book does.  Group rings of free
abelian groups are Laurent polynomials (dicts exponent vector -> integer),
tensor powers of ZZ G are group rings of G^n; finite groups are
multiplication tables from GAP (libgap); everything is exact over ZZ.

What is checked, by section, and where the expected values come from:

§ 4 (pp. 91-98).
  sym and alt (p. 92): T -> S composed with sym is n!, Lambda -> T -> Lambda
  is n!; sym is injective over ZZ, alt is injective over ZZ, Z_2, Z_4, Z_6
  (a unit minor: the rows with increasing indices), rank 4, n <= 4; the
  number of free generators of Lambda^n of a module of rank r is C_r^n =
  binom(r, n) (correction C124; the printed C_n^r = binom(n, r) is
  refuted); exc:sym-not-injective: over Z_p, sym(x^p) = p! x^(x)p = 0.
  The differential of T_G(Delta) (p. 93) in the universal case
  G = Z^n, t_i = x_i - 1, n <= 4, and for random t_i in Delta of Z^2:
  eq:alt-differential, eq:alt-differential-last-factor,
  eq:exterior-differential; for G = S_3 eq:alt-differential fails
  (commutativity is needed).
  th:free-abelian-resolution: the contracting homotopy of the proof
  (s_(-1)(1) = 1, s_n = 0 on Lambda^(n-1)(G_0^+) and (x - 1) (x) ZZ G,
  s_n(a (x) r) = s_n(a (x) alpha(r)) + a and (x - 1) (x) r' on the other
  summand) satisfies d s + s d = id on every a (x) g, g in the box
  [-2, 2]^r, r = 1, 2, 3 (the question of p. 95); d^2 = 0.
  cor:free-abelian-cohomology: the cochain differentials vanish for
  trivial A, so H^n(Z^r, A) = A^(C_r^n) (A = Z, Z_2, Z_6; r <= 4);
  cor:free-abelian-cd: H^r(Z^r, Z) = Z, Lambda^(r+1) = 0.  The values are
  the alternating multilinear functions: for A = Z_2, G = Z^2, n = 2 there
  are 8 forms with f(y, x) = -f(x, y) and 2 alternating ones, while
  |H^2(Z^2, Z_2)| = 2 (the reading «кососимметричные» = sign-changing is
  refuted for A with 2-torsion).
  exc:exterior-graded-commutativity (printed answer: (-1)^(km); t and t =
  0 for homogeneous t of odd degree, not in general),
  exc:differential-antiderivation and exc:exterior-universal-property
  (the two sign conventions agree), on random elements.
  exc:lambda-homomorphisms (correction C130): in the trivialized complex
  the element alt((g_1 - 1) (x) .. (x) (g_n - 1)(g_(n+1) - 1)) equals
  - sum sign(sigma) d_(n+1)(..) over the permutations with n left of
  n + 1 (universal case G = Z^(n+1), n <= 4); the printed sum without
  sign(sigma) and with the opposite sign is refuted; phi of the hint is
  multilinear and alternating for all cocycles (Z_2^2, Z_4, Z_2^3 with
  A = Z_2; n = 2, 3), and lambda_2 is onto Hom(Lambda^2 G, Z_2) for Z_2^2.
  exc:lambda-two: for G = Z_m, A = Z every 2-cocycle is symmetric, so
  lambda_2 = 0 and Ker lambda_2 = H^2(Z_m, Z) = Z_m (m <= 6).

§ 5 (pp. 98-106).
  eq:universal-coefficients-mod-m: H^n(G, Z_m) computed directly (lattice
  quotient of the cochain complex mod m) is H^n G (x) Z_m + Tor(H^(n+1) G,
  Z_m) (Z_2, Z_3, Z_4, Z_2^2, Z_6, S_3, m = 2, 3, 4); the Bockstein
  (1/m) delta(f-bar) is an integral cocycle and its image has order
  |Tor(H^(n+1) G, Z_m)|, |H^n(G, Z_m)| = |H^n G (x) Z_m| |image|;
  H^n(Z_m, Z_m) = Z_m (printed, m <= 6).
  prop:connecting-standard-cocycle (corrections C147, C148) and
  exc:augmentation-connecting-cocycle: for 0 -> Delta -> ZZ G -> Z -> 0 and
  gamma(1) = 1, delta(gamma f) equals the cochain
  phi(f(g_1..g_n), g_(n+1)) = f(g_1..g_n)(g_(n+1) - 1) for every
  integral cocycle f (S_3, Z_4, Z_2^2; n <= 2) and also for
  0 -> Z (diagonal) -> Z^2 (swap) -> sign -> 0 (Z_2, n <= 4);
  exc:augmentation-connecting-derivation: g -> g - 1 is a non-principal
  derivation (H^1(G, Delta) = Z_m), H^0(G, ZZ G) -> H^0(G, Z) has image mZ.
  exc:free-abelian-rank-two-cohomology: the printed action is a module
  (x and y commute); H^n(G, A) = Z, Z^3, Z^2 (computed; no printed answer),
  consistent with the long exact sequence (ranks).

§ 6 (pp. 106-109).
  prop:dimension-shifting for 0 -> Z -> ZZ G -> ZZ G / Z sigma -> 0 and
  0 -> Delta -> ZZ G -> Z -> 0 (ZZ G coinduced for finite G): H^n(G, A')
  = H^(n-1)(G, A'') (n = 2, 3) and H^1(G, A') = Coker(H^0(A) -> H^0(A''))
  (Z_4, Z_2^2, S_3).  Corestriction in dimension 0 (correction C156):
  with representatives of the right cosets S t, a sigma is G-invariant for
  every S-invariant a of ZZ G; with representatives of the left cosets
  t S (the printed reading) it is not, for S_3 > <(1,2)>; Cor_0 Res_0 =
  |G : S| (S_3, two subgroups).  exc:monomorphism-not-preserved: the
  hint works for n >= 1 (Z -> ZZ G, G = Z_2, n = 2, 4: Z_2 -> 0); at
  n = 0 the same map H^0(Z) -> H^0(ZZ G) is injective (left exactness; the
  exercise needs n >= 1; corrected).

§ 7 (pp. 109-116).
  Pull-back along f: G_2 -> G_1 (C158): the coamalgam of Q_8 -> Z_2^2 over
  Z_2 -> Z_2^2 is cyclic of order 4 with factor system f^* h.
  Abelian obstruction: E_1 = Z_4 (G = Z_2, A = Z_2): for B = Z with the
  sign action delta(h-bar) is a cocycle with values in C = 2B and
  nonzero class in H^3(Z_2, C) (and H^2(Z_2, B) = 0); for B = Z trivial the
  class is 0.
  Nonabelian kernel: GL(2, 3) -> PGL(2, 3) = S_4 with B = SL(2, 3),
  C = {+-1}, A = A_4, G = Z_2: eq:nonabelian-cocycle-identity for the
  factor system of 1 -> A_4 -> S_4 -> Z_2 -> 1 (all triples), delta(h-bar)
  takes values in C, is a 3-cocycle and a coboundary; after correcting
  h-bar the printed multiplication of pairs (g, b) is associative, gives an
  extension of G by B, and (g, b) -> g-bar f(b) is a homomorphism onto S_4
  with kernel C.
  p. 115 (both places corrected): G-bar = SL(2, 3) x Z_3,
  A = Q_8 x Z_3 (nonabelian), Z(A) cyclic of order 6, G = Z_3,
  phi = delta t with values of order 3 and 6 (so that delta s and
  (delta s)^-1 differ); all isomorphisms G-bar^o -> G-bar that are the
  identity on A and on G (GAP: IsomorphismGroups, AutomorphismGroup): for
  each, g^-1 alpha(g) lies in Z(A) and depends only on g A, while alpha
  itself does not (printed «α зависит лишь от класса смежности» refuted);
  alpha: G-bar^o -> G-bar, alpha(g_1 o g_2) = alpha(g_1) alpha(g_2),
  gives exactly phi = delta s (corrected reading) and not (delta s)^-1;
  its inverse G-bar -> G-bar^o gives (delta s)^-1 and not delta s; the
  printed g_1 o g_2 = alpha(g_1) alpha(g_2) has no solution (g_2 = 1
  forces alpha(g) = g alpha(1)^-1, and no such map works).

What is NOT established: statements for all groups or all ranks (only the
listed groups, ranks and degrees); the infinite-rank case of
th:free-abelian-resolution (a direct-limit argument); the
correspondence of our text to the printed page.
"""

import itertools
import random

from sage.all import ZZ, Zmod, binomial, factorial, libgap, matrix

SCOPE = 'chapter-2b'
COUNT = [0]


def check(cond, what):
    assert bool(cond), 'FAILED: ' + what
    COUNT[0] += 1


def refuted(cond, what):
    assert not bool(cond), 'printed reading unexpectedly holds: ' + what
    COUNT[0] += 1


def gap(src):
    return libgap.eval(src)


def add(d, k, c):
    if c:
        v = d.get(k, 0) + c
        if v:
            d[k] = v
        else:
            del d[k]


# ---------------------------------------------------------------------------
# Finite groups (as in chapter-2a.py)
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

    def gapelt(self, i):
        return libgap.PermList([v + 1 for v in self.perms[i]])


def group(src, name):
    return TGroup(gap(src), name)


def trivial_module(T):
    return [matrix(ZZ, [[1]]) for _ in range(T.N)]


def regular_module(T):
    rho = []
    for g in range(T.N):
        M = matrix(ZZ, T.N, T.N, sparse=True)
        for h in range(T.N):
            M[h, T.mul[h][g]] = 1
        rho.append(M)
    return rho


def augmentation_ideal_module(T):
    """Delta_G with basis g - 1 (g != 1): (h - 1) g = (hg - 1) - (g - 1)."""
    pos = {h: i for i, h in enumerate(T.nonid)}
    rho = []
    for g in range(T.N):
        M = matrix(ZZ, len(pos), len(pos), sparse=True)
        for h in T.nonid:
            hg = T.mul[h][g]
            if hg != T.e:
                M[pos[h], pos[hg]] += 1
            if g != T.e:
                M[pos[h], pos[g]] -= 1
        rho.append(M)
    return rho


def augmentation_quotient_module(T):
    """ZZ G / Z sigma with basis e_h (h != 1), e_1 = - sum of the others."""
    others = T.nonid
    pos = {h: i for i, h in enumerate(others)}
    rho = []
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


def tuples(T, n):
    return list(itertools.product(T.nonid, repeat=n))


def coboundary_matrix(T, rho, n):
    """delta_n of eq:cochain-coboundary on normalized cochains."""
    k = rho[0].nrows()
    src = {t: i for i, t in enumerate(tuples(T, n))}
    dst = tuples(T, n + 1)
    ent = {}
    for r, t in enumerate(dst):
        M = rho[t[-1]]
        c = src[t[:-1]]
        for a in range(k):
            for b in range(k):
                v = M[a, b]
                if v:
                    add(ent, (r * k + b, c * k + a), v)
        for i in range(1, n + 1):
            p = T.mul[t[i - 1]][t[i]]
            if p != T.e:
                u = t[:i - 1] + (p,) + t[i + 1:]
                for a in range(k):
                    add(ent, (r * k + a, src[u] * k + a), (-1) ** (n + 1 - i))
        for a in range(k):
            add(ent, (r * k + a, src[t[1:]] * k + a), (-1) ** (n + 1))
    return matrix(ZZ, len(dst) * k, len(src) * k, ent, sparse=True)


def invariants_list(elem_divs, free_rank):
    return sorted(int(x) for x in elem_divs if x not in (0, 1)) + \
        [0] * free_rank


def cohomology_from(Dprev, Dcur, dim):
    rp = 0 if Dprev is None else Dprev.rank()
    rc = 0 if Dcur is None else Dcur.rank()
    ed = [] if Dprev is None else Dprev.elementary_divisors()
    return invariants_list(ed, dim - rc - rp)


def standard_cohomology(T, rho, top):
    k = rho[0].nrows()
    D = [coboundary_matrix(T, rho, n) for n in range(top + 1)]
    H = [cohomology_from(D[n - 1] if n else None, D[n],
                         (T.N - 1) ** n * k) for n in range(top + 1)]
    return H, D


def cohomology_mod(Dprev, Dcur, dim, m):
    """H^n of the cochain complex (x) Z_m: {x : Dcur x = 0 mod m} modulo
    Im Dprev + m Z^dim (independent of universal coefficients)."""
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
    return sorted(int(x) for x in (K / L).invariants()), K, L


def primary(lst):
    out = []
    for x in lst:
        if x == 0:
            out.append(0)
            continue
        for p, e in ZZ(x).factor():
            out.append(p ** e)
    return sorted(out)


def order(lst):
    o = 1
    for x in lst:
        assert x != 0
        o *= x
    return o


# ---------------------------------------------------------------------------
# Laurent polynomials and tensors over Z^r
# ---------------------------------------------------------------------------

def lmul(a, b):
    out = {}
    for u, c in a.items():
        for v, d in b.items():
            add(out, tuple(x + y for x, y in zip(u, v)), c * d)
    return out


def unit(r, i=None, k=1):
    e = [0] * r
    if i is not None:
        e[i] = k
    return tuple(e)


def xm1(r, i):
    """x_i - 1 in ZZ[Z^r]."""
    return {unit(r, i): 1, unit(r): -1}


def tensor(*fs):
    out = {(): 1}
    for f in fs:
        new = {}
        for k, c in out.items():
            for u, d in f.items():
                add(new, k + (u,), c * d)
        out = new
    return out


def tplus(*terms):
    out = {}
    for s, a in terms:
        for k, c in a.items():
            add(out, k, s * c)
    return out


def sign(perm):
    s = 1
    p = list(perm)
    for i in range(len(p)):
        for j in range(i + 1, len(p)):
            if p[i] > p[j]:
                s = -s
    return s


def alt(ts):
    out = {}
    for perm in itertools.permutations(range(len(ts))):
        for k, c in tensor(*[ts[i] for i in perm]).items():
            add(out, k, sign(perm) * c)
    return out


def TG_d(x, mulfun):
    """d of T_G(Delta) on pure tensors h_1 (x) .. (x) h_n (x) h (p. 93):
    (h_1..h_(n-1)) (x) h_n h + sum_(i=n-1)^1 (-1)^(n-i) (.. h_i h_(i+1) ..)
    (x) h; mulfun multiplies group elements."""
    out = {}
    for key, c in x.items():
        hs, h = key[:-1], key[-1]
        n = len(hs)
        add(out, hs[:-1] + (mulfun(hs[-1], h),), c)
        for i in range(1, n):
            u = hs[:i - 1] + (mulfun(hs[i - 1], hs[i]),) + hs[i + 1:]
            add(out, u + (h,), (-1) ** (n - i) * c)
    return out


def vadd(u, v):
    return tuple(x + y for x, y in zip(u, v))


# ---------------------------------------------------------------------------
# Section 4
# ---------------------------------------------------------------------------

def section_4():
    # sym and alt, p. 92
    r = 4
    for n in range(1, 5):
        tt = list(itertools.product(range(r), repeat=n))
        tpos = {t: i for i, t in enumerate(tt)}
        mons = list(itertools.combinations_with_replacement(range(r), n))
        incs = list(itertools.combinations(range(r), n))
        Sym = matrix(ZZ, len(tt), len(mons), sparse=True)
        for j, mo in enumerate(mons):
            for perm in itertools.permutations(mo):
                Sym[tpos[perm], j] += 1
        TS = matrix(ZZ, len(mons), len(tt), sparse=True)
        mpos = {mo: j for j, mo in enumerate(mons)}
        for t in tt:
            TS[mpos[tuple(sorted(t))], tpos[t]] = 1
        check(TS * Sym == factorial(n) * matrix.identity(ZZ, len(mons)),
              'S -> T -> S is n!, n = %d (p. 92)' % n)
        check(Sym.rank() == len(mons), 'sym injective over ZZ, n = %d' % n)
        Alt = matrix(ZZ, len(tt), max(1, len(incs)), sparse=True)
        for j, inc in enumerate(incs):
            for perm in itertools.permutations(range(n)):
                Alt[tpos[tuple(inc[i] for i in perm)], j] += sign(perm)
        TL = matrix(ZZ, max(1, len(incs)), len(tt), sparse=True)
        ipos = {inc: j for j, inc in enumerate(incs)}
        for t in tt:
            if len(set(t)) == n:
                srt = tuple(sorted(t))
                p = [srt.index(v) for v in t]
                TL[ipos[srt], tpos[t]] = sign(p)
        if incs:
            check(TL * Alt == factorial(n) * matrix.identity(ZZ, len(incs)),
                  'Lambda -> T -> Lambda is n!, n = %d (p. 92)' % n)
            sub = Alt.matrix_from_rows([tpos[inc] for inc in incs])
            check(sub == matrix.identity(ZZ, len(incs)),
                  'alt: one term with increasing indices, so alt is '
                  'injective over every ring (Z, Z_2, Z_4, Z_6), n = %d' % n)
            for q in (2, 4, 6):
                check(Alt.change_ring(Zmod(q)).matrix_from_rows(
                    [tpos[inc] for inc in incs]).is_one(),
                    'alt injective over Z_%d, n = %d' % (q, n))
        check(len(incs) == binomial(r, n),
              'C124: rank Lambda^n = C_r^n = binom(r, n), r = %d, n = %d'
              % (r, n))
        if n < r:
            refuted(len(incs) == binomial(n, r),
                    'printed C_n^r = binom(n, r), r = %d, n = %d' % (r, n))
    for p in (2, 3, 5):
        check(factorial(p) % p == 0,
              'exc:sym-not-injective: sym(x^%d) = %d! x^(x)%d = 0 over Z_%d '
              '(x^%d != 0 in S^%d)' % (p, p, p, p, p, p))
    # (2.31)-(2.33): universal case G = Z^n, t_i = x_i - 1
    for n in range(1, 5):
        ts = [xm1(n, i) for i in range(n)]
        A = alt(ts)
        lhs = TG_d({k + (unit(n),): c for k, c in A.items()}, vadd)
        check(lhs == A, 'eq:alt-differential, universal case n = %d' % n)
        rhs = {}
        for i in range(n):
            part = alt(ts[:i] + ts[i + 1:])
            for k, c in part.items():
                for u, d in ts[i].items():
                    add(rhs, k + (u,), (-1) ** (n - 1 - i) * c * d)
        check(lhs == rhs, 'eq:alt-differential-last-factor = '
              'eq:exterior-differential, n = %d' % n)
    rnd = random.Random(7)
    for trial in range(20):
        n = rnd.randint(2, 4)
        ts = []
        for i in range(n):
            f = {}
            for _ in range(3):
                add(f, (rnd.randint(-2, 2), rnd.randint(-2, 2)),
                    rnd.randint(-3, 3))
            add(f, (0, 0), -sum(f.values()))  # epsilon = 0
            ts.append(f)
        A = alt(ts)
        check(TG_d({k + ((0, 0),): c for k, c in A.items()}, vadd) == A,
              'eq:alt-differential for random t_i in Delta(Z^2)')
    # nonabelian G = S_3: the alternating elements are not a subcomplex
    S3 = group('SymmetricGroup(3)', 'S3')
    a, b = S3.gens()

    def gm1(g):
        return {g: 1, S3.e: -1}
    A = alt([gm1(a), gm1(b)])
    refuted(TG_d({k + (S3.e,): c for k, c in A.items()},
                 lambda u, v: S3.mul[u][v]) == A,
            'eq:alt-differential for the nonabelian S_3')
    # th:free-abelian-resolution: the homotopy of the proof, r = 1, 2, 3
    for r in (1, 2, 3):
        koszul_homotopy(r)
    # cor:free-abelian-cohomology, cor:free-abelian-cd
    for r in range(1, 5):
        for n in range(0, r + 1):
            Dn = koszul_cochain(r, n, None)
            check(Dn.is_zero(), 'trivial A: the cochain differential '
                  'Hom(Lambda^%d, A) -> Hom(Lambda^%d, A) vanishes, r = %d'
                  % (n, n + 1, r))
        check(len(list(itertools.combinations(range(r), r + 1))) == 0,
              'Lambda^(r+1) = 0: resolution of length r')
        for A_ in (0, 2, 6):
            for n in range(0, r + 1):
                dim = binomial(r, n)
                if A_ == 0:
                    H = cohomology_from(koszul_cochain(r, n - 1, None)
                                        if n else None,
                                        koszul_cochain(r, n, None), dim)
                    check(H == [0] * dim, 'H^%d(Z^%d, Z) = Lambda^%d = Z^%d'
                          % (n, r, n, dim))
                else:
                    H, _, _ = cohomology_mod(
                        koszul_cochain(r, n - 1, None) if n else None,
                        koszul_cochain(r, n, None), dim, A_)
                    check(H == [A_] * dim, 'H^%d(Z^%d, Z_%d) = Z_%d^%d'
                          % (n, r, A_, A_, dim))
        check(binomial(r, r) == 1, 'cor:free-abelian-cd: H^%d(Z^%d) = Z'
              % (r, r))
    # alternating vs sign-changing forms: A = Z_2, G = Z^2, n = 2
    forms = list(itertools.product(range(2), repeat=4))  # f(e_i, e_j)
    skew = [f for f in forms if all((f[2 * i + j] + f[2 * j + i]) % 2 == 0
                                    for i in range(2) for j in range(2))]
    altf = [f for f in skew if f[0] == 0 and f[3] == 0]
    H2, _, _ = cohomology_mod(koszul_cochain(2, 1, None),
                              koszul_cochain(2, 2, None), 1, 2)
    check(order(H2) == len(altf) == 2,
          'H^2(Z^2, Z_2) = Z_2 = alternating bilinear forms')
    refuted(order(H2) == len(skew),
            'H^2(Z^2, Z_2) = forms with f(y, x) = -f(x, y) (8 of them)')
    exterior_algebra_checks()
    lambda_checks()


def koszul_d(r, x):
    """d of Lambda_G(G^+) (eq:exterior-differential); x = {(I, e): c} with
    I an increasing tuple of generator indices, e in Z^r."""
    out = {}
    for (I, e), c in x.items():
        n = len(I)
        for k in range(n):
            J = I[:k] + I[k + 1:]
            s = (-1) ** (n - 1 - k) * c
            add(out, (J, vadd(e, unit(r, I[k]))), s)
            add(out, (J, e), -s)
    return out


def koszul_s(r, x):
    """The contracting homotopy of the proof of th:free-abelian-resolution,
    by induction on the number of generators; s_(-1) is separate."""
    if r == 0:
        return {}
    out = {}
    last = r - 1
    for (I, e), c in x.items():
        if last in I:
            continue  # s_n = 0 on Lambda^(n-1)(G_0^+) and (x - 1) (x) ZZ G
        k = e[last]
        e0 = e[:last] + (0,)
        # s_n(a (x) alpha(r)) by the induction hypothesis (G_0 = Z^(r-1))
        sub = koszul_s(r - 1, {(I, e0[:last]): c})
        for (J, f), v in sub.items():
            add(out, (J, f + (0,)), v)
        # a and (x - 1) (x) r', r - alpha(r) = (x - 1) r'
        if k > 0:
            for j in range(k):
                add(out, (I + (last,), e0[:last] + (j,)), c)
        elif k < 0:
            for j in range(k, 0):
                add(out, (I + (last,), e0[:last] + (j,)), -c)
    return out


def koszul_homotopy(r):
    box = list(itertools.product(range(-2, 3), repeat=r))
    ok = True
    ok_d2 = True
    for n in range(0, r + 1):
        for I in itertools.combinations(range(r), n):
            for e in box:
                x = {(I, e): 1}
                ds = koszul_d(r, koszul_s(r, x))
                if n == 0:
                    sd = {((), unit(r)): 1}  # s_(-1) epsilon
                else:
                    sd = koszul_s(r, koszul_d(r, x))
                tot = tplus((1, ds), (1, sd))
                ok = ok and tot == x
                ok_d2 = ok_d2 and koszul_d(r, koszul_d(r, x)) == {}
    check(ok, 'th:free-abelian-resolution: d s + s d = id for the homotopy '
          'of the proof, r = %d, all a (x) g, g in [-2, 2]^%d' % (r, r))
    check(ok_d2, 'd^2 = 0 on Lambda_G(G^+), r = %d' % r)


def koszul_cochain(r, n, act):
    """delta_n: Hom(Lambda^n, A) -> Hom(Lambda^(n+1), A), A = Z with
    x_i acting by act[i] (trivial if act is None): f(d t_J)."""
    src = list(itertools.combinations(range(r), n))
    dst = list(itertools.combinations(range(r), n + 1))
    spos = {I: i for i, I in enumerate(src)}
    M = matrix(ZZ, max(len(dst), 0), max(len(src), 0), sparse=True)
    for row, J in enumerate(dst):
        img = koszul_d(r, {(J, unit(r)): 1})
        for (I, e), c in img.items():
            a = 1
            for i in range(r):
                if e[i]:
                    a *= (1 if act is None else act[i]) ** e[i]
            M[row, spos[I]] += c * a
    return M


def wedge(a, b):
    out = {}
    for u, c in a.items():
        for v, d in b.items():
            if set(u) & set(v):
                continue
            w = u + v
            add(out, tuple(sorted(w)), sign([sorted(w).index(z) for z in w])
                * c * d)
    return out


def exterior_algebra_checks():
    rnd = random.Random(11)
    r = 6

    def rand_hom(k):
        out = {}
        for _ in range(3):
            add(out, tuple(sorted(rnd.sample(range(r), k))),
                rnd.randint(-3, 3))
        return out
    ok_comm = ok_odd = True
    for _ in range(60):
        k, m = rnd.randint(0, 3), rnd.randint(0, 3)
        t, s = rand_hom(k), rand_hom(m)
        ok_comm = ok_comm and wedge(t, s) == {
            key: (-1) ** (k * m) * c for key, c in wedge(s, t).items()}
        if k % 2:
            ok_odd = ok_odd and wedge(t, t) == {}
    check(ok_comm, 'exc:exterior-graded-commutativity: t and s = '
          '(-1)^(km) s and t')
    check(ok_odd, 'exc:exterior-graded-commutativity: t and t = 0 for '
          'homogeneous t of odd degree')
    t = {(0, 1): 1, (2, 3): 1}
    refuted(wedge(t, t) == {}, 't and t = 0 for t = x1 x2 + x3 x4 '
            '(degree 2): it is 2 x1 x2 x3 x4')
    t = {(0,): 1, (1, 2): 1}
    refuted(wedge(t, t) == {}, 't and t = 0 for t = x1 + x2 x3')
    # exc:differential-antiderivation and exc:exterior-universal-property
    R = 3

    def rand_el(k):
        out = {}
        for _ in range(3):
            I = tuple(sorted(rnd.sample(range(R), k)))
            add(out, (I, tuple(rnd.randint(-1, 1) for _ in range(R))),
                rnd.randint(-2, 2))
        return out

    def lmult(x, y):  # (a (x) r)(b (x) r') = (a and b) (x) r r'
        out = {}
        for (I, e), c in x.items():
            for (J, f), d in y.items():
                for K, s in wedge({I: 1}, {J: 1}).items():
                    add(out, (K, vadd(e, f)), s * c * d)
        return out
    ok3 = ok4 = True
    for _ in range(40):
        k, m = rnd.randint(0, 3), rnd.randint(0, 3)
        if k + m > R:
            continue
        t, s = rand_el(k), rand_el(m)
        lhs = koszul_d(R, lmult(t, s))
        rhs3 = tplus((1, lmult(t, koszul_d(R, s))),
                     ((-1) ** m, lmult(koszul_d(R, t), s)))
        rhs4 = tplus((1, lmult(t, koszul_d(R, s))),
                     ((-1) ** (k * m), lmult(s, koszul_d(R, t))))
        ok3 = ok3 and lhs == rhs3
        ok4 = ok4 and lhs == rhs4
    check(ok3, 'exc:differential-antiderivation: d(t and s) = t and d(s) '
          '+ (-1)^m d(t) and s')
    check(ok4, 'exc:exterior-universal-property: d(t and s) = t d(s) + '
          '(-1)^(km) s d(t)')


def lambda_checks():
    # C130: universal case G = Z^(n+1), u_i = g_i - 1, trivialized complex
    for n in range(1, 5):
        R = n + 1
        u = [xm1(R, i) for i in range(R)]
        E = alt(u[:n - 1] + [lmul(u[n - 1], u[n])])

        def dbar(x):  # trivialized d_(n+1) on (n+1)-fold tensors of Delta
            out = {}
            for key, c in x.items():
                m = len(key)
                for i in range(1, m):
                    w = key[:i - 1] + (vadd(key[i - 1], key[i]),) + key[i + 1:]
                    add(out, w, (-1) ** (m - i) * c)
                # first term (t_1 .. t_n) epsilon(t_(n+1)) handled by
                # multilinearity: epsilon of a group element is 1
                add(out, key[:-1], c)
            return out
        corr, printed = {}, {}
        for perm in itertools.permutations(range(R)):
            if perm.index(n - 1) > perm.index(n):
                continue
            img = dbar(tensor(*[u[i] for i in perm]))
            for k, c in img.items():
                add(corr, k, -sign(perm) * c)
                add(printed, k, c)
        check(corr == E, 'C130: (2.34) = - sum sign(sigma) d_(n+1)(..), '
              'n = %d' % n)
        refuted(printed == E, 'printed sum d_(n+1)(..) without sign(sigma), '
                'n = %d' % n)
        # the hint's identity (g g' - 1) - (g - 1) - (g' - 1) = (g-1)(g'-1)
        gg = {vadd(unit(R, n - 1), unit(R, n)): 1, unit(R): -1}
        check(tplus((1, gg), (-1, u[n - 1]), (-1, u[n])) ==
              lmul(u[n - 1], u[n]), 'p. 97: (g_n g_(n+1) - 1) - (g_n - 1) '
              '- (g_(n+1) - 1) = (g_n - 1)(g_(n+1) - 1)')
    # phi of exc:lambda-homomorphisms is multilinear and alternating
    specs = [('Group((1,2),(3,4))', 'Z2^2', (2, 3)),
             ('CyclicGroup(IsPermGroup, 4)', 'Z4', (2, 3)),
             ('Group((1,2),(3,4),(5,6))', 'Z2^3', (2,))]
    for src, name, ns in specs:
        T = group(src, name)
        for n in ns:
            D = [coboundary_matrix(T, trivial_module(T), k)
                 for k in range(n + 1)]
            H, K, L = cohomology_mod(D[n - 1], D[n], (T.N - 1) ** n, 2)
            tt = tuples(T, n)
            pos = {t: i for i, t in enumerate(tt)}

            def val(f, gs):
                if T.e in gs:
                    return 0
                return f[pos[gs]]

            def phi(f, gs):
                return sum(sign(p) * val(f, tuple(gs[i] for i in p))
                           for p in itertools.permutations(range(n))) % 2
            ok = True
            surj = False
            for f in K.basis():
                for gs in itertools.product(range(T.N), repeat=n + 1):
                    a = gs[:n - 1]
                    lhs = phi(f, a + (T.mul[gs[n - 1]][gs[n]],))
                    rhs = (phi(f, a + (gs[n - 1],)) +
                           phi(f, a + (gs[n],))) % 2
                    ok = ok and lhs == rhs
                for gs in itertools.product(range(T.N), repeat=n):
                    if len(set(gs)) < n:
                        ok = ok and phi(f, gs) == 0
                    surj = surj or phi(f, gs) != 0
            check(ok, 'exc:lambda-homomorphisms: phi multilinear and '
                  'alternating for all mod 2 cocycles, %s, n = %d'
                  % (name, n))
            if name == 'Z2^2' and n == 2:
                check(surj, 'lambda_2 onto Hom(Lambda^2(Z_2^2), Z_2) = Z_2')
    # exc:lambda-two: G = Z_m, A = Z
    for m in range(2, 7):
        T = group('CyclicGroup(IsPermGroup, %d)' % m, 'Z%d' % m)
        D2 = coboundary_matrix(T, trivial_module(T), 2)
        tt = tuples(T, 2)
        pos = {t: i for i, t in enumerate(tt)}
        sym = all(f[pos[(g, h)]] == f[pos[(h, g)]]
                  for f in D2.right_kernel_matrix().rows() for (g, h) in tt)
        H, _ = standard_cohomology(T, trivial_module(T), 2)
        check(sym and H[2] == [m], 'exc:lambda-two: lambda_2 = 0 on '
              'H^2(Z_%d, Z) = Z_%d, so Ker lambda_2 = Z_%d' % (m, m, m))


# ---------------------------------------------------------------------------
# Section 5
# ---------------------------------------------------------------------------

def section_5():
    specs = [('CyclicGroup(IsPermGroup, 2)', 'Z2', 5),
             ('CyclicGroup(IsPermGroup, 3)', 'Z3', 5),
             ('CyclicGroup(IsPermGroup, 4)', 'Z4', 4),
             ('Group((1,2),(3,4))', 'Z2^2', 4),
             ('CyclicGroup(IsPermGroup, 6)', 'Z6', 3),
             ('SymmetricGroup(3)', 'S3', 3)]
    for src, name, top in specs:
        T = group(src, name)
        H, D = standard_cohomology(T, trivial_module(T), top)
        for m in (2, 3, 4):
            for n in range(0, top):
                dim = (T.N - 1) ** n
                Hm, K, L = cohomology_mod(D[n - 1] if n else None, D[n],
                                          dim, m)
                tensor_part = [ZZ(x).gcd(m) if x else m for x in H[n]]
                tor_part = [ZZ(x).gcd(m) for x in H[n + 1] if x]
                expect = [x for x in tensor_part + tor_part if x != 1]
                check(primary(Hm) == primary(expect),
                      'eq:universal-coefficients-mod-m: H^%d(%s, Z_%d)'
                      % (n, name, m))
                # Bockstein: (1/m) delta(f-bar) for the generators of K
                V = ZZ ** ((T.N - 1) ** (n + 1))
                ws = []
                ok = True
                for f in K.basis():
                    w = D[n] * f
                    ok = ok and all(c % m == 0 for c in w)
                    w = V([c // m for c in w])
                    ok = ok and (D[n + 1] * w).is_zero()
                    ws.append(w)
                B1 = V.submodule(D[n].columns())
                B2 = V.submodule(list(D[n].columns()) + ws)
                img = B1.index_in(B2)
                check(ok, 'Bockstein: (1/m) delta(f-bar) is an integral '
                      'cocycle, %s, m = %d, n = %d' % (name, m, n))
                check(img == order(tor_part),
                      'Bockstein image has order |Tor(H^%d G, Z_%d)|, %s'
                      % (n + 1, m, name))
                check(order(Hm) == order(tensor_part) * img,
                      '|H^n(G, Z_m)| = |H^n G (x) Z_m| |Im partial|, %s, '
                      'm = %d, n = %d' % (name, m, n))
        if name.startswith('Z') and '^' not in name:
            mm = T.N
            for n in range(0, top + 1):
                Hm, _, _ = cohomology_mod(D[n - 1] if n else None, D[n],
                                          (mm - 1) ** n, mm)
                check(Hm == [mm], 'p. 104: H^%d(Z_%d, Z_%d) = Z_%d'
                      % (n, mm, mm, mm))
    # prop:connecting-standard-cocycle for 0 -> Delta -> ZZ G -> Z -> 0
    for src, name, top in (('SymmetricGroup(3)', 'S3', 2),
                           ('CyclicGroup(IsPermGroup, 4)', 'Z4', 2),
                           ('Group((1,2),(3,4))', 'Z2^2', 2)):
        T = group(src, name)
        rho = regular_module(T)
        for n in range(0, top + 1):
            Dz = coboundary_matrix(T, trivial_module(T), n)
            Dg = coboundary_matrix(T, rho, n)
            src_t = tuples(T, n)
            dst_t = tuples(T, n + 1)
            spos = {t: i for i, t in enumerate(src_t)}
            ok = True
            for f in Dz.right_kernel_matrix().rows():
                fbar = [0] * (len(src_t) * T.N)
                for i in range(len(src_t)):
                    fbar[i * T.N + T.e] = f[i]  # gamma(c) = c * 1
                dfb = Dg * matrix(ZZ, len(fbar), 1, fbar)
                expect = [0] * (len(dst_t) * T.N)
                for j, t in enumerate(dst_t):
                    c = f[spos[t[:-1]]]
                    expect[j * T.N + t[-1]] += c   # f(..)(g_(n+1) - 1)
                    expect[j * T.N + T.e] -= c
                ok = ok and list(dfb.column(0)) == expect
            check(ok, 'prop:connecting-standard-cocycle (C147, C148) and '
                  'exc:augmentation-connecting-cocycle: delta(gamma f) = '
                  'f(g_1..g_n)(g_(n+1) - 1), %s, n = %d' % (name, n))
    # the same for 0 -> Z(1,1) -> Z^2 (swap) -> sign -> 0, G = Z_2,
    # gamma(1) = (1, 0); phi(a, x) = gamma(a) x - gamma(a x)
    T = group('CyclicGroup(IsPermGroup, 2)', 'Z2')
    swap = [matrix.identity(ZZ, 2), matrix(ZZ, [[0, 1], [1, 0]])]
    rhoA = [swap[0] if g == T.e else swap[1] for g in range(2)]
    rhoS = [matrix(ZZ, [[1 if g == T.e else -1]]) for g in range(2)]
    for n in range(0, 5):
        Ds = coboundary_matrix(T, rhoS, n)
        DA = coboundary_matrix(T, rhoA, n)
        ok = True
        for f in Ds.right_kernel_matrix().rows():
            c = f[0]
            fbar = matrix(ZZ, 2, 1, [c, 0])
            dfb = (DA * fbar).column(0)
            # phi(c, x) = (c, 0) x - gamma(-c) = (0, c) - (-c, 0) = c(1, 1)
            ok = ok and list(dfb) == [c, c]
        check(ok, 'prop:connecting-standard-cocycle for Z(1,1) -> Z^2 -> '
              'sign, Z_2, n = %d' % n)
    # exc:augmentation-connecting-derivation
    for src, name in (('CyclicGroup(IsPermGroup, 4)', 'Z4'),
                      ('Group((1,2),(3,4))', 'Z2^2'),
                      ('SymmetricGroup(3)', 'S3')):
        T = group(src, name)
        rho = augmentation_ideal_module(T)
        k = T.N - 1
        D0 = coboundary_matrix(T, rho, 0)
        D1 = coboundary_matrix(T, rho, 1)
        der = [0] * ((T.N - 1) * k)
        for i, g in enumerate(T.nonid):
            der[i * k + i] = 1  # value g - 1, the basis vector of g
        der = matrix(ZZ, len(der), 1, der)
        V = ZZ ** len(der.column(0))
        check((D1 * der).is_zero() and
              der.column(0) not in V.submodule(D0.columns()),
              'exc:augmentation-connecting-derivation: g -> g - 1 is a '
              'non-principal derivation, %s' % name)
        H1 = cohomology_from(D0, D1, (T.N - 1) * k)
        check(H1 == [T.N], 'H^1(%s, Delta_G) = Z_%d = Coker(H^0(ZZ G) -> '
              'H^0(Z))' % (name, T.N))
    # exc:free-abelian-rank-two-cohomology
    X = matrix(ZZ, [[1, 0, 0], [1, 1, 0], [0, 0, 1]])  # rows: a, b, c
    Y = matrix(ZZ, [[1, 0, 0], [0, 1, 0], [1, 0, 1]])
    check(X * Y == Y * X, 'exc:free-abelian-rank-two-cohomology: the '
          'printed action is a Z^2-module')
    H = koszul_module_cohomology([X, Y])
    check(H == [[0], [0, 0, 0], [0, 0]],
          'H^n(Z^2, A) = Z, Z^3, Z^2 (computed)')
    Hp = koszul_module_cohomology([matrix(ZZ, [[1]])] * 2)
    Hpp = koszul_module_cohomology([matrix.identity(ZZ, 2)] * 2)
    check(Hp == [[0], [0, 0], [0]] and Hpp == [[0] * 2, [0] * 4, [0] * 2],
          "A' = Z and A'' = A / A' = Z^2 are trivial modules: H^n(Z^2, A') "
          "= Z, Z^2, Z; H^n(Z^2, A'') = Z^2, Z^4, Z^2")
    alt_sum = sum((-1) ** n * (len(Hp[n]) - len(H[n]) + len(Hpp[n]))
                  for n in range(3))
    check(alt_sum == 0, 'the long exact sequence of free groups: '
          'alternating sum of ranks 0')


def koszul_module_cohomology(acts):
    """H^n(Z^r, A) via Lambda_G(G^+), A = Z^k, x_i acting by acts[i] on
    row vectors: (delta f)(t_J) = f(d t_J)."""
    r = len(acts)
    k = acts[0].nrows()
    I_ = matrix.identity(ZZ, k)
    Ds = []
    for n in range(0, r + 1):
        src = list(itertools.combinations(range(r), n))
        dst = list(itertools.combinations(range(r), n + 1))
        spos = {I: i for i, I in enumerate(src)}
        M = matrix(ZZ, len(dst) * k, len(src) * k, sparse=True)
        for row, J in enumerate(dst):
            for kk in range(len(J)):
                I = J[:kk] + J[kk + 1:]
                s = (-1) ** (len(J) - 1 - kk)
                blk = (acts[J[kk]] - I_).transpose() * s
                c = spos[I]
                for a in range(k):
                    for b in range(k):
                        if blk[a, b]:
                            M[row * k + a, c * k + b] += blk[a, b]
        Ds.append(M)
    out = []
    for n in range(0, r + 1):
        out.append(cohomology_from(Ds[n - 1] if n else None, Ds[n],
                                   binomial(r, n) * k))
    return out


# ---------------------------------------------------------------------------
# Section 6
# ---------------------------------------------------------------------------

def section_6():
    for src, name, top in (('CyclicGroup(IsPermGroup, 4)', 'Z4', 3),
                           ('Group((1,2),(3,4))', 'Z2^2', 3),
                           ('SymmetricGroup(3)', 'S3', 3)):
        T = group(src, name)
        Hz, _ = standard_cohomology(T, trivial_module(T), top)
        Hq, _ = standard_cohomology(T, augmentation_quotient_module(T),
                                    top - 1)
        Hd, _ = standard_cohomology(T, augmentation_ideal_module(T),
                                    top if T.N <= 4 else 2)
        Hg, _ = standard_cohomology(T, regular_module(T), 1)
        check(Hg[1] == [], 'H^1(G, ZZ G) = 0, %s' % name)
        # 0 -> Z -> ZZ G -> ZZ G / Z sigma -> 0
        for n in range(2, top + 1):
            check(primary(Hz[n]) == primary(Hq[n - 1]),
                  'prop:dimension-shifting: H^%d(%s, Z) = H^%d(G, ZZ G / '
                  'Z sigma)' % (n, name, n - 1))
        check(Hz[1] == [] and Hq[0] == [],
              'H^1(G, Z) = Coker(H^0(ZZ G) -> H^0(ZZ G / Z sigma)) = 0, %s'
              % name)
        # 0 -> Delta -> ZZ G -> Z -> 0
        for n in range(2, len(Hd)):
            check(primary(Hd[n]) == primary(Hz[n - 1]),
                  'prop:dimension-shifting: H^%d(%s, Delta) = H^%d(G, Z)'
                  % (n, name, n - 1))
        check(Hd[1] == [T.N], 'H^1(G, Delta) = Coker(Z sigma -> Z) = Z_%d'
              % T.N)
    # Cor_0 (C156): right cosets S t versus left cosets t S
    T = group('SymmetricGroup(3)', 'S3')
    for gens_s in (['(1,2)'], ['(1,2,3)']):
        Sg = gap('Group(%s)' % ', '.join(gens_s))
        S = sorted(T.elt(x) for x in Sg.AsList())
        right = {}
        left = {}
        for g in range(T.N):
            right.setdefault(frozenset(T.mul[s][g] for s in S), []).append(g)
            left.setdefault(frozenset(T.mul[g][s] for s in S), []).append(g)
        rho = regular_module(T)
        # S-invariants of ZZ G (right action): kernel of a -> a(s - 1)
        stack = matrix(ZZ, T.N, 0)
        for s in S:
            stack = stack.augment(rho[s] - matrix.identity(ZZ, T.N))
        inv_basis = stack.left_kernel_matrix().rows()

        def invariant_under_G(v):
            return all(v * rho[g] == v for g in range(T.N))

        def reps_choices(cosets):
            return itertools.product(*cosets.values())
        ok_right = all(invariant_under_G(sum(a * rho[t] for t in reps))
                       for reps in reps_choices(right) for a in inv_basis)
        ok_left = all(invariant_under_G(sum(a * rho[t] for t in reps))
                      for reps in reps_choices(left) for a in inv_basis)
        check(ok_right, 'C156: a sigma is G-invariant for representatives '
              'of S t, |S| = %d' % len(S))
        if len(S) == 2:
            refuted(ok_left, 'representatives of t S (printed), S = <(1,2)>')
        # Cor_0 Res_0 = |G : S| on H^0(G, ZZ G) = Z sigma
        Ng = matrix(ZZ, 1, T.N, [1] * T.N).row(0)
        for reps in reps_choices(right):
            cr = sum(Ng * rho[t] for t in reps)
            check(cr == (T.N // len(S)) * Ng, 'Cor_0 Res_0 = |G : S| = %d'
                  % (T.N // len(S)))
            break
    # exc:monomorphism-not-preserved: Z -> ZZ G (1 -> sigma), G = Z_2
    T = group('CyclicGroup(IsPermGroup, 2)', 'Z2')
    Hz, _ = standard_cohomology(T, trivial_module(T), 4)
    Hg, _ = standard_cohomology(T, regular_module(T), 4)
    for n in (2, 4):
        check(Hz[n] == [2] and Hg[n] == [],
              'hint: H^%d(Z_2, Z) = Z_2 -> H^%d(Z_2, ZZ G) = 0 is not '
              'injective' % (n, n))
    sigma = [1] * T.N
    check(Hz[0] == [0] and Hg[0] == [0] and any(sigma),
          'n = 0: H^0(Z) = Z -> H^0(ZZ G) = Z sigma, 1 -> sigma, injective '
          '(left exactness; the exercise needs n >= 1)')


# ---------------------------------------------------------------------------
# Section 7
# ---------------------------------------------------------------------------

def section_7():
    # pull-back (coamalgam): Q_8 -> Z_2^2 along Z_2 -> Z_2^2
    Q = group('Image(IsomorphismPermGroup(SmallGroup(8, 4)))', 'Q8')
    Z = [g for g in range(Q.N) if all(Q.mul[g][h] == Q.mul[h][g]
                                      for h in range(Q.N))]
    coset = {g: frozenset(Q.mul[g][z] for z in Z) for g in range(Q.N)}
    G1 = sorted(set(coset.values()), key=min)
    sec = {c: min(c) for c in G1}  # representatives g -> g-bar
    one = coset[Q.e]
    mulG1 = {(c, d): coset[Q.mul[min(c)][min(d)]] for c in G1 for d in G1}

    def h(c, d):  # c-bar d-bar = (cd)-bar h(c, d)
        return Q.mul[Q.inv[sec[mulG1[(c, d)]]]][Q.mul[sec[c]][sec[d]]]
    c0 = next(c for c in G1 if c != one)
    G2 = [0, 1]
    f = {0: one, 1: c0}
    pairs = [(g, q) for q in G2 for g in range(Q.N) if coset[g] == f[q]]
    check(len(pairs) == 4, 'coamalgam: |G_2-bar| = |A| |G_2| = 4')

    def pm(p1, p2):
        return (Q.mul[p1[0]][p2[0]], (p1[1] + p2[1]) % 2)
    orders = []
    for p in pairs:
        k, q = 1, p
        while q != (Q.e, 0):
            q, k = pm(q, p), k + 1
        orders.append(k)
    check(max(orders) == 4, 'the pull-back of Q_8 along Z_2 -> Z_2^2 is '
          'cyclic of order 4')
    ok = True
    for q1 in G2:
        for q2 in G2:
            r1, r2 = (sec[f[q1]], q1), (sec[f[q2]], q2)
            r12 = (sec[f[(q1 + q2) % 2]], (q1 + q2) % 2)
            prod = pm(r1, r2)
            h2 = Q.mul[Q.inv[r12[0]]][prod[0]]
            ok = ok and prod[1] == r12[1] and h2 == h(f[q1], f[q2])
    check(ok, 'factor system of the pull-back = f^* h (p. 110)')
    # (C158) the pair (phi(g), sigma(g)) lies in the coamalgam
    check(all(coset[g] == f[q] for g, q in pairs),
          'C158: sigma_1(phi(g)) = f(sigma(g))')

    abelian_obstruction()
    nonabelian_pullback()
    twisted_multiplication()


def abelian_obstruction():
    T = group('CyclicGroup(IsPermGroup, 2)', 'Z2')
    # E_1 = Z_4: x-bar = 1, h(x, x) = 1 + 1 - 0 = 2 = generator of A = 2Z_4
    # h-bar(x, x) = 1 in B; delta h-bar(x, x, x) per p. 111
    for bname, act in (('sign', -1), ('trivial', 1)):
        hb = 1
        dh = hb * act - 0 + 0 - hb  # h-bar(x,x) x - h-bar(x,1) + .. - ..
        check(dh % 2 == 0, 'delta h-bar takes values in C = 2B, B %s'
              % bname)
        c = dh // 2  # coordinate in C = 2B (C = B as a module)
        rho = [matrix(ZZ, [[1 if g == T.e else act]]) for g in range(2)]
        D2 = coboundary_matrix(T, rho, 2)
        D3 = coboundary_matrix(T, rho, 3)
        V = ZZ ** 1
        cocycle = (D3 * matrix(ZZ, 1, 1, [c])).is_zero()
        trivial = V([c]) in V.submodule(D2.columns())
        H, _ = standard_cohomology(T, rho, 3)
        if act == -1:
            check(cocycle and not trivial and H[3] == [2] and H[2] == [],
                  'E_1 = Z_4, B = Z^-: obstruction != 0 in H^3(Z_2, C) = '
                  'Z_2, and H^2(Z_2, B) = 0')
        else:
            check(cocycle and trivial, 'E_1 = Z_4, B = Z: obstruction 0 '
                  '(E_2 = Z exists)')


def nonabelian_pullback():
    """GL(2,3) -> S_4 = PGL(2,3), B = SL(2,3), C = {+-1}, A = A_4, G = Z_2."""
    W = group('Image(IsomorphismPermGroup(GL(2, 3)))', 'GL23')
    Bg = W.gap.DerivedSubgroup()
    B = sorted(W.elt(y) for y in Bg.AsList())
    Bset = set(B)
    C = [g for g in range(W.N)
         if all(W.mul[g][h] == W.mul[h][g] for h in range(W.N))]
    check(len(B) == 24 and len(C) == 2, '|SL(2,3)| = 24, centre of order 2')
    cls = {g: frozenset(W.mul[g][c] for c in C) for g in range(W.N)}
    G1 = sorted(set(cls.values()), key=min)         # S_4
    A = [c for c in G1 if min(c) in Bset]           # A_4
    check(len(G1) == 24 and len(A) == 12, 'S_4 = GL/C, A_4 = SL/C')

    def m1(c, d):
        return cls[W.mul[min(c)][min(d)]]

    def inv1(c):
        return cls[W.inv[min(c)]]
    Aset = set(A)
    gcls = {c: frozenset(m1(c, a) for a in A) for c in G1}
    Gs = sorted(set(gcls.values()), key=lambda s: min(min(z) for z in s))
    check(len(Gs) == 2, 'G = S_4 / A_4 = Z_2')
    one = gcls[cls[W.e]]
    Gidx = {s: (0 if s == one else 1) for s in Gs}
    sec = {}
    for s in Gs:
        sec[Gidx[s]] = cls[W.e] if s == one else \
            next(c for c in G1 if gcls[c] == s)
    # factor system h(g1, g2) = (g1g2)-bar^-1 g1-bar g2-bar in A
    h = {(a, b): m1(inv1(sec[(a + b) % 2]), m1(sec[a], sec[b]))
         for a in range(2) for b in range(2)}
    check(all(v in Aset for v in h.values()), 'h takes values in A')

    def act1(av, g):  # a^(g-bar) = g-bar^-1 a g-bar in S_4
        return m1(inv1(sec[g]), m1(av, sec[g]))
    ok = all(m1(h[((a + b) % 2, c)], act1(h[(a, b)], c)) ==
             m1(h[(a, (b + c) % 2)], h[(b, c)])
             for a in range(2) for b in range(2) for c in range(2))
    check(ok, 'eq:nonabelian-cocycle-identity for 1 -> A_4 -> S_4 -> Z_2 '
          '-> 1 (all triples)')
    # lifts h-bar in B and the action of G_1-bar on B through GL(2,3)
    hb = {k: min(v) for k, v in h.items()}
    hb[(0, 0)] = hb[(0, 1)] = hb[(1, 0)] = W.e  # normalized

    def actB(b, g):
        y = min(sec[g])
        return W.prod(W.inv[y], b, y)

    def dh(a, b, c):
        return W.prod(hb[((a + b) % 2, c)], actB(hb[(a, b)], c),
                      W.inv[hb[(b, c)]], W.inv[hb[(a, (b + c) % 2)]])
    vals = {(a, b, c): dh(a, b, c) for a in range(2) for b in range(2)
            for c in range(2)}
    check(all(v in C for v in vals.values()),
          'delta h-bar takes values in C (p. 112)')
    # C = Z_2 trivial module; normalized cochains of Z_2: only (x, x, x)
    T2 = group('CyclicGroup(IsPermGroup, 2)', 'Z2')
    D2 = coboundary_matrix(T2, trivial_module(T2), 2)
    D3 = coboundary_matrix(T2, trivial_module(T2), 3)
    cval = 0 if vals[(1, 1, 1)] == W.e else 1
    check((D3 * matrix(ZZ, 1, 1, [cval])).change_ring(Zmod(2)).is_zero(),
          'delta h-bar is a 3-cocycle')
    # its class is 0 mod 2 iff cval is in Im D2 mod 2
    sol = [p for p in range(2) if (D2[0, 0] * p - cval) % 2 == 0]
    check(sol, 'the obstruction vanishes (E_2 = GL(2,3) exists)')
    p = sol[0]
    cel = next(c for c in C if c != W.e)
    if p:
        hb[(1, 1)] = W.mul[hb[(1, 1)]][cel]  # h-bar phi^-1 (C of order 2)
    ok = all(W.prod(hb[((a + b) % 2, c)], actB(hb[(a, b)], c)) ==
             W.prod(hb[(a, (b + c) % 2)], hb[(b, c)])
             for a in range(2) for b in range(2) for c in range(2))
    check(ok, 'corrected h-bar satisfies eq:nonabelian-cocycle-identity')
    pairs = [(g, b) for g in range(2) for b in B]
    idx = {pp: i for i, pp in enumerate(pairs)}

    def pm(p1, p2):
        (g1, b1), (g2, b2) = p1, p2
        return ((g1 + g2) % 2, W.prod(hb[(g1, g2)], actB(b1, g2), b2))
    table = [[idx[pm(p1, p2)] for p2 in pairs] for p1 in pairs]
    n = len(pairs)
    assoc = all(table[table[i][j]][k] == table[i][table[j][k]]
                for i in range(n) for j in range(n) for k in range(n))
    check(assoc, 'p. 113: the multiplication of pairs (g, b) is associative')
    e2 = idx[(0, W.e)]
    check(all(table[e2][i] == i == table[i][e2] for i in range(n)) and
          all(any(table[i][j] == e2 for j in range(n)) for i in range(n)),
          'identity (1, 1) and inverses: a group of order 48')

    def to1(pp):  # (g, b) -> g-bar f(b)
        g, b = pp
        return m1(sec[g], cls[b])
    hom = all(to1(pm(p1, p2)) == m1(to1(p1), to1(p2))
              for p1 in pairs for p2 in pairs)
    check(hom, '(g, b) -> g-bar f(b) is a homomorphism to S_4')
    imgs = set(to1(pp) for pp in pairs)
    ker = [pp for pp in pairs if to1(pp) == cls[W.e]]
    check(len(imgs) == 24 and sorted(ker) == sorted((0, c) for c in C),
          'onto S_4 with kernel C')


def twisted_multiplication():
    """p. 115: G-bar = SL(2,3) x Z_3, A = Q_8 x Z_3 (nonabelian), Z(A) =
    {+-1} x Z_3 cyclic of order 6, G = Z_3; phi = delta t has values of
    order 3 and 6, so delta s and (delta s)^-1 differ."""
    D = gap('function() local S, C, D; S := Image(IsomorphismPermGroup('
            'SL(2, 3))); C := CyclicGroup(IsPermGroup, 3); D := '
            'DirectProduct(S, C); return [D, Group(Concatenation(List('
            'GeneratorsOfGroup(DerivedSubgroup(S)), x -> Image(Embedding(D, '
            '1), x)), List(GeneratorsOfGroup(C), x -> Image(Embedding(D, 2), '
            'x))))]; end')()
    S = TGroup(D[0], 'SL23xZ3')
    A = sorted(S.elt(y) for y in D[1].AsList())
    ZA = [a for a in A if all(S.mul[a][b] == S.mul[b][a] for b in A)]
    check(len(A) == 24 and len(ZA) == 6 and
          any(S.mul[a][b] != S.mul[b][a] for a in A for b in A),
          'A = Q_8 x Z_3 nonabelian, Z(A) of order 6')
    cos = {g: frozenset(S.mul[g][a] for a in A) for g in range(S.N)}
    Gs = sorted(set(cos.values()), key=min)
    check(len(Gs) == 3, 'G = G-bar / A = Z_3')
    gi = {s: i for i, s in enumerate(Gs)}
    sigma = [gi[cos[g]] for g in range(S.N)]
    one = sigma[S.e]
    reps = {gi[s]: min(s) if gi[s] != one else S.e for s in Gs}
    Gmul = {(a, b): sigma[S.mul[reps[a]][reps[b]]]
            for a in range(3) for b in range(3)}

    def conj(zv, b):  # z^(g-bar), g-bar a representative of b in G
        y = reps[b]
        return S.prod(S.inv[y], zv, y)

    def delta(tf):  # (delta t)(a, b) = t(a)^b t(ab)^-1 t(b), Z(A) abelian
        return {(a, b): S.prod(conj(tf[a], b), S.inv[tf[Gmul[(a, b)]]],
                               tf[b]) for a in range(3) for b in range(3)}
    z6 = next(a for a in ZA if all(S.prod(*([a] * k)) != S.e
                                   for k in range(1, 6)))
    t = {one: S.e}
    others = [i for i in range(3) if i != one]
    t[others[0]] = z6
    t[others[1]] = S.e
    phi = delta(t)
    check(any(S.mul[v][v] != S.e for v in phi.values()),
          'phi = delta t has values of order > 2')
    circ = [[S.mul[S.mul[g1][g2]][phi[(sigma[g1], sigma[g2])]]
             for g2 in range(S.N)] for g1 in range(S.N)]

    # regular permutation representations, y -> y o x and y -> y x
    def regperm(tab, x):
        return libgap.PermList([tab[y][x] + 1 for y in range(S.N)])
    Pc = libgap.Group([regperm(circ, x) for x in range(S.N)])
    Pb = libgap.Group([regperm(S.mul, x) for x in range(S.N)])
    iso = libgap.IsomorphismGroups(Pc, Pb)
    check(iso != libgap.fail, 'G-bar^o is isomorphic to G-bar')
    auts = list(libgap.AutomorphismGroup(Pb).AsList())
    good = []
    for au in auts:
        psi = []
        for x in range(S.N):
            img = libgap.Image(au, libgap.Image(iso, regperm(circ, x)))
            psi.append(int(libgap.OnPoints(S.e + 1, img)) - 1)
        if all(psi[a] == a for a in A) and \
                all(sigma[psi[g]] == sigma[g] for g in range(S.N)):
            good.append(psi)
    check(len(good) >= 1, 'there are isomorphisms G-bar^o -> G-bar that are '
          'the identity on A and on G')
    for alpha in good:   # alpha: G-bar^o -> G-bar, alpha(g o h) = ..
        check(all(alpha[circ[g][h]] == S.mul[alpha[g]][alpha[h]]
                  for g in range(S.N) for h in range(S.N)),
              'alpha(g_1 o g_2) = alpha(g_1) alpha(g_2)')
        s = [S.mul[S.inv[g]][alpha[g]] for g in range(S.N)]
        check(all(v in ZA for v in s), 'g^-1 alpha(g) in Z(A)')
        check(all(s[S.mul[g][a]] == s[g] for g in range(S.N) for a in A),
              's depends only on the coset g A')
        refuted(all(alpha[S.mul[g][a]] == alpha[g]
                    for g in range(S.N) for a in A),
                'alpha depends only on the coset g A (printed, p. 115)')
        sG = {sigma[g]: s[g] for g in range(S.N)}
        ds = delta(sG)
        check(all(phi[k] == ds[k] for k in phi),
              'alpha: G-bar^o -> G-bar gives phi = delta s exactly')
        refuted(all(phi[k] == S.inv[ds[k]] for k in phi),
                'phi = (delta s)^-1 for alpha: G-bar^o -> G-bar')
        beta = [None] * S.N
        for x in range(S.N):
            beta[alpha[x]] = x       # beta = alpha^-1: G-bar -> G-bar^o
        check(all(beta[S.mul[g][h]] == circ[beta[g]][beta[h]]
                  for g in range(S.N) for h in range(S.N)),
              'beta(g_1 g_2) = beta(g_1) o beta(g_2)')
        sbe = [S.mul[S.inv[g]][beta[g]] for g in range(S.N)]
        check(all(v in ZA for v in sbe) and
              all(sbe[S.mul[g][a]] == sbe[g] for g in range(S.N) for a in A),
              'beta(g) = g s(g), s(g) in Z(A) constant on g A')
        sb = {sigma[g]: sbe[g] for g in range(S.N)}
        dsb = delta(sb)
        check(all(phi[k] == S.inv[dsb[k]] for k in phi),
              'beta: G-bar -> G-bar^o gives phi = (delta s)^-1')
        refuted(all(phi[k] == dsb[k] for k in phi),
                'phi = delta s for beta: G-bar -> G-bar^o')
    # the printed g_1 o g_2 = alpha(g_1) alpha(g_2): putting g_2 = 1 gives
    # alpha(g) = g u with u = alpha(1)^-1 (phi is normalized), so every
    # solution alpha is of this form; none of the 24 works
    check(all(circ[g][S.e] == g == circ[S.e][g] for g in range(S.N)),
          'phi normalized: g o 1 = g = 1 o g')
    sols = [u for u in range(S.N)
            if all(circ[g][h] == S.prod(g, u, h, u)
                   for g in range(S.N) for h in range(S.N))]
    refuted(sols, 'printed g_1 o g_2 = alpha(g_1) alpha(g_2) has a solution '
            'alpha (all alpha(g) = g u tried)')


def main():
    section_4()
    section_5()
    section_6()
    section_7()
    print('ok %s: %d checks' % (SCOPE, COUNT[0]))


if __name__ == '__main__':
    main()
