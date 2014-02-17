from time import clock


def timer(function):
    def wrapper(*args, **kwargs):
        start = clock()
        print(function(*args, **kwargs))
        print("Solution took: %f seconds." % (clock() - start))

    return wrapper


@timer
def find_answer():
    with open("names.txt") as f:
        names = [name[1:-1] for name in f.read().split(",")]

    names.sort()

    total = 0
    for index, name in enumerate(names):
        total += (index + 1) * sum(map(lambda x: ord(x) - 64, name))

    return total


if __name__ == "__main__":
    find_answer()

