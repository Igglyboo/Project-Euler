from time import clock
from decimal import Decimal


def timer(function):
    def wrapper(*args, **kwargs):
        start = clock()
        print(function(*args, **kwargs))
        print("Solution took: %f seconds." % (clock() - start))

    return wrapper


@timer
def find_answer():
    product = 1
    for num in range(10, 99):
        for den in range(num + 1, 99):
            quotient = Decimal(num) / Decimal(den)
            num_str = str(num)
            den_str = str(den)
            if '0' not in num_str and '0' not in den_str:
                if num_str[0] == den_str[0]:
                    if quotient == Decimal(num_str[1]) / Decimal(den_str[1]):
                        product *= quotient
                elif num_str[0] == den_str[1]:
                    if quotient == Decimal(num_str[1]) / Decimal(den_str[0]):
                        product *= quotient
                elif num_str[1] == den_str[0]:
                    if quotient == Decimal(num_str[0]) / Decimal(den_str[1]):
                        product *= quotient
                elif num_str[1] == den_str[1]:
                    if quotient == Decimal(num_str[0]) / Decimal(den_str[0]):
                        product *= quotient

    return 1 // product


if __name__ == "__main__":
    find_answer()

