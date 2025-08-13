from collections import defaultdict

dependencias = defaultdict(list)

BRANCO = 0
CINZA = 1
PRETO = 2

def temCiclo(node):
    if cor[node] == CINZA:
        return True
    
    if cor[node] == PRETO:
        return False
    
    cor[node] = CINZA
    
    for vizinho in dependencias[node]:
        if temCiclo(vizinho):
            return True
    
    cor[cor] = PRETO

qtdDependencias = int(input())
cor = defaultdict(lambda: BRANCO)
for _ in range(qtdDependencias):
    a, b = input().split()
    dependencias[a].append(b)
    
for modulo in dependencias:
    if cor[modulo] == BRANCO:
        if temCiclo(modulo):
            print('usar injecao tardia') #tem ciclo
            quit()
            
print('ok') #nao tem ciclo