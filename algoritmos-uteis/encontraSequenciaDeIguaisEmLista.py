from math import inf

#encontra maior sequencia de elementos iguais em um array

def encontraMaiorSequenciaIgual(lista):
    indicesMaiorSequencia = list()
    tamanhoMaiorSequencia = -inf
    
    pecaAnterior = lista[0]
    posicoesSequencia = [0]
    for j in range(1, len(lista)):
        pecaAtual = lista[j]
        
        if pecaAtual == pecaAnterior:
            posicoesSequencia.append(j)
            if len(posicoesSequencia) > tamanhoMaiorSequencia:
                tamanhoMaiorSequencia = len(posicoesSequencia)
                indicesMaiorSequencia = posicoesSequencia
        else:
            pecaAnterior = pecaAtual
            posicoesSequencia = [j]
    return indicesMaiorSequencia  

lista = [1,1,1,12,34,5]
print(encontraMaiorSequenciaIgual(lista))