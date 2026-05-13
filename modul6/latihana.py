import networkx as nx
import matplotlib.pyplot as plt

# Fungsi untuk menampilkan graf
def show_graph(G):
    # Menentukan posisi node secara otomatis
    pos = nx.spring_layout(G)
    
    # Menggambar graf
    nx.draw(G, pos,
            with_labels=True,          # Menampilkan nama node
            node_color='lightblue',    # Warna node
            node_size=2000,            # Ukuran node
            font_color='black',        # Warna teks (hitam)
            font_weight='bold')        # Tebal teks
    
    # Mengambil label weight pada edge
    edge_labels = nx.get_edge_attributes(G, 'weight')
    
    # Menampilkan weight pada edge
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    
    plt.show()

# ========================
# MEMBUAT GRAF EROPA
# ========================
G = nx.Graph()  # Membuat graph kosong (tidak berarah)

# Daftar edge beserta weight (jarak)
edges = [
    ('Arad', 'Zerind', 75),
    ('Arad', 'Timisoara', 118),
    ('Arad', 'Sibiu', 140),
    ('Zerind', 'Oradea', 71),
    ('Oradea', 'Sibiu', 151),
    ('Sibiu', 'Fagaras', 99),
    ('Sibiu', 'Rimnicu', 80)
]

# Menambahkan edge ke dalam graf
for u, v, w in edges:
    G.add_edge(u, v, weight=w)  # u dan v adalah node, w adalah weight

# Menampilkan graf
show_graph(G)

# ========================
# PROSES DFS
# ========================
print("DFS dari Arad:")

# Mengambil hasil DFS dalam bentuk edge
dfs = list(nx.dfs_edges(G, source='Arad'))

# Menyusun urutan node dari hasil DFS
path = ['Arad']  # Node awal

for u, v in dfs:
    path.append(v)  # Menambahkan node tujuan ke path

# Menampilkan urutan traversal DFS
for i, node in enumerate(path, start=1):
    print(f"{i}. {node}")