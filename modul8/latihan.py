import random

# Daftar kota
cities = ['A', 'B', 'C', 'D', 'E']

# Matriks jarak
distance = {
    'A': {'A':0,'B':10,'C':15,'D':20,'E':25},
    'B': {'A':10,'B':0,'C':35,'D':25,'E':15},
    'C': {'A':15,'B':35,'C':0,'D':30,'E':20},
    'D': {'A':20,'B':25,'C':30,'D':0,'E':10},
    'E': {'A':25,'B':15,'C':20,'D':10,'E':0}
}

# Fungsi hitung total jarak
def total_distance(route):
    total = 0
    for i in range(len(route) - 1):
        total += distance[route[i]][route[i+1]]
    total += distance[route[-1]][route[0]]  # kembali ke awal
    return total

# Fungsi untuk generate neighbor (swap 2 kota)
def get_neighbors(route):
    neighbors = []
    for i in range(len(route)):
        for j in range(i+1, len(route)):
            new_route = route[:]
            # tukar posisi
            new_route[i], new_route[j] = new_route[j], new_route[i]
            neighbors.append(new_route)
    return neighbors

# Algoritma Hill Climbing
def hill_climbing():
    # solusi awal random
    current = cities[:]
    random.shuffle(current)

    print("Solusi awal:", current)
    print("Jarak awal:", total_distance(current))
    print("="*40)

    while True:
        neighbors = get_neighbors(current)
        current_distance = total_distance(current)

        best_neighbor = None
        best_distance = current_distance

        # cari neighbor terbaik
        for neighbor in neighbors:
            d = total_distance(neighbor)
            if d < best_distance:
                best_neighbor = neighbor
                best_distance = d

        # jika tidak ada perbaikan → stop
        if best_neighbor is None:
            break

        # update solusi
        current = best_neighbor
        print("Update solusi:", current)
        print("Jarak:", best_distance)
        print("-"*40)

    return current, total_distance(current)

# Jalankan
best_route, best_dist = hill_climbing()

print("\nHASIL AKHIR")
print("Rute terbaik:", best_route)
print("Total jarak:", best_dist)