# Dijkstra Algorithm

from heapq import heappop, heappush

def dijkstra(graph, start):

    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    parent = {start: None}

    pq  = []
    heappush(pq, (0, start))
    visited = set()

    