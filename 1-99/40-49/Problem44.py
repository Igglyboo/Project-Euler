from time import clock


def timer(function):
    def wrapper(*args, **kwargs):
        start = clock()
        print(function(*args, **kwargs))
        print("Solution took: %f seconds." % (clock() - start))

    return wrapper


@timer
def find_answer():
    pents = pentagonals(5000)
    pents_membership = set(pents)
    differnces = []
    for i in range(len(pents) - 1):
        for j in range(i, len(pents) - 1):
            if pents[i] + pents[j] in pents_membership:
                if abs(pents[i] - pents[j]) in pents_membership:
                    differnces.append(abs(pents[i] - pents[j]))
    return min(differnces)


def pentagonals(amount):
    pents = []
    for i in range(1, amount + 1):
        pents.append(i * (3 * i - 1) // 2)

    return pents


if __name__ == "__main__":
    find_answer()

