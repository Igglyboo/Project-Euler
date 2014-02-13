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
    factors = [i for i in range(3, int(sqrt(600851475143)) + 1, 2) if 600851475143 % i == 0]
    return max([i for i in factors if is_prime(i)])


def is_prime(n):
    if n % 2 == 0:
        return False
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False

    return True


if __name__ == "__main__":
    find_answer()

