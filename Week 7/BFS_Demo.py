from collections import deque

def bfs_shortest_path(graph, start):
    dist = {v: float('inf') for v in graph}
    parent = {v: None for v in graph}
    visited = set()
    q = deque([start])
    visited.add(start)
    dist[start] = 0
    order = []

    while q:
        u = q.popleft()
        order.append(u)
        for v in graph[u]:

            if v not in visited:
                visited.add(v)
                dist[v] = dist[u] + 1
                parent[v] = u
                q.append(v)

    return dist, parent, order

def reconstruct_path(parent, start, target):
    rev_path = []
    cur = target
    while cur is not None:
        rev_path.append(cur)
        if cur == start:
            break
        cur = parent.get(cur, None)
    if not rev_path or rev_path[-1] != start:
        return []
    return list(reversed(rev_path))


# Demo BFS Function
if __name__ == "__main__":
    campus = {
        "CS": ["LIB", "GYM"],
        "LIB": ["CS", "CAFE"],
        "GYM": ["CS", "CAFE"],
        "CAFE": ["LIB", "GYM"]
    }


    dist, parent, order = bfs_shortest_path(campus, "CS")
    print("BFS order from CS: ", order)
    path = reconstruct_path(parent, "CS", "CAFE")
    print("Shortest (fewer hops) path CS -> CAFE: ", path)
