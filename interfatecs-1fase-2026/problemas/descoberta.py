from math import sqrt

n = int(input())

soma = 0
for i in range(1, n+1):
    soma += i**3

raiz = int(sqrt(soma))

print(soma, raiz)