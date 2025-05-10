# from math import sqrt, ceil
# def isPrime(number):
#     if number == 2:
#         return True
    
#     if number == 1 or number % 2 == 0:
#         return False
    
#     for divisor in range(3, ceil(sqrt(number)), 2):
#         if number % divisor == 0:
#             return False
        
#     return True

# def generatePrimes(numberOfPrimes):
#     if numberOfPrimes <= 0:
#         return 0
#     if numberOfPrimes == 1:
#         return 2

#     impar = 3
#     cont = 1
#     while cont < numberOfPrimes:
#         if isPrime(impar):
#             cont+=1
#             primo = impar
#         impar += 2
            
#     return primo
        
# print(generatePrimes(100000))

import math

def prime(n):
    if n < 6:
        limit = 15
    else:
        limit = int(n * (math.log(n) + math.log(math.log(n)))) + 10

    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False

    for i in range(2, int(math.sqrt(limit)) + 1):
        if sieve[i]:
            for j in range(i * i, limit + 1, i):
                sieve[j] = False

    primes = [i for i, is_p in enumerate(sieve) if is_p]

    return primes[n - 1]


