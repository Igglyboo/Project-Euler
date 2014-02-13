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
    for i in count(20, 20):
        for j in range(11, 21):
            if i % j != 0:
                break
        else:
            return i


if __name__ == "__main__":
    find_answer()

