################################################################################
# Objetivo: Dada a sequência de variações mensais no preço de uma ação, 
#           determinar qual foi o período ideal para comprá-la e vendê-la 
#           a fim de obter o o maior lucro possível.
# 
#           Tecnicamente falando, trata-se do conhecido "Maximum Subarray Problem"
#           ou o problema da "Sublista Contígua de Soma Máxima".
# 
#           A solução apresentada aqui é pouco performática, pois tem 
#           complexidade quadrada. A melhor solução conhecida é o elegante 
#           "Algoritmo de Kadane", que possui complexidade algorítimica linear.
# 
# Autor: Rodrigo
# Data: 30/01/2025
# Duração: 25min
################################################################################

while True:
    qtdMeses = int(input())
    if qtdMeses == 0:
        break
    
    maiorVariacao = None
    mesInicial = mesFinal = None
    variacoes = []
    
    for _ in range(qtdMeses):
        variacoes.append(int(input()))
     
    for i in range(qtdMeses):
        for j in range(i, qtdMeses):
            somaPeriodo = sum(variacoes[i:j+1])
            if maiorVariacao == None or somaPeriodo >= maiorVariacao:
                maiorVariacao = somaPeriodo
                mesInicial, mesFinal = i+1, j+1
                
    print(mesInicial, mesFinal)