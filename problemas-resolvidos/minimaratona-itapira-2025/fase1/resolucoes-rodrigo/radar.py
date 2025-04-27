from math import ceil, floor

velocidade = int(input())

if velocidade <= 107:
    maxima = velocidade+7
else:
    maxima = velocidade * 1.07

print(round(maxima))