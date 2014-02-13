from time import clock

months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
months_leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def timer(function):
    def wrapper(*args, **kwargs):
        start = clock()
        print(function(*args, **kwargs))
        print("Solution took: %f seconds." % (clock() - start))

    return wrapper


@timer
def find_answer():
    sundays = 0
    day = 1
    day += sum(months_leap)  #account for 1900
    for year in range(1901, 2001):
        if year % 4 == 0:
            for month in months_leap:
                if day % 7 == 0:
                    sundays += 1
                day += month
        else:
            for month in months:
                if day % 7 == 0:
                    sundays += 1
                day += month
    return sundays


if __name__ == "__main__":
    find_answer()

