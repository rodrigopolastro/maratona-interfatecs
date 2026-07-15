def bounded(pesos,valores,quantidades,capacidade):
    # print(pesos)
    # print(valores)
    # print(quantidades)
    # print(capacidade)

    n = len(pesos)
    dp= [[0] * (capacidade + 1) for _ in range(n + 1)]

    escolha = [[0]* (capacidade+1) for _ in range(n + 1)]

    for i in range(1,n+1):
        peso = pesos[i-1]
        valor = valores[i-1]
        max_q = quantidades[i-1]

        for w in range(capacidade + 1):
            dp[i][w] = dp[i-1][w]
            escolha[i][w] = 0
            # print(max_q)
            for k in range(1,max_q + 1):
                if k * peso <= w:
                    val = dp[i-1][w-k*peso] + k*valor
                    if val > dp[i][w]:
                        dp[i][w] = val
                        escolha[i][w] = k
    w = capacidade
    itens_usados = [0] * n 

    for i in range(n,0,-1):
        k = escolha[i][w]
        itens_usados[i-1] = k
        w -= k*pesos[i-1]
    
    return(dp[n][capacidade], sum(itens_usados))




entrada = input().split(' ')
nServicos = int(entrada[0])
rolo_restante = int(entrada[1]) * 100

pesos = []
quantidades = []
valores = []

for _ in range(nServicos):
    entrada1 = input().split(' ')
    descricao = int(entrada1[0].replace('x','').replace('10','',1))
    pesos.append(descricao)
    n_copias = int(entrada1[1])
    quantidades.append(n_copias)
    valor_unitario = int(entrada1[2])
    valores.append(valor_unitario)


#def bounded(pesos,valores,quantidades,capacidade):
valor_quantidade = bounded(pesos,valores,quantidades,rolo_restante)
valores_resposta = valor_quantidade[0]
quantidades_resposta = valor_quantidade[1]

status = ""
if sum(quantidades) == quantidades_resposta:
    status = "COMPLETO"
else:
    status = "PARCIAL"

print(status,valores_resposta)
