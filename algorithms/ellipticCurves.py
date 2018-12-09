from .euclidean import inverse
from .util import xxrange

def points((a, b, p)):
    """
    Find all points on an elliptic curve y^2 = x^3 + ax + b
    over a field with p elements with characteristic greater than 3.
    """
    sqrt = {x: [] for x in xxrange(p)}
    sqrt[0].append(0)
    for x in xxrange(1, (p+1)//2):
        sqrt[x*x % p].append(x)
        sqrt[x*x % p].append(p-x)
    return [()] + sum([[(x, y) for y in sqrt[(x**3 + a*x + b) % p]]
                       for x in xxrange(p)], [])

def pointSum(P, Q, (a, b, p)):
    """
    Compute the sum of the points P and Q
    on an elliptic curve y^2 = x^3 + ax + b
    over a field with p elements with characteristic greater than 3.
    """
    if P == ():
        return Q
    elif Q == ():
        return P
    Px, Py = P
    Qx, Qy = Q
    if Px == Qx:
        if Py == Qy:
            lm = (3*Px*Px + a) * inverse(2*Py, p) % p
        else:
            return ()
    else:
        lm = (Qy-Py) * inverse(Qx-Px, p) % p
    x = (lm*lm - Px - Qx) % p
    y = (lm*(Px - x) - Py) % p
    return (x, y)

def pointMultiply(k, P, (a, b, p), trace = False):
    """
    Compute the multiple of the point P by the scalar k
    on an elliptic curve y^2 = x^3 + ax + b
    over a field with p elements with characteristic greater than 3.
    """
    if k == 0:
        return ()
    elif k < 0:
        k = -k
        x, y = P
        P = (x, p-y)
    Q = ()
    if trace:
        r, s = 0, 1
    while k > 0:
        if k % 2 == 1:
            Q = pointSum(P, Q, (a, b, p))
            if trace:
                r += s
                print("%dP = %s" % (r, Q))
        P = pointSum(P, P, (a, b, p))
        k //= 2
        if trace:
            s *= 2
            print("%dP = %s" % (s, P))
    return Q
