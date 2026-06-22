import networkx as nx

# 1. Inisialisasi graf tidak berarah
G1 = nx.Graph()

# Menambahkan edge (node akan otomatis terbentuk)
edges_s1 = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D'), ('D', 'E')]
G1.add_edges_from(edges_s1)

# 2. Menghitung Degree dan Neighbor
print("--- HASIL SOAL 1 ---")
print("Degree dari setiap node:")
for node in G1.nodes():
    print(f"Node {node}: {G1.degree(node)}")

print(f"\nNeighbor dari node D: {list(G1.neighbors('D'))}")

# 3. Cek Siklus
has_cycle = nx.has_cycles(G1) if hasattr(nx, 'has_cycles') else any(nx.cycle_basis(G1))
print(f"\nApakah graf memiliki siklus? {has_cycle}")
if has_cycle:
    print(f"Siklus yang ditemukan: {nx.cycle_basis(G1)}")