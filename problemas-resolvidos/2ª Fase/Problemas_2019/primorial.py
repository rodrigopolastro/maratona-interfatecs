import math
def primes_up_to_n(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False

    for i in range(2, int(math.sqrt(limit)) + 1):
        if sieve[i]:
            for j in range(i * i, limit + 1, i):
                sieve[j] = False

    primes = [i for i, is_p in enumerate(sieve) if is_p]
    return primes


numeroUsuario = int(input())
numerosPrimos = primes_up_to_n(5000)

def multiplicar(lista : list[int]) -> int :
    multiplicado = 1
    for m in lista:
        multiplicado *= m
    return multiplicado    

flagControle = True
for indexMultiplicador in range(1,len(numerosPrimos)+1):
    if multiplicar(numerosPrimos[:indexMultiplicador]) == numeroUsuario:
        flagControle = False
        break
    
    
if flagControle:
    print("N")
else:
    print("S")
    
    