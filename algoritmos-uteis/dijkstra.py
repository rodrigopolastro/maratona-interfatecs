import heapq  # heapq é como uma "fila de prioridade" otimizada.
              # Sempre que tiramos um elemento, ele devolve o menor.
              # Aqui vamos usar para pegar sempre o nó com menor distância acumulada.

def dijkstra(graph, start) -> dict[str, float]:
    # Se o nó inicial não existir no grafo, não há nada para calcular
    if start not in graph:
        return {}

    # min_heap guarda pares (distância_acumulada, nó)
    # Começamos no nó inicial com distância 0
    min_heap = [(0, start)]

    # Distâncias conhecidas até cada nó começam como infinito (desconhecidas)
    distances = {node: float('inf') for node in graph}
    distances[start] = 0  # A distância até o ponto de partida é 0

    # Enquanto ainda houver nós para explorar
    while min_heap:
        # Pegamos o nó com a menor distância acumulada conhecida
        current_distance, current_node = heapq.heappop(min_heap)

        # Se essa distância não for a melhor encontrada para esse nó, ignoramos
        # Isso evita processar caminhos piores que já conhecemos
        if current_distance > distances[current_node]:
            continue

        # Para cada vizinho do nó atual...
        for neighbor, weight in graph[current_node].items():
            # Calculamos a distância até ele passando pelo nó atual
            distance = current_distance + weight

            # Se essa nova distância for menor que a distância conhecida
            if distance < distances[neighbor]:
                # Atualizamos a distância para esse vizinho
                distances[neighbor] = distance
                # E colocamos o vizinho na fila para explorar depois
                heapq.heappush(min_heap, (distance, neighbor))

    # Quando a fila acabar, temos as menores distâncias de 'start' para todos os nós
    return distances

# Grafo de exemplo: cada chave é um nó e cada valor é um dicionário de vizinhos com pesos
graph = {
    'A': { 'B': 1, 'C': 4},
    'B': { 'A': 1, 'C': 2, 'D': 5},
    'C': { 'A': 4, 'B': 2, 'D': 1},
    'D': { 'B': 5, 'C': 1},
}

# Calculamos as distâncias mais curtas partindo de 'A'
shortest_path = dijkstra(graph, 'A')
print(shortest_path)  # Exemplo: {'A': 0, 'B': 1, 'C': 3, 'D': 4}
