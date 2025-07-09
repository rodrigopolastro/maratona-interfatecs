'''

- armazena dados em matriz de distancias
- busca (dfs?) em elementos vizinhos
- armazena quais estacoes ja foram visitadas
- quando acabar os vizinhos, verifica ta

["0": [], "1": []]


'''
# distancias = [
#     [0, 1, 15, 6, 0] #0
#     [1, 0, 5, 14, 3] #1
#     [0, 1, 0, 6, 0] #2
#     [0, 1, 15, 0, 0] #3
#     [0, 1, 15, 0, 0] #4
# ]

visitados = list()
caminhoPercorrido = list()
menorDistancia = 0

# [0, 1, 3, 4]
def tamanhoCaminho(caminhoPercorrido):
    tamanho = 0
    for i in range(len(caminhoPercorrido)-1):
        tamanho += distancias[i][i+1]
    print(caminhoPercorrido ,' -> ' , tamanho)
    return tamanho

def dfs(inicio):
    global menorDistancia
    
    vizinhos = [[i, d] for i, d in enumerate(distancias[inicio]) if d > 0 and i not in visitados]
    print('vizinhos do ', inicio, ': ', vizinhos)
    if len(vizinhos) == 0:
        if len(caminhoPercorrido) == qtdEstacoes:
            menorDistancia = min(menorDistancia, tamanhoCaminho(caminhoPercorrido))
        caminhoPercorrido.pop()
        visitados.pop() 
        return   

    for indexVizinho, distanciaVizinho in vizinhos: #[0, 1, 15, 6, 0]      
        visitados.append(indexVizinho)
        caminhoPercorrido.append(indexVizinho)
        dfs(indexVizinho)           
    
qtdEstacoes, qtdLigacoes = [int(_) for _ in input().split()]
distancias = [[0 for i in range(qtdEstacoes)] for j in range(qtdEstacoes)]
for _ in range(qtdLigacoes):
    estacaoA, estacaoB, distancia = [int(_) for _ in input().split()]
    distancias[estacaoA-1][estacaoB-1] = distancia
    
for estacaoInicial in range(qtdEstacoes):
    visitados = [estacaoInicial]
    caminhoPercorrido = [estacaoInicial]
    dfs(estacaoInicial)

print(menorDistancia)