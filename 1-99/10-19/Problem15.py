from time import clock


def timer(function):
    def wrapper(*args, **kwargs):
        start = clock()
        print(function(*args, **kwargs))
        print("Solution took: %f seconds." % (clock() - start))

    return wrapper


@timer
def find_answer():
    # Combinatorics Approach (2n choose n)
    paths = 1
    for i in range(20):
        paths *= 2 * 20 - i
        paths //= i + 1

    return paths


if __name__ == "__main__":
    find_answer()

