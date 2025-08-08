estacoes = [None]
qtdEstacoes = int(input())
for _ in range(qtdEstacoes):
    estacoes.append(int(input()))
    
results = list()
for i in range(1, qtdEstacoes+1):
    atual = estacoes[i]
    esq, dir = None, None
    if 2*i <= qtdEstacoes:
        esq = estacoes[2*i]
    if 2*i+1 <= qtdEstacoes:
        dir = estacoes[2*i+1]
    proximos = list()
    if esq: proximos.append(esq)
    if dir: proximos.append(dir)
    
    for proximo in proximos:
        if proximo > atual:
            results.append(1)
        elif proximo < atual:
            results.append(-1)
filtrado = set(results)  
soma = sum(results)
if soma == len(results)*1:
    print(1)
elif soma == len(results)*-1:
    print(2)
else:
    print(0)    
    
