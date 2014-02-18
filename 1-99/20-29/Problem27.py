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
    primes = sieve(1000000)
    primes.remove(0)
    poly = lambda x, y, z: z ** 2 + x * z + y
    maximum = 0
    for a in range(-1000, 1001):
        for b in range(-1000, 1001):
            for n in count(0):
                if poly(a, b, n) not in primes:
                    if n > maximum:
                        product = a * b
                        maximum = n
                    break

    return product


def sieve(upperlimit):
    l = list(range(2, upperlimit + 1))

    # Do p = 2 first so we can change step size to 2*p below
    for i in range(4, upperlimit + 1, 2):
        l[i - 2] = 0

    for p in l:
        if p ** 2 > upperlimit:
            break
        elif p:
            for i in range(p * p, upperlimit + 1, 2 * p):
                l[i - 2] = 0

    return set(l)


if __name__ == "__main__":
    find_answer()

