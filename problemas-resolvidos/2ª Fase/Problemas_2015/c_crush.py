################################################################################
# Objetivo:
#
# Autor: Rodrigo
# Data: 26/07/2025
# Duração: 18:25
################################################################################

def encontraSequenciasEmLista(lista) -> dict:
    sequencias = {}

    pecaAnterior = None
    posicoesSequencia = []

    for i, peca in enumerate(lista):
        if peca == '.':
            if pecaAnterior is not None and len(posicoesSequencia) >= 3:
                sequencias[tuple(posicoesSequencia)] = pecaAnterior

            pecaAnterior = None
            posicoesSequencia = []
            continue

        if peca == pecaAnterior:
            posicoesSequencia.append(i)
        else:
            if len(posicoesSequencia) >= 3:
                sequencias[tuple(posicoesSequencia)] = pecaAnterior
            pecaAnterior = peca
            posicoesSequencia = [i]

    # eliminar a última sequência se for menor que 3
    if len(posicoesSequencia) >= 3:
        sequencias[tuple(posicoesSequencia)] = pecaAnterior

    return sequencias

def calculaPontuacao(tamanhoSequencia) -> int:
    if tamanhoSequencia < 3:
        return 0

    if tamanhoSequencia == 3:
        return 60

    if tamanhoSequencia == 4:
        return 120

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
            posicoesSequencias = encontraSequenciasEmLista(linha)
            numeroSequencias = len(posicoesSequencias)
            if numeroSequencias > 0:
                encontrouAlgumaSequencia = True
                for posicoes, peca in posicoesSequencias.items():
                    pontuacao += calculaPontuacao(len(posicoes))
                    sequencias.append(('linha', linha, posicoes, peca))
                    # marcar quais terá que eliminar
                    for indexColuna in posicoes:
                        eliminar.append((indexLinha, indexColuna))

        for indexColuna in range(colunas):
            coluna = [l[indexColuna] for l in matriz]
            posicoesSequencias = encontraSequenciasEmLista(coluna)
            numeroSequencias = len(posicoesSequencias)
            if numeroSequencias > 0:
                encontrouAlgumaSequencia = True
                for posicoes, peca in posicoesSequencias.items():
                    pontuacao += calculaPontuacao(len(posicoes))
                    sequencias.append(('coluna', coluna, posicoes, peca))
                    # marcar quais terá que eliminar
                    for indexLinha in posicoes:
                        eliminar.append((indexLinha, indexColuna))

        if encontrouAlgumaSequencia:
            for i, j in eliminar:
                matriz[i][j] = '.'
            eliminar = list()

            # descer peças de cima
            cList = list()
            for indexColuna in range(colunas):
                coluna = [l[indexColuna] for l in matriz]
                # for i in range(len(coluna)):
                #     if coluna[i] == '.':
                #         coluna.insert(0, coluna.pop(i))
                validos = [peca for peca in coluna if peca != '.']
                pontos = [peca for peca in coluna if peca == '.']
                coluna = pontos + validos
                cList.append(coluna)

            for l in range(linhas):
                matriz[l] = [c[l] for c in cList]

            # for c in cList
                #passa pontos pro começa

    return pontuacao

    # -> percorre linhas e colunas em busca de seuqneicas;
    # -> se encontrar uma sequencia, incrementa a pontuação e marca as posicoes
    # -> depois de encontrar todas as sequencias, remove as posicoes da matriz (seta para '')
    # -> se encontrou uma sequencia, repete o processo ate nao encontrar mais

try:
    while True:
        pontuacao = main()
        print(pontuacao)
except EOFError:
    pass
