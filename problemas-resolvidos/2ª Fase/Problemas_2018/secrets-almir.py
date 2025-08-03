from math import sqrt, ceil

def isPrime(number: int) -> bool:
    if number == 2:
        return True

    if number == 1 or number % 2 == 0:
        return False

    for divisor in range(3, ceil(sqrt(number)) + 1, 2):
        if number % divisor == 0:
            return False

    return True

def isInFibonacci(n: int) -> bool:
    a, b = 1, 1
    while a < n: a, b = b, a+b
    return a == n

def isFactorial(n: int) -> bool:
    f = 1
    i = 2
    while f < n:
        f *= i
        i += 1
    return f == n

def decode(read: str) -> int:
    first = ord('a')
    value = 0
    for i, ch in enumerate(read):
        if str(ch).isnumeric():
            value += (int(ch)) * (i+1)
            continue
        value += (ord(ch)-first+1) * (i+1)
    return value

def solve(read: str) -> str:
    decoded = decode(read)
    result = '!'

    if isFactorial(decoded):
        result = 'ultimate'
    elif isInFibonacci(decoded):
        result = 'premium'
    elif isPrime(decoded):
        result = 'basic'

    return f'{decoded}: {result}'

try:
    while True:
        read = input()
        print(solve(read))
except EOFError:
    pass
