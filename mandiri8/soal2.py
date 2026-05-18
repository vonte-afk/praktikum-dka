import random

# Data tugas
tasks = ['A', 'B', 'C', 'D', 'E']

# Waktu pengerjaan setiap tugas
task_time = {
    'A': 7,
    'B': 3,
    'C': 6,
    'D': 2,
    'E': 5
}

# Menghitung total cost urutan tugas
# Semakin belakang posisi tugas,
# semakin besar pengaruh cost

def calculate_cost(order):

    # Menyimpan total cost
    total = 0

    # Menghitung cost setiap tugas
    for i in range(len(order)):

        # Mengambil waktu tugas
        time = task_time[order[i]]

        # Menambahkan cost
        total += (i + 1) * time

    return total

# Membuat seluruh neighbor
# Neighbor dibuat dengan menukar dua tugas

def generate_neighbors(order):

    # Menyimpan seluruh neighbor
    neighbors = []

    # Perulangan indeks pertama
    for i in range(len(order)):

        # Perulangan indeks kedua
        for j in range(i + 1, len(order)):

            # Menyalin solusi lama
            new_order = order[:]

            # Menukar posisi tugas
            new_order[i], new_order[j] = new_order[j], new_order[i]

            # Menyimpan neighbor baru
            neighbors.append(new_order)

    return neighbors

# Algoritma Hill Climbing
# Langkah:
# 1. Membuat solusi awal acak
# 2. Membuat seluruh neighbor
# 3. Memilih neighbor terbaik
# 4. Berhenti jika tidak ada solusi lebih baik

def hill_climbing(tasks):

    # Menyalin data tugas
    current_solution = tasks[:]

    # Mengacak solusi awal
    random.shuffle(current_solution)

    # Menghitung cost solusi awal
    current_cost = calculate_cost(current_solution)

    # Nomor iterasi
    iteration = 1

    # Menampilkan solusi awal
    print("Solusi Awal:")
    print(current_solution)

    print("Cost Awal:", current_cost)
    print()

    # Perulangan utama algoritma
    while True:

        # Membuat seluruh neighbor
        neighbors = generate_neighbors(current_solution)

        # Solusi terbaik sementara
        best_neighbor = current_solution
        best_cost = current_cost

        # Mengecek seluruh neighbor
        for neighbor in neighbors:

            # Menghitung cost neighbor
            neighbor_cost = calculate_cost(neighbor)

            # Jika neighbor lebih baik
            if neighbor_cost < best_cost:

                best_neighbor = neighbor
                best_cost = neighbor_cost

        # Jika tidak ada solusi lebih baik
        if best_cost >= current_cost:

            print("Tidak ditemukan solusi lebih baik")
            break

        # Menampilkan hasil iterasi
        print("Iterasi", iteration)
        print("Solusi:", best_neighbor)
        print("Cost:", best_cost)
        print()

        # Memperbarui solusi sekarang
        current_solution = best_neighbor
        current_cost = best_cost

        # Menambah iterasi
        iteration += 1

    # Menampilkan hasil akhir
    print("Solusi Terbaik:")
    print(current_solution)

    print("Total Cost Akhir:", current_cost)

# Program utama
hill_climbing(tasks)