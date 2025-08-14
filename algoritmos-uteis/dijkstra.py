import heapq 

def dijkstra(grafo, inicio):
    min_heap = [(0, inicio)] # min_heap guarda pares (distância_acumulada, nó)
    distancias = {node: float('inf') for node in grafo} # começam como infinito
    distancias[inicio] = 0  # A distância até o ponto de partida é 0
    anteriores = {node: None for node in grafo}  # armazenar o anteiror no menor caminho
 
    while min_heap:
        # Pegamos o nó com a menor distância acumulada conhecida
        distancia_atual, atual = heapq.heappop(min_heap)
        
        # Se essa distância não for a melhor encontrada para esse nó, ignoramos
        # Isso evita processar caminhos piores que já conhecemos
        if distancia_atual > distancias[atual]:
            continue

        for vizinho, peso in grafo[atual].items():
            # Calculamos a distância até ele passando pelo nó atual
            distancia = distancia_atual + peso

            # Se essa nova distância for menor que a distância conhecida
            if distancia < distancias[vizinho]:
                # 1 - Atualizamos a distância para esse vizinho
                distancias[vizinho] = distancia
                # 2 - Armazenamos o antrior do vizinho
                anteriores[vizinho] = atual
                # 3 - Colocamos o vizinho na fila para explorar depois
                heapq.heappush(min_heap, (distancia, vizinho))

    return (distancias, anteriores)

grafo = {
    'A': { 'B': 1, 'C': 4},
    'B': { 'A': 1, 'C': 2, 'D': 5},
    'C': { 'A': 4, 'B': 2, 'D': 1},
    'D': { 'B': 5, 'C': 1},
}

def reconstruir_caminho(inicio, fim, anteriores):
    caminho = []
    atual = fim
    while atual is not None:
        caminho.append(atual)
        atual = anteriores[atual]
    caminho.reverse()
    # Só retorna o caminho se ele começar no start (senão significa que não há caminho)
    return caminho if caminho[0] == inicio else []

distancias, anteriores = dijkstra(grafo, 'A')
print(distancias) # => {'A': 0, 'B': 1, 'C': 3, 'D': 4}
print(anteriores) # => {'A': None, 'B': 'A', 'C': 'B', 'D': 'C'}




