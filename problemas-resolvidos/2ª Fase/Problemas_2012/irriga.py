################################################################################
# Objetivo:
#
# Autor: Alexandre e Rodrigo
# Data: 12/07/2025
# Duração: (discussao: 22:50 - 23:40) (codigo: 23:40 - )
################################################################################
from math import inf, sqrt, ceil

def dist2Pontos(ponto1, ponto2):
    x1, x2, y1, y2 = ponto1[0], ponto2[0], ponto1[1], ponto2[1]
    # print('dist: ' , ponto1, ponto2, sqrt((x1-x2)**2 + (y1-y2)**2))
    return sqrt((x1-x2)**2 + (y1-y2)**2)

while True:
    comprimentoArea, larguraArea = [int(_) for _ in input().split()]
    if comprimentoArea == larguraArea == 0:
        break
    
    plantas = set()
    
    #leitura dados
    maiorX = maiorY = -inf
    menorX = menorY = inf
    
    qtdPlantas = int(input())
    for _ in range(qtdPlantas):
        xPlanta, yPlanta = [int(_) for _ in input().split()]
        
        if xPlanta > maiorX:
            maiorX = xPlanta
            plantas.add(tuple([xPlanta, yPlanta]))
        elif xPlanta < menorX:
            menorX = xPlanta
            plantas.add(tuple([xPlanta, yPlanta]))
        if yPlanta > maiorY:
            maiorY = yPlanta
            plantas.add(tuple([xPlanta, yPlanta]))
        if yPlanta < menorY:
            menorY = xPlanta
            plantas.add(tuple([xPlanta, yPlanta]))
        # maiorX = max(xPlanta, maiorX)
        # menorX = min(xPlanta, menorX)
        # maiorY = max(yPlanta, maiorY)
        # menorY = min(yPlanta, menorY)
    
    alturaRetangulo = maiorY - menorY
    comprimentoRetangulo = maiorX - menorX
    
    maiorDist2Plantas = -inf
    for planta1 in plantas:
        for planta2 in plantas:
            dist = dist2Pontos(planta1, planta2)
            if dist > maiorDist2Plantas:
                maiorDist2Plantas = dist
                plantasMaiorDist = tuple([planta1, planta2])
    # print('maior dist: ', maiorDist2Plantas)
    # print('plantas  ', plantasMaiorDist)

    # raioCirculo = maiorDist2Plantas/2
    # planta1, planta2 = plantasMaiorDist
    # x1, x2, y1, y2 = planta1[0], planta2[0], planta1[1], planta2[1]
    # xAspersor = (x1 + x2)/2
    # yAspersor = (y1 + y2)/2
    
    #distancia centro e coordenada inferior (pitagoras)
    # raioCirculo = sqrt((comprimentoRetangulo/2)**2 + (alturaRetangulo/2)**2 )
    raioAspersor = ceil(raioCirculo / 5) * 5
    # 1 / 5 = 0 -> 1 * 5 = 5
    # 6/5 = 1.. -> 2 % 
    #
    print(f"{xAspersor:.2f} {yAspersor:.2f} {raioAspersor}")
        