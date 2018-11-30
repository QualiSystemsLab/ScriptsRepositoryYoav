from joblib import Parallel, delayed
from math import sqrt

# what are your inputs, and what operation do you want to
# perform on each input. For example...
inputs = range(10)


def processInput(i):
    return i * i

results = Parallel(n_jobs=2)(delayed(sqrt)(i**2) for i in range(10))
pass