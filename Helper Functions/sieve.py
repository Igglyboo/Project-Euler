from math import sqrt

def sieve(upper_bound):
    # generate all primes < upperbound
    primes = list(range(2, upper_bound+1))
    primes[2::2] = [0] * ((len(primes) - 3) // 2 + 1)
    limit = sqrt(upper_bound)

    for p in primes:
        if p > limit:
            break
        elif p:
            for i in range(p * p - 2, upper_bound - 1, p + p):
                primes[i] = 0

    return [x for x in primes if x]
