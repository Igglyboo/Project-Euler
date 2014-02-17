from time import clock


def timer(function):
    def wrapper(*args, **kwargs):
        start = clock()
        print(function(*args, **kwargs))
        print("Solution took: %f seconds." % (clock() - start))

    return wrapper


@timer
def find_answer():
    total = 0
    primes = sieve(1000000)
    primes.remove(0)
    for prime in primes:
        p_str = list(str(prime))
        p_str.append(p_str.pop(0))
        for i in range(len(p_str) - 1):
            current = int(''.join(x for x in p_str))
            if current not in primes:
                break
            p_str.append(p_str.pop(0))
        else:
            total += 1

    return total


def sieve(upperlimit):
    l = list(range(2, upperlimit + 1))

    # Do p = 2 first so we can change step size to 2*p below
    for i in range(4, upperlimit + 1, 2):
        l[i - 2] = 0

    for p in l:
        if p ** 2 > upperlimit:
            break
        elif p:
            for i in range(p * p, upperlimit + 1, 2 * p):
                l[i - 2] = 0

    return set(l)


if __name__ == "__main__":
    find_answer()

