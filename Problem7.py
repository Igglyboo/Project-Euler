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
    n = 1
    for i in count(3, 2):
        n += is_prime(i)
        if n == 10001:
            return i


def is_prime(n):
    if n % 2 == 0:
        return False
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False

    return True


if __name__ == "__main__":
    find_answer()

