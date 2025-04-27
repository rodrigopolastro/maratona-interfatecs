from collections import Counter
entrada = input().split()
avaliar = Counter(entrada)
avaliar = dict(avaliar)
listaTupla = []
for chave,valor in avaliar.items():
    listaTupla.append((chave,valor))
listaTupla = list(sorted(listaTupla,key= lambda x: (x[0],x[1])))


for elemento in listaTupla:
    print(elemento[0],elemento[1])
