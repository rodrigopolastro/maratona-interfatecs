################################################################################
# Objetivo:
# -> Dadas estações de energias numeradas e distâncias entre elas, determinar o menor 
#    caminho possível para interligar todas as estações.
# Comentários:
# -> É um problema de MST: Minimum SPanning Tree ou Árvore Geradora Mínima
# Autor: Rodrigo
# Data: 06/08/25
# Duração: 25m
################################################################################

ligacoes = list()
pai = list()
peso = list()

def find(a):
    if pai[a] == a:
        return a
    
    patriarca = find(pai[a])
    pai[a] = patriarca
    return patriarca
    
def union(a, b):
    paiA = find(a)
    paiB = find(b)
    
    if peso[paiA] > peso[paiB]: pai[paiB] = paiA
    elif peso[paiB] > peso[paiA]: pai[paiA] = paiB
    else: 
        pai[paiA] = paiB
        peso[paiA] = peso[paiA]+1

qtdEstacoes, qtdLigacoes = [int(_) for _ in input().split()]
pai = [i for i in range(qtdEstacoes)]
peso = [0 for _ in range(qtdEstacoes)]

for _ in range(qtdLigacoes):
    estacao1, estacao2, distancia = [int(_) for _ in input().split()]
    ligacoes.append((estacao1-1, estacao2-1, distancia))
    
ligacoes.sort(key=lambda l: l[2]) #ordena arestas pelo seu tamanho de forma crescente

tamanhoArvore = 0
qtdElementosArvore = 0
for ligacao in ligacoes:
    a, b, distancia = ligacao
    if find(a) != find(b): #verifica se pontos já não estão conectados
        union(a, b)
        qtdElementosArvore += 1
        tamanhoArvore += distancia
        if qtdElementosArvore == qtdEstacoes-1:
            break
print(tamanhoArvore)
