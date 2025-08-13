################################################################################
# Objetivo: Algoritmo pathfinder. Encontrar a distância do menor caminho até um 
#           objetivo desviando de obstáculos no cenário 
################################################################################

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

proximasPosicoes = list()        # => fila de próximas posições (tuplas)
posicoesAnteriores = dict()      # => (iAtual, jAtual) -> (iAnterior, jAnterior)
proximasPosicoes.append((0,0))   # => inicia fila com posição inicial
posicoesAnteriores[(0,0)] = None # => posicao inicial não possui posição anterior
    
def buscaEmLargura():
    while len(proximasPosicoes) > 0:
        posicaoAtual = proximasPosicoes.pop(0)
        if posicaoAtual == POSICAO_FINAL:
            menorCaminho = getMenorCaminho(POSICAO_INICIAL, POSICAO_FINAL, posicoesAnteriores)
            return menorCaminho
        
        for proximaPosicao in posicoesVizinhas(posicaoAtual, QTD_LINHAS_CENARIO, QTD_COLUNAS_CENARIO):
            if proximaPosicao in posicoesAnteriores:
                continue
            
            if CENARIO[proximaPosicao[0]][proximaPosicao[1]] == BLOQUEIO:
                continue
            
            posicoesAnteriores[proximaPosicao] = posicaoAtual
            proximasPosicoes.append(proximaPosicao)
        
menorCaminho = buscaEmLargura()
print(menorCaminho)
# => [(0, 1), (1, 1), (2, 1), (3, 1), (3, 2), (3, 3), (3, 4), (2, 4), (2, 5), (2, 6), (3, 6)]

