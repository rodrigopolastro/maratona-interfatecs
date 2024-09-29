verba = int(input())
localizacoes = int(input())
lista = []
for i in range(localizacoes):
    entrada = input().split(' ')
    lista.append((int(entrada[1]),int(entrada[2]),int(entrada[1])/int(entrada[2])))
from operator import itemgetter
resultado = sorted(lista,key=itemgetter(2))
local = 0
resultado_print = 0
for i in resultado:
    if local+i[0] > verba:
        pass
    else:
        local+=i[0]
        resultado_print+=i[1]
print(resultado_print)