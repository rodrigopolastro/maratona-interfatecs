numero = int(input())
divisores = 0
for i in range(1,numero+1):
    if numero % i == 0:
        divisores +=1
    if divisores > 3:
        print('nao')
        break
# maior número que ele pode colocar é 10000000 (1 milhao), python não tem um processamento tão ruim na casa dos milhões, por isso não vejo a
# necessidade de uma otimização
if divisores == 3:
    print('sim')
elif divisores < 3:
    print('nao')