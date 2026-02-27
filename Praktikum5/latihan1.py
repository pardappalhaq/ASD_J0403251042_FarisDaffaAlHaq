# ==========================================================
# Nama      : Faris Daffa Al Haq
# NIM       : J0403251042
# Kelas     : A1
# ==========================================================

# ==========================================================
# Latihan 1: Rekursi Pangkat
# ==========================================================
def pangkat(a, n):
    # Memeriksa apakah nilai eksponen (n) sudah mencapai 0
    if n == 0:
        # Kembalikan angka 1 (karena a^0 = 1)
        return 1

    # Kalikan 'a' dengan fungsi ini lagi, sambil kurangi pangkatnya 1
    return a * pangkat(a, n - 1)

# Hitung 2 pangkat 4 dan cetak hasilnya
print(pangkat(2, 4)) # Output: 16