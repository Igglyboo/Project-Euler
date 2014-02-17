from time import clock


def timer(function):
    def wrapper(*args, **kwargs):
        start = clock()
        print(function(*args, **kwargs))
        print("Solution took: %f seconds." % (clock() - start))

    return wrapper


@timer
def find_answer():
    total = 1
    previous_max = 1
    size = 1001
    for level in range(2, size, 2):
        total += (4 * previous_max) + (10 * level)
        previous_max += 4 * level

    return total


if __name__ == "__main__":
    find_answer()

