from math import sqrt, ceil
from .euclidean import inverse
from .modular import crt
from .factorization import totalFactorization

def babyStepGiantStep(a, b, n, order = None, trace = False):
    """
    Perform Shank's Baby step-Giant step algorithm
    to find the discrete logarithm of b with basis a modulo n.

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
    for i in range(1, m):
        ap = ap * am % n
        gs[ap] = i
        if trace:
            print("a^(%d*%d) = %d" % (i, m, ap))
    bp = b
    ai = inverse(a, n)
    for j in range(m):
        if trace:
            print("b*a^-%d = %d" % (j, bp))
        if bp in gs:
            return m * gs[bp] + j
        bp = bp * ai % n

def pohligHellman(a, b, p, trace = False):
    """
    Perform the Pohlig-Hellman algorithm
    to find the discrete logarithm of b with basis a modulo a prime p.
    """
    n = p - 1
    f = totalFactorization(n)
    ai = inverse(a, p)
    if trace:
        print("%d-1 = %s" % (p, ' * '.join("%d^%d" % (q, e)
                                           for q, e in f.items())))
        print("a^-1 = %d" % ai)
    v, m = [], []
    for q, e in f.items():
        if trace:
            print("prime power factor: %d^%d" % (q, e))
        nq = n // q
        ap = pow(a, nq, p)
        if trace:
            print("a^(%d/%d) = %d" % (n, q, ap))
        bp, qp = b, 1
        c, k, x = 1, 0, 0
        for i in range(e):
            c = c * pow(ai, k, p) % p
            bp = pow(b*c, nq, p)
            if trace:
                print("c_%d = c_%d * a^-k_%d = %d" % (i, i-1, i-1, c))
                print("b_%d = (b_%d*c_%d)^(%d/%d^%d) = %d" %
                                                    (i, i-1, i, n, q, i+1, bp))
                print("z = log_%d(%d) mod %d, order = %d" % (ap, bp, p, q))
            k = (babyStepGiantStep(ap, bp, p, order = q) % q) * qp
            x += k
            if trace:
                print("k_%d = z*q^%d = %d" % (i, i, k))
            qp *= q
            nq //= q
        v.append(x)
        m.append(qp)
    if trace:
        print("CRT")
        for q, r in zip(m, v):
            print("x = %d\t(mod %d)" % (r, q))
    return crt(dict(zip(m, v)))
