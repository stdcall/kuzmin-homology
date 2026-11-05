"""Exact checks of Chapter 6 "Гомологии свободных абелевых расширений",
§§ 4-5 (Sage).

Run from the project root: sage -python checks/sage/chapter-6b.py (plain
asserts; do not use -O).  The last line is "ok chapter-6b: N checks".

Book: Ю. В. Кузьмин, «Гомологическая теория групп» (Факториал Пресс, 2006),
chapter 6, printed pp. 313-338.  Pages are the printed pages; labels are
those of content/06-04-*.typ and 06-05-*.typ.  Exact arithmetic only:
polynomials over ZZ (Sage PolynomialRing), integers, rational functions
over QQ; power series are truncated polynomials.  The polynomials f_n^(p)
are computed from eq:polynomial-recursion; the expected values are the
printed ones (examples, exercises) or the statements of the propositions.

What is checked (p = 3, 5, 7, 11, 13 where not said otherwise):

§ 4 (pp. 313-323).
  eq:polynomial-examples (also the intermediate steps), the example n = 12
  (f_12^(3) = x^8 + x^4 + x^3, the dimensions 20, 16, 15 of T_12 and 15, 14
  of K_12, C_12 for p = 11), the introduction's T-bar_p = H_(p+2)(B, Z_p)
  (f_p = x^2); prop:polynomial-degree (all m p < 6 p^3, resp. 3 p^3);
  prop:polynomial-lowest-degree and its proof (52 = 1 2 2 1 in base 3; the
  digits of n - p, sigma_p(n - p), epsilon_p(n - p), the identity
  delta_p(n - p) + 2 = delta_p(n) + (t - 1)(2p - 3) + gamma with equality
  exactly when n/p != 0; 1 mod p, C564; the printed delta_p(n - p) >=
  delta_p(n) refuted); th:extreme-dimensions; cor:torsion-vanishing-dimension
  and cor:homology-stabilization for d < 60 (all n > d - 2) and
  delta_p(p^t) = 2 < delta_p(n) otherwise; gamma(m) = f_(m p)^(p)(1): the
  increments of p. 318, eq:gamma-sum, the linear bound
  1 + 2(m - p)/p (C568; the printed 1 + 2(m - 1)/p refuted at m = 2, p),
  gamma(k + 1) <= 2 gamma(k) with equality at k = p - 1 (C573; the printed
  strict inequality refuted); th:gamma-asymptotics: eq:model-ratio as an
  identity of rational functions in alpha, L = ln x, P = ln p (log f(x) =
  alpha L^2/P), the step Delta f = f(x/p) sqrt(p) log_p x at alpha = 1/2,
  and the bounds p^(k^2/4) < gamma(p^k) < p^(k^2/2) for 2 <= k <= 11, 7, 6
  (p = 3, 5, 7: an illustration of the theorem, not a proof of it);
  prop:parity-differences: f_n^(p)(-1) = ||n||_p, the decomposition with
  g_n^(p) >= 0, g_n^(p)(-1) = 0, the three cases of the proof (C579:
  ||n - p||_p = ||n/p - 1||_p + 1; the printed equality without + 1
  refuted), eq:sign-differences for T_n, C_n, K_n from the polynomials,
  ||n||_p <= log_p n; exercises exc:polynomial-formulas,
  exc:coefficient-greater-one (with the hint), exc:single-summand,
  exc:delta-unbounded (delta_p(p^t - p) = (t - 1)(2p - 3) + 1),
  exc:max-coefficient-growth (mu <= gamma <= 2 m mu), and
  exc:generating-function-equation, exc:generating-function-product modulo
  t^(3 p^2 + 6).
§ 5 (pp. 323-338).
  lem:koszul-sequence over ZZ with the printed d_k: D D = 0, exactness and
  saturated images (Smith form) for rank A' <= 3, rank A'' <= 2, n <= 4;
  for rank A = 1 and A'' = 0 the sequence is A (x) S^(n-1) A = S^n A for
  every n (the question of p. 324).  lem:projection-binomial from the
  definition of pi^n_i (sum over permutations, n <= 6, 1/(i!(n - i)!)
  integral): the factor is C_(n-k)^(i-k); the printed C_(i-k)^(n-k) of
  C588 is 0 for i < n (refuted); cor:projection-kernel.  lem:lucas and
  eq:lucas (all a <= b < p^3, and p^4 for p = 3; (1 + x)^(p^a) =
  1 + x^(p^a) mod p).  lem:regular-section-single, -double, -top and
  lem:top-section-homology (v_p C_n^(p^s) = 1 when ||n||_p = s + 1) for
  p = 3, 5 and n <= 3 p^3 (p = 3), 2 p^3 (p = 5).  Elementary sections: the
  special case p does not divide n of p. 329 is the full list; the series
  of lem:elementary-acyclic exists (tiling of the floors by elementary
  sections below n); lem:section-shift (the section R^i_(k+1) is elementary
  of type (ii), R^i_(j k+1) regular); the remark of p. 333 (R^(p-1)_1 is
  the regular section R^p_(p-1 1)).  Basic sections: lem:basic-series for
  every s <= t (tiling exists, all basic sections used), with the filling
  sections of C596 elementary (the printed ones refuted); the basic sections
  of type (i) of R^(n/p) and R^n paired by phi in case 3) (C603: upper
  indices (n - p^alpha)/p + p^(alpha-2) and n - p^alpha + p^(alpha-1)); the
  indices of the three expressions after eq:three-cases (lem:section-shift and
  lem:top-section-homology apply, the sections are R^N_(N-p^s'+1) with
  s' < ||N||_p).  The polynomials f_n^(p,s) with case (iii) summed to t - 1
  (C606; the printed sum to t, read with f_0 = 1, gives 2 x^2 at n = p:
  refuted) equal f_(n/p^s)^(p) (lem:section-polynomials) for p = 3, 5, 7,
  n <= p^4 + 2 p^2; C607 (the printed f_(n/p^s - p) refuted at p = 3,
  n = 18); the identity f_(n/p^s) = sum_(alpha=s+1)^t x^2
  f_(n/p^(alpha-1)-p) + f_(n/p^t), obtained by applying
  eq:polynomial-recursion t - s times, in the three cases (the corrected
  proof of lem:section-polynomials; the printed first equality at s = 0 is
  f_n = f_n^(p,0), the statement itself); over Z_p, the corrected
  eq:delta-p-mod-p gives x^2 + x as cor:delta-p-homology, the printed
  H_(m+1)(B, Delta) gives 2 x^2 (C595, refuted).

What is NOT established: the homological statements of §§ 4-5 themselves
(no group B without p-torsion and with non-zero H_n(B, Z_p) for large n is
computed here: such B have infinite-rank relation modules); the asymptotic
theorem th:gamma-asymptotics (only finite ranges); identities beyond the
stated ranges.  Nothing here compares our text with the printed book.
"""

