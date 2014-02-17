from time import clock


def timer(function):
    def wrapper(*args, **kwargs):
        start = clock()
        print(function(*args, **kwargs))
        print("Solution took: %f seconds." % (clock() - start))

    return wrapper


@timer
def find_answer():
    terms = set()
    for a in range(2, 101):
        for b in range(2, 101):
            terms.add(a ** b)

    return len(terms)


if __name__ == "__main__":
    find_answer()

