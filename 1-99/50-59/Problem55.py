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
    for i in range(10000):
        if is_lychrel(i):
            total += 1
    return total


def is_lychrel(n, iterations=0):
    reverse_n = int(''.join([x for x in str(n)][::-1]))
    total = n + reverse_n
    if iterations == 50:
        return True
    if str(total) == str(total)[::-1]:
        return False
    else:
        return is_lychrel(total, iterations=iterations + 1)


if __name__ == "__main__":
    find_answer()

