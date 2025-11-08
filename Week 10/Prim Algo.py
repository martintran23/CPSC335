from heapq import heappop , heappush # for our min-heap priority queue

def prim(graph, start):
    # Graph: dictionary of node -> list of (neighbor, weight)
    # Start: starting node, e.g., 'A'

    visited = set()                 # Track which nodes are already in the MST
    mst_edges = []                  # List to store edges in the final MST
    total_cost = 0                  # Running total of MST weight

    # Priority queue stores (edge_weight, from_node, to_node)
    pq = []
    visited.add(start)

    # Push all edges coming out of the starting node
    for neighbor, weight in graph[start]:
        heappush(pq, (weight, start, neighbor))

    # While we still have edges to explore
    while pq:
        weight, u, v = heappop(pq)

        # If target node already in MST, skip it
        if v in visited:
            continue

        # Otherwise, we take this edge as part of MST
        visited.add(v)
        mst_edges.append((u, v, weight))
        total_cost += weight

        # Now add all edges from this newly added node
        for neighbor, w in graph[v]:
            if neighbor not in visited:
                heappush(pq, (w, v, neighbor))

    # Return final MST
    return mst_edges, total_cost

# ------------------ Demo ------------------

if __name__ == "__main__":
    # Undirected weighted graph
    graph = {
        'A': [('B', 4), ('C', 2), ('D', 3)],
        'B': [('A', 4), ('D', 2)],
        'C': [('A', 2), ('D', 4)],
        'D': [('A', 3), ('B', 2), ('C', 4)]
    }

    start_node = 'A'
    mst, cost = prim(graph, start_node)

    print(f"Starting from {start_node}")
    print("Edges in the Minimum Spanning Tree:")
    for u, v, w in mst:
        print(f"{u} -- {v} (weight {w})")

    print(f"Total MST cost: {cost}")