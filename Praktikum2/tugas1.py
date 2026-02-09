# ==========================================================
# TUGAS HANDS-ON MODUL 1
# Studi Kasus: Sistem Stok Barang Kantin (Berbasis File .txt)
#
# Nama :
# NIM :
# Kelas :
# ==========================================================

# -------------------------------
# Konstanta nama file
# -------------------------------
data_kantin = "stok_barang.txt"

# -------------------------------
# Fungsi: Membaca data dari file
# -------------------------------
def baca_stok(nama_file):
    """
    Membaca data stok dari file teks.
    Format per baris: KodeBarang,NamaBarang,Stok
    Output:
    - stok_dict (dictionary)
      key = kode_barang
      value = {"nama": nama_barang, "stok": stok_int}
    """
    stok_dict = {}
    try:
        with open(nama_file, "r", encoding="utf-8") as f:
            for baris in f:
                baris = baris.strip()
                if baris:  # Lewati baris kosong
                    bagian = baris.split(",")
                    if len(bagian) == 3:
                        kode_barang = bagian[0]
                        nama_barang = bagian[1]
                        stok_int = int(bagian[2])
                        stok_dict[kode_barang] = {"nama": nama_barang, "stok": stok_int}
    except FileNotFoundError:
        # Jika file belum ada, kembalikan dictionary kosong
        pass
    return stok_dict

# -------------------------------
# Fungsi: Menyimpan data ke file
# -------------------------------
def simpan_stok(nama_file, stok_dict):
    """
    Menyimpan seluruh data stok ke file teks.
    Format per baris: KodeBarang,NamaBarang,Stok
    """
    with open(nama_file, "w", encoding="utf-8") as f:
        for kode, data in stok_dict.items():
            f.write(f"{kode},{data['nama']},{data['stok']}\n")

# -------------------------------
# Fungsi: Menampilkan semua data
# -------------------------------
def tampilkan_semua(stok_dict):
    """
    Menampilkan semua barang di stok_dict.
    """
    if not stok_dict:
        print("Stok kosong.")
        return
    
    print("\n=== DAFTAR SEMUA BARANG ===")
    print(f"{'Kode':<10} | {'Nama':<20} | {'Stok':>5}")
    print("-" * 40)
    for kode, data in stok_dict.items():
        print(f"{kode:<10} | {data['nama']:<20} | {data['stok']:>5}")

# -------------------------------
# Fungsi: Cari barang berdasarkan kode
# -------------------------------
def cari_barang(stok_dict):
    """
    Mencari barang berdasarkan kode barang.
    """
    kode = input("Masukkan kode barang: ").strip()
    if kode in stok_dict:
        data = stok_dict[kode]
        print(f"\nKode: {kode}")
        print(f"Nama: {data['nama']}")
        print(f"Stok: {data['stok']}")
    else:
        print("Barang tidak ditemukan.")

# -------------------------------
# Fungsi: Tambah barang baru
# -------------------------------
def tambah_barang(stok_dict):
    """
    Menambah barang baru ke stok_dict.
    """
    kode = input("Masukkan kode barang baru: ").strip()
    nama = input("Masukkan nama barang: ").strip()
    
    if kode in stok_dict:
        print("Kode sudah digunakan.")
        return
    
    stok_awal = int(input("Masukkan stok awal: "))
    stok_dict[kode] = {"nama": nama, "stok": stok_awal}
    print(f"Barang '{nama}' berhasil ditambahkan.")

# -------------------------------
# Fungsi: Update stok barang
# -------------------------------
def update_stok(stok_dict):
    """
    Mengubah stok barang (tambah atau kurangi).
    Stok tidak boleh menjadi negatif.
    """
    kode = input("Masukkan kode barang yang ingin diupdate: ").strip()
    
    if kode not in stok_dict:
        print("Barang tidak ditemukan.")
        return
    
    print("Pilih jenis update:")
    print("1. Tambah stok")
    print("2. Kurangi stok")
    pilihan = input("Masukkan pilihan (1/2): ").strip()
    
    jumlah = int(input("Masukkan jumlah: "))
    
    if pilihan == "1":
        stok_dict[kode]["stok"] += jumlah
        print(f"Stok berhasil ditambah. Stok saat ini: {stok_dict[kode]['stok']}")
    elif pilihan == "2":
        stok_baru = stok_dict[kode]["stok"] - jumlah
        if stok_baru < 0:
            print("Error: Stok tidak boleh negatif. Update dibatalkan.")
        else:
            stok_dict[kode]["stok"] = stok_baru
            print(f"Stok berhasil dikurangi. Stok saat ini: {stok_dict[kode]['stok']}")
    else:
        print("Pilihan tidak valid.")

# -------------------------------
# Program Utama
# -------------------------------
def main():
    # Membaca data dari file saat program mulai
    stok_barang = baca_stok(data_kantin)
    
    while True:
        print("\n=== MENU STOK KANTIN ===")
        print("1. Tampilkan semua barang")
        print("2. Cari barang berdasarkan kode")
        print("3. Tambah barang baru")
        print("4. Update stok barang")
        print("5. Simpan ke file")
        print("0. Keluar")
        pilihan = input("Pilih menu: ").strip()
        
        if pilihan == "1":
            tampilkan_semua(stok_barang)
        elif pilihan == "2":
            cari_barang(stok_barang)
        elif pilihan == "3":
            tambah_barang(stok_barang)
        elif pilihan == "4":
            update_stok(stok_barang)
        elif pilihan == "5":
            simpan_stok(data_kantin, stok_barang)
            print("Data berhasil disimpan.")
        elif pilihan == "0":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Menjalankan program utama
if __name__ == "__main__":
    main()