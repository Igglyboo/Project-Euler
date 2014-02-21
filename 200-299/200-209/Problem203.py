from time import clock
from math import sqrt


def timer(function):
    def wrapper(*args, **kwargs):
        start = clock()
        print(function(*args, **kwargs))
        print("Solution took: %f seconds." % (clock() - start))

    return wrapper


@timer
def find_answer():
    distinct = set()
    previous = [1, 1]
    for levels in range(49):
        current = [1] + [0] * (len(previous) - 1) + [1]
        for index in range(1, len(previous)):
            current[index] = previous[index - 1] + previous[index]
        distinct |= set(current)
        previous = current

    primes = sieve(int(sqrt(max(distinct))) + 1)
    total = 0
    for i in distinct:
        for prime in primes:
            if i % prime ** 2 == 0:
                break
            if i < prime ** 2:
                total += i
                break
        else:
            total += i

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


if __name__ == "__main__":
    find_answer()

