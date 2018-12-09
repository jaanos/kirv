from random import randrange
from .modular import jacobi
from .util import descend, xxrange

def solovayStrassen(n, a = None, trace = False, **kargs):
    """
    Perform the Solovay-Strassen primality testing algorithm.

    Returns True if n is determined to be composite.
    Returns False if n is not determined to be composite
    -- i.e., it is a probable prime.
    """
    assert n > 1
    if n <= 3:
        if trace:
            print("%d <= 3  => prime" % n)
        return False
    elif n % 2 == 0:
        if trace:
            print("%d > 3 even  => composite" % n)
        return True
    if a is None:
        a = randrange(2, n-1)
    x = jacobi(a, n, trace = descend(trace))
    if x == 0:
        if trace:
            print("(%d/n) = 0  => composite" % a)
        return True
    y = pow(a, (n-1)//2, n)
    res = x % n != y
    if trace:
        print("x = (%d/n) = %d" % (a, x))
        print("y = %d ^ ((n-1)/2) mod n = %d" % (a, y))
        if res:
            print("x !== y (mod n)  => composite")
        else:
            print("x == y (mod n)  => probable prime")
    return res

def millerRabin(n, a = None, trace = False, **kargs):
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
        print("n-1 = m * 2^k = %d * 2^%d" % (m, k))
    if a is None:
        a = randrange(2, n-1)
    b = pow(a, m, n)
    if trace:
        print("b = %d ^ m mod n = %d" % (a, b))
    if b % n == 1:
        if trace:
            print("b mod n = 1  => probable prime")
        return False
    for i in xxrange(k):
        if (b+1) % n == 0:
            if trace:
                print("b ^ (2^%d) == -1 (mod n)  => probable prime" % i)
            return False
        b = b*b % n
    if trace:
        print("for all i < %d: b ^ (2^i) !== -1 (mod n)  => composite" % k)
    return True
