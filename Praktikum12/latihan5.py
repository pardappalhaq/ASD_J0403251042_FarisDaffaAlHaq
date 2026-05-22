# ==========================================================
# Nama : Faris Daffa Al Haq
# NIM  : J0403251042
# Kelas: A1
# Praktikum 12 Graph II: Shortest Path
# ==========================================================

# ==========================================================
# Latihan 5: Studi Kasus Jalur Terpendek Antar Kota
# Algoritma: Dijkstra
# ==========================================================

import heapq  # Modul untuk priority queue (antrian berprioritas)

# 1. Representasi graph berbobot menggunakan dictionary
# Setiap kota menyimpan tetangga beserta bobot (jarak) nya
graph = {
    'Bogor': {'Jakarta': 5, 'Depok': 2},
    'Depok': {'Jakarta': 2, 'Bandung': 6},
    'Jakarta': {'Bandung': 7},
    'Bandung': {}
}

# 2. Fungsi Dijkstra untuk mencari jarak terpendek
def dijkstra(graph, start):
    # Inisialisasi semua jarak ke infinity (tak hingga)
    distances = {node: float('inf') for node in graph}
    # Jarak dari node awal ke dirinya sendiri = 0
    distances[start] = 0
    # Priority queue berisi (jarak, node), dimulai dari node awal
    priority_queue = [(0, start)]

    while priority_queue:
        # Ambil node dengan jarak terkecil dari antrian
        current_distance, current_node = heapq.heappop(priority_queue)

        # Lewati jika sudah ditemukan jarak yang lebih pendek sebelumnya
        if current_distance > distances[current_node]:
            continue

        # Proses relaksasi: cek semua tetangga dari node saat ini
        for neighbor, weight in graph[current_node].items():
            # Hitung jarak baru melalui node saat ini
            distance = current_distance + weight

            # Jika jarak baru lebih kecil, update jarak terpendek
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# 3. Penentuan node awal
start_node = 'Bogor'

# 4. Jalankan Dijkstra dan tampilkan output jarak terpendek
hasil = dijkstra(graph, start_node)
print(f"Jarak terpendek dari {start_node}:")
for kota, jarak in hasil.items():
    print(f"{start_node} -> {kota} = {jarak}")

# Jawaban Analisis:
# 1. Node awal yang digunakan apa? = Bogor

# 2. Node mana yang memiliki jarak paling kecil dari node awal? = Depok, dengan jarak 2

# 3. Node mana yang memiliki jarak paling besar dari node awal? = Bandung, dengan jarak 7

# 4. Jelaskan bagaimana algoritma Dijkstra bekerja pada kasus yang Anda buat. = Dijkstra selalu memilih 
#    kota terdekat yang belum diproses, lalu mengecek apakah lewat kota itu bisa membuat jarak ke kota 
#    lain menjadi lebih pendek (relaksasi). Proses ini diulang sampai semua kota selesai diproses