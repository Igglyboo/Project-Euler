from time import clock
from math import sqrt
from itertools import count


def timer(function):
    def wrapper(*args, **kwargs):
        start = clock()
        print(function(*args, **kwargs))
        print("Solution took: %f seconds." % (clock() - start))

    return wrapper


@timer
def find_answer():
    consecutive = 0
    for i in count(647):
        if len(distinct_prime_factors(i)) == 4:
            consecutive += 1
        else:
            consecutive = 0

        if consecutive == 4:
            return i - 3


def distinct_prime_factors(n):
    factors = set()

    while n % 2 == 0:
        factors.add(2)
        n //= 2

    limit = sqrt(n + 1)
    i = 3
    while i <= limit:
        if n % i == 0:
            factors.add(i)
            n //= i
            limit = sqrt(n + i)
        else:
            i += 2
    if n != 1:
        factors.add(n)

    return factors

if __name__ == "__main__":
    find_answer()

