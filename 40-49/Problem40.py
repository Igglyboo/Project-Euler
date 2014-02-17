from time import clock


def timer(function):
    def wrapper(*args, **kwargs):
        start = clock()
        print(function(*args, **kwargs))
        print("Solution took: %f seconds." % (clock() - start))

    return wrapper


@timer
def find_answer():
    num = "."
    i = 1
    while len(num) < 1000001:
        num += str(i)
        i += 1

    return int(num[1]) * int(num[10]) * int(num[100]) * int(num[1000]) * int(num[10000]) * int(num[100000]) * int(
        num[1000000])


if __name__ == "__main__":
    find_answer()

