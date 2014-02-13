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
    abundants = []
    for i in range(2, 28123):
        if is_abundant(i):
            abundants.append(i)

    sums = set()
    for a_index, a in enumerate(abundants):
        for b in abundants[a_index:]:
            if a + b > 28123:
                break
            else:
                sums.add(a + b)

    total = 0
    for i in range(1, 28123):
        if i not in sums:
            total += i

    return total


def is_abundant(n):
    div_sum = 1
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            div_sum += i
            if n // i != i:
                div_sum += n // i
    return n < div_sum


if __name__ == "__main__":
    find_answer()

