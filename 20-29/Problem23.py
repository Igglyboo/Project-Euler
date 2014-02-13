from time import clock
from itertools import permutations


def timer(function):
    def wrapper(*args, **kwargs):
        start = clock()
        print(function(*args, **kwargs))
        print("Solution took: %f seconds." % (clock() - start))

    return wrapper


@timer
def find_answer():
    for index, permutation in enumerate(permutations("0123456789")):
        if index == 999999:
            return int("".join(permutation))


if __name__ == "__main__":
    find_answer()

