# Import library
import networkx as nx
import matplotlib.pyplot as plt

# Fungsi untuk menampilkan graph
def show_graph(G):
    """
    Menampilkan graph dengan posisi node berdasarkan bobot (jarak)
    """
    # Posisi node dihitung otomatis berdasarkan bobot
    pos = nx.kamada_kawai_layout(G, weight='weight')

    # Mengambil label bobot
    labels = nx.get_edge_attributes(G, 'weight')

    # Menggambar graph
    nx.draw(G, pos, with_labels=True)

    # Menampilkan bobot pada edge
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    plt.show()

# Membuat graph
G = nx.Graph()

# Menambahkan edge berbobot
G.add_weighted_edges_from([
    ('Bandung', 'Jakarta', 150),
    ('Bandung', 'Yogyakarta', 380),
    ('Jakarta', 'Semarang', 450),
    ('Yogyakarta', 'Surabaya', 330),
    ('Semarang', 'Surabaya', 350)
])

# Menampilkan graph
show_graph(G)

# BFS dari node 'Bandung'
bfs_edges = list(nx.bfs_edges(G, source='Bandung'))

# Output BFS
print("Urutan BFS (edge):")
print(bfs_edges)