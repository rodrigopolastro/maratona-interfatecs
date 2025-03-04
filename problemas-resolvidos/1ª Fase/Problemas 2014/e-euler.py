from math import factorial
while True:
    n = int(input())
    if n < 0:
        break
    retornar = float(0)
    for numero in range(n+1):
        retornar += 1/factorial(numero)
    print(f"{retornar:.6f}")
    
