def gcd(m, n):
    """
    Compute the greatest common divisor of m and n
    using the Euclidean algorithm.
    """
    assert m >= 0 and n >= 0
    while n != 0:
        m, n = n, m % n
    return m

def inverse(a, n, strict = True):
    """
    Compute the inverse of a modulo n using the Extended Euclidean algorithm.

    If strict is True (default), raises an error if a is not invertible.
    Otherwise, a number b is output such that a*b % n == gcd(a, b).
    """
    b, x, y = n, 0, 1
    while a != 0:
        k = b // a
        b, a, x, y = a, b - k*a, y, x - k*y
    if strict and b != 1:
        raise ValueError("input not invertible")
    return x % n

def eea(m, n):
    """
    Compute numbers a, b such that a*m + b*n = gcd(m, n)
    using the Extended Euclidean algorithm.
    """
    p, q, r, s = 1, 0, 0, 1
    while n != 0:
        k = m // n
        m, n, p, q, r, s = n, m - k*n, q, p - k*q, s, r - k*s
    return (p, r)
