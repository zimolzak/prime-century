"""Are there 100-number ranges that contain no prime numbers?

My original point was OEIS A038822, "Number of primes between 100n and 100n+99." https://oeis.org/A038822 . Look at
the scatterplot graph. < 5 primes in a 100 digit range is pretty special. Started out finding those, but then we got
faster, so we can find primefree.

For sequence of primes per century:
EXPECTED = np.array([25, 21, 16, 16, 17, 14, 16, 14, 15, 14, 16, 12, 15, 11, 17, 12, 15, 12, 12, 13, 14, 10])

Primefree centuries A181098:
16718, 26378, 31173, 39336, 46406, 46524, 51782, 55187, 58374, 58452, 60129, 60850

Single-prime A186393:
1559, 2683, 4133, 10048, 11400, 12727, 12800, 13572, 14223, 14443, 14514, 14680, 14913, 15536, 15619, 16538, 16557,
17334, 19043, 20452, 20465, 20522, 21162, 21663, 22440, 22832, 23055, 23144, 23214, 23460, 24833, 25139, 25278,
25980, 26207, 26257, 26702, 26747, 27536, 27878, 28448, 28671, 29180, 29873, 30212, 30232

Okay 15 and 16 are much rarer than 0!

OEIS for 16 (A186408) goes up to century 8995086259, meaning 8.99E11.
10 ** 10 takes 45 sec to find the primes.
Biggest 16-prime century my laptop likes is 37400476 meaning 3.7E9
4E9 is 16 seconds
"""

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
