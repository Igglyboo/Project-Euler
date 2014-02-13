from time import clock


def timer(function):
    def wrapper(*args, **kwargs):
        start = clock()
        print(function(*args, **kwargs))
        print("Solution took: %f seconds." % (clock() - start))

    return wrapper


@timer
def find_answer():
    sum_of_squares = sum([i ** 2 for i in range(1, 101)])
    square_of_sums = sum([i for i in range(1, 101)]) ** 2
    return square_of_sums - sum_of_squares


if __name__ == "__main__":
    find_answer()

