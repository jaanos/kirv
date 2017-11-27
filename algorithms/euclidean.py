def gcd(m, n):
    """
    Compute the greatest common divisor of m and n
    using the Euclidean algorithm.
    """
    assert m >= 0 and n >= 0
    while n != 0:
        m, n = n, m % n
    return m
