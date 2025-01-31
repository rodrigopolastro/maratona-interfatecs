while True:
    qtdMeses = int(input())
    if qtdMeses == 0:
        break
    
    maiorVariacao = -101
    mesInicial = mesFinal = None
    variacoes = []
    
    for _ in range(qtdMeses):
        variacoes.append(int(input()))
     
    for i in range(qtdMeses):
        for j in range(i, qtdMeses):
            somaPeriodo = sum(variacoes[i:j+1])
            if somaPeriodo >= maiorVariacao:
                maiorVariacao = somaPeriodo
                mesInicial, mesFinal = i+1, j+1
                
    print(mesInicial, mesFinal)