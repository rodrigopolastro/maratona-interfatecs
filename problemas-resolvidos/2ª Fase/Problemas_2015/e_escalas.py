################################################################################
# Objetivo:
#
# Autor: Rodrigo
# Data: 18/07/2025
# Duração: 1h
################################################################################
from math import floor

countCasos = 0
while True:
    entrada = input().split()
    if not entrada:
        quit()
    countCasos +=1
        
        
    multiplicadorHorizontal = int(entrada[0].split(':')[1])
    multiplicadorVertical = int(entrada[1].split(':')[1])
    qtdCasos = int(entrada[2])
    
    print(f"Escalas {countCasos}:")
    for _ in range(qtdCasos):
        largura, comprimento, altura = [int(_) for _ in input().split()]
        
        alturaMetros  = altura * multiplicadorVertical / 100
        larguraMetros = largura * multiplicadorHorizontal / 100
        comprimentoMetros = comprimento * multiplicadorHorizontal / 100
        
        
        #contando terreo como um andar
        if alturaMetros >= 6:
            qtdAndares = floor(alturaMetros/ 3)
        else:
            qtdAndares =1
            
        # print(qtdAndares+1)
        areaAndar = larguraMetros * comprimentoMetros
        areaTotal = int(areaAndar * qtdAndares)
        
        print(areaTotal)
        
    