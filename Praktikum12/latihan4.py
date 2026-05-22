# ==========================================================
# Nama : Faris Daffa Al Haq
# NIM  : J0403251042
# Kelas: A1
# Praktikum 12 Graph II: Shortest Path
# ==========================================================

# ==========================================================
# Latihan 4: Studi Kasus Jalur Terpendek Lokasi Kampus
# Algoritma: Dijkstra
# ==========================================================

import heapq

# Graph lokasi kampus
# Bobot menunjukkan waktu tempuh dalam menit
graph = {
    'Gerbang': {'Perpustakaan': 6, 'Kantin': 2},
    'Perpustakaan': {'Lab': 3},
    'Kantin': {'Lab': 4, 'Aula': 7},
    'Lab': {'Aula': 1},
    'Aula': {}
}

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

hasil = dijkstra(graph, 'Gerbang')
print("Jarak terpendek dari Gerbang Kampus:")
for lokasi, jarak in hasil.items():
    print(lokasi, "=", jarak, "menit")

# Jawaban Analisis:
# 1. Lokasi mana yang paling dekat dari Gerbang? = Kantin, dengan waktu tempuh 2 menit

# 2. Berapa waktu tempuh terpendek dari Gerbang ke Aula? = 7 menit, melalui jalur: Gerbang → Kantin (2) → Lab (4) → Aula (1) = 2 + 4 + 1 = 7 menit

# 3. Apakah jalur langsung selalu menghasilkan jarak paling kecil? Jelaskan. = Tidak, karena
#    Meskipun jalur langsung dari Gerbang ke Perpustakaan hanya memerlukan 6 menit,
#    namun jalur melalui Kantin (2 menit) lalu ke Lab (4 menit) dan Aula (1 menit) 
#    secara total menjadi 7 menit. Dalam kasus ini, jalur tidak langsung (Gerbang -> 
#    Kantin -> Lab -> Aula) ternyata lebih efisien untuk mencapai tujuan akhir (Aula) 
#    dibandingkan jalur langsung ke Perpustakaan yang memakan waktu lebih lama.

# 4. Mengapa Dijkstra cocok digunakan pada kasus lokasi kampus ini? = Karena Dijkstra cocok digunakan pada kasus lokasi kampus karena 
#    Dijkstra adalah algoritma yang efisien untuk menemukan jarak terpendek dari satu 
#    sumber ke semua node lain dalam graph berbobot dengan bobot positif, 
#    seperti waktu tempuh antar lokasi kampus.