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
    for i in triangle_generator():
        if number_of_divisors(i) > 500:
            return i


def number_of_divisors(n):
    num = 0
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            num += 2
    return num


def triangle_generator():
    tri = 0
    for i in count(1):
        tri = tri + i
        yield tri


if __name__ == "__main__":
    find_answer()

