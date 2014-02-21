from time import clock
from math import sqrt
#19340598

def timer(function):
    def wrapper(*args, **kwargs):
        start = clock()
        print(function(*args, **kwargs))
        print("Solution took: %f seconds." % (clock() - start))

    return wrapper


@timer
def find_answer():
    total = 0
    maximum = 10 ** 8
    primes = sieve(maximum // 2)
    primes_set = set(primes)
    composites = composite_sieve(maximum)
    for i in composites:
        for prime in primes:
            if i % prime == 0:
                if i / prime in primes_set:
                    total += 1
                break

    return total


def sieve(upper_bound):
    primes = list(range(2, upper_bound + 1))
    primes[2::2] = [0] * ((len(primes) - 3) // 2 + 1)
    limit = sqrt(upper_bound)

    for p in primes:
        if p > limit:
            break
        elif p:
            for i in range(p * p - 2, upper_bound - 1, p + p):
                primes[i] = 0

    return [x for x in primes if x]


def composite_sieve(upper_bound):
    primes = list(range(2, upper_bound + 1))
    primes[2::2] = [0] * ((len(primes) - 3) // 2 + 1)
    limit = sqrt(upper_bound)

    for p in primes:
        if p > limit:
            break
        elif p:
            for i in range(p * p - 2, upper_bound - 1, p + p):
                primes[i] = 0

    return (i + 2 for i, x in enumerate(primes) if not x)


if __name__ == "__main__":
    find_answer()

