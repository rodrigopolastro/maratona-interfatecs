from math import inf

# solução óptima usando o algoritmo de kadane

def kadane(qtdMeses, variacoes):
    maiorVariacao = max(variacoes)
    if maiorVariacao < 0: return maiorVariacao
    
    maiorSoma = -inf
    soma = 0
    for variacao in variacoes:
        soma = max(soma, soma + variacao)
        maiorSoma = max(soma, maiorSoma)
        
    return maiorSoma

# while True:
#     qtdMeses = int(input())
#     if qtdMeses == 0:
#         break
    
#     variacoes = []   
#     for _ in range(qtdMeses):
#         variacoes.append(int(input()))
        
def maiorSoma(qtdMeses, variacoes):
    soma = variacoes[0]
    maiorSoma = -inf
    mesInicial = 0
    mesFinal = 0

    for i in range(1, qtdMeses):
        if soma + variacoes[i] > soma:
            soma += variacoes[i]
            mesFinal = i
        else:
            soma = 0
            mesInicial = i
    
        if soma > maiorSoma:
            maiorSoma = soma
                       
    return([mesInicial+1, mesFinal+1])
# x = float('-inf')
# print(x>1)

lista = [-1,-2,-3]
print(kadane(len(lista), lista))
print(maiorSoma(len(lista), lista))