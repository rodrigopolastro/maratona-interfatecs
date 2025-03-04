################################################################################
# Objetivo: Determinar distância do menor caminho para sair de um labirinto sem
#           esbarrar em inimigos
# Autor: Rodrigo
# Data: 14/02/2025
# Duração: 53min
################################################################################
TAMANHO_LABIRINTO = 100
def posicoesVizinhas(posicao):
    i, j = posicao[0], posicao[1]
    vizinhosPossiveis = [
        (i, j-1),
        (i, j+1),
        (i-1, j),
        (i+1, j)
    ]
    posicoesVizinhas = []
    for vizinho in vizinhosPossiveis:
        if 0 <= vizinho[0] < TAMANHO_LABIRINTO and 0 <= vizinho[1] < TAMANHO_LABIRINTO:
            if labirinto[vizinho[0]][vizinho[1]] != 'INIMIGO':
                posicoesVizinhas.append(vizinho)
    
    return posicoesVizinhas

def tamanhoMenorCaminho():
    tamanhoCaminho = 0
    posicao = SAIDA
    while posicao != INICIO:
        tamanhoCaminho += 1
        posicao = posicoesAnteriores[posicao]
    
    return tamanhoCaminho
    

labirinto = [['' for i in range(TAMANHO_LABIRINTO)] for j in range(TAMANHO_LABIRINTO)]
INICIO = tuple([int(_) for _ in input().split()])
SAIDA = tuple([int(_) for _ in input().split()])

labirinto[INICIO[0]][INICIO[1]] = 'I'
labirinto[SAIDA[0]][SAIDA[1]] = 'S'

numInimigos = int(input())
for inimigo in range(numInimigos):
    iInimigo, jInimigo = [int(_) for _ in input().split()]
    labirinto[iInimigo][jInimigo] = 'INIMIGO'
    
max_l = 0
posicoesAnteriores = dict()
posicoesAnteriores[INICIO] = None
proximasPosicoes = [INICIO]
while len(proximasPosicoes) > 0:
    a = len(proximasPosicoes)
    if a > max_l:
        max_l = a
    posicaoAtual = proximasPosicoes.pop(0)
    
    if posicaoAtual == SAIDA:
        print(tamanhoMenorCaminho())
        print(max_l)

        quit()
    
    for proximaPosicao in posicoesVizinhas(posicaoAtual):
        if proximaPosicao in posicoesAnteriores:
            continue
        
        if proximaPosicao in proximasPosicoes:
            continue
            
        posicoesAnteriores[proximaPosicao] = posicaoAtual
        proximasPosicoes.append(proximaPosicao)
        
print(-1)