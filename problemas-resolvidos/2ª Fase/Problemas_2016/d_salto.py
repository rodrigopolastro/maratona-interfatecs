################################################################################
# Objetivo:
#
# Autor: Rodrigo
# Data: 28/07/2025
# Duração: inicio: 21:58 - 22:10
################################################################################
from math import lcm

def main():
    entrada = input().split()
    tamanhoPista, qtdCompetidores = int(entrada[0]), int(entrada[1])
    numeros = list()
    for _ in range(qtdCompetidores):
        numeros.append(int(input()))
        
    mmc = lcm(*numeros)
    print(tamanhoPista//mmc)

try: 
    while True:
        main()
except EOFError:
    pass