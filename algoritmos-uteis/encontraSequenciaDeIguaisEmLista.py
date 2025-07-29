from math import inf

#encontra maior sequencia de elementos iguais em um array

def encontraMaiorSequenciaIgual(lista):
    maiorSequencia = list()
    tamanhoMaiorSequencia = -inf
    
    pecaAnterior = lista[0]
    posicoesSequencia = [0]
    for j in range(1, len(lista)):
        pecaAtual = lista[j]
        
        if pecaAtual == pecaAnterior:
            posicoesSequencia.append(j)
            if len(posicoesSequencia) > tamanhoMaiorSequencia:
                tamanhoMaiorSequencia = len(posicoesSequencia)
                maiorSequencia = posicoesSequencia
        else:
            pecaAnterior = pecaAtual
            posicoesSequencia = [j]
    return maiorSequencia  