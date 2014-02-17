from time import clock
from itertools import product


def timer(function):
    def wrapper(*args, **kwargs):
        start = clock()
        print(function(*args, **kwargs))
        print("Solution took: %f seconds." % (clock() - start))

    return wrapper


@timer
def find_answer():
    pete = [0] * 37
    for rolls in product([1, 2, 3, 4], repeat=9):
        pete[sum(rolls)] += 1

    colin = [0] * 37
    for rolls in product([1, 2, 3, 4, 5, 6], repeat=6):
        colin[sum(rolls)] += 1

    total_games = (4 ** 9) * (6 ** 6)
    pete_wins = 0
    for c in range(37):
        for p in range(c + 1, 37):
            pete_wins += colin[c] * pete[p]

    return round(pete_wins / total_games, 7)


if __name__ == "__main__":
    find_answer()

