from time import clock


def timer(function):
    def wrapper(*args, **kwargs):
        start = clock()
        print(function(*args, **kwargs))
        print("Solution took: %f seconds." % (clock() - start))

    return wrapper


@timer
def find_answer():
    return triangles(286, 100000).intersection(pentagonals(166, 100000).intersection(hexagons(144, 100000))).pop()


def pentagonals(start, amount):
    pents = set()
    for i in range(start, amount + 1):
        pents.add(i * (3 * i - 1) // 2)

    return pents


def triangles(start, amount):
    tris = set()
    for i in range(start, amount + 1):
        tris.add(i * (i + 1) // 2)

    return tris


def hexagons(start, amount):
    hexs = set()
    for i in range(start, amount + 1):
        hexs.add(i * (2 * i - 1))

    return hexs


if __name__ == "__main__":
    find_answer()

