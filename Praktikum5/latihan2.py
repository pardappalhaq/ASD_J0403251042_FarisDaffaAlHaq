# ==========================================================
# Nama      : Faris Daffa Al Haq
# NIM       : J0403251042
# Kelas     : A1
# ==========================================================

# ==========================================================
# Latihan 2: Tracing Rekursi
# ==========================================================
# Fungsi buat hitung mundur dari angka 'n'
def countdown(n):
    # kalau angkanya sudah 0, stop rekursinya
    if n == 0:
        print("Selesai") # Cetak tulisan "Selesai"
        return # Langsung keluar dari fungsi

    # Cetak angka saat baru masuk ke fungsi
    print("Masuk:", n)

    # Panggil fungsi ini lagi, tapi angkanya dikurangi 1
    countdown(n - 1)

    # Cetak angka saat keluar dari fungsi
    print("Keluar:", n)

# Mulai hitung mundur dari angka 3
countdown(3)