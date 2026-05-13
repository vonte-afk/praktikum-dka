import networkx as nx
import matplotlib.pyplot as plt

# 1. Buat graph
G = nx.Graph()

# 2. Tambah edge (SESUAI GAMBAR)
G.add_weighted_edges_from([
    ("Arad", "Zerind", 75),
    ("Zerind", "Oradea", 71),
    ("Oradea", "Sibiu", 151),
    ("Arad", "Sibiu", 140),
    ("Arad", "Timisoara", 118),
    ("Timisoara", "Lugoj", 111),
    ("Lugoj", "Mehadia", 70),
    ("Mehadia", "Drobeta", 75),
    ("Drobeta", "Craiova", 120),
    ("Craiova", "Rimnicu Vilcea", 146),
    ("Rimnicu Vilcea", "Sibiu", 80),
    ("Sibiu", "Fagaras", 99),
    ("Fagaras", "Bucharest", 211),
    ("Rimnicu Vilcea", "Pitesti", 97),
    ("Craiova", "Pitesti", 138),
    ("Pitesti", "Bucharest", 101),
    ("Bucharest", "Giurgiu", 90),
    ("Bucharest", "Urziceni", 85),
    ("Urziceni", "Hirsova", 98),
    ("Hirsova", "Eforie", 86),
    ("Urziceni", "Vaslui", 142),
    ("Vaslui", "Iasi", 92),
    ("Iasi", "Neamt", 87)
])

# 3. Shortest path semua pasangan
print("=== SHORTEST PATH EROPA ===")
for s in G.nodes():
    for t in G.nodes():
        if s != t:
            path = nx.shortest_path(G, s, t, weight='weight')
            dist = nx.shortest_path_length(G, s, t, weight='weight')
            print(f"{s} -> {t} = {path}, jarak = {dist}")

# 4. Visualisasi
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

plt.title("Graf Eropa")
plt.show()