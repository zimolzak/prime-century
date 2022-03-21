"""Whole point is OEIS A038822.
https://oeis.org/A038822
Number of primes between 100n and 100n+99.
Look at the scatterplot graph. < 5 primes in a 100 digit range is pretty special.
The first w/ 0 primes occurs at 16718 (1671800  .. 1671899).

FIXME - some kind of bug where it skips primefree centuries rather than counting them.
"""

import numpy as np

EXPECTED = np.array([25, 21, 16, 16, 17, 14, 16, 14, 15, 14, 16, 12, 15, 11, 17, 12, 15, 12, 12, 13, 14, 10])

MAX_NUM = 3 * 10 ** 6  # 100 * len(EXPECTED)


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


def sparse_centuries_primes(p, max_primes=1):
    """Basically a printing function, very little math."""
    list_of_str = []
    count_list = primes_per_century_vec(p)
    for century, count in enumerate(count_list):
        lower = century * 100
        upper = lower + 99
        if count <= max_primes:
            list_of_str.append("%i %i %i %s" % (century, lower, upper, count))
    return list_of_str


def primes_per_century_vec(p):
    idx_new_century = np.hstack((-1,
                                np.nonzero(np.diff(p // 100))[0],
                                #                  hundreds place
                                #          =1 where it switches to new century
                                # indices where it switches
                                 len(p) - 1))

    return np.diff(idx_new_century)


if __name__ == '__main__':
    # print('\n'.join(sparse_centuries_primes(P, 100)))
    # print()
    P = primesfrom2to(MAX_NUM)

    #simple_diff = primes_per_century_vec(P)
    #print(simple_diff)

    print('\n'.join(sparse_centuries_primes(P)))
