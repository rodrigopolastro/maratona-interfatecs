################################################################################
# Objetivo: 
#   Sistema antimísseis -> calcular distancias entre pontos no plano cartesiano 
#   e um radar e exibi-los em ordem crescente caso estejam dentro do raio de 
#   alcance do radar
#
# Autor: Rodrigo Polastro
# Data: 16/07/2025
# Duração: (25m)
################################################################################
from string import ascii_uppercase
from math import sqrt

def distancia_pontos(x1, y1, x2, y2):
    return sqrt((x1-x2)**2 + (y1-y2)**2)

qtdCasos = int(input())
for _ in range(qtdCasos):
    xRadar, yRadar = [int(_) for _ in input().split()]
    raioRadar = int(input())
    qtdMisseis = int(input())
    misseis = list()
    for indexMissel in range(1, qtdMisseis+1): #começa no index 1 -> B
        xMissel, yMissel = [int(_) for _ in input().split()]
        letraMissel = ascii_uppercase[indexMissel]

        distanciaMissel = distancia_pontos(xRadar, yRadar, xMissel, yMissel)
        if distanciaMissel <= raioRadar:
            misseis.append(tuple([letraMissel, distanciaMissel]))

    qtdMisseisAlcance = len(misseis)
    if qtdMisseisAlcance == 0:
        print('OUT OF RANGE')
    else:
        #ordena pela distancia e depois pela letra do missel (ordem de entrada)
        misseisOrdenados = sorted(misseis, key=lambda missel: (missel[1], missel[0]))
        for i, missel in enumerate(misseisOrdenados):
            if i == qtdMisseisAlcance-1:
                print(missel[0])
            else:
                print(missel[0], end=' ')

        