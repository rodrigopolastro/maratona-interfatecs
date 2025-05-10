tamanho = int(input())
sequencia = [int(_) for _ in input().split()]
# tamanho = 10000
# sequencia = [i for i in range(tamanho)]

def kadane(lista):
    soma = 0
    maiorSoma = 0
    for valor in lista:
        soma = max(soma+valor, 0)
        maiorSoma = max(soma, maiorSoma)
    return maiorSoma

maiorSubsequencia = 0
for passo in range(1, int((tamanho/2)+1)):
    # print('passo', passo)
    for indexInicio in range(passo):
        listaComPassos = list()
        for indexElemento in range(indexInicio, tamanho, passo):
            listaComPassos.append(sequencia[indexElemento])
        somaLista = kadane(listaComPassos)
        # print(listaComPassos)
        maiorSubsequencia = max(maiorSubsequencia, somaLista)

print(maiorSubsequencia)
# for i in range(len(sequencia)):
#     for j in range(i, len(sequencia)):
