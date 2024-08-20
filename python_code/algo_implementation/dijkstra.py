"""
Given number of vertices and edges, the source vertex, and edges info
Return the shortest distances from the source vertex to every other one
Implement for directed graph (adjust adjacency matrix creation for undirected graph)
Assume that the graph is simple
"""
def dijkstra_shortest_path(n, source, edges):
    # Convert edges to adjacency matrix
    INF = 10**10    # Replace with a huge number that will 100% exceed problem distance constraint
    adj_mat = [[INF for _ in range(n)] for _ in range(n)]
    for i in range(n):
        adj_mat[i][i] = 0
    for s, d, dist in edges:
        adj_mat[s][d] = dist
    # Begin the algorithm
    shortest_dists = [INF for _ in range(n)]
    shortest_dists[source] = 0
    fixed_nodes = set([source])

    def update_dists(node):
        for i in range(n):
            if shortest_dists[i] > shortest_dists[node] + adj_mat[node][i]:
                shortest_dists[i] = shortest_dists[node] + adj_mat[node][i]
        # Fix next node
        next_shortest, next_node = INF, 0
        for i in range(n):
            if shortest_dists[i] < next_shortest and i not in fixed_nodes:
                next_shortest = shortest_dists[i]
                next_node = i
        fixed_nodes.add(next_node)
        return next_node
    
    for i in range(n - 1):  # Need to fix n - 1 more nodes
        source = update_dists(source)
    return shortest_dists


if __name__ == "__main__":
    n, m = list(map(int, input().strip().split()))  # Number of vertices and edges
    source = int(input().strip())
    edges = []
    for i in range(m):
        edges.append(list(map(int, input().strip().split())))   # source, destination, distance
    print(dijkstra_shortest_path(n, source, edges))