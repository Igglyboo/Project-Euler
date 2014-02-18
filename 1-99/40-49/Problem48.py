from time import clock


def timer(function):
    def wrapper(*args, **kwargs):
        start = clock()
        print(function(*args, **kwargs))
        print("Solution took: %f seconds." % (clock() - start))

    return wrapper


@timer
def find_answer():
    total = 0
    for i in range(1, 1000):
        total += i ** i
    return total % 10000000000


if __name__ == "__main__":
    find_answer()

