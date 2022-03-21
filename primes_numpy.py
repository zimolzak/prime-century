"""Whole point is OEIS A038822.
https://oeis.org/A038822
Number of primes between 100n and 100n+99.
Look at the scatterplot graph. < 5 primes in a 100 digit range is pretty special.
The first w/ 0 primes occurs at 16718 (1671800  .. 1671899).
"""

import numpy as np
from tqdm import tqdm

EXPECTED = [25, 21, 16, 16, 17, 14, 16, 14, 15, 14, 16, 12]

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
    """Basically a printing function, very little math."""
    list_of_str = []
    count_list = primes_per_century(p)
    for century, count in enumerate(count_list):
        lower = century * 100
        upper = lower + 99
        if count <= max_primes:
            list_of_str.append("%i %i %i %s" % (century, lower, upper, count))
    return list_of_str


def primes_per_century(p):
    list_of_counts = []
    for century in tqdm(range(MAX_NUM // 100)):
        lower = century * 100
        upper = lower + 99
        count = np.sum(np.greater_equal(p, lower) * np.less_equal(p, upper))
        list_of_counts.append(count)
    return list_of_counts


if __name__ == '__main__':
    # print('\n'.join(sparse_centuries_primes(P, 100)))
    # print()

    ppc = primes_per_century(P)
    idx_new_century = np.nonzero(np.diff(P // 100))
    idx_new_century = np.hstack((-1, idx_new_century[0]))
    simple_diff = np.diff(idx_new_century)
    #                                         1st digit
    #                                 1 where switch
    #                     indices where switch
    #             diff in indices

    exp_reduce = np.add.reduceat(EXPECTED, [0,3, 4,7])[::2]
    ppc_reduce = np.add.reduceat(ppc, [0,3, 4,7])[::2]
    sd_reduce = np.add.reduceat(simple_diff, [0,3, 4,7])

    print("Expected")
    print(EXPECTED)
    print(exp_reduce)
    print()

    print("first way")
    print(ppc)
    print(ppc_reduce)
    print()

    print("third way (diff)")
    print(simple_diff)
    print(sd_reduce)
