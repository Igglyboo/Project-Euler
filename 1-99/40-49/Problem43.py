from time import clock
from itertools import permutations


def timer(function):
    def wrapper(*args, **kwargs):
        start = clock()
        print(function(*args, **kwargs))
        print("Solution took: %f seconds." % (clock() - start))

    return wrapper


@timer
def find_answer():
    total = 0
    for i in permutations("0123456789"):
        current = ''.join(i)
        if int(current[7:10]) % 17 == 0:
            if int(current[6:9]) % 13 == 0:
                if int(current[5:8]) % 11 == 0:
                    if int(current[4:7]) % 7 == 0:
                        if int(current[3:6]) % 5 == 0:
                            if int(current[2:5]) % 3 == 0:
                                if int(current[1:4]) % 2 == 0:
                                    total += int(current)
    return total


if __name__ == "__main__":
    find_answer()

