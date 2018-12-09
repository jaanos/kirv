from operator import gt, lt

def descend(trace):
    """
    Return reduced trace level.
    """
    return trace and (trace-1)

try:
    xrange
    def xxrange(start, stop=None, step=1):
        """
        Return a range iterator without overflow.
        """
        if stop is None:
            stop = start
            start = 0
        try:
            return xrange(start, stop, step)
        except OverflowError:
            assert step != 0
            op = lt if step > 0 else gt
            def xxr():
                x = start
                while op(x, stop):
                    yield x
                    x += step
            return xxr()
except NameError:
    xxrange = range
