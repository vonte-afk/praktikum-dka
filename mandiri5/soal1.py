# Import library yang diperlukan
import networkx as nx
import matplotlib.pyplot as plt

# Fungsi untuk menampilkan graph
def show_graph(G, pos):
    # G   : objek graph
    # pos : posisi setiap node
    nx.draw(G, pos, with_labels=True)
    plt.show()

# Membuat graph kosong
G = nx.Graph()

# Menambahkan edge sesuai struktur tree
G.add_edges_from([
    ('A','B'), ('A','C'),
    ('B','D'), ('B','E'),
    ('C','F'), ('C','G')
])

# Menentukan posisi node agar membentuk tree
pos = {
    'A': (0, 2),
    'B': (-1, 1),
    'C': (1, 1),
    'D': (-1.5, 0),
    'E': (-0.5, 0),
    'F': (0.5, 0),
    'G': (1.5, 0)
}

# Menampilkan graph
show_graph(G, pos)

# Melakukan BFS dari node 'A'
bfs_edges = list(nx.bfs_edges(G, source='A'))

# Menampilkan urutan BFS dalam bentuk edge
print("Urutan BFS (edge):")
print(bfs_edges)

# Mengubah hasil BFS menjadi urutan node
bfs_nodes = ['A']
for u, v in bfs_edges:
    bfs_nodes.append(v)

# Menampilkan urutan BFS dalam bentuk node
print("Urutan BFS (node):")
print(bfs_nodes)