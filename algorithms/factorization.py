from math import ceil, log
from random import randrange
from .euclidean import gcd

def pollardP1(n, B = None, trace = False, **kargs):
    """
    Perform the Pollard p-1 factoring algorithm.

    Returns a nontrivial factor of n is one is found,
    otherwise returns None.
    """
    assert n > 1
    if n == 2:
        return None
    if n % 2 == 0:
        return 2
    if B is None:
        B = 4*int(ceil(log(n, 2)))
        if trace:
            print("B = %d" % B)
    else:
        assert B > 1
    a = 2
    for i in range(2, B+1):
        a = pow(a, i, n)
        if trace:
            print("a%d = 2 ^ %d! mod n = %d" % (i, i, a))
        d = gcd(a-1, n)
        if trace:
            print("gcd(a%d-1, n) = %d" % (i, d))
        if 1 < d and d < n:
            return d
    return None

def pollardRho(n, f = None, a = None, x = None, trace = False, **kargs):
    """
    Perform the Pollard rho factoring algorithm.

    Returns a nontrivial factor of n is one is found,
    otherwise returns None.
    """
    assert n > 1
    if n == 2:
        return None
    if f is None:
        if a is None:
            a = randrange(1, n)
        f = lambda z: (z*z + a) % n
        if trace:
            print("f(z) = (z^2 + %d) mod n" % a)
    if x is None:
        x = randrange(1, n)
    y = f(x)
    p = gcd(abs(x-y), n)
    if trace:
        i = 0
        print("x = %d" % x)
        print("f(x) = %d" % y)
        print("gcd(x-f(x), n) = %d" % p)
    while p == 1:
        x = f(x)
        y = f(f(y))
        p = gcd(abs(x-y), n)
        if trace:
            i += 1
            print("f^%d(x) = %d" % (i, x))
            print("f^%d(x) = %d" % (2*i+1, y))
            print("gcd(f^%d(x)-f^%d(x), n) = %d" % (i, 2*i+1, p))
    if p != n:
        return p
    return None

def totalFactorization(n, methods = [pollardRho, pollardP1], **kargs):
    """
    Attempt to find a total factorization of n using the available methods.
    """
    assert n > 1
    factors = {}
    for f in methods:
        m = f(n, **kargs)
        if m is not None:
            f1 = totalFactorization(m, methods = methods, **kargs)
            f2 = totalFactorization(n//m, methods = methods, **kargs)
            for p, e in f2.items():
                if p in f1:
                    f1[p] += f2[p]
                else:
                    f1[p] = f2[p]
            return f1
    return {n: 1}

def factorizeByBase(n, base):
    """
    Find a factorization of n with factors from base,
    if one exists.
    """
    assert n > 0
    assert all(p > 0 for p in base)
    factors = [0 for i in base]
    for i, p in enumerate(base):
        while n % p == 0:
            n //= p
            factors[i] += 1
    if n != 1:
        return False
    return factors
