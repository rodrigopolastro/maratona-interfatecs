################################################################################
# Nome: Distância dos pontos
# Objetivo:
# -> 
# Comentários:
# -> 
# Autor: Rodrigo
# Data: 01/08/2025
# Duração: inicio 22:10
################################################################################
from math import sqrt
from itertools import combinations

def distancia_pontos(ponto1, ponto2):
    x1, y1 = ponto1
    x2, y2 = ponto2
    return sqrt((x1-x2)**2 + (y1-y2)**2)

pontos = list()
# arestas = list()

# qtdCasos = int(input())
# qtdPontos = int(input())
# for _ in range(qtdPontos):
#     xPonto, yPonto = [int(_) for _ in input().split()]
#     pontos.append((xPonto, yPonto))
qtdCasos = 1
qtdPontos = 3
pontos = [
    (0, 0),
    (4, 0),
    (4, 3)
]
    
arestas = list(combinations(pontos, 2))
print(len(arestas))
arestasComDistancias = list()
for i in range(len(arestas)):
    arestas    
    
    
# for pontoPartida in pontos:
#     for pontoDestino in pontos:
#         if pontoPartida == pontoDestino:
#             continue
#         distancia = distancia_pontos(pontoPartida, pontoDestino)
#         arestas.append((pontoDestino, pontoPartida, distancia))
print(arestas)
for a in arestas: print(a) 

1
    
    