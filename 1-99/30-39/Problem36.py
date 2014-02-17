from time import clock


def timer(function):
    def wrapper(*args, **kwargs):
        start = clock()
        print(function(*args, **kwargs))
        print("Solution took: %f seconds." % (clock() - start))

    return wrapper


@timer
def find_answer():
    total = 0
    for i in range(1000000):
        if str(i) == str(i)[::-1]:
            if bin(i)[2:] == bin(i)[:1:-1]:
                total += i

    return total


if __name__ == "__main__":
    find_answer()

