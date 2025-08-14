from collections import defaultdict
vizinhos = defaultdict(list)

def temCiclo(node, anterior):
    if node in visitado:
        return True
    
    visitado.add(node)
    
    for vizinho in vizinhos[node]:
        if vizinho != anterior:
            if temCiclo(vizinho, node):
                return True
    return False
            
def grafoBidirecionalPossuiCiclo():
    modulosIniciais = list(vizinhos) #evitar "dictionary changed size during iteration"
    for modulo in modulosIniciais:
        if modulo not in visitado:
            if temCiclo(modulo, None):
                return True
    return False

qtdVizinhos = int(input())
visitado = set()
for _ in range(qtdVizinhos):
    a, b = input().split()
    vizinhos[a].append(b)
    vizinhos[b].append(a)
    
print(grafoBidirecionalPossuiCiclo())
    
    
    
    
    