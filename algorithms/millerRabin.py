from random import randrange

def millerRabin(n, a = None, trace = False):
    """
    Perform the Miller-Rabin primality testing algorithm.

    Returns True if n is determined to be composite.
    Returns False if n is not determined to be composite
    -- i.e., it is a probable prime.
    """
    assert n > 1
    m = n-1
    k = 0
    while m % 2 == 0:
        m //= 2
        k += 1
    if trace:
        print("n = m * 2^k = %d * 2^%d" % (m, k))
    if a is None:
        a = randrange(2, n)
    b = pow(a, m, n)
    if trace:
        print("b = %d ^ m mod n = %d" % (a, b))
    if b % n == 1:
        if trace:
            print("b mod n = 1  => probable prime")
        return False
    for i in range(k):
        if (b+1) % n == 0:
            if trace:
                print("b ^ (2^%d) == -1 (mod n)  => probable prime" % i)
            return False
        b = b*b % n
    if trace:
        print("for all i < %d: b ^ (2^i) !== -1 (mod n)  => composite" % k)
    return True
