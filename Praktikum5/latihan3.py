# ==========================================================
# Nama      : Faris Daffa Al Haq
# NIM       : J0403251042
# Kelas     : A1
# ==========================================================

# ==========================================================
# Latihan 3: Mencari Nilai Maksimum
# ==========================================================
# Fungsi buat nyari angka paling gede di list
def cari_maks(data, index=0):
    # Mengecek sampai elemen yang paling ujung kanan
    if index == len(data) - 1:
        # Kembalikan elemen terakhir
        return data[index]
    # Panggil fungsi ini lagi, tapi elemen selanjutnya
    maks_sisa = cari_maks(data, index + 1)
    
    # Mengecek apakah elemen saat ini lebih besar
    if data[index] > maks_sisa:
        # Kembalikan elemen saat ini
        return data[index]
    else:
        # Kembalikan maksimum sisa
        return maks_sisa
# Deretan angka buat dites
angka = [3, 7, 2, 9, 5]
# Panggil fungsi dan cetak hasil
print("Nilai maksimum:", cari_maks(angka)) # Output: Nilai maksimum: 9