# feito por rodrigo
# 14/04/25
# inicio: 20:33
from collections import defaultdict

def dfs(modulo):
    if qtdVisitasModulos[modulo] == 2:
        print('usar injecao tardia')
        exit()
        
    qtdVisitasModulos[modulo] += 1
    for dependencia in modulosDependencias.get(modulo, set()):
        dfs(dependencia)

            


modulosDependencias = defaultdict(set)
qtdDependencias = int(input())
for _ in range(qtdDependencias):
    modulo, dependenciaModulo = input().split()
    modulosDependencias[modulo].add(dependenciaModulo)
# modulosDependencias = defaultdict()
# modulosDependencias['a'] = {'b', 'c'}
# modulosDependencias['b'] = {'c'}

# modulosVisitados

    
for modulo in modulosDependencias.keys():
    qtdVisitasModulos = defaultdict(int)
    # visitados = set()
    dfs(modulo)  
        
print('ok')