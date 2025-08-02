import math
from functools import lru_cache

@lru_cache
def primes_up_to_n(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False

    for i in range(2, int(math.sqrt(limit)) + 1):
        if sieve[i]:
            for j in range(i * i, limit + 1, i):
                sieve[j] = False

    primes = [i for i, is_p in enumerate(sieve) if is_p]
    return primes

def solve(numbers):
    for i in numbers:
        primes = primes_up_to_n(i)
        if i in primes:
            print('primo')
            continue
        anterior = primes[0]
        posterior = primes[1]
        for k, prime in enumerate(primes):
            if prime > i:
                posterior = prime
                break
            anterior = primes[k]

        print(f'{anterior} e {posterior}')


try:
    i = 1
    while True:
        print(f"CASO {i}:")
        cases = int(input())
        numbers = []
        for _ in range(cases):
            number = int(input())
            numbers.append(number)
        solve(numbers)
        i += 1
except EOFError:
    pass
