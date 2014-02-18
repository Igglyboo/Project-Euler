from time import clock


def timer(function):
    def wrapper(*args, **kwargs):
        start = clock()
        print(function(*args, **kwargs))
        print("Solution took: %f seconds." % (clock() - start))

    return wrapper


@timer
def find_answer():
    longest = max(recurring_cycle(1, i) for i in range(2, 1001))
    return [i for i in range(2, 1001) if recurring_cycle(1, i) == longest][0]


def recurring_cycle(n, d):
    for t in range(1, d):
        if 1 == 10 ** t % d:
            return t
    return 0


if __name__ == "__main__":
    find_answer()

