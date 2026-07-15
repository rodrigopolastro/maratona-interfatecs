entrada = input().split(' ')

capacidade = int(entrada[0]) * 60

n = int(entrada[1])
dp = [[0 for _ in range(capacidade + 1)] for _ in range(n + 1)]

valores = [] # valores
pesos = [] # pesos

for i in range(n * 2):
    entrada2 = input().split(' ')
    if i % 2 == 0:
        pass
    else:
        nota = int(entrada2[0])
        tempo = int(entrada2[1])
        valores.append(nota)
        pesos.append(tempo)


for i in range(1,n + 1):
    for w in range(capacidade + 1):
        if pesos[i-1] <= w:
            dp[i][w] = max(dp[i-1][w], valores[i-1] + dp[i-1][w-pesos[i-1]])
        else:
            dp[i][w] = dp[i-1][w]

print(dp[n][capacidade])

    

