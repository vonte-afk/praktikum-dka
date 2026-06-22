import networkx as nx

# 1. Inisialisasi graf berbobot
G2 = nx.Graph()

# Menambahkan edge beserta bobotnya (weight)
G2.add_edge('A', 'B', weight=4)
G2.add_edge('A', 'C', weight=2)
G2.add_edge('B', 'C', weight=1)
G2.add_edge('B', 'D', weight=5)
G2.add_edge('C', 'D', weight=8)
G2.add_edge('C', 'E', weight=10)
G2.add_edge('D', 'E', weight=2)

print("--- HASIL SOAL 2 ---")
# 2. Menentukan jalur dengan total weight terkecil dari A ke E
shortest_path = nx.shortest_path(G2, source='A', target='E', weight='weight')
shortest_path_length = nx.shortest_path_length(G2, source='A', target='E', weight='weight')

print(f"Jalur optimal (bobot terkecil) dari A ke E: {' -> '.join(shortest_path)}")
print(f"Total weight jalur tersebut: {shortest_path_length}")