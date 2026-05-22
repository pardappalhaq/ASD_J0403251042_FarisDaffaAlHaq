# ==============================================================================
# UJIAN TENGAH PRAKTIKUM - ALGORITMA & STRUKTUR DATA (TPL2106)
# Nama    : Faris Daffa Al Haq
# NIM     : J0403251042
# Kelas   : A1
# ==============================================================================

# 1. FILE HANDLING & DICTIONARY (Sub-CPMK 1) [cite: 31]
def muat_data_buku(nama_file):
    """
    Fungsi untuk membaca 'buku.txt' dan menyimpannya ke Dictionary.
    Format file: kode_buku,judul,harga
    """
    database_buku = {}
    try:
        with open(nama_file, 'r') as file:
            for baris in file:
                # Menghapus spasi/newline berlebih dan memisahkan berdasarkan koma
                kode_buku, judul, harga = baris.strip().split(',')
                # Menyimpan judul dan harga sebagai dictionary di dalam dictionary utama
                database_buku[kode_buku] = {'judul': judul, 'harga': int(harga)}
    except FileNotFoundError:
        print(f"Peringatan: File {nama_file} tidak ditemukan. Pastikan file berada di direktori yang sama.")
    return database_buku

# 2. LINKED LIST - MANAJEMEN PROMOSI (Sub-CPMK 2) [cite: 32]
class Node:
    def __init__(self, judul): # Node untuk menyimpan judul buku promosi
        self.judul = judul # Data yang disimpan adalah judul buku
        self.next = None # Untuk ke node berikutnya

class LinkedListPromosi:
    def __init__(self): # Linked List untuk menyimpan daftar buku promosi
         self.head = None 

    def tambah_buku_promosi(self, judul): # Method untuk menambah buku ke daftar promosi
        """Menambahkan buku ke daftar promosi (Linked List)"""
        node_baru = Node(judul) # Membuat node baru dengan judul buku yang diberikan
        if self.head is None: # Jika daftar promosi masih kosong, node baru menjadi head
            self.head = node_baru # Jika daftar promosi sudah ada, tambahkan node baru di akhir daftar
        else:
            current = self.head 
            while current.next is not None: 
                current = current.next
            current.next = node_baru
        print(f"Sukses: '{judul}' ditambahkan ke daftar promosi.")

    def tampilkan_promosi(self):
        """Menampilkan semua buku dalam daftar promosi"""
        if self.head is None: # Jika daftar promosi kosong, tampilkan pesan
            print("\nDaftar promosi saat ini kosong.")
            return
        
        print("\n--- Daftar Buku Promosi ---")
        current = self.head 
        nomor = 1
        while current is not None: # Menampilkan judul buku promosi satu per satu dengan nomor urut
            print(f"{nomor}. {current.judul}") 
            current = current.next 
            nomor += 1

# 3. QUEUE - ANTIREAN KASIR (Sub-CPMK 3) [cite: 33]
class AntreanKasir:
    def __init__(self): # Queue untuk mengelola antrean pelanggan di kasir
        self.antrean = [] # List untuk menyimpan nama pelanggan dalam antrean

    def tambah_antrean(self, nama_pelanggan): 
        """Menambah antrean (Enqueue)"""
        self.antrean.append(nama_pelanggan) # Menambahkan nama pelanggan ke akhir antrean
        print(f"Pelanggan '{nama_pelanggan}' masuk ke antrean. Posisi: {len(self.antrean)}") # Menampilkan posisi pelanggan dalam antrean setelah ditambahkan

    def layani_pelanggan(self):
        """Menghapus antrean (Dequeue)"""
        if len(self.antrean) == 0: # Jika antrean kosong, tampilkan pesan bahwa tidak ada pelanggan yang bisa dilayani
            print("Tidak ada pelanggan dalam antrean.")
        else:
            pelanggan_dilayani = self.antrean.pop(0) # Mengambil nama pelanggan yang paling depan dalam antrean untuk dilayani
            print(f"Mulai melayani pelanggan: '{pelanggan_dilayani}'. Sisa antrean: {len(self.antrean)}")

# 4. SORTING - LAPORAN TRANSAKSI (Sub-CPMK 4) [cite: 34]
def urutkan_transaksi(list_harga): # Fungsi untuk mengurutkan list harga
    """
    Mengurutkan list harga secara manual menggunakan Insertion Sort.
    """
    # Membuat salinan list agar tidak mengubah list asli jika dipanggil berulang
    arr = list_harga.copy() 
    n = len(arr)
    
    for i in range(1, n): 
        key = arr[i]
        j = i - 1
        # Pindahkan elemen arr[0..i-1] yang lebih besar dari key ke satu posisi di depannya
        while j >= 0 and arr[j] > key: # Bandingkan elemen saat ini dengan key, jika lebih besar, geser ke kanan
            arr[j + 1] = arr[j] 
            j -= 1
        arr[j + 1] = key
        
    return arr

# ==============================================================================
# MAIN PROGRAM - MENU ANTARMUKA
# ==============================================================================
def main():
    # Inisialisasi Data
    file_db = "buku.txt"
    data_buku = muat_data_buku(file_db) # Memuat data buku dari file 'buku.txt' ke dalam dictionary
    list_promosi = LinkedListPromosi() 
    antrean_toko = AntreanKasir() 
    riwayat_transaksi = [150000, 50000, 200000, 75000, 120000] # Contoh data harga untuk laporan penjualan

    while True:
        print("\n--- SISTEM MANAJEMEN TOKO BUKU ---")
        print("1. Lihat Katalog Buku (Dictionary/File)")
        print("2. Kelola Daftar Promosi (Linked List)")
        print("3. Kelola Antrean Kasir (Queue)")
        print("4. Lihat Laporan Penjualan Terurut (Sorting)")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == '1': 
            print("\nKatalog Buku:")
            if not data_buku:
                print("Data kosong atau file tidak ditemukan.")
            else:
                for kode, info in data_buku.items(): # Menampilkan kode buku, judul, dan harga dari dictionary data_buku
                    print(f"Kode: {kode} | Judul: {info['judul']} | Harga: Rp{info['harga']}")
        
        elif pilihan == '2':
            print("\n1. Tambah Promosi Baru")
            print("2. Lihat Daftar Promosi")
            sub_pil = input("Pilih aksi (1/2): ")
            if sub_pil == '1':
                judul_baru = input("Masukkan judul buku untuk promosi: ")
                list_promosi.tambah_buku_promosi(judul_baru)
            elif sub_pil == '2': # Menampilkan daftar buku yang sedang dalam promosi menggunakan linked list
                list_promosi.tampilkan_promosi()
            else:
                print("Pilihan tidak valid.")

        elif pilihan == '3':
            print("\n1. Tambah Antrean")
            print("2. Layani Pelanggan")
            sub_pil = input("Pilih aksi (1/2): ")
            if sub_pil == '1':
                nama = input("Nama Pelanggan: ")
                antrean_toko.tambah_antrean(nama)
            elif sub_pil == '2':
                antrean_toko.layani_pelanggan()
            else:
                print("Pilihan tidak valid.")

        elif pilihan == '4':
            print("\nHarga Sebelum Urut:", riwayat_transaksi)
            hasil_sort = urutkan_transaksi(riwayat_transaksi) # Mengurutkan harga transaksi menggunakan insertion sort
            print("Harga Sesudah Urut (Terkecil - Terbesar):", hasil_sort)

        elif pilihan == '5':
            print("Program selesai. Terima kasih.")
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()