import random
import math

# Data koordinat kota
cities = [
    (0, 0),
    (2, 3),
    (5, 1),
    (6, 4),
    (8, 2)
]

# Menghitung jarak Euclidean antar dua kota
# Rumus:
# d = √((x2 - x1)^2 + (y2 - y1)^2)

def distance(city1, city2):

    # Mengambil koordinat kota pertama
    x1, y1 = city1

    # Mengambil koordinat kota kedua
    x2, y2 = city2

    # Mengembalikan hasil perhitungan jarak
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Menghitung total jarak seluruh rute
# Program menghitung:
# 1. Jarak antar kota berurutan
# 2. Jarak kembali ke kota awal

def total_distance(route):

    # Menyimpan total jarak
    total = 0

    # Menghitung jarak antar kota
    for i in range(len(route) - 1):

        total += distance(route[i], route[i + 1])

    # Menambahkan jarak dari kota terakhir ke kota awal
    total += distance(route[-1], route[0])

    return total

# Membuat seluruh neighbor
# Neighbor diperoleh dengan menukar posisi dua kota

def generate_neighbors(route):

    # Menyimpan seluruh neighbor
    neighbors = []

    # Perulangan indeks pertama
    for i in range(len(route)):

        # Perulangan indeks kedua
        for j in range(i + 1, len(route)):

            # Menyalin rute lama
            new_route = route[:]

            # Menukar posisi dua kota
            new_route[i], new_route[j] = new_route[j], new_route[i]

            # Menyimpan neighbor baru
            neighbors.append(new_route)

    return neighbors

# Algoritma Hill Climbing
# Langkah:
# 1. Membuat solusi awal acak
# 2. Membuat seluruh neighbor
# 3. Memilih neighbor terbaik
# 4. Berpindah ke solusi lebih baik
# 5. Berhenti jika tidak ada peningkatan

def hill_climbing(cities):

    # Menyalin data kota
    current_route = cities[:]

    # Mengacak solusi awal
    random.shuffle(current_route)

    # Menghitung total jarak solusi awal
    current_distance = total_distance(current_route)

    # Menampilkan solusi awal
    print("Rute Awal:")
    print(current_route)

    print("Total Jarak Awal:", round(current_distance, 2))
    print()

    # Perulangan utama algoritma
    while True:

        # Membuat seluruh neighbor
        neighbors = generate_neighbors(current_route)

        # Solusi terbaik sementara
        best_neighbor = current_route
        best_distance = current_distance

        # Mengecek semua neighbor
        for neighbor in neighbors:

            # Menghitung total jarak neighbor
            neighbor_distance = total_distance(neighbor)

            # Jika neighbor lebih baik
            if neighbor_distance < best_distance:

                best_neighbor = neighbor
                best_distance = neighbor_distance

        # Jika tidak ada solusi lebih baik
        if best_distance >= current_distance:

            print("Solusi optimal lokal telah ditemukan")
            break

        # Memperbarui solusi sekarang
        current_route = best_neighbor
        current_distance = best_distance

    # Menampilkan hasil akhir
    print()
    print("Rute Terbaik:")
    print(current_route)

    print("Total Jarak Terbaik:", round(current_distance, 2))

# Program utama
hill_climbing(cities)