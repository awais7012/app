from collections import deque

def bfs(graph, start):
    """
    graph: dict[node] -> list of neighbors
    start: starting node
    returns list of nodes in BFS order
    """
    visited = set([start])
    order = []
    q = deque([start])

    while q:
        node = q.popleft()
        order.append(node)
        for nbr in graph.get(node, []):
            if nbr not in visited:
                visited.add(nbr)
                q.append(nbr)
    return order

# Example usage:
if __name__ == "__main__":
    G = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [], 'E': [], 'F': []
    }
    print(bfs(G, 'A'))  # ['A', 'B', 'C', 'D', 'E', 'F']
