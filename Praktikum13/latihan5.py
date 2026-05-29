# ==============================================================
# Nama : Faris Daffa Al Haq
# NIM : J0403251042
# Kelas : A1
# Praktikum 13 - Graph III: Spanning Tree
# ==============================================================

# Representasi weighted graph
# Format: (router1, router2, bobot)
edges = [
    ('RouterA', 'RouterB', 3),
    ('RouterA', 'RouterC', 2),
    ('RouterB', 'RouterD', 5),
    ('RouterC', 'RouterD', 1),
    ('RouterB', 'RouterC', 4)
]

# Urutkan edge dari bobot terkecil
edges.sort(key=lambda x: x[2])

# Setiap router awalnya menjadi kelompok sendiri
parent = {
    'RouterA': 'RouterA',
    'RouterB': 'RouterB',
    'RouterC': 'RouterC',
    'RouterD': 'RouterD'
}


def find(router):
    # Mencari kelompok dari router
    if parent[router] != router:
        parent[router] = find(parent[router])
    return parent[router]


def union(router1, router2):
    # Menggabungkan dua kelompok router
    parent[find(router2)] = find(router1)


mst = []
total_bobot = 0

# Algoritma Kruskal
for router1, router2, bobot in edges:
    # Edge dipilih jika tidak membentuk cycle
    if find(router1) != find(router2):
        mst.append((router1, router2, bobot))
        total_bobot += bobot
        union(router1, router2)

print("Minimum Spanning Tree:")
for router1, router2, bobot in mst:
    print(router1, "-", router2, "=", bobot)

print("Total bobot minimum =", total_bobot)

# Jawaban Analisis:
# 1. Kasus apa yang dipilih?
#  Kasus yang dipilih adalah membangun jaringan komputer dengan biaya minimum menggunakan MST.
# 2. Algoritma apa yang digunakan?
#  Algoritma yang digunakan adalah Kruskal.
# 3. Edge mana saja yang dipilih dalam MST?
#  Edge yang dipilih dalam MST adalah: ('RouterA', 'RouterC', 2), ('RouterC', 'RouterD', 1), ('RouterA', 'RouterB', 3)
# 4. Berapa total bobot MST?
#  Total bobot MST adalah 6.
# 5. Mengapa edge tertentu tidak dipilih?
#  Edge tidak dipilih jika menghasilkan siklus dalam graf, yang berarti node-node tersebut 
#  sudah terhubung melalui jalur lain.