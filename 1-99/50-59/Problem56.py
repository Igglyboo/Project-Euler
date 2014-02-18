from time import clock


def timer(function):
    def wrapper(*args, **kwargs):
        start = clock()
        print(function(*args, **kwargs))
        print("Solution took: %f seconds." % (clock() - start))

    return wrapper


@timer
def find_answer():
    max = 0
    for a in range(1, 101):
        for b in range(1, 101):
            current = digit_sum(a ** b)
            if current > max:
                max = current
    return max


def digit_sum(n):
    return sum([int(x) for x in str(n)])


if __name__ == "__main__":
    find_answer()

