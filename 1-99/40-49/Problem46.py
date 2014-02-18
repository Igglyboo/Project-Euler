from time import clock
from itertools import count


def timer(function):
    def wrapper(*args, **kwargs):
        start = clock()
        print(function(*args, **kwargs))
        print("Solution took: %f seconds." % (clock() - start))

    return wrapper


@timer
def find_answer():
    primes = sieve(10000)
    primes = [x for x in primes if x]
    for odd_composite in range(35, 10000, 2):
        if odd_composite not in primes:
            if not calc_sum(odd_composite, primes):
                return odd_composite


def calc_sum(n, primes):
    for prime in primes:
        if prime > n - 2:
            break
        for square in count(1):
            total = prime + 2 * square ** 2
            if n == total:
                return True
            elif n < total:
                break
    return False


def sieve(upperlimit):
    l = [2] + [x if x % 2 != 0 else 0 for x in range(3, upperlimit + 1)]

    for p in l:
        if p ** 2 > upperlimit:
            break
        elif p:
            for i in range(p * p, upperlimit + 1, 2 * p):
                l[i - 2] = 0

    return l


if __name__ == "__main__":
    find_answer()

