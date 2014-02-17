from time import clock
from math import sqrt, floor


def timer(function):
    def wrapper(*args, **kwargs):
        start = clock()
        print(function(*args, **kwargs))
        print("Solution took: %f seconds." % (clock() - start))

    return wrapper


@timer
def find_answer():
    # If the last digit of a number is 0, its square ends in an even number of 0s (so at least 00)
    # The digits preceding the ending 0s must also form a square.
    # 1_2_3_4_5_6_7_8_9_0 ends in a 0, so the last _ must be 0
    # The minimum number is 1020304050607080900
    # The maximum number is 1929394959697989900
    # 1_2_3_4_5_6_7_8_9 must also be a square and since it ends in 9, the square root ends in 3 or 7
    minimum = 1020304050607080900
    maximum = 1929394959697989900
    sqrt_min = sqrt(minimum)  # lower bound, needs to end in 00
    sqrt_min = int(floor(sqrt_min / 100.0)) * 100 + 30  # round down to tens place
    sqrt_max = int(sqrt(maximum) + 1)  # upper bound
    increment = 40
    other_increment = 60

    while sqrt_min < sqrt_max:
        a = str(sqrt_min ** 2)
        a = a[0] + a[2] + a[4] + a[6] + a[8] + a[10] + a[12] + a[14] + a[16]
        if a == "123456789":
            return sqrt_min
        sqrt_min += increment
        increment, other_increment = other_increment, increment


if __name__ == "__main__":
    find_answer()

