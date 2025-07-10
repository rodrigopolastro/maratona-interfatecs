#data: 03/04/2025
#duração: 5min

from math import comb

qtdEntradas = int(input())
for _ in range(qtdEntradas):
    linha, coluna = [int(_) for _ in input().split()]
    print(comb(linha, coluna))