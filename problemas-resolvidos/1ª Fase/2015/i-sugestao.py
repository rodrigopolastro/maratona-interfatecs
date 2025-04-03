################################################################################
# Objetivo: Implementar o sistema de sugestões do corretor de texto automático.
#
#           É dada uma lista de palavras conhecidas e uma de palavras incorretas.
#           O código deve verificar, para cada palavra incorreta, qual palavra 
#           conhecida está mais próxima. 
#           Para calcular o menor número de alterações necessárias entre 2 strings
#           é utilizado o algoritmo da distância de levenshtein.
# 
# Autor: Rodrigo
# Data: 14/03/2025
# Duração: umas 2 horas 
# (demorei pq assumi incorretamente que a matriz sempre era quadrada)
################################################################################

def distancia_levenshtein(incorreta, correta):
    linhas = len(incorreta)+1
    colunas = len(correta)+1

    matriz = [["" for _ in range(colunas)] for _ in range(linhas)]
    for i in range(linhas):
        matriz[i][0] = i

    for j in range(colunas):
        matriz[0][j] = j
    
    for i in range(1, linhas):
        for j in range(1, colunas):
            if incorreta[i-1] == correta[j-1]:
                matriz[i][j] = matriz[i-1][j-1]
            else:
                matriz[i][j] = min(matriz[i-1][j] + 1, matriz[i][j-1] + 1, matriz[i-1][j-1] + 1)
    
    return matriz[-1][-1]  

corretas = list()
incorretas = list()

qtd_corretas = int(input())
for _ in range(qtd_corretas):
    corretas.append(input())
    
qtd_incorretas = int(input())
for _ in range(qtd_incorretas):
    incorretas.append(input())
    
for incorreta in incorretas:
    menor_distancia = 99999999999
    mais_proxima = None
    for correta in corretas:
        distancia = distancia_levenshtein(incorreta, correta)    
        if distancia < menor_distancia:
            menor_distancia = distancia
            mais_proxima = correta
        elif distancia == menor_distancia:
            # pega a primeira por ordem alfabética
            lista = [mais_proxima, correta]
            lista.sort()
            mais_proxima = lista[0]
        
    print(f"voce quis dizer {mais_proxima} {menor_distancia}")            