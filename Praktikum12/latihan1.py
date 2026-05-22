# ==========================================================
# Nama : Faris Daffa Al Haq
# NIM  : J0403251042
# Kelas: A1
# Praktikum 12 Graph II: Shortest Path
# ==========================================================

# ==========================================================
# Latihan 1: Weighted Graph dan Perhitungan Jalur
# ==========================================================
# Representasi weighted graph menggunakan dictionary bersarang
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}
# Menghitung dua kemungkinan jalur dari A ke D
jalur_1 = graph['A']['B'] + graph['B']['D'] # A -> B -> D
jalur_2 = graph['A']['C'] + graph['C']['D'] # A -> C -> D

print("Jalur 1: A -> B -> D =", jalur_1)
print("Jalur 2: A -> C -> D =", jalur_2)

if jalur_1 < jalur_2:
    print("Jalur terpendek adalah A -> B -> D")
else:
    print("Jalur terpendek adalah A -> C -> D")

# Jawaban Analisis:
# 1. Berapa total bobot jalur A -> B -> D? = 9

# 2. Berapa total bobot jalur A -> C -> D? = 3

# 3. Jalur mana yang dipilih sebagai jalur terpendek? = A -> C -> D

# 4. Mengapa jalur terpendek tidak selalu ditentukan dari jumlah edge yang paling sedikit?
#    = Karena pada graph berbobot, setiap edge memiliki bobot yang berbeda-beda, 
#    sehingga untuk menentukan jalur terpendek tidak cukup dengan menghitung jumlah 
#    edge yang paling sedikit, melainkan harus menghitung total bobot dari setiap jalur
