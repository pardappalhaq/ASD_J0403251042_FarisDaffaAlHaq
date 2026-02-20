#======================================================
#       NAMA : FARIS DAFFA ALHAQ
#       NIM  : J0403251042
#       KELAS: A1
#======================================================

#======================================================
#Implementasi Dasar : Stack
#======================================================

class Node:
    #konstruktor adalah fungsi yang dijalankan secara otomatis saat class Node dipanggil / diinstantiasi
    def __init__(self, data):
        self.data = data #menyimpan nilai atau data pada list
        self.next = None #pointer ini merujuk ke note berikutnya (awal=none)

#stack ada operasi push(memasukkan head baru) dan pop(menghapus head)

class Stack:
    def __init__(self):
        self.top = None #top menunjuk pada node paling atas (awalnya kosong)

    def is_empty(self): #mengecek apakah stack kosong
        return self.top is None

    def push(self, data): #memasukkan data baru ke stack
        #1 membuat node baru
        nodeBaru = Node(data) #instantiasi/memanggil konstruktor pada class Node

        #2 node baru menunjuk ke top yang lama (head lama)
        nodeBaru.next = self.top

        #3 geser top pindah ke node baru
        self.top = nodeBaru

    def pop(self): #mengambil/menghapus node paling atas
        if self.is_empty():
            print("Stack kosong, tidak bisa pop")
            return None
        data_terhapus = self.top.data #soroti bagian top dan simpan di variabel
        self.top = self.top.next #geser top ke node berikutnya
        return data_terhapus

    def peek(self): 
        #melihat data paling atas
        if self.is_empty():
            print("Stack kosong, tidak bisa peek")
            return None
        return self.top.data
        
    def tampilkan(self):
        current = self.top
        print ("Top ->", end = " ")
        while current is not None:
            print(current.data, end = "->")
            current = current.next
        print("None")

#Instantiasi Class Stack
s = Stack()
s.push("A")
s.push("B")
s.push("C")
s.tampilkan()
print ("Peek (Lihat Toko): ", s.peek())
s.pop()
s.tampilkan()
print ("Peek (Lihat Toko): ", s.peek())
s.pop()
s.tampilkan()
print ("Peek (Lihat Toko): ", s.peek())
s.pop()
s.tampilkan()