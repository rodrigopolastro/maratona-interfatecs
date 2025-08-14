def dfs(grafo, node, visitados):
    if node in visitados:
        return
    visitados.add(node)
    for vizinho in grafo[node]:
        dfs(grafo, vizinho, visitados)

def eh_conexo(grafo):
    nodes = set(grafo.keys()) #assumindo que grafo é um dicionário de lista de adjacencias
    for inicio in nodes:
        visitados = set()
        dfs(grafo, inicio, visitados)

    return visitados == nodes


# Exemplo de uso:

# Grafo representado por lista/dicionário de adjacências
grafo_exemplo = {
    1: [2, 3],
    2: [1, 4],
    3: [1],
    4: [2]
}

print(eh_conexo(grafo_exemplo))  # True

grafo_nao_conexo = {
    1: [2],
    2: [1, 3],
    3: [1]
}

print(eh_conexo(grafo_nao_conexo))  # False
