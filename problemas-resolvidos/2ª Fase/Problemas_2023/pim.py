numero = int(input())
resposta = []
for i in range(1,numero+1):
    if i % 4 == 0:
        resposta.append('pim')
    else:
        resposta.append(i)
print(*resposta)