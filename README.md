# Are there 100-number ranges that contain no prime numbers?

TLDR: Yes, lots. But here are some rarer finds: 3,740,047,600 has 16
primes (surprisingly many) following it in the next 100 integers. And
2,704,900 has 17 following.

## Details

My original point was to re-create OEIS A038822, "Number of primes
between 100n and 100n+99." https://oeis.org/A038822 . Look at the
scatterplot graph. Less than 5 primes in a 100 digit range is pretty
special. Started out finding those, but then we got faster, so we can
find primefree. And even find 15-, 16-, and 17-prime centuries!

For sequence of primes per century:

`EXPECTED = np.array([25, 21, 16, 16, 17, 14, 16, 14, 15, 14, 16, 12, 15, 11, 17, 12, 15, 12, 12, 13, 14, 10])`

Primefree centuries A181098: 16718, 26378, 31173, 39336, 46406, 46524,
51782, 55187, 58374, 58452, 60129, 60850

Single-prime centuries A186393: 1559, 2683, 4133, 10048, 11400, 12727, 12800,
13572, 14223, 14443, 14514, 14680, 14913, 15536, 15619, 16538, 16557,
17334, 19043, 20452, 20465, 20522, 21162, 21663, 22440, 22832, 23055,
23144, 23214, 23460, 24833, 25139, 25278, 25980, 26207, 26257, 26702,
26747, 27536, 27878, 28448, 28671, 29180, 29873, 30212, 30232

Okay, so 15 and 16 are much rarer than 0! OEIS for 16 (A186408) goes
up to century 8995086259, meaning 8.99E11.

10 ** 10 takes 45 sec to find the primes. The biggest 16-prime century
my laptop handles okay with tqdm is 37400476, meaning 3.7E9. So I set
max to 4E9, which takes about 16 seconds.
