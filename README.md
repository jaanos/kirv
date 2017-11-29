# Cryptography and computer security

This repository contains materials for the Cryptography and computer security course at the Faculty of Computer Science and Informatics, University of Ljubljana.

## `algorithms`

To use the algorithms in Python, make sure that the root of the repository is visible to Python. Then you may import them with
```python
import algorithms
```
or
```python
from algorithms import *
```
Currently, the following functions are available:
* `gcd` (from `euclidean.py`)
* `inverse` (from `euclidean.py`)
* `eea` (from `euclidean.py`)
* `crt` (from `modular.py`)
* `jacobi` (from `modular.py`)
* `solovayStrassen` (from `primality.py`)
* `millerRabin` (from `primality.py`)
* `pollardP1`(from `factorization.py`)
* `pollardRho`(from `factorization.py`)
* `totalFactorization` (from `factorization.py`)
* `factorizeByBase` (from `factorization.py`)
* `babyStepGiantStep` (from `discreteLogarithm.py`)
* `pohligHellman` (from `discreteLogarithm.py`)

See sources for the documentation.
