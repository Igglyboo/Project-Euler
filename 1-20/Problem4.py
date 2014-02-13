from time import clock


def timer(function):
    def wrapper(*args, **kwargs):
        start = clock()
        print(function(*args, **kwargs))
        print("Solution took: %f seconds." % (clock() - start))

    return wrapper


@timer
def find_answer():
    palindrome = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            product = str(i * j)
            if product == product[::-1] and int(product) > palindrome:
                palindrome = int(product)

    return palindrome


if __name__ == "__main__":
    find_answer()

