# ==========================================================
# Nama      : Faris Daffa Al Haq
# NIM       : J0403251042
# Kelas     : A1
# ==========================================================

# ==========================================================
# Latihan Kuliah
# ==========================================================

# 1. Membuat cetakan "Kotak" (Node)
# Setiap kotak akan menyimpan 1 data, dan punya 2 tangan (kiri dan kanan)
class Node:
    def __init__(self, data):
        self.data = data
        self.kiri = None   # Tangan kiri awalnya kosong
        self.kanan = None  # Tangan kanan awalnya kosong

# 2. Fungsi untuk memasukkan data baru ke dalam Tree
def masukkan_data(akar, data_baru):
    # Jika tree masih kosong, data ini otomatis jadi akar (paling atas)
    if akar is None:
        return Node(data_baru)

    # Aturan BST: Jika data baru LEBIH KECIL, lempar ke KIRI
    if data_baru < akar.data:
        akar.kiri = masukkan_data(akar.kiri, data_baru)
    
    # Aturan BST: Jika data baru LEBIH BESAR, lempar ke KANAN
    else:
        akar.kanan = masukkan_data(akar.kanan, data_baru)

    return akar

# 3. Fungsi untuk mengecek isi Tree (In-order Traversal)
# Fungsi ini akan membaca Tree dari ujung kiri ke ujung kanan.
# Efek ajaibnya: Data yang dicetak akan otomatis terurut dari kecil ke besar!
def cetak_berurutan(akar):
    if akar is not None:
        cetak_berurutan(akar.kiri)       # Mampir ke kiri dulu
        print(akar.data, end=", ")       # Cetak datanya
        cetak_berurutan(akar.kanan)      # Baru mampir ke kanan

print("=== JAWABAN SOAL 1 (Angka) ===")
input_1 = [10, 15, 25, 17, 9, 7, 8]

# Angka pertama (10) otomatis jadi akar utama
akar_angka = Node(input_1[0])

# Masukkan sisa angkanya satu per satu
for angka in input_1[1:]:
    masukkan_data(akar_angka, angka)

print("Hasil urutan Tree (In-order):")
cetak_berurutan(akar_angka)
print("\n")


print("=== JAWABAN SOAL 2 (Huruf/String) ===")
# Note: String akan diurutkan berdasarkan abjad
input_2 = ["ORY", "JFK", "BRU", "DUS", "ZRH", "MEX", "ORD", "NRT", "ARN", "GLA", "GCM"]

# Kata pertama ("ORY") otomatis jadi akar utama
akar_huruf = Node(input_2[0])

# Masukkan sisa katanya satu per satu
for kata in input_2[1:]:
    masukkan_data(akar_huruf, kata)

print("Hasil urutan Tree (In-order):")
cetak_berurutan(akar_huruf)
print()