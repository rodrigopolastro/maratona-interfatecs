numeros = [int(i) for i in input().split()]

pares = 0
impares = 0

if len(numeros) != 10:
    print("ERRO")
else:
    for i in numeros:
        if i % 2 == 0:
            pares+=1
        else:
            impares+=1

    print(pares, impares)

