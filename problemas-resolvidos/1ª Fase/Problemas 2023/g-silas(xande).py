################################################################################
# Objetivo: Algoritmo pathfinder. Encontrar a distância do menor caminho até um 
#           objetivo desviando de obstáculos no cenário 
# Autor: Alexandre
# Data: 27/01/2025
# Duração: ?
################################################################################
from time import sleep

caminhos = dict()
ja_visitados = []
forca = int(input())
matriz = []
linhas,colunas = list(map(int,input().split()))

for inputLinhas in range(linhas):
    matriz.append(input().split(' '))
    
posicaoInicial = ()
for linha in range(len(matriz)):
    for coluna in range(len(matriz[0])):
        if matriz[linha][coluna] == 'S':
            posicaoInicial = (linha,coluna)
        elif matriz[linha][coluna].isnumeric():
            if int(matriz[linha][coluna]) <= forca:
                matriz[linha][coluna] = '.'
            else:
                matriz[linha][coluna] = '#'
                
proximos_na_fila = []
proximos_na_fila.append(posicaoInicial)
caminhos[posicaoInicial] = None
for linha in range(len(matriz)):
    for coluna in range(len(matriz[0])):
        if matriz[linha][coluna] == 'K':
            Objetivo = (linha,coluna)
            break
        
def adicionarVizinhosNaFila(posicaoAtual : tuple):
    for proximos_x in [-1,0,1]:
        for proximos_y in [-1,0,1]:
            if posicaoAtual[0] + proximos_x >= 0 and posicaoAtual[0] + proximos_x < len(matriz) and posicaoAtual[1] + proximos_y >= 0 and posicaoAtual[1]  + proximos_y < len(matriz[0]):
                if (posicaoAtual[0] + proximos_x, posicaoAtual[1] + proximos_y) not in ja_visitados and (posicaoAtual[0] + proximos_x, posicaoAtual[1] + proximos_y) not in proximos_na_fila and matriz[posicaoAtual[0] + proximos_x][posicaoAtual[1] + proximos_y] != "#" and abs(proximos_x) != abs(proximos_y) :
                    proximos_na_fila.append((posicaoAtual[0] + proximos_x, posicaoAtual[1] + proximos_y))
                    caminhos[(posicaoAtual[0] + proximos_x, posicaoAtual[1] + proximos_y)] = posicaoAtual
                    
printou = False
for item in proximos_na_fila:
    matriz[item[0]][item[1]] = 'S'
    if item == Objetivo:
        resposta = []
        while True:
            if caminhos[item] == None:
                break
            else:
                resposta.append(item)
                item =  caminhos[item]
        print(len(resposta))
        printou = True
        break
    adicionarVizinhosNaFila(item)
if not printou: # uso apenas para focar no nosso boca, se não poderia colocar return encima e deixar o print em aberto em baixo
    print("N")