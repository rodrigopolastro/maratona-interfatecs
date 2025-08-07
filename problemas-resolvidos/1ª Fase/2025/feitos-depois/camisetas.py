capacidade = int(input())

custo = []
valor = []

for _ in range(3):
    cus, val = [int(x) for x in input().split()]
    custo.append(cus)
    valor.append(val)

bag = [0 for _ in range(capacidade+1)]

for j in range(1, capacidade + 1):
    # print(j)
    for i in range(len(custo)):
        # print(i)
        # print(bag[j])
        # print(valor[i] + bag[j - custo[i]])
        if custo[i] <= j:
            bag[j] = max(bag[j], valor[i] + bag[j - custo[i]])


print(max(bag))
