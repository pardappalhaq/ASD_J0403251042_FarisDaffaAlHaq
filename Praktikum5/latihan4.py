# ==========================================================
# Nama      : Faris Daffa Al Haq
# NIM       : J0403251042
# Kelas     : A1
# ==========================================================

# ==========================================================
# Latihan 4: Kombinasi Huruf
# ==========================================================
# Fungsi buat nyari kombinasi huruf
def kombinasi(n, hasil=""):
    # Mengecek panjang teks
    if len(hasil) == n:
        # Cetak teks
        print(hasil)
        # Balik ke fungsi
        return
    # Tambah huruf "A" ke hasil
    kombinasi(n, hasil + "A")
    # Tambah huruf "B" ke hasil
    kombinasi(n, hasil + "B")
# Panggil fungsi
kombinasi(2)