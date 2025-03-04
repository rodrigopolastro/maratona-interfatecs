<<<<<<< HEAD
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
=======
entrada = tuple([int(_) for _ in input().split()])
saida = tuple([int(_) for _ in input().split()])
qtdMonstros = int(input())
matrizInicial = [
    list('.'*100) for _ in range(100)
]

for monstro in range(qtdMonstros):
    posicao_monstro = [int(_) for _ in input().split()]
    matrizInicial[posicao_monstro[0]][posicao_monstro[1]] = "#"

caminho = {entrada: None}
proximosNaLista = [entrada]



def varredura(posicao: tuple):
    
    # for x in [-1, 0, 1]:
    #     for y in [-1, 0, 1]:
            
    listaVerificar = [
        (posicao[0]-1, posicao[1]),
        (posicao[0]+1, posicao[1]),
        (posicao[0], posicao[1]+1),
        (posicao[0], posicao[1]-1),
    ]
        # if 0 <= posicao[0]+x < 100 and 0 <= posicao[1]+y < 100 and matrizInicial[posicao[0]+x][posicao[1]+y] != "#" and abs(x) != abs(y) and (posicao[0]+x, posicao[1]+y) not in proximosNaLista and (posicao[0]+x, posicao[1]+y) not in jaVisitados:
    for p in listaVerificar:
        if 0 <= p[0] < 100 and 0 <= p[1] < 100 and matrizInicial[p[0]][p[1]] != "#" and (p[0], p[1]) not in proximosNaLista and (p[0], p[1]) not in caminho:
            
                
            caminho[(p[0], p[1])] = posicao 
            proximosNaLista.append((p[0], p[1]))

while True:

    if proximosNaLista == []:
        break

    
    if proximosNaLista[0] == saida:
        break
    varredura(proximosNaLista[0])

    
    proximosNaLista.pop(0)

  

if saida not in caminho.keys():
    print(-1)
else:
   
    resposta = []
    while True:
        if caminho[saida] == None:
            break
        resposta.append(caminho[saida])
        saida = caminho[saida]
    print(len(resposta))
>>>>>>> aa4d7f79a210f6ee22da6383824a06536737e605
