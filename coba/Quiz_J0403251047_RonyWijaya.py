# ==============================================================================
# UJIAN TENGAH PRAKTIKUM - ALGORITMA & STRUKTUR DATA (TPL2106)
# Nama    : Rony Wijaya
# NIM     : J0403251047
# Kelas   : TPL B/P2
# ==============================================================================

# 1. FILE HANDLING & DICTIONARY (Sub-CPMK 1) [cite: 31]
def muat_data_buku(nama_file):
    """
    Fungsi untuk membaca 'buku.txt' dan menyimpannya ke Dictionary.
    Format file: kode_buku,judul,harga
    """
    database_buku = {}

    try:
        with open(nama_file, "r", encoding="utf-8") as file:
            for baris in file:
                baris = baris.strip()

                if not baris:
                    continue

                data = baris.split(",")

                if len(data) != 3:
                    continue

                kode, judul, harga = data

                database_buku[kode] = {
                    "judul": judul,
                    "harga": int(harga)
                }

    except FileNotFoundError:
        print("File buku.txt tidak ditemukan.")

    return database_buku


# 2. LINKED LIST - MANAJEMEN PROMOSI (Sub-CPMK 2) [cite: 32]
class Node:
    def __init__(self, kode_barang, judul, harga):
        self.kode_barang = kode_barang
        self.judul = judul
        self.harga = harga
        self.next = None


class LinkedListPromosi:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def tambah_buku_promosi(self, kode_barang, judul, harga):

        nodeBaru = Node(kode_barang, judul, harga)

        if self.is_empty():
            self.head = nodeBaru
        else:
            nodeBaru.next = self.head
            self.head = nodeBaru

        print("Buku berhasil ditambahkan ke promosi.")

    def tampilkan_promosi(self):

        if self.is_empty():
            print("Daftar promosi kosong.")
            return

        print("\n=== Daftar Buku Promosi ===")

        current = self.head
        no = 1

        while current is not None:
            print(f"{no}. {current.kode_barang} - {current.judul} - Rp{current.harga}")
            current = current.next
            no += 1


# 3. QUEUE - ANTIREAN KASIR (Sub-CPMK 3) [cite: 33]
class NodeQueue:
    def __init__(self, no, nama, servis):
        self.no = no
        self.nama = nama
        self.servis = servis
        self.next = None


class AntreanKasir:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, no, nama, servis):

        node_baru = NodeQueue(no, nama, servis)

        if self.is_empty():
            self.front = node_baru
            self.rear = node_baru
        else:
            self.rear.next = node_baru
            self.rear = node_baru

        print(f"Pelanggan {nama} dengan nomor antrian {no} telah ditambahkan.")

    def dequeue(self):

        if self.is_empty():
            print("Antrian kosong.")
            return None

        data = self.front
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        print(f"Pelanggan dilayani: {data.no} - {data.nama} - {data.servis}")

        return data


# 4. SORTING - LAPORAN TRANSAKSI (Sub-CPMK 4) [cite: 34]
def urutkan_transaksi(list_harga):

    for posisi in range(1, len(list_harga)):

        nilai_sekarang = list_harga[posisi]
        banding = posisi - 1

        while banding >= 0 and list_harga[banding] > nilai_sekarang:
            list_harga[banding + 1] = list_harga[banding]
            banding -= 1

        list_harga[banding + 1] = nilai_sekarang

    return list_harga


# ==============================================================================
# MAIN PROGRAM
# ==============================================================================
def main():
    data_buku = muat_data_buku("buku.txt")
    list_promosi = LinkedListPromosi()
    antrean = AntreanKasir()
    riwayat_transaksi = [150000, 50000, 200000, 75000, 120000]

    while True:

        print("\n--- SISTEM MANAJEMEN TOKO BUKU ---")
        print("1. Lihat Katalog Buku")
        print("2. Kelola Daftar Promosi (Linked List)")
        print("3. Kelola Antrean Kasir (Queue)")
        print("4. Lihat Laporan Penjualan Terurut (Sorting)")
        print("5. Keluar")

        pilihan = input("Pilih menu (1-5): ")

        if pilihan == '1':

            print("\n=== KATALOG BUKU ===")

            if not data_buku:
                print("Tidak ada data buku.")
            else:
                for kode, info in data_buku.items():
                    print(f"{kode} - {info['judul']} - Rp{info['harga']}")

        elif pilihan == '2':

            kode = input("Kode Buku: ")
            judul = input("Judul Buku: ")
            harga = int(input("Harga Buku: "))

            list_promosi.tambah_buku_promosi(kode, judul, harga)
            list_promosi.tampilkan_promosi()

        elif pilihan == '3':

            print("\n1. Tambah Antrean")
            print("2. Layani Pelanggan")

            pilih = input("Pilih: ")

            if pilih == "1":
                no = input("Nomor Antrian: ")
                nama = input("Nama Pelanggan: ")
                servis = input("Jenis Servis: ")

                antrean.enqueue(no, nama, servis)

            elif pilih == "2":
                antrean.dequeue()

        elif pilihan == '4':

            print("Harga Sebelum Urut:", riwayat_transaksi)

            hasil_sort = urutkan_transaksi(riwayat_transaksi.copy())

            print("Harga Sesudah Urut:", hasil_sort)

        elif pilihan == '5':
            print("Program selesai. Terima kasih.")
            break

        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()