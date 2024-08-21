"""
DFS traversal for simple directed graph
Use stack instead of recursion
"""
def dfs(n, source, edges):
    # Convert edges to adjacency matrix
    adj_mat = [[0 for _ in range(n)] for _ in range(n)]
    for s, d in edges:
        adj_mat[s][d] = 1
    # Begin DFS
    stack = [source]
    traversal = []
    visited = set()
    while stack:
        node = stack.pop()
        for i in range(n):
            if adj_mat[node][i] == 1 and i not in visited:
                stack.append(i)
        traversal.append(node)
        visited.add(node)
    return traversal


if __name__ == "__main__":
    n, m = list(map(int, input().strip().split()))  # no. vertices, no. edges
    source = int(input().strip())    # source vertex
    edges = []
    for i in range(m):
        edges.append(list(map(int, input().strip().split())))   # source, destination
    print(dfs(n, source, edges))