from time import clock
from math import factorial


def timer(function):
    def wrapper(*args, **kwargs):
        start = clock()
        print(function(*args, **kwargs))
        print("Solution took: %f seconds." % (clock() - start))

    return wrapper


@timer
def find_answer():
    total = 0
    for n in range(1, 101):
        for r in range(1, n + 1):
            if combinations(n, r) > 1000000:
                total += 1

    return total


def combinations(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))


if __name__ == "__main__":
    find_answer()

