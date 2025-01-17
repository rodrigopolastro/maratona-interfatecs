# Data: 16/01/2025
# Início: 19:25 - Término:
# Feito por: Alexandre e Rodrigo

# ETAPAS
# - Multiplicar a matriz fixa pelos valores de entrada
# - separar sinais de alta e baixa frequência (ímpar/par)
# - realizar a somatória dos quadrados e dividir (equação informada)
# - se der > 0.5, printa "INIMIGO", se não, printa "-"
from math import sqrt
H1 = round(1/sqrt(2),1)
H2 = round(1/sqrt(2),1)
G1 = round(1/sqrt(2),1)
G2 = round(-1/sqrt(2),1)

sinalSaida = [None,None,None,None,None,None,None,None]
# sinaisBaixaFreq = []

def calculoEnergiaDigital(linha):
    return sum([x**2 for x in linha])

n = int(input())
for _ in range(n):
    sinalEntrada = list(map(int,input().split(' ')))
    # print(sinalEntrada)
    
    sinalSaida[0] = H1 * sinalEntrada[0] + H2 * sinalEntrada[1]
    sinalSaida[1] = G1 * sinalEntrada[0] + G2 * sinalEntrada[1]
    sinalSaida[2] = H1 * sinalEntrada[2] + H2 * sinalEntrada[3]
    sinalSaida[3] = G1 * sinalEntrada[2] + G2 * sinalEntrada[3]
    sinalSaida[4] = H1 * sinalEntrada[4] + H2 * sinalEntrada[5]
    sinalSaida[5] = G1 * sinalEntrada[4] + G2 * sinalEntrada[5]
    sinalSaida[6] = H1 * sinalEntrada[6] + H2 * sinalEntrada[7]
    sinalSaida[7] = G1 * sinalEntrada[6] + G2 * sinalEntrada[7]

    # print(sinalSaida)

    # for i in range(8, step=2):
    #     sinaisBaixaFreq.appen
    sinaisBaixaFreq = []
    for i, sinal in enumerate(sinalSaida):
        if i % 2 == 0:
            sinaisBaixaFreq.append(sinal)
            
    # print(sinalSaida)
    # print(sinaisBaixaFreq)
    
    # sinaisBaixaFreq 
    # sinaisBaixaFreq = list(filter(lambda sinal: sinal % 2 == 0, sinalSaida))
    # print(sinaisBaixaFreq)

    energiaEntrada = calculoEnergiaDigital(sinalEntrada)

    if energiaEntrada == 0: # ZeroDivisionError aqui não 🐿️
        print("-")
        continue
    
    resultado = calculoEnergiaDigital(sinaisBaixaFreq) / energiaEntrada
    
    # print('resultado: ', resultado)
    if resultado > 0.5:
        print("INIMIGO")
    else:
        print("-")

# 1
# -6 8 -10 -8 -7 10 -7 -7
    



    
