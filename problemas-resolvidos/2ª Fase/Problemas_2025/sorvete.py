from math import inf

temperaturas = list()

qtdClientes, diferencaMaxima = [int(_) for _ in input().split()]
for _ in range(qtdClientes):
    tempCliente = int(input())
    temperaturas.append(tempCliente)

temperaturas.sort()
# print('temps: ', temperaturas)
qtdGrupos = 1
menorTempGrupo = temperaturas[0]    


for temp in temperaturas:
    diferencaAtual = temp - menorTempGrupo
    # print('dif do ', temp, ' pro ', menorTempGrupo, ' = ', diferencaAtual, ' | max -> ', diferencaMaxima)
    # id diferencaAtual <= diferencaMaxima:
    #     grupo
    if diferencaAtual > diferencaMaxima:
        qtdGrupos += 1
        menorTempGrupo = inf
    menorTempGrupo = min(menorTempGrupo, temp)
print(qtdGrupos)

  
