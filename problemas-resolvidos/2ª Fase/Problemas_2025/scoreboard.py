problemas = int(input())
times = int(input())



resposta = []

for _ in range(times):
    
    time,fatec = input().split('|')
    pontuacoes = [int(x) for x in input().split()]
    acertos = 0
    tempo = 0
    for index in range(0,problemas*2,2):
        if pontuacoes[index+1] == 0: #nao acertou
            continue
        
        acertos +=1
        if pontuacoes[index] != 1:
            tempo += (pontuacoes[index+1]) + ((pontuacoes[index]-1) * 20) #erros
        else:
            tempo += pontuacoes[index+1]
    resposta.append([time,fatec,acertos,tempo])
    
resposta.sort(key = lambda x : (-x[2],x[3]))

for r in resposta:
    print(f"{r[0]} - {r[1]} ({r[2]},{r[3]})")
        