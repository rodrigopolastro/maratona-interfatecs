def least_loaded_server(servers: dict[int, list[int]]):
    min_load = len(servers[1])
    min_index = 1

    for server_id, load in servers.items():
        if len(load) < min_load:
            min_load = len(load)
            min_index = server_id

    return min_index

import heapq

s, r, a = map(int, [input() for _ in range(3)])

requests = []

for i in range(1, r + 1):
    t, d = map(int, input().split())
    heapq.heappush(requests, (t, i, d))

servers = {i: [] for i in range(1, s + 1)}

while requests:
    t, i, d = heapq.heappop(requests)

    for server_id in servers:
        if servers[server_id]:
            servers[server_id] = [x for x in servers[server_id] if x >= t]

    min_server = least_loaded_server(servers)

    if t == i:
        break

    servers[min_server].append(t + d - 1)

print(min_server)
