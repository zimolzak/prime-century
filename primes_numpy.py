"""Whole point is OEIS A038822.
https://oeis.org/A038822
Number of primes between 100n and 100n+99.
Look at the scatterplot graph. < 5 primes in a 100 digit range is pretty special.
The first w/ 0 primes occurs at 16718 (1671800  .. 1671899).
"""

import numpy as np
from tqdm import tqdm

#  MAX_NUM = 3 * 10 ** 6
n_rows = 4
n_sieve_elements = 100 * n_rows
MAX_NUM = 3 * n_sieve_elements


def sievefrom2to(n):
    # https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = np.ones(n // 3 + (n % 6 == 2), dtype=np.bool)
    sieve[0] = False
    for i in range(int(n ** 0.5) // 3 + 1):
        if sieve[i]:
            k = 3 * i + 1 | 1
            sieve[((k * k) // 3)::2 * k] = False
            sieve[(k * k + 4 * k - 2 * k * (i & 1)) // 3::2 * k] = False
    return sieve


def primesfrom2to(n):
    sieve = sievefrom2to(n)
    return np.r_[2, 3, ((3 * np.nonzero(sieve)[0] + 1) | 1)]


P = primesfrom2to(MAX_NUM)


def sparse_centuries_primes(p, max_primes=1):
    list_of_str = []
    for century in tqdm(range(MAX_NUM // 100)):
        lower = century * 100
        upper = lower + 99
        indices = np.greater(p, lower) * np.less(p, upper)
        count = len(p[indices])
        if count <= max_primes:
            list_of_str.append("%i %i %i %i" % (century, lower, upper, count))
    return list_of_str


s6 = sievefrom2to(MAX_NUM).reshape((-1, 100))  # 2 row * 100 col
indices = np.argwhere(s6)  # ary of [i,j] nonzero indices
unrolled_indices = indices

simple_diff = np.diff(np.nonzero(np.diff(P // 100)))
#                                         1st digit
#                                 1 where switch
#                     indices where switch
#             diff in indices

if __name__ == '__main__':
    print('\n'.join(sparse_centuries_primes(P, 100)))
    print(np.sum(np.equal(indices[:, 0], 0)), "from 0 .. 300?")
    print(np.sum(np.equal(indices[:, 0], 1)), "from 301 .. 600?")
    print(simple_diff)
