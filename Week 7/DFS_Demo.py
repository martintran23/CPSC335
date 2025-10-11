# Directed Acylic Graph (DAG)
def dfs_cycle_and_topo(graph):
    color = {v:0 for v in graph}
    postorder = []

    has_cycle = False

    def visit(u):
        nonlocal has_cycle
        color[u] = 1
        for v in graph[u]:
            if color[v] == 0:
                visit(v)
            elif color[v] == 1:
                has_cycle = True
        color[u] = 2
        postorder.append(u)

    for node in graph:
        if color[node] == 0:
            visit(node)
        if has_cycle:
            return True, []

    topo = list(reversed(postorder))

    return False, topo

# Demonstration of DFS
if __name__ == "__main__":
    prereq_dag = {
        "CS1": ["CS2"],
        "CS2": ["ALGO"],
        "MATH": ["ALGO"],
        "ALGO": []

    }

    has_cycle, topo = dfs_cycle_and_topo(prereq_dag)
    print("Cycle in preque_dag?", has_cycle)
    print("One Valid course order:", topo)


    cyclic = {
        "A": ["B"],
        "B": ["C"],
        "C": ["A"]

    }

    cyc, topo2 = dfs_cycle_and_topo(cyclic)
    print("Cyclic in Cyclic?", cyc)
    print("Topo in Cyclic (should be empty):", topo2)