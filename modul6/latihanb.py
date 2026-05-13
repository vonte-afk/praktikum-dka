import networkx as nx
import matplotlib.pyplot as plt

# Fungsi untuk menampilkan graf
def show_graph(G):
    pos = nx.spring_layout(G)
    
    nx.draw(G, pos,
            with_labels=True,
            node_color='lightblue',
            node_size=2000,
            font_color='black',
            font_weight='bold')
    
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    
    plt.show()

# ========================
# MEMBUAT GRAF JAWA
# ========================
G = nx.Graph()

edges = [
    ('Bandung', 'Jakarta', 150),
    ('Bandung', 'Cirebon', 130),
    ('Jakarta', 'Semarang', 450),
    ('Cirebon', 'Semarang', 250),
    ('Semarang', 'Surabaya', 350),
    ('Cirebon', 'Yogyakarta', 200),
    ('Yogyakarta', 'Surabaya', 300)
]

# Menambahkan edge ke graf
for u, v, w in edges:
    G.add_edge(u, v, weight=w)

# Menampilkan graf
show_graph(G)

# ========================
# PROSES DFS
# ========================
print("DFS dari Bandung:")

dfs = list(nx.dfs_edges(G, source='Bandung'))

path = ['Bandung']

for u, v in dfs:
    path.append(v)

# Output urutan DFS
for i, node in enumerate(path, start=1):
    print(f"{i}. {node}")