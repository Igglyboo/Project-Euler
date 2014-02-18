from time import clock


def timer(function):
    def wrapper(*args, **kwargs):
        start = clock()
        print(function(*args, **kwargs))
        print("Solution took: %f seconds." % (clock() - start))

    return wrapper


@timer
def find_answer():
    primes = sieve(1000000)
    primes_cache = [[0, 0, 0]] * len(primes)
    maximum = [0, 0, 0]
    # enumerates all the primes
    for i in range(len(primes)):
        #enumerates all the primes lower than i, where we start the sequence
        for j in range(i):
            total = primes_cache[j][:]
            found_sum = False
            #enumerates all the primes from start of sequence to i
            for k in range(j, i):
                k += total[2]
                total[0] += primes[k]
                total[1] += 1
                if total[0] > primes[i]:
                    if total[1] - 1 < maximum[1]:
                        found_sum = True
                    break
                elif total[0] == primes[i]:
                    primes_cache[j] = [total[0], total[1], k + 1 - j]
                    if total[1] > maximum[1]:
                        maximum = total
                    found_sum = True
                    break
            if found_sum:
                break
    return maximum[0]


def sieve(upperlimit):
    l = [2] + [x if x % 2 != 0 else 0 for x in range(3, upperlimit + 1)]

    for p in l:
        if p ** 2 > upperlimit:
            break
        elif p:
            for i in range(p * p, upperlimit + 1, 2 * p):
                l[i - 2] = 0

    return [x for x in l if x]


if __name__ == "__main__":
    find_answer()

