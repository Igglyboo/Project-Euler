from time import clock


def timer(function):
    def wrapper(*args, **kwargs):
        start = clock()
        print(function(*args, **kwargs))
        print("Solution took: %f seconds." % (clock() - start))

    return wrapper


@timer
def find_answer():
    words = []
    with open("words.txt") as f:
        for item in f.read().split(","):
            words.append(item.strip("\""))

    tri = triangles(100)
    amount = 0
    for word in words:
        total = sum([ord(x) - 64 for x in word])
        if total in tri:
            amount += 1
    return amount


def triangles(amount):
    tri = set()
    for i in range(1, amount + 1):
        tri.add(i * (i + 1) // 2)

    return tri


if __name__ == "__main__":
    find_answer()

