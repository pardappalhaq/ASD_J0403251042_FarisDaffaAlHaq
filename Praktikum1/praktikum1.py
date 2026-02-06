print("====Membuka file dalam satu string====")
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    isi_file = file.read()
print(isi_file)

print("Tipe Data :", type(isi_file))

print("====Membuka file baris per baris====")
jumlah_baris = 0
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        jumlah_baris = jumlah_baris + 1
        baris = baris
        print("Baris ke -", jumlah_baris)
        print("Isi baris :", baris)
        
print("====Membuka file dan memisahkan data berdasarkan koma====")
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()
        nim, nama, nilai = baris.split(",")
        print("NIM :", nim, "| Nama :", nama, "| Nilai :", nilai)
        
print("====Membuka file dan menyimpan data ke dalam list====")
data_list = []
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()
        nim, nama, nilai = baris.split(",")
        data_list.append([nim, nama, int(nilai)])
print("Menampilkan list")
print(data_list)
print("Contoh Record ke-1", data_list[0])
print("Contoh Record ke-2", data_list[1])
print("Jumlah Record :", len(data_list))

print("====Menampilkan data dictionary====")
data_dict = {}
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()
        nim, nama, nilai = baris.split(",")
        data_dict[nim] = {
            "nama": nama,
            "nilai": int(nilai)
        }
print("Menampilkan dictionary")
print(data_dict)