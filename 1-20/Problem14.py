from time import clock

collatz_cache = {1: 1}


def timer(function):
    def wrapper(*args, **kwargs):
        start = clock()
        print(function(*args, **kwargs))
        print("Solution took: %f seconds." % (clock() - start))

    return wrapper


@timer
def find_answer():
    maximum = (0, 0)
    for i in range(1, 1000000):
        length = collatz_length(i)
        collatz_cache[i] = length
        if length > maximum[0]:
            maximum = length, i

    return maximum[1]


def collatz_length(n):
    if n in collatz_cache:
        return collatz_cache[n]
    elif n % 2 == 0:
        return 1 + collatz_length(n / 2)
    else:
        return 1 + collatz_length(3 * n + 1)


if __name__ == "__main__":
    find_answer()

