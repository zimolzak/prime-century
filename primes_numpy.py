"""Find 100-number ranges that contain atypically many/few primes."""

import numpy as np
from tqdm import tqdm
from timeit import default_timer

MAX_NUM = 4 * 10 ** 9


def primes_from_2_to(n):
    # https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """Input n>=6. Return an array of primes, 2 <= p < n."""
    sieve = np.ones(n // 3 + (n % 6 == 2), dtype=np.bool)
    sieve[0] = False
    for i in tqdm(range(int(n ** 0.5) // 3 + 1)):
        if sieve[i]:
            k = 3 * i + 1 | 1
            sieve[((k * k) // 3)::2 * k] = False
            sieve[(k * k + 4 * k - 2 * k * (i & 1)) // 3::2 * k] = False
    return np.r_[2, 3, ((3 * np.nonzero(sieve)[0] + 1) | 1)]


def pretty_print_primes(primes_per_century, k):
    array_of_centuries = np.flatnonzero(primes_per_century == k)
    if len(array_of_centuries) > 0:
        print("{}-prime centuries below {:,}:".format(k, MAX_NUM))
        print(array_of_centuries)
        print()


if __name__ == '__main__':
    print("Calculating primes. Do not be dismayed: speedup coming, first 2% about equal to last 98%.")
    p = primes_from_2_to(MAX_NUM)
    print()

    print("Calculating primes per century....")
    s = default_timer()
    primes_per_century = np.bincount(p // 100)
    e = default_timer()
    print("took %f sec" % (e - s))
    print()

    print("Displaying....")
    for i in range(15, 27):
        pretty_print_primes(primes_per_century, i)

    print("Histogram....")
    hist_values = np.bincount(primes_per_century)
    hist_bins = np.arange(0, len(hist_values))
    hist = np.transpose(np.vstack((hist_bins, hist_values)))
    print(hist)
