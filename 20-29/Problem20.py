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
    return sum(map(int, str(factorial(100))))


if __name__ == "__main__":
    find_answer()

