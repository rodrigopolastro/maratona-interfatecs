from math import inf
custoEstaiada,custoTrelicada,orcamento = [int(x) for x in input().split()]
# custoEstaiada,custoTrelicada,orcamento = 4, 5, 20

combinacoes = list()

qtdDivisoesEstaiadas = orcamento // custoEstaiada

for qtdEstaiadas in range(0, qtdDivisoesEstaiadas+1):
    custoEstaiadas = qtdEstaiadas * custoEstaiada
    restante = orcamento - custoEstaiadas
    # print('custo estaiadas: ', custoEstaiadas, ', restante: ', restante)
    if restante % custoTrelicada == 0:
        qtdTrelicadas = int(restante / custoTrelicada)
        combinacao = (qtdEstaiadas, qtdTrelicadas) 
        combinacoes.append(combinacao)
        
# print('combinacoes: ', combinacoes)
if len(combinacoes) > 0:
    melhorCombinacao = sorted(combinacoes, key=lambda c: (c[0]+c[1], c[0]))[0]
    print(f"{melhorCombinacao[0]} {melhorCombinacao[1]}")
else:
    print('IMPOSSIVEL')
    