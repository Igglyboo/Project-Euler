from time import clock


def timer(function):
    def wrapper(*args, **kwargs):
        start = clock()
        print(function(*args, **kwargs))
        print("Solution took: %f seconds." % (clock() - start))

    return wrapper


@timer
def find_answer():
    for index, value in enumerate(fibonacci_generator()):
        if len(str(value)) >= 1000:
            return index + 1


def fibonacci_generator():
    a = 1
    b = 2
    yield 1
    yield 1
    yield 2
    while True:
        a, b = b, a + b
        yield b


if __name__ == "__main__":
    find_answer()

