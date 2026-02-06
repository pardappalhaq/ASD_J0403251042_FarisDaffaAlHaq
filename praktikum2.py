# ===============================================
# Praktikum 2: Konsep ADT dan File Handling (STUDI KASUS)
# Latihan   1: Membuat Fungsi Load Data dari File
# Nama : Faris Daffa AlHaq
# NIM  : J0403251042
# ===============================================

#variabel menyimpan data file
nama_file = "data_mahasiswa.txt"

def baca_data(nama_file):
    data_dict = {} #inisialisasi data dictionary
    with open(nama_file, "r", encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip() #ambil data per baris dan hilangkan new line
            nim, nama, nilai = baris.split(",") #ambil data per item data
            data_dict[nim] = {"nama": nama,"nilai": int(nilai)} #masukan dalam dictionary
    return data_dict

#memanggil fungsi
buka_data = baca_data(nama_file)
print("jumlah data terbaca :", len(buka_data))

# ===============================================
# Praktikum 2: Konsep ADT dan File Handling (STUDI KASUS)
# Latihan   2: Membuat Fungsi Menampilkan Data
# ===============================================

def tampilkan_data(data_dict):
    print("\n=== Data Mahasiswa ===") #membuat header tabel
    print(f"{'NIM' : <10} | {'Nama' : <12} | {'Nilai' : >5}")
    print("-" * 35) #membuat garis pemisah
    for nim, data in data_dict.items():
        print(f"{nim : <10} | {data['nama'] : <12} | {data['nilai'] : >5}")
    print("-" * 35) #membuat garis pemisah

    #menampilkan isi datanya
    for nim in sorted(data_dict.keys()):
        nama = data_dict[nim]["nama"]
        nilai = data_dict[nim]["nilai"]
        print(f"{nim : <10} | {nama : <12} | {int(nilai) : >5}")
#memanggil fungsi
# tampilkan_data(buka_data)

# ===============================================
# Praktikum 2: Konsep ADT dan File Handling (STUDI KASUS)
# Latihan   3: Membuat Fungsi Mencari Data
# ===============================================

def cari_data(data_dict):
    #pencarian data berdasarkan NIM sebagai key dictionary
    #membuat input NIM Mahasiswa yang akan dicari
    nim_cari = input("Masukkan NIM yang akan dicari : ").strip()

    if nim_cari in data_dict:
        nama = data_dict[nim_cari]["nama"]
        nilai = data_dict[nim_cari]["nilai"]
        
        print("\n=== Data Mahasiswa Ditemukan ===")
        print(f"NIM : {nim_cari}")
        print(f"Nama : {nama}")
        print(f"Nilai : {nilai}")
    else:
        print("Data tidak ditemukan. Pastikan NIM yang dimasukkan benar")

#memanggil fungsi
# cari_data(buka_data)

# ===============================================
# Praktikum 2: Konsep ADT dan File Handling (STUDI KASUS)
# Latihan   4: Membuat Fungsi Update Data
# ===============================================

def ubah_data(data_dict):
    #awali dulu dengan mencari NIM / Data Mahasiswa yang ingin di ubah
    nim = input("Masukkan NIM yang akan diubah :").strip()

    if nim not in data_dict:
        print("NIM tidak ditemukan. Pastikan NIM yang dimasukkan benar")
        return

    try:
        nilai_baru = int(input("Masukkan nilai baru 0-100 :").strip())
    except ValueError:
        print("Nilai harus berupa angka. Update Dibatalkan")

    if nilai_baru < 0 or nilai_baru > 100:
        print("Nilai harus antara 0-100. Update Dibatalkan")

    nilai_lama = data_dict[nim]["nilai"]
    data_dict[nim]["nilai"] = nilai_baru

    print(f"Update Berhasil. Nilai {nim} dari {nilai_lama} menjadi {nilai_baru}")

#memanggil fungsi
# ubah_data(buka_data)

# ===============================================
# Praktikum 2: Konsep ADT dan File Handling (STUDI KASUS)
# Latihan   5: Membuat Fungsi Simpan Data
# ===============================================

def simpan_data(nama_file, data_dict):
    with open(nama_file, "w", encoding="utf-8") as file:
        for nim in sorted(data_dict.keys()):
            nama = data_dict[nim]["nama"]
            nilai = data_dict[nim]["nilai"]
            file.write(f"{nim},{nama},{nilai}\n")

#memanggil fungsi
# simpan_data(nama_file, buka_data)
print("\nData Berhasil Disimpan ke file: ", nama_file)

# ===============================================
# Praktikum 2: Konsep ADT dan File Handling (STUDI KASUS)
# Latihan   6: Membuat Menu Interaktif
# ===============================================

def main():
    #load data otomatis saat program dijalankan
    buka_data = baca_data(nama_file) #fs.1 fungsi load data

    while True:
        print("\n=== Menu Data Mahasiswa ===")
        print("1. Tampilkan Data Mahasiswa")
        print("2. Cari Data Mahasiswa")
        print("3. Ubah Data Mahasiswa")
        print("4. Simpan Data Mahasiswa")
        print("0. Keluar")

        pilihan = input("\nPilih Menu: ").strip()

        if pilihan == "1":
            tampilkan_data(buka_data)
        elif pilihan == "2":
            cari_data(buka_data)
        elif pilihan == "3":
            ubah_data(buka_data)
        elif pilihan == "4":
            simpan_data(nama_file, buka_data)
            print("\nData berhasil disimpan ke file: ", nama_file)
        elif pilihan == "0":
            print("\nTerima kasih. Program selesai.")
            break
        else:
            print("\nPilihan tidak valid. Silahkan pilih menu yang benar.")
if __name__ == "__main__":
    main()