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
    for exp in count():
        for i in range(10 ** exp, 10 ** (exp + 1) // 6 + 1):
            current = digits(i)
            if current == digits(i * 6):
                if current == digits(i * 5):
                    if current == digits(i * 4):
                        if current == digits(i * 3):
                            if current == digits(i * 2):
                                return i


def digits(n):
    return sorted([x for x in str(n)])


if __name__ == "__main__":
    find_answer()

