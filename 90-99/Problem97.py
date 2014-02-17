from time import clock


def timer(function):
    def wrapper(*args, **kwargs):
        start = clock()
        print(function(*args, **kwargs))
        print("Solution took: %f seconds." % (clock() - start))

    return wrapper


@timer
def find_answer():
    return (28433 * pow(2, 7830457, 10000000000) + 1) % 10000000000


if __name__ == "__main__":
    find_answer()