import itertools

from sage.all import (QQ, ZZ, PolynomialRing, binomial, factorial, identity_matrix,
                      matrix)

SCOPE = 'chapter-6b'
COUNT = [0]
R = PolynomialRing(ZZ, 'x')
x = R.gen()
PRIMES = (3, 5, 7, 11, 13)


def check(cond, what):
    assert bool(cond), 'FAILED: ' + what
    COUNT[0] += 1


def refuted(cond, what):
    assert not bool(cond), 'printed reading unexpectedly holds: ' + what
    COUNT[0] += 1


class Tally:
    """One check per statement over a range of cases; a failure reports
    the first failing case."""

    def __init__(self):
        self.ok, self.first = {}, {}

    def __call__(self, key, cond, case=''):
        if self.ok.setdefault(key, True) and not cond:
            self.ok[key] = False
            self.first[key] = case

    def flush(self, suffix):
        for key, v in self.ok.items():
            check(v, key + suffix + ('' if v else '; first failure: ' + self.first[key]))
        self.ok, self.first = {}, {}


# ---------------------------------------------------------------------------
# Polynomials f_n^(p) and arithmetic functions
# ---------------------------------------------------------------------------

def f_table(p, N):
    """f_n^(p) for 2 <= n <= N by eq:polynomial-recursion."""
    f = {}
    for n in range(2, N + 1):
        if n % p not in (0, 1):
            f[n] = R(0)
        elif n % p == 1:
            f[n] = x * f[n - 1]
        elif n == p:
            f[n] = x ** 2
        else:
            f[n] = x ** 2 * f[n - p] + (f[n // p] if n // p > 1 else R(0))
    return f


def digits(n, p):
    d = []
    while n:
        d.append(n % p)
        n //= p
    return d


def sigma(n, p):
    return sum(digits(n, p))


def eps(n, p):
    return sum(1 for c in digits(n, p) if c)


def delta(n, p):
    return 2 * sigma(n, p) - eps(n, p) + 1


def val(n, p):
    """||n||_p, with ||0||_p = infinity."""
    if n == 0:
        return float('inf')
    s = 0
    while n % p == 0:
        n //= p
        s += 1
    return s


def lowdeg(g):
    return min(g.exponents())


def bound(p):
    return 6 * p ** 3 if p < 7 else 3 * p ** 3


# ---------------------------------------------------------------------------
# § 4
# ---------------------------------------------------------------------------

def section_4_polynomials():
    for p in PRIMES:
        f = f_table(p, bound(p))
        for r in range(1, p):
            check(f[r * p] == x ** (2 * r), 'f_(%d p)^(%d) = x^%d' % (r, p, 2 * r))
            if r > 1:
                check(f[r * p] == x ** 2 * f[(r - 1) * p], 'p. 314: f_(r p) = x^2 f_((r-1) p)')
        check(f[p * p] == x ** 2 * x ** (2 * (p - 1)) + x ** 2 == x ** (2 * p) + x ** 2,
              'eq:polynomial-examples: f_(p^2) = x^(2p) + x^2 (p = %d)' % p)
        check(f[p + 1] == x ** 3 and
              f[p * p + p] == x ** 2 * (x ** (2 * p) + x ** 2) + x ** 3 ==
              x ** (2 * p + 2) + x ** 4 + x ** 3,
              'eq:polynomial-examples: f_(p^2 + p) = x^(2p + 2) + x^4 + x^3 (p = %d)' % p)
        check(f[p] == x ** 2, 'introduction: f_p = x^2, so T-bar_p = H_(p+2)(B, Z_p) (p = %d)' % p)
        T = Tally()
        for n in range(2, bound(p) + 1):
            g = f[n]
            case = 'n = %d' % n
            if n % p not in (0, 1):
                T('eq:polynomial-recursion: f_n = 0 for n != 0; 1 mod p', g == 0, case)
                continue
            if n % p == 0:
                m = n // p
                T('prop:polynomial-degree: deg f_(m p) = 2m, leading coefficient 1',
                  g.degree() == 2 * m and g.leading_coefficient() == 1, case)
            if n >= p:
                T('prop:polynomial-lowest-degree: lowest degree delta_p(n), coefficient 1',
                  lowdeg(g) == delta(n, p) and g[delta(n, p)] == 1, case)
            if n % p == 1 and n > p:
                T('p. 316: sigma_p(n) = sigma_p(n - 1) + 1, epsilon_p(n) = epsilon_p(n - 1) + 1 '
                  'for n = 1 mod p',
                  sigma(n, p) == sigma(n - 1, p) + 1 and eps(n, p) == eps(n - 1, p) + 1, case)
            if n % p == 0 and n > p:
                t = val(n, p)
                dg = digits(n, p)
                gam = 1 if dg[t] == 1 else 0
                expect = [0] + [p - 1] * (t - 1) + [dg[t] - 1] + dg[t + 1:]
                while expect and expect[-1] == 0:
                    expect.pop()
                T('p. 316: the p-adic digits of n - p', digits(n - p, p) == expect, case)
                T('p. 317: sigma_p(n - p) = (t - 1)(p - 1) + sigma_p(n) - 1, epsilon_p(n - p) = '
                  '(t - 1) + epsilon_p(n) - gamma, delta_p(n/p) = delta_p(n)',
                  sigma(n - p, p) == (t - 1) * (p - 1) + sigma(n, p) - 1 and
                  eps(n - p, p) == (t - 1) + eps(n, p) - gam and delta(n // p, p) == delta(n, p),
                  case)
                T('p. 317: delta_p(n - p) + 2 = delta_p(n) + (t - 1)(2p - 3) + gamma',
                  delta(n - p, p) + 2 == delta(n, p) + (t - 1) * (2 * p - 3) + gam, case)
                T('C564: delta_p(n - p) + 2 = delta_p(n) iff n/p != 0; 1 mod p',
                  (delta(n - p, p) + 2 == delta(n, p)) == ((n // p) % p not in (0, 1)), case)
        T.flush(' (p = %d, n <= %d)' % (p, bound(p)))
        bad = [n for n in range(2 * p, bound(p) + 1, p) if delta(n - p, p) < delta(n, p)]
        refuted(not bad, 'C564: printed delta_p(n - p) >= delta_p(n) fails for n = %s... (p = %d)'
                % (bad[:3], p))
        check(digits(52, 3) == [1, 2, 2, 1], 'p. 316: 52 = 1 3^3 + 2 3^2 + 2 3 + 1')
    # example n = 12
    f3, f11 = f_table(3, 40), f_table(11, 40)
    check(f3[12] == x ** 8 + x ** 4 + x ** 3 and 12 == 3 ** 2 + 3,
          'p. 315: f_12^(3) = x^8 + x^4 + x^3')
    check(sorted(12 + e for e in f3[12].exponents()) == [15, 16, 20],
          'p. 315: T_12 = H_20 + H_16 + H_15 (B, Z_3)')
    check(f11[11] == x ** 2 and 12 + 1 + 2 == 15 and 12 + 2 == 14,
          'p. 315: K_12 = H_15(B, Z_11), C_12 = H_14(B, Z_11) (f_11^(11) = x^2)')


def section_4_dimensions():
    for p in PRIMES:
        f = f_table(p, bound(p))
        T = Tally()
        for n in range(2, bound(p) + 1):
            if n % p == 0:
                ex = f[n].exponents()
                T('th:extreme-dimensions: dimensions n + 2n/p and n + delta_p(n), multiplicity 1',
                  n + max(ex) == n + 2 * n // p and n + min(ex) == n + delta(n, p) and
                  f[n][max(ex)] == 1 and f[n][min(ex)] == 1, 'n = %d' % n)
            is_power = n == p ** val(n, p) if n % p == 0 else False
            T('p. 317: delta_p(n) >= 2, with equality exactly for the powers of p',
              (delta(n, p) == 2) == is_power and delta(n, p) >= 2, 'n = %d' % n)
        T.flush(' (p = %d, n <= %d)' % (p, bound(p)))
        for d in range(0, 60):
            for n in range(max(2, d - 1), d + 40):
                if n % p == 0:
                    T('cor:homology-stabilization: t_p T_n = 0 for n > d - 2',
                      n + delta(n, p) > d, 'd = %d, n = %d' % (d, n))
                if n % p == 1 and n > p:
                    T('cor:homology-stabilization: t_p C_n = t_p K_n = 0 for n > d - 2',
                      n + delta(n - 1, p) > d and n + 1 + delta(n - 1, p) > d,
                      'd = %d, n = %d' % (d, n))
        T.flush(' (hd B = d < 60, p = %d)' % p)
        check(3 + delta(3, 3) == 5, 'cor:torsion-vanishing-dimension is sharp: n = 3 = d - 2, '
              't_3 T_3 = H_5(B, Z_3) for hd B = 5')
        for t in range(2, 6):
            check(delta(p ** t - p, p) == (t - 1) * (2 * p - 3) + 1,
                  'exc:delta-unbounded: delta_p(p^t - p) = (t - 1)(2p - 3) + 1 (t = %d)' % t)


def gammas(p, M):
    g = [0, 1]
    for m in range(2, M + 1):
        if m % p == 0:
            g.append(g[m - 1] + g[m // p])
        elif m % p == 1:
            g.append(g[m - 1] + g[(m - 1) // p])
        else:
            g.append(g[m - 1])
    return g


def section_4_growth():
    for p in (3, 5, 7, 11):
        f = f_table(p, 5 * p ** 3)
        M = 5 * p * p
        gam = [None] + [f[m * p](1) for m in range(1, M + 1)]
        g2 = gammas(p, M)
        check(gam[1:] == g2[1:], 'p. 318: gamma(m) = f_(m p)(1) obeys the increments rule (p = %d)'
              % p)
        T = Tally()
        for m in range(2, M + 1):
            if m % p not in (0, 1):
                T('p. 318: gamma(m) = gamma(m - 1) for m != 0; 1 mod p', gam[m] == gam[m - 1],
                  'm = %d' % m)
        for k in range(1, M // p):
            T('p. 318: gamma(k p) = gamma(k p - 1) + gamma(k), gamma(k p + 1) = gamma(k p) + '
              'gamma(k)', gam[k * p] == gam[k * p - 1] + gam[k] and
              gam[k * p + 1] == gam[k * p] + gam[k], 'k = %d' % k)
            T('eq:gamma-sum and gamma(k p + 1) >= 1 + 2k',
              gam[k * p + 1] == 1 + 2 * sum(gam[1:k + 1]) >= 1 + 2 * k, 'k = %d' % k)
            if k > 1:
                T('p. 318: the increment on [(k - 1)p + 1, k p + 1] is 2 gamma(k)',
                  gam[k * p + 1] - gam[(k - 1) * p + 1] == 2 * gam[k], 'k = %d' % k)
        T.flush(' (p = %d, m <= %d)' % (p, M))
        check(all(p * gam[m] >= p + 2 * (m - p) for m in range(1, M + 1)),
              'C568: gamma(m) >= 1 + 2(m - p)/p for m <= %d (p = %d)' % (M, p))
        bad = [m for m in range(1, M + 1) if p * gam[m] < p + 2 * (m - 1)]
        refuted(not bad, 'C568: printed gamma(m) >= 1 + 2(m - 1)/p fails at m = %s (p = %d)'
                % (bad[:4], p))
        check(2 in bad and p in bad, 'C568: the printed bound fails at m = 2 and m = p (p = %d)' % p)
        eq = [k for k in range(1, M) if gam[k + 1] == 2 * gam[k]]
        check(all(gam[k + 1] <= 2 * gam[k] for k in range(1, M)) and eq == [p - 1],
              'C573: gamma(k + 1) <= 2 gamma(k), equality only at k = p - 1 (p = %d)' % p)
        refuted(not eq, 'C573: printed gamma(k + 1) < 2 gamma(k) fails at k = %s (p = %d)' % (eq, p))
        mu = [None] + [max(f[m * p].coefficients()) for m in range(1, M + 1)]
        check(all(mu[m] <= gam[m] <= 2 * m * mu[m] for m in range(1, M + 1)),
              'exc:max-coefficient-growth: mu(m) <= gamma(m) <= 2 m mu(m) (p = %d)' % p)
    # th:gamma-asymptotics, eq:model-ratio as identities in alpha, L = ln x, P = ln p
    S = PolynomialRing(QQ, ['alpha', 'L', 'P'])
    alpha, L, P = S.gens()
    logf = alpha * L ** 2 / P                         # log f(x), f = x^(alpha log_p x)
    dlogf = 2 * alpha * L / P                         # x d/dx log f(x)
    check(S(logf * P).derivative(L) == S(dlogf * P),
          'eq:model-ratio: f\'(x) = f(x) 2 alpha log_p x / x')
    logf_xp = alpha * (L - P) ** 2 / P                # log f(x/p)
    check(logf_xp - (logf + alpha * P - 2 * alpha * L) == 0,
          'eq:model-ratio: f(x/p) = f(x) p^alpha / x^(2 alpha)')
    # log(f'(x)/f(x/p)) = log(2 alpha log_p x) - L + logf - logf_xp
    #                   = log(2 alpha log_p x) - alpha P + (2 alpha - 1) L
    check((-L + logf - logf_xp) - (-alpha * P + (2 * alpha - 1) * L) == 0,
          'eq:model-ratio: f\'(x)/f(x/p) = (2 alpha/p^alpha) x^(2 alpha - 1) log_p x')
    # alpha = 1/2: Delta f = p f'(xi) = f(xi/p) (log_p xi/sqrt p) p = f(xi/p) sqrt(p) log_p xi:
    # log of p (2 alpha/p^alpha) xi^(2 alpha - 1) is P - alpha P + (2 alpha - 1) L = P/2
    half = (P - alpha * P + (2 * alpha - 1) * L).subs(alpha=QQ(1) / 2)
    check(half == P / 2, 'p. 319: at alpha = 1/2, Delta f = p f\'(x) = f(x/p) sqrt(p) log_p x')
    for p in (3, 5, 7):
        K = {3: 11, 5: 7, 7: 6}[p]
        g = gammas(p, p ** K)
        check(all(g[p ** k] ** 2 < p ** (k * k) < g[p ** k] ** 4 for k in range(2, K + 1)),
              'th:gamma-asymptotics (illustration): p^(k^2/4) < gamma(p^k) < p^(k^2/2), '
              '2 <= k <= %d (p = %d)' % (K, p))


def section_4_parity():
    for p in PRIMES:
        f = f_table(p, bound(p))
        T = Tally()
        printed_c579 = []
        for n in range(p, bound(p) + 1, p):
            s = val(n, p)
            case = 'n = %d' % n
            T('prop:parity-differences: f_n^(p)(-1) = ||n||_p', f[n](-1) == s, case)
            g = f[n] - sum(x ** (2 * n // p ** i) for i in range(1, s + 1))
            T('p. 321: g_n^(p) = f_n^(p) - sum x^(2n/p^i) has non-negative coefficients and '
              'g_n^(p)(-1) = 0', all(c >= 0 for c in g.coefficients()) and g(-1) == 0, case)
            if n == p:
                check(g == 0, 'p. 321: g_p = x^2 - x^2 = 0 (p = %d)' % p)
            if n > p:
                q = n // p
                if q % p not in (0, 1):
                    T('p. 321: n/p != 0; 1 mod p: ||n|| = ||n - p|| = 1, f_n = x^2 f_(n-p)',
                      val(n, p) == val(n - p, p) == 1 and f[n] == x ** 2 * f[n - p], case)
                elif q % p == 0:
                    T('p. 321: n/p = 0 mod p: ||n - p|| = 1', val(n - p, p) == 1, case)
                else:
                    T('C579: n/p = 1 mod p: ||n - p|| = ||n/p - 1|| + 1, f_n = x^2 f_(n-p) + '
                      'x f_(n/p-1)', val(n, p) == 1 and val(n - p, p) == val(q - 1, p) + 1 and
                      f[n] == x ** 2 * f[n - p] + x * f[q - 1], case)
                    printed_c579.append(val(n - p, p) == val(q - 1, p))
        for n in range(2, bound(p) + 1):
            # h^+ - h^- from the decompositions of th:polynomial-homology
            fT = f[n] if n % p == 0 else R(0)
            fC = f[n - 1] if n % p == 1 and n - 1 >= 2 else R(0)
            hT = sum(c * (-1) ** (n + k) for k, c in enumerate(fT.list()))
            hC = sum(c * (-1) ** (n + k) for k, c in enumerate(fC.list()))
            hK = sum(c * (-1) ** (n + 1 + k) for k, c in enumerate(fC.list()))
            vn, vn1 = val(n, p), val(n - 1, p)
            T('eq:sign-differences for T_n, C_n, K_n',
              hT == (-1) ** n * vn and hC == (-1) ** n * vn1 and hK == (-1) ** (n + 1) * vn1,
              'n = %d' % n)
            T('p. 320: ||n||_p <= log_p n', p ** vn <= n, 'n = %d' % n)
        T.flush(' (p = %d, n <= %d)' % (p, bound(p)))
        refuted(not printed_c579 or any(printed_c579), 'C579: printed ||n - p||_p = ||n/p - 1||_p '
                '(it fails for all %d cases n/p = 1 mod p, n > p; p = %d)' % (len(printed_c579), p))


def series_coeffs(A, T):
    return [A.get(k, R(0)) for k in range(T + 1)]


def smul(A, B, T):
    C = [R(0)] * (T + 1)
    for i, a in enumerate(A):
        if a:
            for j in range(0, T + 1 - i):
                if B[j]:
                    C[i + j] += a * B[j]
    return C


def ssub(A, q, T):
    """A(t^q) truncated at t^T."""
    C = [R(0)] * (T + 1)
    for i, a in enumerate(A):
        if i * q <= T:
            C[i * q] = a
    return C


def section_4_exercises():
    for p in (3, 5, 7, 11):
        f = f_table(p, p ** 3 + p * p + p)
        for r2 in range(1, p):
            rhs = x ** (2 * r2 * p) + x ** (2 * r2) + (1 + x) * sum(
                (x ** (2 * ((r2 - r) * p + r) - 1) for r in range(1, r2)), R(0))
            check(f[r2 * p * p] == rhs, 'exc:polynomial-formulas: f_(%d p^2) (p = %d)' % (r2, p))
            for r1 in range(1, p):
                rhs = x ** (2 * (r2 * p + r1)) + (1 + x) * sum(
                    (x ** (2 * ((r2 - r) * p + r1 + r) - 1) for r in range(1, r2 + 1)), R(0))
                check(f[r2 * p * p + r1 * p] == rhs,
                      'exc:polynomial-formulas: f_(%d p^2 + %d p) (p = %d)' % (r2, r1, p))
        rhs = x ** (2 * p * p) + x ** (2 * p) + x ** 2 + (1 + x) * sum(
            (x ** (2 * ((p - r) * p + r) - 1) for r in range(1, p)), R(0))
        check(f[p ** 3] == rhs, 'exc:polynomial-formulas: f_(p^3) (p = %d)' % p)
        n = p ** 3 + p * p
        check(f[n] == x ** 2 * f[p ** 3 + (p - 1) * p] + f[p * p + p] and
              f[p * p + p].degree() == 2 * (p + 1) and
              (x ** 2 * f[p ** 3 + (p - 1) * p])[2 * (p + 1)] > 0 and f[n][2 * (p + 1)] > 1,
              'exc:coefficient-greater-one: coefficient of x^(2(p + 1)) in f_(p^3 + p^2) is %d '
              '(p = %d)' % (f[n][2 * (p + 1)], p))
        check(all(f[m][delta(m, p)] == 1 for m in range(p, p ** 3, p)),
              'exc:single-summand: n + delta_p(n) = d leaves one summand H_d(B, Z_p) (p = %d)' % p)
    for p in (3, 5, 7):
        T = 3 * p * p + 5
        f = f_table(p, T)
        Phi = [R(0)] * (T + 1)
        for k in range(p, T + 1):
            Phi[k] = f[k]
        geo = [R(0)] * (T + 1)
        for j in range(0, T // p + 1):
            geo[p * j] = x ** (2 * j)
        Mser = smul([R(1), x] + [R(0)] * (T - 1), geo, T)        # (1 + x t)/(1 - x^2 t^p)
        x2tp = [R(0)] * (T + 1)
        x2tp[p] = x ** 2
        Lser = smul(Mser, x2tp, T)
        rhs6 = [a + b for a, b in zip(Lser, smul(Mser, ssub(Phi, p, T), T))]
        check(Phi == rhs6, 'exc:generating-function-equation modulo t^%d (p = %d)' % (T + 1, p))
        rhs7 = list(Lser)
        d = 1
        while p ** (d + 1) <= T:
            term = ssub(Lser, p ** d, T)
            for j in range(d):
                term = smul(term, ssub(Mser, p ** j, T), T)
            rhs7 = [a + b for a, b in zip(rhs7, term)]
            d += 1
        check(Phi == rhs7, 'exc:generating-function-product modulo t^%d (p = %d)' % (T + 1, p))


# ---------------------------------------------------------------------------
# § 5: lem:koszul-sequence, projections, binomial coefficients
# ---------------------------------------------------------------------------

def koszul_check(a1, a2, n):
    """The sequence eq:koszul-sequence for A' = Z^a1, A'' = Z^a2."""
    a = a1 + a2
    terms = []
    for k in range(n, -1, -1):
        L = list(itertools.combinations(range(a1), k))
        S = list(itertools.combinations_with_replacement(range(a), n - k))
        terms.append((k, [(I, c) for I in L for c in S]))
    idx = {k: {b: i for i, b in enumerate(basis)} for k, basis in terms}
    mats = []
    for k, basis in terms:
        if k == 0:
            continue
        D = matrix(ZZ, len(basis), len(idx[k - 1]))
        for row, (I, c) in enumerate(basis):
            for t in range(k, 0, -1):
                I2 = I[:t - 1] + I[t:]
                c2 = tuple(sorted(c + (I[t - 1],)))
                D[row, idx[k - 1][(I2, c2)]] += (-1) ** (k - t)
        mats.append(D)
    S0 = list(itertools.combinations_with_replacement(range(a), n))
    T0 = list(itertools.combinations_with_replacement(range(a1, a), n))
    t0 = {b: i for i, b in enumerate(T0)}
    D0 = matrix(ZZ, len(S0), len(T0))
    for row, c in enumerate(S0):
        if all(v >= a1 for v in c):
            D0[row, t0[c]] = 1
    mats.append(D0)
    ok = all((mats[i] * mats[i + 1]).is_zero() for i in range(len(mats) - 1))
    dims = [m.nrows() for m in mats] + [mats[-1].ncols()]
    ranks = [m.rank() for m in mats]
    exact = ranks[0] == dims[0] and ranks[-1] == dims[-1] and all(
        ranks[i] + ranks[i + 1] == dims[i + 1] for i in range(len(mats) - 1))
    sat = all(e in (0, 1) for m in mats for e in m.elementary_divisors())
    return ok, exact and sat


def section_5_koszul():
    for a1, a2 in [(1, 0), (2, 0), (3, 0), (1, 1), (2, 1), (1, 2), (2, 2), (3, 1), (3, 2)]:
        for n in range(1, 5):
            dd, ex = koszul_check(a1, a2, n)
            check(dd and ex, 'lem:koszul-sequence: D D = 0, exact with saturated images over ZZ '
                  '(rank A\' = %d, rank A\'\' = %d, n = %d)' % (a1, a2, n))
    for n in range(1, 6):
        dd, ex = koszul_check(1, 0, n)
        check(dd and ex, 'p. 324: for A free cyclic and A\'\' = 0 the sequence is A (x) S^%d(A) = '
              'S^%d(A) (any n, not only n = 1)' % (n - 1, n))


def projection(word, i, n):
    """pi^n_i on r_1 o .. o r_n, r_j in {0 (= 1), 1, 2, 3 (= delta_j)},
    by the definition of p. 327 (sum over all permutations)."""
    acc = {}
    for w in itertools.permutations(range(n)):
        first = [word[w[t]] for t in range(i)]
        rest = [word[w[t]] for t in range(i, n)]
        if all(r == 0 for r in rest):          # eps(1) = 1, eps(delta) = 0
            key = tuple(sorted(first))
            acc[key] = acc.get(key, 0) + 1
    out = {}
    for key, v in acc.items():
        assert v % (factorial(i) * factorial(n - i)) == 0
        out[key] = v // (factorial(i) * factorial(n - i))
    return out


def section_5_projections():
    for n in range(1, 7):
        for k in range(0, n + 1):
            word = tuple(sorted([1 + (j % 3) for j in range(k)] + [0] * (n - k)))
            for i in range(0, n + 1):
                img = projection(word, i, n)
                if k > i:
                    check(img == {}, 'cor:projection-kernel: pi^%d_%d vanishes on R^%d_%d'
                          % (n, i, n, i + 1))
                else:
                    target = tuple(sorted([1 + (j % 3) for j in range(k)] + [0] * (i - k)))
                    check(img == {target: binomial(n - k, i - k)},
                          'lem:projection-binomial: pi^%d_%d = C_(n-k)^(i-k) = %d on floor k = %d'
                          % (n, i, binomial(n - k, i - k), k))
                    if i < n:
                        refuted(binomial(i - k, n - k) == binomial(n - k, i - k),
                                'C588: printed C_(i-k)^(n-k) = %d (n = %d, i = %d, k = %d)'
                                % (binomial(i - k, n - k), n, i, k))


def section_5_lucas():
    for p in (3, 5, 7):
        top = p ** 4 if p == 3 else p ** 3
        ok = True
        for b in range(top):
            db = digits(b, p)
            for a in range(b + 1):
                da = digits(a, p) + [0] * (len(db) - len(digits(a, p)))
                prod = 1
                for aa, bb in zip(da, db):
                    prod *= binomial(bb, aa)
                c = binomial(b, a)
                ok = ok and (c - prod) % p == 0 and \
                    ((c % p != 0) == all(bb >= aa for aa, bb in zip(da, db)))
        check(ok, 'lem:lucas, eq:lucas: C_b^a = prod C_(b_alpha)^(a_alpha) mod %d, non-zero '
              'iff b_alpha >= a_alpha (all a <= b < %d)' % (p, top))
        for al in range(0, 4):
            q = p ** al
            check(all(c % p == 0 for c in ((1 + x) ** q - 1 - x ** q).coefficients()),
                  'p. 328: (1 + x)^(p^%d) = 1 + x^(p^%d) mod p (p = %d)' % (al, al, p))


def regular(n, i, j, p):
    """Section R^n_(i j) (floors j..i) regular: C_(n-k)^(i-k) invertible."""
    return all(binomial(n - k, i - k) % p for k in range(j, i + 1))


def elementary_sections(n, p):
    """Floors intervals (lo, hi) of the elementary sections of R^n."""
    out = set()
    tn = val(n, p)
    for i in range(1, n + 1):
        s = 0
        while p ** s <= i:
            j = i - p ** s
            if j >= 1 and val(i, p) == val(j, p) == s and s <= tn:
                out.add((j + 1, i))
            j = i - 2 * p ** s
            if j >= 1 and val(i, p) == val(j, p) == tn == s and val((i + j) // 2, p) > s:
                out.add((j + 1, i))
            s += 1
    if p ** tn <= n:
        out.add((0, p ** tn))
    return out


def tilable(lo, hi, pieces, mandatory=()):
    """Can the floors lo..hi be tiled by intervals of `pieces`, using every
    interval of `mandatory`?"""
    mand = set(mandatory)
    avail = set(pieces) | mand
    reach = {lo: frozenset()}
    for start in range(lo, hi + 1):
        if start not in reach:
            continue
        for (a, b) in avail:
            if a == start and b <= hi:
                used = reach[start] | ({(a, b)} & mand)
                if b + 1 not in reach or len(used) > len(reach[b + 1]):
                    reach[b + 1] = used
    return hi + 1 in reach and reach[hi + 1] == frozenset(mand)


def basic_sections(n, p):
    t = val(n, p)
    out = []
    for s in range(1, t + 1):
        out.append((n - p ** s + 1, n - p ** s + p ** (s - 1)))
    if val(n - p ** t, p) > t and n != p ** t:
        out.append((n - 2 * p ** t + 1, n - p ** t))
    if n == p ** t:
        out.append((0, 0))
    return out


def section_5_sections():
    for p in (3, 5):
        top = 3 * p ** 3 if p == 3 else 2 * p ** 3
        T = Tally()
        for n in range(1, top + 1):
            tn = val(n, p)
            for i in range(1, n + 1):
                s = 0
                while p ** s <= i:
                    j = i - p ** s
                    case = 'n = %d, i = %d, s = %d' % (n, i, s)
                    if val(i, p) >= s and tn >= s:
                        T('lem:regular-section-single: R^n_(i j+1) regular (i - j = p^s, '
                          '||i||, ||n|| >= s)', regular(n, i, j + 1, p), case)
                        if j >= 1 and val(j, p) > val(i, p):
                            k = j - p ** s
                            if k >= 0:
                                T('lem:section-shift: R^i_(k+1) is elementary of type (ii) and '
                                  'R^i_(j k+1) regular', (k + 1, i) in elementary_sections(i, p)
                                  and regular(i, j, k + 1, p), case)
                    j2 = i - 2 * p ** s
                    if j2 >= 1 and val(i, p) == val(j2, p) == tn == s and \
                            val((i + j2) // 2, p) > s:
                        T('lem:regular-section-double: R^n_(i j+1) regular (i - j = 2 p^s)',
                          regular(n, i, j2 + 1, p), case)
                    s += 1
            case = 'n = %d' % n
            if p ** tn <= n:
                T('lem:regular-section-top: R^n_(p^s 0) regular (s = ||n||_p)',
                  regular(n, p ** tn, 0, p), case)
            if tn >= 1:
                c = binomial(n, p ** (tn - 1))
                T('lem:top-section-homology: C_n^(p^s) is divisible by p, not by p^2 '
                  '(||n||_p = s + 1)', c % p == 0 and c % (p * p) != 0, case)
            el = elementary_sections(n, p)
            if tn == 0:
                expect = {(i, i) for i in range(2, n + 1) if i % p not in (0, 1)} | \
                         {(i - 1, i) for i in range(3, n + 1) if i % p == 1} | {(0, 1)}
                T('p. 329: for p not dividing n the elementary sections are R^n_(i i) '
                  '(i != 0; 1), R^n_(i i-1) (i = 1 mod p) and R^n_(1 0)', el == expect, case)
            below = {iv for iv in el if iv[1] < n}
            for (lo, hi) in el:
                if hi == n and lo > 0:
                    T('lem:elementary-acyclic: R^n / R^n_(j+1) has a series of elementary '
                      'sections R^n_(i\' j\') with i\' < n', tilable(0, lo - 1, below), case)
            if tn >= 1:
                bas = basic_sections(n, p)
                for s in range(0, tn + 1):
                    hi = n - p ** s
                    mand = [b for b in bas if b[1] <= hi]
                    T('lem:basic-series: R^n / R^n_(n-p^s+1) has a series of elementary sections '
                      'and all basic sections below n - p^s + 1', tilable(0, hi, el, mand),
                      '%s, s = %d' % (case, s))
                for al in range(1, tn):
                    for r in range(2, p):
                        lo = n - p ** (al + 1) + (r - 1) * p ** al + 1
                        hi = n - p ** (al + 1) + r * p ** al
                        lo_pr = n - p ** (al + 1) - (r - 1) * p ** al + 1
                        T('C596: the filling sections R^(n-p^(alpha+1)+r p^alpha)_'
                          '(n-p^(alpha+1)+(r-1)p^alpha+1) are elementary, the printed ones '
                          '(with -(r - 1)p^alpha) are not',
                          (lo, hi) in el and (lo_pr, hi) not in el, '%s, alpha = %d' % (case, al))
                t = tn
                kind = 'iii' if n == p ** t else ('ii' if val(n - p ** t, p) > t else 'i')
                for al in range(1, (t if kind == 'iii' else t + 1)):
                    i, j = n - p ** al + p ** (al - 1), n - p ** al
                    T('p. 337-338: lem:section-shift applies to R^(n-p^alpha+p^(alpha-1))_'
                      '(n-p^alpha+1) and gives R^N_(N-p^(alpha-1)+1), N = n - p^alpha, '
                      'alpha - 1 < ||N||_p', i - j == p ** (al - 1) and val(i, p) == al - 1 and
                      val(j, p) > val(i, p) and al - 1 < val(j, p), '%s, alpha = %d' % (case, al))
                for al in range(2, t + 1):
                    T('C603: phi maps the basic section of type (i) of R^(n/p) (s = alpha - 1) '
                      'to that of R^n (s = alpha): upper indices (n - p^alpha)/p + p^(alpha-2) and '
                      '(n - p^alpha) + p^(alpha-1)',
                      n // p - p ** (al - 1) + p ** (al - 2) == (n - p ** al) // p + p ** (al - 2)
                      and n // p - p ** (al - 1) + 1 == (n - p ** al) // p + 1 and
                      p * ((n - p ** al) // p + p ** (al - 2)) == (n - p ** al) + p ** (al - 1),
                      '%s, alpha = %d' % (case, al))
                if kind == 'ii':
                    T('p. 337: case (ii): R^(n-p^t)_(n-2p^t+1) = R^N_(N-p^t+1) with '
                      't < ||N||_p', t < val(n - p ** t, p), case)
                if kind == 'iii':
                    T('p. 338: case (iii): lem:top-section-homology applies to R^n_(p^(t-1) 0)',
                      val(n, p) == (t - 1) + 1, case)
        T.flush(' (p = %d, n <= %d)' % (p, top))
        refuted(all((n - p ** 2 - (r - 1) * p + 1, n - p ** 2 + r * p) in elementary_sections(n, p)
                    for n in range(p * p, top + 1, p * p) for r in range(2, p)),
                'C596: the printed sections R^(n-p^2+r p)_(n-p^2-(r-1)p+1) elementary (p = %d)' % p)
        # remark of p. 333: R^(p-1)_1 is the regular section R^p_(p-1 1)
        check(regular(p, p - 1, 1, p) and all((i, i) in elementary_sections(p, p)
                                              for i in range(2, p)),
              'p. 333: R^p_(p-1 1) = R^(p-1)_1 (projection), floors 2..p-1 elementary (p = %d)' % p)


def f_ps_table(p, N):
    """f_n^(p,s) by the corrected recursions (case (iii) summed to t - 1)."""
    fps = {}
    for n in range(p, N + 1, p):
        t = val(n, p)
        case = 'iii' if n == p ** t else ('ii' if val(n - p ** t, p) > t else 'i')
        for s in range(t - 1, -1, -1):
            top = t - 1 if case == 'iii' else t
            v = sum((x ** 2 * fps[(n - p ** al, al - 1)] for al in range(s + 1, top + 1)), R(0))
            if case == 'ii':
                v += x * fps[(n - p ** t, t)]
            if case == 'iii':
                v += x ** 2
            fps[(n, s)] = v
    return fps


def section_5_polynomials():
    for p in (3, 5, 7):
        N = p ** 4 + 2 * p * p
        f = f_table(p, N)
        fps = f_ps_table(p, N)
        check(all(fps[(n, s)] == f[n // p ** s] for (n, s) in fps),
              'lem:section-polynomials: f_n^(p,s) = f_(n/p^s)^(p), n <= %d, p = %d (C606)' % (N, p))
        refuted(x ** 2 * 1 + x ** 2 == f[p], 'C606: printed (iii) summed to t with f_0 read as 1 '
                'gives f_p^(p,0) = 2 x^2 (p = %d)' % p)
        T = Tally()
        for n in range(p, N + 1, p):
            t = val(n, p)
            case = 'iii' if n == p ** t else ('ii' if val(n - p ** t, p) > t else 'i')
            for s in range(0, t):
                q = n // p ** s
                if case == 'iii':
                    v = sum((x ** 2 * f[n // p ** (al - 1) - p] for al in range(s + 1, t)), R(0)) \
                        + x ** 2
                else:
                    v = sum((x ** 2 * f[n // p ** (al - 1) - p] for al in range(s + 1, t + 1)), R(0))
                    last = n // p ** t
                    if case == 'i':
                        T('p. 338: in case (i) n/p^t != 0; 1 mod p, so f_(n/p^t) = 0',
                          last % p not in (0, 1) and last > 1, 'n = %d' % n)
                    else:
                        v += x * f[last - 1]
                T('p. 338: f_(n/p^s) = sum_(alpha=s+1)^t x^2 f_(n/p^(alpha-1) - p) + f_(n/p^t) '
                  '(eq:polynomial-recursion applied t - s times; in case (iii) the sum ends at '
                  't - 1 and f_p = x^2)', v == f[q], 'n = %d, s = %d, case %s' % (n, s, case))
        T.flush(' (p = %d, n <= %d)' % (p, N))
    f = f_table(3, 40)
    good = x ** 2 * (f[15] + f[3])
    printed = 2 * x ** 2 * f[15]
    check(good == f[18] == x ** 12 + x ** 8 + x ** 7 + x ** 4,
          'C607: f_18^(3) = x^2 (f_15 + f_3) = x^12 + x^8 + x^7 + x^4')
    refuted(printed == f[18], 'C607: printed sum with f_(n/p^s - p) gives 2 x^2 f_15')
    # over Z_p: H_m(B, Delta^j (x) Z_p) = G_j H_m(B, Z_p), G_0 = 1, G_1 = x
    G0, G1 = R(1), x
    check(x ** 2 * G0 + G1 == x ** 2 + x, 'C595: corrected eq:delta-p-mod-p H_(m+2)(B, Z_p) + '
          'H_m(B, Delta) agrees with cor:delta-p-homology (x^2 + x)')
    refuted(x ** 2 * G0 + x * G1 == x ** 2 + x, 'C595: printed H_(m+2)(B, Z_p) + H_(m+1)(B, Delta) '
            'gives 2 x^2')


def main():
    section_4_polynomials()
    section_4_dimensions()
    section_4_growth()
    section_4_parity()
    section_4_exercises()
    section_5_koszul()
    section_5_projections()
    section_5_lucas()
    section_5_sections()
    section_5_polynomials()
    print('ok %s: %d checks' % (SCOPE, COUNT[0]))


if __name__ == '__main__':
    main()
