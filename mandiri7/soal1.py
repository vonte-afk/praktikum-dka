import heapq  # priority queue

def ucs(graph, start, goal):
    pq = [(0, start, [start])]  # (cost, node, path)
    visited = set()

    while pq:
        cost, node, path = heapq.heappop(pq)
        # ambil node dengan cost terkecil

        if node == goal:
            return path, cost  # kalau sampai tujuan

        if node not in visited:
            visited.add(node)

            # cek semua tetangga
            for neighbor, weight in graph.get(node, []):
                if neighbor not in visited:
                    # masukkan ke queue dengan cost baru
                    heapq.heappush(
                        pq,
                        (cost + weight, neighbor, path + [neighbor])
                    )

    return None, None  # jika tidak ada jalur


# adjacency list sesuai instruksi
graph = {
    'A': [('B', 4), ('C', 2)],
    'B': [('D', 5)],
    'C': [('D', 1)],
    'D': [('E', 3)],
    'E': []
}

# input start dan goal
start = input("Masukkan node awal: ").upper()
goal = input("Masukkan node tujuan: ").upper()

# proses UCS
path, cost = ucs(graph, start, goal)

# output
if path:
    print("Jalur terpendek:", " -> ".join(path))
    print("Total cost:", cost)
else:
    print("Jalur tidak ditemukan")