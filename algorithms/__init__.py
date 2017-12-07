"""
Number-theoretic algorithms for use in cryptography.

The trace parameter appearing in various function
can take a boolean or integral argument,
with False and True being equivalent to 1 and 0, respectively.
It denotes the deepest level of nested function calls
for which a trace will be printed.
A negative integer means that traces should be printed at all levels.
Note that currently, no nested calls in levels deeper than 2 occur.
"""

from .euclidean import gcd, inverse, eea
from .modular import crt, jacobi
from .primality import solovayStrassen, millerRabin
from .factorization import pollardP1, pollardRho, totalFactorization, factorizeByBase
from .discreteLogarithm import babyStepGiantStep, pohligHellman

__all__ = ['gcd',
           'inverse',
           'eea',
           'crt',
           'jacobi',
           'solovayStrassen',
           'millerRabin',
           'pollardP1',
           'pollardRho',
           'totalFactorization',
           'factorizeByBase',
           'babyStepGiantStep',
           'pohligHellman',
          ]
