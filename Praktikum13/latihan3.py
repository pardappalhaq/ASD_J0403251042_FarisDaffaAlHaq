# ==============================================================
# Nama : Faris Daffa Al Haq
# NIM : J0403251042
# Kelas : A1
# Praktikum 13 - Graph III: Spanning Tree
# ==============================================================

import heapq

graph = {
    'A': {'B': 4, 'C': 2, 'D': 5},
    'B': {'A': 4, 'D': 3},
    'C': {'A': 2, 'D': 1},
    'D': {'A': 5, 'B': 3, 'C': 1}
}
def prim(graph, start):
    
    visited = set([start])

    edges = []
    
    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))
        
    mst = []
    total_weight = 0
    
    while edges:   
        weight, u, v = heapq.heappop(edges)
    if v not in visited:
        visited.add(v)
        
        mst.append((u, v, weight))
        total_weight += weight
        
        
    for neighbor, w in graph[v].items():
        
        if neighbor not in visited:
            heapq.heappush(edges, (w, v, neighbor))

    return mst, total_weight

mst, total = prim(graph, 'A')

print("Minimum Spanning Tree:")

for edge in mst:
    print(edge)
    
print("Total bobot =", total)

# Jawaban Analisis:
# 1. Node awal apa yang digunakan?
#  Node awal yang digunakan adalah 'A'. Prim memulai dari node ini dan membangun MST dengan 
#  menambahkan edge terdekat secara bertahap.
# 2. Edge mana yang dipilih pertama kali?
#  Edge pertama yang dipilih adalah edge dengan bobot terkecil yang menghubungkan node 'A' 
#  dengan salah satu node tetangganya.
# 3. Bagaimana Prim menentukan edge berikutnya?
#  Prim menentukan edge berikutnya dengan memilih edge dengan bobot terkecil yang menghubungkan 
#  node yang sudah dikunjungi dengan node yang belum dikunjungi.
# 4. Berapa total bobot MST yang dihasilkan?
#  Total bobot MST yang dihasilkan adalah 6 (2 + 1 + 3).
# 5. Apa perbedaan pendekatan Prim dan Kruskal?
#  Prim mulai dari satu node, lalu berkembang ke node lain dengan memilih edge terkecil.
#  Kruskal memilih edge terkecil dari seluruh graph, lalu menghindari cycle.