from collections import defaultdict
vizinhos = defaultdict(list)
BRANCO = 0 # nao visitado
CINZA  = 1 # visitado na stack atual
PRETO  = 2 # visitado e fora da stack atual

def temCiclo(node):
    #para grafos direcionaddos, só é ciclo se for repetido na stack atual
    if cor[node] == CINZA:
        return True
    
    if cor[node] == PRETO:
        return False
    
    cor[node] = CINZA
    
    for vizinho in vizinhos[node]:
        if temCiclo(vizinho):
            return True
    cor[node] = PRETO
    return False

def grafoDirecionadoPossuiCiclo():
    modulosIniciais = list(vizinhos) #evitar "dictionary changed size during iteration"
    for modulo in modulosIniciais:
        if cor[modulo] == BRANCO:
            if temCiclo(modulo):
                return True
    return False

qtdVizinhos = int(input())
cor = defaultdict(lambda: BRANCO)
for _ in range(vizinhos):
    a, b = input().split()
    vizinhos[a].append(b)
    
    
    
    
    
    