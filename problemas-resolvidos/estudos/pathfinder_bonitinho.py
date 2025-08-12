################################################################################
# Objetivo: Algoritmo pathfinder. Encontrar a distância do menor caminho até um 
#           objetivo desviando de obstáculos no cenário 
################################################################################

from pprint import pprint
from copy import deepcopy
import time
import os

def posicoesVizinhas(posicao, qtdLinhasCenario, qtdColunasCenario):
    i, j = posicao[0], posicao[1]
    posicoesVizinhasPossiveis = [
        (i,j+1),
        (i,j-1),
        (i+1,j),
        (i-1,j),    
    ]
    posicoesVizinhasValidas = []
    for posicao in posicoesVizinhasPossiveis:
        if 0 <= posicao[0] <= qtdLinhasCenario-1 and 0 <= posicao[1] <= qtdColunasCenario-1:
            posicoesVizinhasValidas.append(posicao)
        
    return posicoesVizinhasValidas


POSICAO_INICIAL = 2
    
def getMenorCaminho(posicaoInicial, posicaoFinal, posicoesAnteriores):
    caminhoPercorrido = []
    posicao = posicaoFinal
    while posicao != posicaoInicial:
        caminhoPercorrido.append(posicao)
        posicao = posicoesAnteriores[posicao]
        
    return caminhoPercorrido[::-1]
    
CENARIO = [
    ['I', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '#', '#', '#'],
    ['.', '.', '#', '#', '.', '.', ''],
    ['.', '.', '.', '.', '.', '#', 'F'],
]
QTD_LINHAS_CENARIO = 4
QTD_COLUNAS_CENARIO = 7
POSICAO_INICIAL = (0, 0)
POSICAO_FINAL = (3, 6)
BLOQUEIO = '#'

# posicaoSilas = []
# cenario = []
proximasPosicoes = list()
posicoesAnteriores = dict() 
proximasPosicoes.append((0,0)) 
posicoesAnteriores[(0,0)] = None
    
def obtemMenorCaminho():
    while len(proximasPosicoes) > 0:
        posicaoAtual = proximasPosicoes.pop(0)
        if posicaoAtual == POSICAO_FINAL:
            print('a')
            menorCaminho = getMenorCaminho(POSICAO_INICIAL, POSICAO_FINAL, posicoesAnteriores)
            return menorCaminho
        
        for proximaPosicao in posicoesVizinhas(posicaoAtual, QTD_LINHAS_CENARIO, QTD_COLUNAS_CENARIO):
            if proximaPosicao in posicoesAnteriores:
                continue
            
            if CENARIO[proximaPosicao[0]][proximaPosicao[1]] == BLOQUEIO:
                continue
            
            posicoesAnteriores[proximaPosicao] = posicaoAtual
            proximasPosicoes.append(proximaPosicao)
        
def clear_terminal():
    # Limpa a tela no Windows ou Linux/Mac
    os.system('cls' if os.name == 'nt' else 'clear')

# def print_matrix(matrix):
#     for row in matrix:
#         print(' '.join(str(cell) for cell in row))

def print_matrix(matrix):
    print("\033c", end='')
    render = ''
    for row in matrix:
        render += ' '.join(str(cell) for cell in row) + '\n'
    print(f'{render}\r', end='')
        
menorCaminho = obtemMenorCaminho()
cenario = deepcopy(CENARIO)
for passo in menorCaminho:
    clear_terminal()
    cenario[passo[0]][passo[1]] = 'O'
    print_matrix(cenario)
    time.sleep(0.25)
    # pprint(cenario)
    # print('-------------------')
# print(menorCaminho)

