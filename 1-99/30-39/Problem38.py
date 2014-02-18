from time import clock


def timer(function):
    def wrapper(*args, **kwargs):
        start = clock()
        print(function(*args, **kwargs))
        print("Solution took: %f seconds." % (clock() - start))

    return wrapper


@timer
def find_answer():
    target = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    for i in range(9387, 9233, -1):
        current = [x for x in str(i)] + [x for x in str(i * 2)]
        current.sort()
        if current == target:
            return str(i) + str(i * 2)
    return 5


if __name__ == "__main__":
    find_answer()

