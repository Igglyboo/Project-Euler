from time import clock

words = {0: 0, 1: 3, 2: 3, 3: 5, 4: 4, 5: 4, 6: 3, 7: 5, 8: 5, 9: 4, 10: 3, 11: 6, 12: 6,
         13: 8, 14: 8, 15: 7, 16: 7, 17: 9, 18: 8, 19: 8, 20: 6, 30: 6, 40: 5, 50: 5,
         60: 5, 70: 7, 80: 6, 90: 6, 100: 7, 1000: 8}


def timer(function):
    def wrapper(*args, **kwargs):
        start = clock()
        print(function(*args, **kwargs))
        print("Solution took: %f seconds." % (clock() - start))

    return wrapper


@timer
def find_answer():
    one_to_9 = 0
    # 1 - 20
    for i in range(10):
        one_to_9 += words[i]

    ten_to_19 = 0
    for i in range(10, 20):
        ten_to_19 += words[i]

    twenty_to_99 = 0
    # 20 - 99
    for i in range(20, 100, 10):
        twenty_to_99 += words[i] * 10 + one_to_9

    hundreds = one_to_9 + words[100] * 9
    hundred_and = (words[100] + 3) * 99 * 9
    total = (one_to_9 * 99) + (one_to_9 + ten_to_19 + twenty_to_99) * 10 + hundreds + hundred_and
    total += words[1] + words[1000]

    return total


if __name__ == "__main__":
    find_answer()

