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
    for i in range(10, 400000):
        current = [int(x) for x in str(i)]
        if i == sum(map(factorial, current)):
            total += i

    return total


if __name__ == "__main__":
    find_answer()

