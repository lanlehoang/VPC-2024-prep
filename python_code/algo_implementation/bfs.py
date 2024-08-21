"""
BFS traversal for simple directed graph
"""
def bfs(n, source, edges):
    # Convert edges to adjacency matrix
    adj_mat = [[0 for _ in range(n)] for _ in range(n)]
    for s, d in edges:
        adj_mat[s][d] = 1
    # Begin BFS
    queue = [source]
    traversal = [source]
    visited = set([source])
    while queue:
        node = queue.pop(0)
        for i in range(n):
            if adj_mat[node][i] == 1 and i not in visited:
                queue.append(i)
                visited.add(i)
                traversal.append(i)
    return traversal


if __name__ == "__main__":
    n, m = list(map(int, input().strip().split()))  # no. vertices, no. edges
    source = int(input().strip())    # source vertex
    edges = []
    for i in range(m):
        edges.append(list(map(int, input().strip().split())))   # source, destination
    print(bfs(n, source, edges))