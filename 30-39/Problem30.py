from time import clock


def timer(function):
    def wrapper(*args, **kwargs):
        start = clock()
        print(function(*args, **kwargs))
        print("Solution took: %f seconds." % (clock() - start))

    return wrapper


@timer
def find_answer():
    answer = 0
    for num in range(2, 1000000):
        total = sum(map(lambda x: int(x) ** 5, str(num)))
        if total == num:
            answer += num

    return answer


if __name__ == "__main__":
    find_answer()

