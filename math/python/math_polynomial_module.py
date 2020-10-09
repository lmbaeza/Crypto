from math import ceil, log
from numpy.fft import fft, ifft
from numpy import array

MOD = 7 # int(1e9+7)

def poly_deg(p):
    return len(p) - 1


def poly_scale(p, n):
    """Multiply polynomial ``p(x)`` with ``x^n``.
    If n is negative, poly ``p(x)`` is divided with ``x^n``, and remainder is
    discarded (truncated division).
    """
    if n >= 0:
        return list(p) + [0] * n
    else:
        return list(p)[:n]


def poly_scalar_mul(a, p):
    """Multiply polynomial ``p(x)`` with scalar (constant) ``a``."""
    return [(a*pi)%MOD for pi in p]


def poly_extend(p, d):
    """Extend list ``p`` representing a polynomial ``p(x)`` to
    match polynomials of degree ``d-1``.
    """
    return [0] * (d-len(p)) + list(p)


def poly_norm(p):
    """Normalize the polynomial ``p(x)`` to have a non-zero most significant
    coefficient.
    """
    for i,a in enumerate(p):
        if a != 0:
            return p[i:]
    return []


def poly_add(u, v):
    """Add polynomials ``u(x)`` and ``v(x)``."""
    d = max(len(u), len(v))
    return [(a+b)%MOD for a,b in zip(poly_extend(u, d), poly_extend(v, d))]


def poly_sub(u, v):
    """Subtract polynomials ``u(x)`` and ``v(x)``."""
    d = max(len(u), len(v))
    return poly_norm([(a-b)%MOD for a,b in zip(poly_extend(u, d), poly_extend(v, d))])


def poly_mul(u, v):
    """Multiply polynomials ``u(x)`` and ``v(x)`` with FFT."""
    if not u or not v:
        return []
    d = poly_deg(u) + poly_deg(v) + 1
    U = fft(poly_extend(u, d)[::-1])
    V = fft(poly_extend(v, d)[::-1])
    res = list(ifft(U*V).real)
    return [int(round(x))%MOD for x in res[::-1]]


def poly_recip(p):
    """Calculate the reciprocal of polynomial ``p(x)`` with degree ``k-1``,
    defined as: ``x^(2k-2) / p(x)``, where ``k`` is a power of 2.
    """
    k = poly_deg(p) + 1
    assert k>0 and p[0] != 0 and 2**round(log(k,2)) == k

    if k == 1:
        return [1 // p[0]]

    q = poly_recip(p[:k//2])
    r = poly_sub(poly_scale(poly_scalar_mul(2, q), 3*k//2-2),
                 poly_mul(poly_mul(q, q), p))

    return poly_scale(r, -k+2)


def poly_divmod(u, v):
    """Fast polynomial division ``u(x)`` / ``v(x)`` of polynomials with degrees
    m and n. Time complexity is ``O(n*log(n))`` if ``m`` is of the same order
    as ``n``.
    """
    if not u or not v:
        return []
    m = poly_deg(u)
    n = poly_deg(v)

    # ensure deg(v) is one less than some power of 2
    # by extending v -> ve, u -> ue (mult by x^nd)
    nd = int(2**ceil(log(n+1, 2))) - 1 - n
    ue = poly_scale(u, nd)
    ve = poly_scale(v, nd)
    me = m + nd
    ne = n + nd

    s = poly_recip(ve)
    q = poly_scale(poly_mul(ue, s), -2*ne)

    # handle the case when m>2n
    if me > 2*ne:
        # t = x^2n - s*v
        t = poly_sub(poly_scale([1], 2*ne), poly_mul(s, ve))
        q2, r2 = poly_divmod(poly_scale(poly_mul(ue, t), -2*ne), ve)
        q = poly_add(q, q2)

    # remainder, r = u - v*q
    r = poly_sub(u, poly_mul(v, q))

    return q, r

# fft division for fast polynomial division
# https://stackoverflow.com/questions/44770632/fft-division-for-fast-polynomial-division
# Not Tested yet

if __name__ == '__main__':
    # print(poly_divmod([1,0,-1], [1,-1]))
    # print(poly_divmod([3,-5,10,8], [1,2,-3]))
    # print(poly_divmod([1, -11, 0, -22, 1], [1, -3, 0, 1, 2]))
    # print(poly_divmod([1, -11, 0, -22, 1], [1, -3, 0, 1, 2, 20]))
    x = [1, 12, -4]
    y = [4, 0, 23]
    print(poly_mul(x, y))
    print(poly_divmod(x, y))