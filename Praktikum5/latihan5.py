# ==========================================================
# Nama      : Faris Daffa Al Haq
# NIM       : J0403251042
# Kelas     : A1
# ==========================================================
# ==========================================================
# Studi Kasus: Generator PIN
# ==========================================================
# Fungsi buat PIN dengan panjang tertentu
def buat_pin(panjang, hasil=""):
    # Mengecek panjang PIN
    if len(hasil) == panjang:
        # Cetak PIN
        print("PIN:", hasil)
        # Balik ke fungsi
        return
    # Tambah angka ke PIN 
    for angka in ["0", "1", "2"]:
        # Panggil fungsi lagi dengan angka baru
        buat_pin(panjang, hasil + angka)
# Panggil fungsi
buat_pin(3)