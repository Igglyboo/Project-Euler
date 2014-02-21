from time import clock
from sys import setrecursionlimit


def timer(function):
    def wrapper(*args, **kwargs):
        start = clock()
        print(function(*args, **kwargs))
        print("Solution took: %f seconds." % (clock() - start))

    return wrapper


@timer
def find_answer():
    setrecursionlimit(2000)
    return hyperexponentiate(1777, 1855, 100000000)


def hyperexponentiate(a, b, m):
    if b == 2:
        return pow(a, a, m)
    else:
        return pow(a, hyperexponentiate(a, b - 1, m), m)


if __name__ == "__main__":
    find_answer()

