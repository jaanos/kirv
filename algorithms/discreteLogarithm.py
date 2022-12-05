from math import sqrt, ceil
from random import randint
from .euclidean import gcd, inverse
from .modular import crt
from .factorization import totalFactorization, factorizeByBase
from .util import descend, xxrange

def babyStepGiantStep(a, b, n, order = None, trace = False):
    """
    Perform Shanks's Baby step-Giant step algorithm
    to find the discrete logarithm of b with base a modulo n.

    If order is given, it is assumed to be the order of a.
    Otherwise, n-1 is used as an upper limit of the order.
    """
    if order is None:
        order = n - 1
    m = int(ceil(sqrt(order)))
    if trace:
        print("m = %d" % m)
    am = pow(a, m, n)
    gs = {1: 0}
    ap = 1
    for i in xxrange(1, m):
        ap = ap * am % n
        gs[ap] = i
        if trace:
            print("a^(%d*%d) = %d" % (i, m, ap))
    bp = b
    ai = inverse(int(a), n)
    for j in xxrange(m):
        if trace:
            print("b*a^-%d = %d" % (j, bp))
        if bp in gs:
            return m * gs[bp] + j
        bp = bp * ai % n

def pohligHellman(a, b, p, trace = False):
    """
    Perform the Pohlig-Hellman algorithm
    to find the discrete logarithm of b with base a modulo a prime p.
    """
    dtrace = descend(trace)
    n = p - 1
    f = totalFactorization(n, trace = dtrace)
    ai = inverse(a, p)
    if trace:
        print("%d-1 = %s" % (p, ' * '.join("%d^%d" % (q, e)
                                           for q, e in f.items())))
        print("a^-1 = %d" % ai)
    v = {}
    for q, e in f.items():
        if trace:
            print("prime power factor: %d^%d" % (q, e))
        nq = n // q
        ap = pow(a, nq, p)
        if trace:
            print("a^(%d/%d) = %d" % (n, q, ap))
        bp, qp = b, 1
        c, k, x = 1, 0, 0
        for i in xxrange(e):
            c = c * pow(ai, k, p) % p
            bp = pow(b*c, nq, p)
            if trace:
                print("c_%d = c_%d * a^-k_%d = %d" % (i, i-1, i-1, c))
                print("b_%d = (b_%d*c_%d)^(%d/%d^%d) = %d" %
                                                    (i, i-1, i, n, q, i+1, bp))
                print("z = log_%d(%d) mod %d, order = %d" % (ap, bp, p, q))
            k = (babyStepGiantStep(ap, bp, p, order = q,
                                   trace = dtrace) % q) * qp
            x += k
            if trace:
                print("k_%d = z*q^%d = %d" % (i, i, k))
            qp *= q
            nq //= q
        v[qp] = x
    if trace:
        print("CRT")
        for q, r in v.items():
            print("x = %d\t(mod %d)" % (r, q))
    return crt(v)

def logarithmTable(a, p, base, trace = False):
    """
    Compute the tables of logarithms with base a modulo a prime p
    for the given factor base, as needed by the Index calculus algorithm.

    Requires Sage to run.
    """
    from sage.matrix.constructor import Matrix
    from sage.rings.finite_rings.integer_mod_ring import Integers
    v = []
    s = set()
    r, l = 0, len(base)
    M = Matrix(nrows=0, ncols=l)
    fields = [Integers(q) for q in totalFactorization(p-1, trace = descend(trace))]
    while r < l:
        i = randint(1, p-1)
        if i in s:
            continue
        s.add(i)
        x = pow(a, i, p)
        f = factorizeByBase(int(x), base, p)
        if not f:
            continue
        if trace:
            print("found factorization %d^%d = %s (mod %d)" % (a, i,
                  ' * '.join("%d^%d" % (q, e) for q, e in zip(base, f) if e != 0), p))
        MM = Matrix(list(M) + [f])
        if all(Matrix(F, MM).rank() > r for F in fields):
            M = MM
            r += 1
            v.append(i)
        elif trace:
            print("rank not increased, discarding")
    return [e for e, in M**-1 * Matrix(zip(v)) % (p-1)]

def indexCalculus(a, b, p, base, table = None, trace = False):
    """
    Perform the Index calculus algorithm
    to find the discrete logarithm of b with base a modulo a prime p
    given the table of logarithms for the given factor base.
    """
    if table is None:
        if isinstance(base, dict):
            base, table = zip(*base.items())
        else:
            table = logarithmTable(a, p, base, trace = descend(trace))
    while True:
        i = randint(1, p-1)
        x = pow(b, i, p)
        f = factorizeByBase(int(x), base, p)
        if f is not False:
            break
    g = gcd(i, p-1)
    m = (p-1) // g
    x = sum(u*v for u, v in zip(f, table)) * inverse(i, m) % m
    if trace:
        print("found factorization %d^%d = %s (mod %d)" % (b, i,
                  ' * '.join("%d^%d" % (q, e) for q, e in zip(base, f) if e != 0), p))
        print("checking %d solutions for %d^x = %d, x = %d (mod %d)" % (g, a, b, x, m))
    for j in xxrange(g):
        y = pow(a, x, p)
        if trace:
            print("%d^%d mod %d = %d" % (a, x, p, y))
        if y == b:
            return x
        x += m
    return False
