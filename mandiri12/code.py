import networkx as nx

# --- SOLUSI A: Membuat Graf Berbobot ---
G = nx.Graph()

# Menambahkan edge berdasarkan tabel jarak (km)
edges = [
    ("Malang", "Blitar", 45),
    ("Malang", "Pasuruan", 55),
    ("Blitar", "Tulungagung", 35),
    ("Blitar", "Kediri", 40),
    ("Tulungagung", "Kediri", 30),
    ("Kediri", "Jombang", 45),
    ("Pasuruan", "Sidoarjo", 40),
    ("Pasuruan", "Probolinggo", 50),
    ("Probolinggo", "Sidoarjo", 80),
    ("Jombang", "Sidoarjo", 50),
    ("Jombang", "Surabaya", 70),
    ("Sidoarjo", "Surabaya", 25)
]

for u, v, w in edges:
    G.add_edge(u, v, weight=w)

# --- SOLUSI B: Membuat Fungsi Heuristik ---
# Kamus nilai h(n) ke Surabaya berdasarkan tabel koordinat
heuristic_values = {
    "Malang": 117,
    "Blitar": 125,
    "Tulungagung": 111,
    "Kediri": 90,
    "Pasuruan": 72,
    "Probolinggo": 90,
    "Jombang": 56,
    "Sidoarjo": 25,
    "Surabaya": 0
}

def heuristic_func(u, v):
    # Karena target nx.astar_path selalu tujuan (Surabaya),
    # kita bisa langsung mengembalikan nilai heuristik dari node asal 'u' ke Surabaya.
    return heuristic_values.get(u, 0)

# --- SOLUSI C & D: Menjalankan A* & Menampilkan Rute ---
start_node = "Malang"
goal_node = "Surabaya"

# Menemukan rute terpendek menggunakan A*
rute = nx.astar_path(G, source=start_node, target=goal_node, heuristic=heuristic_func, weight='weight')

# Menghitung total jarak dari rute yang ditemukan
total_jarak = nx.path_weight(G, rute, weight='weight')

print("HASIL ALGORITMA A")
print(f"Rute yang ditemukan : {' -> '.join(rute)}")
print(f"Total Jarak         : {total_jarak} km")