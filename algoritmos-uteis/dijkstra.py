import heapq # é um array que faz uma espécie de autosort

def dijkstra(graph, start) -> dict[str, float]:
    if start not in graph:
        return {} # não existe o nó inicial no grafo

    min_heap = [(0, start)]
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    while min_heap:
        current_distance, current_node = heapq.heappop(min_heap)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(min_heap, (distance, neighbor))

    return distances

graph = {
    'A': { 'B': 1, 'C': 4},
    'B': { 'A': 1, 'C': 2, 'D': 5},
    'C': { 'A': 4, 'B': 2, 'D': 1},
    'D': { 'B': 5, 'C': 1},
}

shortest_path = dijkstra(graph, 'A')
print(shortest_path)
