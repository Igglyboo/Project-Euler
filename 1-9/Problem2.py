from time import clock


def timer(function):
    def wrapper(*args, **kwargs):
        start = clock()
        print(function(*args, **kwargs))
        print("Solution took: %f seconds." % (clock() - start))

    return wrapper


@timer
def find_answer():
    return sum([i for i in fibonacci_generator(4000000) if i % 2 == 0])


def fibonacci_generator(max_value):
    a = 1
    b = 2
    yield a
    yield b
    while a + b < max_value:
        a, b = b, a + b
        yield b


if __name__ == "__main__":
    find_answer()

