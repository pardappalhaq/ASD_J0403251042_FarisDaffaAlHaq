# ==========================================================
# Nama      : Faris Daffa Al Haq
# NIM       : J0403251042
# Kelas     : A1
# ==========================================================

# ==========================================================
# Contoh Algoritma Traversal Pohon: Pre-order Traversal
# ==========================================================

class Node: # Membuat class Node untuk merepresentasikan node pada binary tree
    def __init__(self, data): # Membuat constructor untuk inisialisasi node dengan data dan pointer ke anak kiri dan kanan
        self.left = None 
        self.right = None
        self.data = data

# Insert Node
    def insert(self, data): # Membuat method untuk memasukkan data ke dalam tree dengan aturan binary search tree
        if self.data: # Jika node saat ini memiliki data
            if data < self.data: 
                if self.left is None: # Jika anak kiri dari node saat ini kosong, buat node baru dengan data yang akan dimasukkan
                    self.left = Node(data)
                else:
                    self.left.insert(data) # Jika anak kiri dari node saat ini tidak kosong, panggil method insert pada anak kiri
            elif data > self.data:
                if self.right is None: # Jika anak kanan dari node saat ini kosong, buat node baru dengan data yang akan dimasukkan
                    self.right = Node(data)
                else:
                    self.right.insert(data) # Jika anak kanan dari node saat ini tidak kosong, panggil method insert pada anak kanan
        else:
            self.data = data # Jika node saat ini tidak memiliki data, isi data pada node dengan data yang akan dimasukkan
            
# Print the Tree
    def PrintTree(self): # Membuat method untuk mencetak isi tree dengan cara traversal
        if self.left:    
            self.left.PrintTree() # Panggil method PrintTree pada anak kiri terlebih dahulu (traversal ke kiri)
        print( self.data), # Cetak data pada node saat ini
        if self.right:
            self.right.PrintTree() # Panggil method PrintTree pada anak kanan (traversal ke kanan)
            
# Preorder traversal
# Root -> Left ->Right
    def PreorderTraversal(self, root): # Membuat method untuk melakukan traversal pre-order
        res = [] # Membuat list kosong untuk menyimpan hasil traversal
        if root: # Jika node saat ini tidak kosong
            res.append(root.data) # Tambahkan data pada node saat ini ke dalam list hasil traversal sebelum traversal ke kiri dan kanan
            res = res + self.PreorderTraversal(root.left) # Panggil method PreorderTraversal pada anak kiri terlebih dahulu (traversal ke kiri) dan gabungkan hasilnya dengan list hasil traversal sebelumnya
            res = res + self.PreorderTraversal(root.right) # Panggil method PreorderTraversal pada anak kanan (traversal ke kanan) dan gabungkan hasilnya dengan list hasil traversal sebelumnya
        return res # Kembalikan list hasil traversal
    
root = Node(27) # Membuat root node dengan data 27
root.insert(14) # Memasukkan data 14 ke dalam tree
root.insert(35) # Memasukkan data 35 ke dalam tree
root.insert(10) # Memasukkan data 10 ke dalam tree
root.insert(19) # Memasukkan data 19 ke dalam tree
root.insert(31) # Memasukkan data 31 ke dalam tree
root.insert(42) # Memasukkan data 42 ke dalam tree
print(root.PreorderTraversal(root)) # Memanggil method PreorderTraversal untuk mencetak isi tree dengan urutan pre-order, yang akan menghasilkan list [27, 14, 10, 19, 35, 31, 42] karena data pada tree diurutkan sesuai aturan binary search tree dan traversal dilakukan dengan urutan root-left-right