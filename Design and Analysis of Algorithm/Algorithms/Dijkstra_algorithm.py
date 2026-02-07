def dijkstra(graph, source):
    n = len(graph)
    visited = [False] * n
    dist = [float('inf')] * n

    dist[source] = 0

    for _ in range(n):
        # Step 1: find minimum distance vertex
        min_dist = float('inf')
        u = -1
        for i in range(n):
            if not visited[i] and dist[i] < min_dist:
                min_dist = dist[i]
                u = i

        visited[u] = True

        # Step 2: relax adjacent vertices
        for v in range(n):
            if graph[u][v] > 0 and not visited[v]:
                if dist[u] + graph[u][v] < dist[v]:
                    dist[v] = dist[u] + graph[u][v]

    return dist


graph = [
    [0, 4, 1, 0],
    [4, 0, 2, 5],
    [1, 2, 0, 8],
    [0, 5, 8, 0]
]

source = 0
print(dijkstra(graph, source))



# Dijkstra(G, s):
#     for each vertex v:
#         dist[v] = ∞
#         visited[v] = false

#     dist[s] = 0

#     for i = 1 to V:
#         u = minimum distance unvisited vertex
#         visited[u] = true

#         for each neighbor v of u:
#             if not visited[v] and dist[u] + w(u,v) < dist[v]:
#                 dist[v] = dist[u] + w(u,v)

#     return dist
