import heapq

def ucs(graph, start, goal):
    pq = [(0, start, [start])]

    visited = set()
    visited_order = []     # node yang dikunjungi
    expansion_order = []   # urutan node diekspansi

    while pq:
        cost, node, path = heapq.heappop(pq)

        if node not in visited:
            visited.add(node)
            visited_order.append(node)
            expansion_order.append(node)

            if node == goal:
                return path, cost, visited_order, expansion_order

            # tambah tetangga ke queue
            for neighbor, weight in graph.get(node, []):
                if neighbor not in visited:
                    heapq.heappush(
                        pq,
                        (cost + weight, neighbor, path + [neighbor])
                    )

    return None, None, visited_order, expansion_order


# graf berbobot minimal 6 node
graph = {
    'A': [('B', 2), ('C', 5)],
    'B': [('D', 4), ('E', 10)],
    'C': [('F', 3)],
    'D': [('G', 6)],
    'E': [('G', 1)],
    'F': [('G', 2)],
    'G': []
}

# tampilkan seluruh graf (sesuai instruksi)
print("Graf:")
for node in graph:
    print(node, "->", graph[node])

# input kota asal dan tujuan
start = input("Masukkan kota asal: ").upper()
goal = input("Masukkan kota tujuan: ").upper()

# proses UCS
path, cost, visited_order, expansion_order = ucs(graph, start, goal)

# output hasil
if path:
    print("Jalur terbaik:", " -> ".join(path))
    print("Total biaya:", cost)
else:
    print("Jalur tidak ditemukan")

print("Node dikunjungi:", visited_order)
print("Urutan ekspansi:", expansion_order)