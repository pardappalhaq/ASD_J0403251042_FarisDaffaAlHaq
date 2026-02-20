#======================================================
#       NAMA : FARIS DAFFA ALHAQ
#       NIM  : J0403251042
#       KELAS: A1
#======================================================

#======================================================
#Implementasi Dasar : Queue
#======================================================

class Node:
    #konstruktor adalah fungsi yang dijalankan secara otomatis saat class Node dipanggil / diinstantiasi
    def __init__(self, data):
        self.data = data #menyimpan nilai atau data pada list
        self.next = None #pointer ini merujuk ke note berikutnya (awal=none)

class Queue:
    #buat konstruktor untuk inisialisasi variabel front dan rear
    def __init__(self):
        self.front = None #Node paling depan
        self.rear = None #Node paling belakang
    
    def is_empty(self):
        return self.front is None

    #membuat fungsi untuk menambahkan data baru pada bagian paling belakang
    def enqueue(self, data):
        nodeBaru = Node(data)
        
        #jika queue kosong, front dan rear akan menunjuk ke node yang sama
        if self.is_empty():
            self.front = nodeBaru
            self.rear = nodeBaru
            return
        
        #jika queue tidak kosong, maka letakkan data baru ke setelah rear, dan jadikan data baru sebagai rear        
        self.rear.next = nodeBaru #letakkan data baru pada setelahnya rear
        self.rear = nodeBaru #jadikan data baru sebagai rear

    def dequeue(self):
        #menghapus data dari depan/front
        data_terhapus = self.front.data #lihat data paling depan
        self.front = self.front.next #geser front ke node berikutnya
        
        #jika setelah geser front menjadi none, maka queue kosong
        if self.front is None:
            self.rear = None
        return data_terhapus


    def tampilkan(self):
        current = self.front
        print("Front ->", end = " ")
        while current is not None:
            print(current.data, end = "->")
            current = current.next
        print("Rear")

#Instantiasi class Queue
q = Queue()
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
q.tampilkan()
q.dequeue()
q.tampilkan()
q.dequeue()
q.tampilkan()
q.dequeue()
q.tampilkan()