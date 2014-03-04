def sieve(upper_bound):
    prime = [False, False, True] + [True, False] * (upper_bound // 2)
    for p in range(3, int(upper_bound ** .5) + 1, 2):
        if prime[p]:
            for i in range(p * p, upper_bound, 2 * p):
                prime[i] = False
    return [p for p in range(2, upper_bound) if prime[p]]
