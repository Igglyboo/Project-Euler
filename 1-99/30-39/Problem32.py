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
    products = set()
    for i in range(2, 100):
        for j in range(0, 10000 // i):
            product = i * j
            current = [x for x in str(product)] + [x for x in str(i)] + [x for x in str(j)]
            current.sort()
            if current == target:
                products.add(product)

    return sum(products)


if __name__ == "__main__":
    find_answer()

