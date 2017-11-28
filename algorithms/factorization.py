from .pollard import pollardRho, pollardP1

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
