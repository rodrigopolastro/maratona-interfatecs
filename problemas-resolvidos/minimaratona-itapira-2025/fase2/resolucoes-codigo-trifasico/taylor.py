from math import factorial

def grausParaRadianos(x):
    return x * 3.1415 / 180

anguloGraus = int(input())
anguloRadianos = grausParaRadianos(anguloGraus)
soma = 0.0
for n in range(5): 
    numerador = anguloRadianos ** (2*n)
    denominador = factorial(2*n)
    soma += (-1)**n * numerador/denominador

parteInteira, parteDecimal = str(soma).split('.')
parteDecimal = parteDecimal.ljust(4, '0')
quartaCasa = int(parteDecimal[3])

if 0 <= quartaCasa <= 6:
    print(f"{parteInteira}.{parteDecimal[:3]}")
else:
    parteDecimal = int(parteDecimal[:3])
    parteDecimal += 1
    print(f"{parteInteira}.{parteDecimal}")