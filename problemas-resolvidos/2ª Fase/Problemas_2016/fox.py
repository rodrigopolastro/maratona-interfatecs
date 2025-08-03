import math

#comeco 9:58 fim 10:11

def generate_first_n_primes(n):
    # if n < 6:
    #     limit = 15
    # else:
    #     limit = int(n * (math.log(n) + math.log(math.log(n)))) + 10
    limit = n #  <- pega até o número que você especificar
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False

    for i in range(2, int(math.sqrt(limit)) + 1):
        if sieve[i]:
            for j in range(i * i, limit + 1, i):
                sieve[j] = False

    primes = [i for i, is_p in enumerate(sieve) if is_p]
    #OBS: se quiser retornar somente o enésimo primo, utilize:
    # -> return primes[n-1]
    return primes[:n] 

respostas = []
primos = generate_first_n_primes(1_001_000)
comparacaoO1 = set(primos)
caso = 1
try:
    while True:
        numeros = int(input())
        analisar = []
        for _ in range(numeros):
            analisar.append(int(input()))
        # print(f'CASO {caso}:')
        respostas.append(f'CASO {caso}:')
        caso+=1
        for a in analisar:
            if a in comparacaoO1:
                # print('primo')
                respostas.append('primo')
            else:
                for i in range(len(primos)):
                    if primos[i] < a and primos[i+1] > a:
                        #print(f'{primos[i]} e {primos[i+1]}')
                        respostas.append(f'{primos[i]} e {primos[i+1]}')
                        break
except EOFError:
    for r in respostas:
        print(r)
    
    
    
        