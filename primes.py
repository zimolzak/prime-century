import math
primes = [2]
MAX_NUM = 100000

for i in range(3, MAX_NUM):
    foundFactor = False
    for j in primes: #range(2, int(math.sqrt(i))):
        if i / j == i // j:
            foundFactor = True
            break
    if not foundFactor:
        primes.append(i)

for century in range(MAX_NUM // 100):
    lower = century * 100
    upper = lower + 99
    count = 0
    plist = []
    for p in primes:
        if lower <= p <= upper:
            count += 1
            plist.append(p)
    if count < 6:
        print("%i (%i..%i) %i" % (century, lower, upper, count))

print()

