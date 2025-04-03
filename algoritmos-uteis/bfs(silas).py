################################################################################
# Objetivo: Algoritmo pathfinder. Encontrar a distância do menor caminho até um 
#           objetivo desviando de obstáculos no cenário 
################################################################################

posicaoSilas = []
cenario = []
proximasPosicoes = []
posicoesAnteriores = dict()   

def posicoesVizinhas(posicao):
    i, j = posicao[0], posicao[1]
     
    posicoesVizinhasPossiveis = [
        (i,j+1),
        (i,j-1),
        (i+1,j),
        (i-1,j),    
    ]
    
    posicoesVizinhasValidas = []
    for posicao in posicoesVizinhasPossiveis:
        if 0 <= posicao[0] <= linhasCenario-1 and 0 <= posicao[1] <= colunasCenario-1:
            posicoesVizinhasValidas.append(posicao)
        
    return posicoesVizinhasValidas
    
def imprimeTamanhoMenorCaminho():
    qtdMovimentos = 0
    caminhoPercorrido = []
    posicao = POSICAO_CHAVE
    while posicao != POSICAO_SILAS:
        qtdMovimentos+=1
        caminhoPercorrido.append(posicao)
        posicao = posicoesAnteriores[posicao]
        
    print(len(caminhoPercorrido))
    
forcaSilas = int(input())
linhasCenario, colunasCenario = [int(valor) for valor in input().split()]

for indexLinha in range(linhasCenario):
    linha = input().split()
    cenario.append(linha)
    
    if 'S' in linha:
        POSICAO_SILAS = (indexLinha, linha.index('S'))
        posicoesAnteriores[POSICAO_SILAS] = None
        proximasPosicoes.append(POSICAO_SILAS) 
        
    if 'K' in linha:
        POSICAO_CHAVE = (indexLinha, linha.index('K'))
    
while len(proximasPosicoes) > 0:
    posicaoAtual = proximasPosicoes.pop(0)
    if posicaoAtual == POSICAO_CHAVE:
        imprimeTamanhoMenorCaminho()
        quit()
       
    for proximaPosicao in posicoesVizinhas(posicaoAtual):
        if proximaPosicao in posicoesAnteriores:
            continue
        
        if cenario[proximaPosicao[0]][proximaPosicao[1]] == '#':
            continue
        
        if cenario[proximaPosicao[0]][proximaPosicao[1]].isdigit(): #is a number
            if int(cenario[proximaPosicao[0]][proximaPosicao[1]]) > forcaSilas:
                continue
        
        posicoesAnteriores[proximaPosicao] = posicaoAtual
        proximasPosicoes.append(proximaPosicao)
        
print('N')