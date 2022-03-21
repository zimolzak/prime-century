import numpy as np
from tqdm import tqdm

MAX_NUM = 3 * 10 ** 6


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


def sparse_centuries_primes(p):
    list_of_str = []
    for century in tqdm(range(MAX_NUM // 100)):
        lower = century * 100
        upper = lower + 99
        indices = np.greater(p, lower) * np.less(p, upper)
        count = len(p[indices])
        if count < 2:
            list_of_str.append("%i %i %i %i" % (century, lower, upper, count))
    return list_of_str


if __name__ == '__main__':
    # print('\n'.join(sparse_centuries_primes(P)))
    for i, x in enumerate(sievefrom2to(30)):
        print(i, i + 1, i + 2, i + 3, i + 4, x)
