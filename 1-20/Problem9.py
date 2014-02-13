from time import clock


def timer(function):
    def wrapper(*args, **kwargs):
        start = clock()
        print(function(*args, **kwargs))
        print("Solution took: %f seconds." % (clock() - start))

    return wrapper


@timer
def find_answer():
    for a in range(1, 332):
        for b in range(a + 1, 499):
            c = 1000 - a - b
            if (a ** 2 + b ** 2) == c ** 2:
                return a * b * c


if __name__ == "__main__":
    find_answer()

