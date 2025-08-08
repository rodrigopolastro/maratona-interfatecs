################################################################################
# Objetivo:
# -> Dada uma lista de coordenadas de pontos no plano cartesiano, calcular a distância
#    do menor caminho possível para interligar todos eles
# Comentários:
# -> Problema clássico de grafos: MST - Minimum Spanning Tree (Árvore Geradora Mínima).
#    O diferencial é que as distâncias entre os pontos devem ser computadas manualmente
#    e calculadas para todas as combinações de pontos possíveis
# Autor: Rodrigo Polastro
# Data: 06/08/2025
# Duração: 22:47 inicio - 23:36
################################################################################

from itertools import combinations
from math import sqrt

arestas = list()
pontos = list()
pai = list()
peso = list()

def distancia_pontos(ponto1, ponto2):
    x1, y1 = ponto1
    x2, y2 = ponto2
    
    return float(sqrt((x1-x2)**2 + (y1-y2)**2))

def find(a):
    if a not in pai.keys():
        pai[a] = a
        peso[a] = 0
    
    if pai[a] == a:
        return a
    patriarca = find(pai[a])
    pai[a] = patriarca
    return patriarca

def union(a, b):
    paiA = find(a)
    paiB = find(b)
    
    if peso[paiA] < peso[paiB]: pai[paiA] = paiB
    elif peso[paiB] < peso[paiA]: pai[paiB] = paiA
    else: 
        pai[paiA] = paiB
        peso[paiB] += 1     

qtdTestes = int(input())
for _ in range(qtdTestes):
    arestas = list()
    pontos = list()
    pai = dict()
    peso = dict()
    
    qtdPontos = int(input())
    for _ in range(qtdPontos):
        xPonto, yPonto = [int(_) for _ in input().split()]
        pontos.append((xPonto, yPonto))
    combinacoes = combinations(pontos, 2)
    for ponto1, ponto2 in combinacoes: 
        aresta = (ponto1, ponto2, distancia_pontos(ponto1, ponto2))
        arestas.append(aresta)
    arestas.sort(key=lambda a: a[2]) #ordena pela distância
    qtdElementosArvore = 0
    comprimentoArvore = 0
    for ponto1, ponto2, distancia in arestas:
        if find(ponto1) == find(ponto2):
            continue
        union(ponto1, ponto2)
        qtdElementosArvore += 1
        comprimentoArvore += distancia
        if qtdElementosArvore == qtdPontos-1:
            break
    print(f"{comprimentoArvore:.4f}")
        
    
    
    