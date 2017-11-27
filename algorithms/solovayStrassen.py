from random import randrange
from jacobi import jacobi

def solovayStrassen(n, a = None, trace = False):
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
    x = jacobi(a, n)
    if x == 0:
        if trace:
            print("(%d/n) = 0  => composite" % a)
        return True
    y = pow(a, (n-1)/2, n)
    res = x % n != y
    if trace:
        print("x = (%d/n) = %d" % (a, x))
        print("y = %d ^ ((n-1)/2) mod n = %d" % (a, y))
        if res:
            print("x !== y (mod n)  => composite")
        else:
            print("x == y (mod n)  => probable prime")
    return res
