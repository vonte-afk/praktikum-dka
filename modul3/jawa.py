import networkx as nx
import matplotlib.pyplot as plt

# 1. Buat graph
G = nx.Graph()

# 2. Tambah edge (SESUAI GAMBAR)
G.add_weighted_edges_from([
    ("Jakarta", "Cirebon", 327),
    ("Jakarta", "Bandung", 270),
    ("Bandung", "Cirebon", 120),
    ("Bandung", "Yogyakarta", 373),
    ("Cirebon", "Semarang", 305),
    ("Cirebon", "Yogyakarta", 210),
    ("Semarang", "Yogyakarta", 109),
    ("Semarang", "Surakarta", 97),
    ("Yogyakarta", "Surakarta", 60),
    ("Semarang", "Surabaya", 369),
    ("Surakarta", "Malang", 370),
    ("Surabaya", "Malang", 94)
])

# 3. Shortest path semua pasangan
print("=== SHORTEST PATH JAWA ===")
for s in G.nodes():
    for t in G.nodes():
        if s != t:
            path = nx.shortest_path(G, s, t, weight='weight')
            dist = nx.shortest_path_length(G, s, t, weight='weight')
            print(f"{s} -> {t} = {path}, jarak = {dist}")

# 4. Visualisasi
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightgreen', node_size=2000)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

plt.title("Graf Pulau Jawa")
plt.show()