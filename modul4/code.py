# =========================
# MODUL 4 - BFS & DFS
# =========================

import networkx as nx

# 1. Buat graph
G = nx.Graph()

G.add_edges_from([
    ("Tunjungan", "Gubeng"),
    ("Tunjungan", "Darmo"),
    ("Darmo", "Wonokromo"),
    ("Wonokromo", "Rungkut"),
    ("Gubeng", "Kenjeran"),
    ("Gubeng", "Rungkut"),
    ("Rungkut", "Lakarsantri"),
    ("Darmo", "Lakarsantri"),
    ("Kenjeran", "Rungkut")
])

# =========================
# 2. BFS (Breadth First Search)
# =========================
def bfs(graph, start):
    visited = []
    queue = []

    visited.append(start)
    queue.append(start)

    while queue:
        node = queue.pop(0)
        print(node, end=" ")

        for neighbor in graph.neighbors(node):
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)

# =========================
# 3. DFS (Depth First Search)
# =========================
def dfs(graph, node, visited=None):
    if visited is None:
        visited = []

    visited.append(node)
    print(node, end=" ")

    for neighbor in graph.neighbors(node):
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# =========================
# 4. RUN
# =========================
print("BFS dari Tunjungan:")
bfs(G, "Tunjungan")

print("\n\nDFS dari Tunjungan:")
dfs(G, "Tunjungan")