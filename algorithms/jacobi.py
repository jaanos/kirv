from random import randrange

def jacobi(m, n, trace = False):
    """
    Compute the Jacobi symbol (m/n), where n is an odd integer.
    """
    assert n > 0 and n % 2 == 1
    x = 1
    while True:
        m = m % n
        if trace:
            print(m, n, x)
        if m == 0:
            return 0
        y = -1 if n % 8 in [3, 5] else 1
        if trace:
            print("\t%d mod 8 = %d" % (n, n % 8))
        while m % 2 == 0:
            m //= 2
            x *= y
            if trace:
                print(m, n, x)
        if m == 1:
            return x
        if trace:
            print("\t%d mod 4 = %d" % (m, m % 4))
            print("\t%d mod 4 = %d" % (n, n % 4))
        if m % 4 == 3 and n % 4 == 3:
            x = -x
        m, n = n, m
        if trace:
            print(m, n, x)
