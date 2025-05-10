f = input()
vt,ve = [int(x) for x in input().split()]
qtdf = int(input())
dados = []
md = dict()
for _ in range(qtdf):
    local=input().split('|')
    dados.append(local)
    if md.get(local[1]) == None:
        md[local[1]] = [(local[0],local[1],int(local[2]),int(local[3]))]
    else:
        md[local[1]].append((local[0],local[1],int(local[2]),int(local[3])))
no = dict()
# print(md)
for chave in md.keys():
    no[chave] = sorted(md[chave], key= lambda x: (-x[2],x[3]))
clas = []
espe = []
desc = []

    

for _ in range(ve):
    if len(no[f]) >= 1 and no[f][0][2] != 0:
        clas.append(no[f].pop(0))
        vt -= 1
# vt -= ve 
# print(clas)
a = list(no.keys())
# a.remove(f)
# print(a)
vc = a
# print(vc)

for _ in vc:
    if len(no[_]) > 0:
        if no[_][0][2] > 0:
            clas.append(no[_].pop(0))
            vt -= 1

lfin = []
for c in no.keys():
    lfin.extend(no[c])
lfin = sorted(lfin, key= lambda x : (-x[2],x[3]))
remover = []
for i in range(len(lfin)):
    if lfin[i][2] == 0:
        remover.append(i)
for _ in remover[::-1]:
    desc.append(lfin.pop(_))
lfin = sorted(lfin, key= lambda x : (-x[2],x[3]))
while vt > 0:
    if len(lfin) >= 1:
        clas.append(lfin.pop(0))
        vt-=1
    else:
        break

espe = lfin
# print(lfin)
cf = sorted(clas,key=lambda x: x[0])
ef = sorted(espe,key=lambda x: (-x[2],x[3]))
df = sorted(desc,key=lambda x: x[0])

print('Classificados para a Final')
for x in cf:
    print(f"{x[0]} - {x[1]} {x[2],x[3]}")
print()
print('Lista de Espera')
for x in ef:
    print(f"{x[0]} - {x[1]} {x[2],x[3]}")
print()
print('Desclassificados')
for x in df:
    print(f"{x[0]} - {x[1]} {x[2],x[3]}")
print()
print('Apuracao concluida!')
