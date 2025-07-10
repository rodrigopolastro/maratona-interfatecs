# duração: 10min
# 03/04/25
from operator import itemgetter

qtdCasos = int(input())
for _ in range(qtdCasos):
    nomes = list()
    qtdPessoas = int(input())
    for _ in range(qtdPessoas):
        nome = input()
        nomes.append((len(nome), nome))
    nomesOrdenados = sorted(nomes, key=itemgetter(0, 1))
    for i in range(qtdPessoas):
        separador = ".\n" if i == qtdPessoas-1 else ', '
        print(nomesOrdenados[i][1], end=separador)
        