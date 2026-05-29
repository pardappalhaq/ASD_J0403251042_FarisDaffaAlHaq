# ==============================================================
# Nama : Faris Daffa Al Haq
# NIM : J0403251042
# Kelas : A1
# Praktikum 13 - Graph III: Spanning Tree
# ==============================================================

# Daftar edge graph
edges = [
    ('A', 'B'),
    ('A', 'C'),
    ('A', 'D'),
    ('C', 'D'),
    ('B', 'D')
]
# Contoh spanning tree
spanning_tree = [
    ('A', 'C'),
    ('C', 'D'),
    ('D', 'B')
]

print("Edge pada graph:")
for edge in edges:
    print(edge)
    
print("\nSpanning Tree:")
for edge in spanning_tree:
    print(edge)
    
print("\nJumlah edge graph =", len(edges))
print("Jumlah edge spanning tree =", len(spanning_tree))

# Jawaban Analisis:
# 1. Apa perbedaan graph awal dan spanning tree? 
#  Graph awal adalah graph lengkap sesuai data aslinya, jadi bisa memiliki banyak edge dan 
#  mungkin ada cycle.Spanning tree adalah bagian dari graph awal yang tetap menghubungkan 
#  semua vertex, tetapi hanya memakai edge yang diperlukan.
# 2. Mengapa spanning tree tidak boleh memiliki cycle?
#  Karena spanning tree berbentuk tree. Dalam tree, antar vertex cukup ada satu jalur saja. 
#  Kalau ada cycle, berarti ada jalur berputar dan ada edge yang sebenarnya tidak perlu.
# 3. Mengapa jumlah edge spanning tree selalu lebih sedikit?
#  Karena spanning tree membuang edge yang tidak diperlukan, terutama edge yang 
#  menyebabkan cycle. 