import math

# retorna uma lista com os primeiros N primos informados
def first_n_primes(numberOfPrimes):
    if numberOfPrimes < 6:
        limit = 15 
    else:
        limit = int(numberOfPrimes * (math.log(numberOfPrimes) + math.log(math.log(numberOfPrimes)))) + 10
        # limit = n #  <- pega até o número que você especificar

    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False

    for i in range(2, int(math.sqrt(limit)) + 1):
        if sieve[i]:
            for j in range(i * i, limit + 1, i):
                sieve[j] = False

    primes = [i for i, is_p in enumerate(sieve) if is_p]
    #OBS: se quiser retornar somente o enésimo primo, utilize:
    # -> return primes[n-1]
    return primes[:numberOfPrimes] 

# retorna a lista de primos até o limite informado (INCLUI O LIMITE NO INTERVALO)
def primes_up_to_n(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False

    for i in range(2, int(math.sqrt(limit)) + 1):
        if sieve[i]:
            for j in range(i * i, limit + 1, i):
                sieve[j] = False

    primes = [i for i, is_p in enumerate(sieve) if is_p]
    return primes

while True:
    n = int(input())
    print('primeiros ', n, ' primos: ', first_n_primes(n)[-1])
    print('primos até ', n, ': ', primes_up_to_n(n)[-1])