# Cryptography and Computer Security

This repository contains materials for the Cryptography and Computer Security course at the Faculty of Computer Science and Informatics, University of Ljubljana.

## [Notes from tutorials](notes)

* Online tutorials from [2020/21](notes/2020-21)

## Notebooks

Currently, the following Jupyter [notebooks](notebooks/) for Python/Sage are available:
* [![Launch in Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/jaanos/kirv/master?filepath=notebooks/VigenereCipher.ipynb) [`VigenereCipher.ipynb`](https://nbviewer.jupyter.org/github/jaanos/kirv/blob/master/notebooks/VigenereCipher.ipynb): Vigenère cipher in Python
* [![Launch in Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/jaanos/kirv/master?filepath=notebooks/LFSR.ipynb) [`LFSR.ipynb`](https://nbviewer.jupyter.org/github/jaanos/kirv/blob/master/notebooks/LFSR.ipynb): LFSR in Sage
* [![Launch in Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/jaanos/kirv/master?filepath=notebooks/Coppersmith.ipynb) [`Coppersmith.ipynb`](https://nbviewer.jupyter.org/github/jaanos/kirv/blob/master/notebooks/Coppersmith.ipynb): Coppersmith's attack on a small exponent
* [![Launch in Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/jaanos/kirv/master?filepath=notebooks/CommonModulus.ipynb) [`CommonModulus.ipynb`](https://nbviewer.jupyter.org/github/jaanos/kirv/blob/master/notebooks/CommonModulus.ipynb): Common modulus attack
* [![Launch in Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/jaanos/kirv/master?filepath=notebooks/RSA-ECB.ipynb) [`RSA-ECB.ipynb`](https://nbviewer.jupyter.org/github/jaanos/kirv/blob/master/notebooks/RSA-ECB.ipynb): RSA in ECB mode
* [![Launch in Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/jaanos/kirv/master?filepath=notebooks/Jacobi.ipynb) [`Jacobi.ipynb`](https://nbviewer.jupyter.org/github/jaanos/kirv/blob/master/notebooks/Jacobi.ipynb): Computing Jacobi symbols
* [![Launch in Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/jaanos/kirv/master?filepath=notebooks/Factorization.ipynb) [`Factorization.ipynb`](https://nbviewer.jupyter.org/github/jaanos/kirv/blob/master/notebooks/Factorization.ipynb): Integer factorization
* [![Launch in Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/jaanos/kirv/master?filepath=notebooks/BabyStepGiantStep.ipynb) [`BabyStepGiantStep.ipynb`](https://nbviewer.jupyter.org/github/jaanos/kirv/blob/master/notebooks/BabyStepGiantStep.ipynb): Shanks's baby-step/giant-step algorithm
* [![Launch in Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/jaanos/kirv/master?filepath=notebooks/PohligHellman.ipynb) [`PohligHellman.ipynb`](https://nbviewer.jupyter.org/github/jaanos/kirv/blob/master/notebooks/PohligHellman.ipynb): The Pohlig-Hellman algorithm
* [![Launch in Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/jaanos/kirv/master?filepath=notebooks/IndexCalculus.ipynb) [`IndexCalculus.ipynb`](https://nbviewer.jupyter.org/github/jaanos/kirv/blob/master/notebooks/IndexCalculus.ipynb): The Index calculus algorithm
* [![Launch in Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/jaanos/kirv/master?filepath=notebooks/ReblockingProblem.ipynb) [`ReblockingProblem.ipynb`](https://nbviewer.jupyter.org/github/jaanos/kirv/blob/master/notebooks/ReblockingProblem.ipynb): The reblocking problem for RSA
* [![Launch in Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/jaanos/kirv/master?filepath=notebooks/GroupSignature.ipynb) [`GroupSignature.ipynb`](https://nbviewer.jupyter.org/github/jaanos/kirv/blob/master/notebooks/GroupSignature.ipynb): The ACJT2000 group signature scheme

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
* `logarithmTable` (from `discreteLogarithm.py`)
* `indexCalculus` (from `discreteLogarithm.py`)
* `points` (from `ellipticCurves.py`)
* `pointSum` (from `ellipticCurves.py`)
* `pointMultiply` (from `ellipticCurves.py`)

See sources for the documentation.

Note that `logarithmTable` requires Sage and will therefore not work with plain Python. `indexCalculus` calls `logarithmTable` if a table of logarithms is not specified. If it is given, the function can be used with plain Python.
