from collections import defaultdict



def dfs(universo, ligacoes, universosVisitados):
    # if universo in universosVisitados:
    if universosVisitados[universo] == True:
        return
    
    universosVisitados[universo] = True
    for vizinho in ligacoes[universo]:
        dfs(vizinho, ligacoes, universosVisitados)
    
def ehConexo(qtdUniversos):
    ligacoes = defaultdict(list)
    
    for _ in range(qtdLigacoes):
        universo1, universo2 = [int(_) for _ in input().split()]
        ligacoes[universo1].append(universo2)
    
    for universoInicial in range(1, qtdUniversos+1):
        # print('iniciando busca em ', universoInicial)
        universosVisitados = [False for _ in range(qtdUniversos+1)]
        universosVisitados[0] = True #ignora o
        # universosVisitados.add(universoInicial)
        dfs(universoInicial, ligacoes, universosVisitados)
        # print('visitados partindo de ', universoInicial, ': ', universosVisitados)
        if False in universosVisitados:
            return False
    return True

respostas = list()
while True:
    qtdUniversos, qtdLigacoes = [int(_) for _ in input().split()]
    if qtdUniversos == qtdLigacoes == 0:
        break
        
    # print(ligacoes)
    if ehConexo(qtdUniversos):
        respostas.append('S')
        print('S')
    else:
        respostas.append('N')
        print('N')
# for r in respostas: print(r)