# ==============================================================
# Nama : Faris Daffa Al Haq
# NIM : J0403251042
# Kelas : A1
# Praktikum 13 - Graph III: Spanning Tree
# ==============================================================

# Representasi weighted graph
# Format data: (gedung1, gedung2, biaya)
edges = [
    ('GedungA', 'GedungB', 4),
    ('GedungA', 'GedungC', 2),
    ('GedungB', 'GedungD', 3),
    ('GedungC', 'GedungD', 1),
    ('GedungA', 'GedungD', 5)
]

# Daftar semua gedung
nodes = ['GedungA', 'GedungB', 'GedungC', 'GedungD']

# Algoritma Prim dimulai dari GedungA
visited = ['GedungA']
mst = []
total_biaya = 0

# Ulangi sampai semua gedung terhubung
while len(visited) < len(nodes):
    edge_terkecil = None

    # Cari edge termurah dari gedung yang sudah terhubung
    # ke gedung yang belum terhubung
    for gedung1, gedung2, biaya in edges:
        if gedung1 in visited and gedung2 not in visited:
            if edge_terkecil is None or biaya < edge_terkecil[2]:
                edge_terkecil = (gedung1, gedung2, biaya)

        if gedung2 in visited and gedung1 not in visited:
            if edge_terkecil is None or biaya < edge_terkecil[2]:
                edge_terkecil = (gedung2, gedung1, biaya)

    # Masukkan edge termurah ke MST
    mst.append(edge_terkecil)
    total_biaya += edge_terkecil[2]
    visited.append(edge_terkecil[1])

print("Edge yang dipilih:")
for gedung1, gedung2, biaya in mst:
    print(gedung1, "-", gedung2, "=", biaya)

print("Total biaya minimum =", total_biaya)

# Jawaban Analisis:
# 1. Algoritma apa yang digunakan?
#  Algoritma yang digunakan adalah Prim, yang membangun MST dengan menambahkan edge 
#  terdekat secara bertahap dari node awal.
# 2. Edge mana saja yang dipilih?
#  Edge yang dipilih adalah: ('GedungA', 'GedungC', 2), ('GedungC', 'GedungD', 1), ('GedungB', 'GedungD', 3)
# 3. Berapa total biaya minimum?
#  Total biaya minimum adalah 6.
# 4. Mengapa MST cocok digunakan pada kasus ini?
#  MST cocok digunakan pada kasus ini karena kita ingin menghubungkan semua gedung dengan biaya minimum, tanpa membentuk siklus.