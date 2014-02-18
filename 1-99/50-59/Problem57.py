from time import clock
from itertools import count
from math import sqrt


def timer(function):
    def wrapper(*args, **kwargs):
        start = clock()
        print(function(*args, **kwargs))
        print("Solution took: %f seconds." % (clock() - start))

    return wrapper


@timer
def find_answer():
    previous_max = 1
    corners = set([1])
    corner_primes = set()
    for level in count(2, 2):
        current_corners = set()
        for corner in range(1, 5):
            current = previous_max + level * corner
            current_corners.add(current)
            corners.add(current)
        for corner in current_corners:
            if is_prime(corner):
                corner_primes.add(corner)
        if len(corner_primes) / len(corners) < 0.1:
            return level + 1
        previous_max += 4 * level


def is_prime(n):
    if n % 2 == 0:
        return False
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False

    return True


if __name__ == "__main__":
    find_answer()

