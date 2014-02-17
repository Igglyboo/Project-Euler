from time import clock


def timer(function):
    def wrapper(*args, **kwargs):
        start = clock()
        print(function(*args, **kwargs))
        print("Solution took: %f seconds." % (clock() - start))

    return wrapper


@timer
def find_answer():
    return sum([i for i in range(1000) if i % 3 == 0 or i % 5 == 0])


if __name__ == "__main__":
    find_answer()

