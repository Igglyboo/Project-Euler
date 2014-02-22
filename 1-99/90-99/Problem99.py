from time import clock
from math import log


def timer(function):
    def wrapper(*args, **kwargs):
        start = clock()
        print(function(*args, **kwargs))
        print("Solution took: %f seconds." % (clock() - start))

    return wrapper


@timer
def find_answer():
    maximum = (0, 0)
    with open("base_exp.txt") as f:
        for line_num, line in enumerate(f):
            current = [int(x) for x in line.rstrip().split(",")]
            value = current[1] * log(current[0])
            print(value)
            if value > maximum[0]:
                maximum = value, line_num + 1

    return maximum[1]


if __name__ == "__main__":
    find_answer()

