"""Whole point is OEIS A038822.
https://oeis.org/A038822
Number of primes between 100n and 100n+99.
Look at the scatterplot graph. < 5 primes in a 100 digit range is pretty special.
Expect the first primefree century occurs at 16718 (1671800  .. 1671899).

For sequence of primes per century:
EXPECTED = np.array([25, 21, 16, 16, 17, 14, 16, 14, 15, 14, 16, 12, 15, 11, 17, 12, 15, 12, 12, 13, 14, 10])
"""

import numpy as np
MAX_NUM = 6100000


def primesfrom2to(n):
    # https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = np.ones(n // 3 + (n % 6 == 2), dtype=np.bool)
    sieve[0] = False
    for i in range(int(n ** 0.5) // 3 + 1):
        if sieve[i]:
            k = 3 * i + 1 | 1
            sieve[((k * k) // 3)::2 * k] = False
            sieve[(k * k + 4 * k - 2 * k * (i & 1)) // 3::2 * k] = False
    return np.r_[2, 3, ((3 * np.nonzero(sieve)[0] + 1) | 1)]


if __name__ == '__main__':
    p = primesfrom2to(MAX_NUM)
    primes_per_century = np.bincount(p // 100)

    print("Primefree centuries below {:,}:".format(MAX_NUM))
    print(np.flatnonzero(primes_per_century == 0))
    print()

    print("Single-prime centuries below {:,}:".format(MAX_NUM))
    print(np.flatnonzero(primes_per_century == 1))
