largura,altura,comandos = [int(x) for x in input().split()]

resposta = [0 for _ in range(largura+1)]

for _ in range(comandos):
    comeco,fim,compr = [int(x) for x in input().split()]
    for i in range(comeco,fim+1):
        resposta[i] += compr


alturaFinal = max(resposta)


if alturaFinal > altura:
    print("invalida")    
else:
    print(alturaFinal)