################################################################################
# Objetivo:
#
# Autor: Rodrigo
# Data: 26/07/2025
# Duração: 999+h
################################################################################
#VERSAO ORIGINAL:# 
def encontraSequenciaEmLista(lista):
    pecaAnterior = lista[0]
    posicoesSequencia = [0]
    for j in range(1, len(lista)):
        pecaAtual = lista[j]
        # if pecaAtual == '.':
        #     continue
        
        if pecaAtual != '.' and pecaAtual == pecaAnterior:
            posicoesSequencia.append(j)
        else:
            if len(posicoesSequencia) >= 3:
                #a sequencia a ser estourada ja encontrou. volta pq não haverá outra
                break
            pecaAnterior = pecaAtual
            posicoesSequencia = [j]
    return posicoesSequencia  


def encontraSequenciaEmLista2(lista):
    pecaAnterior = None
    posicoesSequencia = []

    for j, pecaAtual in enumerate(lista):
        if pecaAtual == '.':
            if len(posicoesSequencia) >= 3:
                break
            pecaAnterior = None
            posicoesSequencia = []
        
        if pecaAtual == pecaAnterior:
            posicoesSequencia.append(j)
        else:
            if len(posicoesSequencia) >= 3:
                break
            pecaAnterior = pecaAtual
            posicoesSequencia = [j]

    return posicoesSequencia       
# from itertools import groupby
# def encontraSequenciaEmLista(arr):
#     # if not arr:
#     #     return []

#     # max_len = 0
#     # max_indices = []

#     # for _, g in groupby(enumerate(arr), key=lambda x: x[1]):
#     #     grupo = list(g)
#     #     idxs = [i for i, _ in grupo]
#     #     if len(idxs) > max_len:
#     #         max_len = len(idxs)
#     #         max_indices = idxs

#     # return max_indices
#     # previous = arr[0]
#     # for elem in arr[1:]:
#     max_len = 0
#     max_start_idx = 0
#     current_idx = 0

#     for _, group in groupby(arr):
#         group_size = sum(1 for _ in group)

#         if group_size > max_len:
#             max_len = group_size
#             max_start_idx = current_idx

#         current_idx += group_size

#     return list(range(max_start_idx, max_start_idx + max_len))
        

def calculaPontuacao(tamanhoSequencia):
    if tamanhoSequencia < 3:
        return 0
    
    if tamanhoSequencia == 3:
        return 60
    
    if tamanhoSequencia == 4:
        return 120
    
    if tamanhoSequencia >= 5:
        return 180
      
sequencias = list()
def main():
    #leitura da matriz
    linhas, colunas = [int(_) for _ in input().split()]
    i1, j1, i2, j2 = [int(_) for _ in input().split()]
    matriz = list()
    for _ in range(linhas):
        linha = input().split()
        matriz.append(linha)
    matriz[i1][j1], matriz[i2][j2] = matriz[i2][j2], matriz[i1][j1]
    
    # 5 5
    # 3 2 3 1
    # 2 3 3 1 4
    # 1 1 2 3 4
    # 1 1 2 2 3
    # 3 2 1 2 3
    # 4 4 3 3 1
    

    # linhas, colunas = 5,5
    # i1, j1, i2, j2 = 3, 2, 3, 1
    # matriz = list()
    # matriz.append([2, 3, 3, 1, 4])
    # matriz.append([1, 1, 2, 3, 4])
    # matriz.append([1, 1, 2, 2, 3])
    # matriz.append([3, 2, 1, 2, 3])
    # matriz.append([4, 4, 3, 3, 1])
    # matriz[i1][j1], matriz[i2][j2] = matriz[i2][j2], matriz[i1][j1]

    pontuacao = 0
    encontrouAlgumaSequencia = True
    eliminar = list()
    while encontrouAlgumaSequencia:
        encontrouAlgumaSequencia = False
        for indexLinha in range(linhas):
            linha = matriz[indexLinha]
            posicoesSequencia = encontraSequenciaEmLista(linha) 
            tamanhoSequencia = len(posicoesSequencia)
            if tamanhoSequencia >= 3:
                encontrouAlgumaSequencia = True
                pontuacao = pontuacao + calculaPontuacao(tamanhoSequencia)
                seq = [linha[x] for x in posicoesSequencia]
                sequencias.append(('linha ' , indexLinha, seq, linha))
                #marcar quais terá que eliminar
                for indexColuna in posicoesSequencia:
                    eliminar.append((indexLinha, indexColuna))
                
        for indexColuna in range(colunas):
            coluna = [l[indexColuna] for l in matriz]
            posicoesSequencia = encontraSequenciaEmLista(coluna) 
            tamanhoSequencia = len(posicoesSequencia)
            if tamanhoSequencia >= 3:
                encontrouAlgumaSequencia = True
                pontuacao = pontuacao + calculaPontuacao(tamanhoSequencia)
                seq = [coluna[x] for x in posicoesSequencia]
                sequencias.append(('coluna ' , indexColuna, seq, coluna))
                #marcar quais terá que eliminar
                for indexLinha in posicoesSequencia:
                    eliminar.append((indexLinha, indexColuna))
             
        if encontrouAlgumaSequencia:
            for i, j in eliminar:
                matriz[i][j] = '.'
            eliminar = list()
               
            # descer peças de cima
            cList = list()
            for indexColuna in range(colunas):
                coluna = [l[indexColuna] for l in matriz]
                for i in range(len(coluna)):
                    if coluna[i] == '.':
                        coluna.insert(0, coluna.pop(i))        
                cList.append(coluna)
                
            for l in range(linhas):
                matriz[l] = [c[l] for c in cList]
        # print('MATRIZ:')
        # for l in matriz:
        #     print(l)
        # from pprint import pprint
        # pprint(matriz)        
            # for c in cList 
                #passa pontos pro começa
    for s in sequencias:
        print(s)
    return pontuacao  
    
    # -> percorre linhas e colunas em busca de seuqneicas;
    # -> se encontrar uma sequencia, incrementa a pontuação e marca as posicoes
    # -> depois de encontrar todas as sequencias, remove as posicoes da matriz (seta para '')
    # -> se encontrou uma sequencia, repete o processo ate nao encontrar mais
    
try:
    # while True:
    #     pontuacao = main()
    #     print(pontuacao)
    # lista = ['.','.','.', '.',1,1,1, '.','.', '.', 2, 2, 2, 2]
    lista = ['2', '3', '4', '1', '.', '.', '.', '.', '4', '5', '2', '3', '1', '1', '5', '4', '1', '2', '3', '3', '1', '5', '2', '2', '4', '3', '2', '3', '1', '2', '1', '1', '3', '1', '2', '3', '5', '2', '2', '5', '5', '2', '2', '3', '3', '1', '4', '5', '3', '3', '1', '1', '2', '4', '2', '1', '3', '5', '4', '5', '2', '1']
    res = encontraSequenciaEmLista(lista)
    print(res)
    print([lista[x] for x in res])
except EOFError:
    pass