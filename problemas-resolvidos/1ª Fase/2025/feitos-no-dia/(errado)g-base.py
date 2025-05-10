saidaGuarda1, rondaGuarda1 = [int(_) for _ in input().split()]
saidaGuarda2, rondaGuarda2 = [int(_) for _ in input().split()]

# saidaGuarda1 = -saidaGuarda1
# saidaGuarda2 = -saidaGuarda2

atual1 = -saidaGuarda1
lista1 = list()
while atual1 <= 5000:
    lista1.append(atual1)
    atual1 += rondaGuarda1

atual2 = -saidaGuarda2
set2 = set()
while atual2 <= 5000:
    set2.add(atual2)
    atual2 += rondaGuarda2

# set2 = set(lista2)
print(lista1[:10])
print(list(sorted(set2))[:10])
for elm in lista1:
    if elm in set2:
        print(elm)
        exit()

