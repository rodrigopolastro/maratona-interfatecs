from collections import defaultdict

def listaCaminho(pontoInicial, pontoFinal, pontosAnteriores):
    caminho = []
    tamanhoCaminho = 0
    pontoAtual = pontoFinal
    while pontoAtual != pontoInicial:
        caminho.append(pontoAtual)
        tamanhoCaminho += pontosAnteriores[pontoAtual][1]
        pontoAtual = pontosAnteriores[pontoAtual][0]

    return (caminho, tamanhoCaminho)
        
ligacoes = defaultdict(list)

qtdPontos, qtdLigacoes, pontoFinal = [int(_) for _ in input().split()]
for _ in range(qtdLigacoes):
    ponto1, ponto2, distancia = [int(_) for _ in input().split()]
    ligacoes[ponto1].append((ponto2, distancia))
    ligacoes[ponto2].append((ponto1, distancia))
    
proximosPontos = list()
pontosAnteriores = dict() #[atual] => [(anterior, distancia)]

proximosPontos = [(0, 0)]
# proximosPontos = [0]
pontosAnteriores[0] = (0, 0)
# caminhos = list()
menorCaminho = list()

while len(proximosPontos) > 0:
    proximosPontos.sort(key=lambda p: p[1])
    pontoAtual = proximosPontos.pop(0)[0]
    if pontoAtual == pontoFinal:
        caminho, tamanhoCaminho = listaCaminho(0, pontoFinal, pontosAnteriores)
        # caminhos.append((caminho, tamanhoCaminho))
        menorCaminho = '0 ' + ' '.join([str(i) for i in caminho[::-1]])
        # print('caminho encontrado: ', caminho, ' tamanho: ', tamanhoCaminho)
        # caminhos.append(caminho)
        # break
    
    for proximoPonto, distancia in ligacoes[pontoAtual]:
        distanciaTotal = pontosAnteriores[pontoAtual][1] + distancia
        # if 
        
        if proximoPonto in pontosAnteriores: #ver se o keys quebra
            distanciaAtual = pontosAnteriores[proximoPonto][1]
            if distanciaAtual < distanciaTotal:
                continue
            
        # pontosAnteriores[proximoPonto] = distanciaTotal
        # distanciaTotal = pontosAnteriores[pontoAtual][1] + distancia
        pontosAnteriores[proximoPonto] = (pontoAtual, distanciaTotal)
        # proximosPontos.append((proximoPonto, distancia))
        proximosPontos.append((proximoPonto, distanciaTotal))
        # quit() # nao sei se funcion
        
print(menorCaminho)
# print(caminhos)
# menorCaminho = sorted(caminhos, key=lambda c: c[1])[0][0]
# print(menorCaminho)