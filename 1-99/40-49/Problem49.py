from time import clock


def timer(function):
    def wrapper(*args, **kwargs):
        start = clock()
        print(function(*args, **kwargs))
        print("Solution took: %f seconds." % (clock() - start))

    return wrapper


@timer
def find_answer():
    # all the primes from 1000 to 10000
    primes = [x for x in sieve(100000) if x > 1000]
    primes.remove(1487)
    for i in range(len(primes)):
        for j in range(i + 1, len(primes)):
            if check_if_permutation(primes[i], primes[j]):
                candidate = primes[j] + primes[j] - primes[i]
                if candidate in primes and check_if_permutation(primes[i], candidate):
                    return str(primes[i]) + str(primes[j]) + str(candidate)


def sieve(upperlimit):
    l = [2] + [x if x % 2 != 0 else 0 for x in range(3, upperlimit + 1)]

    for p in l:
        if p ** 2 > upperlimit:
            break
        elif p:
            for i in range(p * p, upperlimit + 1, 2 * p):
                l[i - 2] = 0

    return [x for x in l if x]


def check_if_permutation(target, n):
    target = sorted([x for x in str(target)])
    n = sorted([x for x in str(n)])
    return target == n


if __name__ == "__main__":
    find_answer()

