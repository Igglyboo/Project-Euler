from time import clock
from math import sqrt


def timer(function):
    def wrapper(*args, **kwargs):
        start = clock()
        print(function(*args, **kwargs))
        print("Solution took: %f seconds." % (clock() - start))

    return wrapper


@timer
def find_answer():
    total = 0
    for i in range(2, 10000):
        n = sum_of_divisors(i)
        m = sum_of_divisors(n)
        if i == m and i != n:
            total += i
    return total


def sum_of_divisors(n):
    div_sum = 1
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            div_sum += i
            if n // i != i:
                div_sum += n // i
    return div_sum


if __name__ == "__main__":
    find_answer()

