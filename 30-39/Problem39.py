from time import clock


def timer(function):
    def wrapper(*args, **kwargs):
        start = clock()
        print(function(*args, **kwargs))
        print("Solution took: %f seconds." % (clock() - start))

    return wrapper


@timer
def find_answer():
    maximum = (0, 0)
    for p in range(1, 1001):
        current = 0
        for a in range(1, p // 3 + 1):
            if p * (p - 2 * a) % (2 * (p - a)) == 0:
                current += 1
        if current > maximum[0]:
            maximum = (current, p)

    return maximum[1]


if __name__ == "__main__":
    find_answer()

