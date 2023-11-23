import heapq

def prim(graph):
    start_node = list(graph.nodes)[0]
    visited = set([start_node])
    edges = [(graph[u][v]['distance'], u, v) for u, v in graph.edges(start_node)]
    heapq.heapify(edges)
    minimum_spanning_tree = []

    while edges:
        distance, frm, to = heapq.heappop(edges)

        if to not in visited:
            visited.add(to)
            minimum_spanning_tree.append((frm, to, distance))

            for next_to in graph.neighbors(to):
                if next_to not in visited:
                    heapq.heappush(edges, (graph[to][next_to]['distance'], to, next_to))

    return minimum_spanning_tree
