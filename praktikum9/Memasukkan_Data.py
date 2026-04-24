# ==========================================================
# Nama      : Faris Daffa Al Haq
# NIM       : J0403251042
# Kelas     : A1
# ==========================================================

# ==========================================================
# Contoh Binary Tree: Memasukkan Data ke dalam Pohon
# ==========================================================

class Node: # Membuat class Node untuk merepresentasikan node pada binary tree
    def __init__(self, data): # Membuat constructor untuk inisialisasi node dengan data dan pointer ke anak kiri dan kanan
        self.left = None 
        self.right = None
        self.data = data
    def insert(self, data): # Membuat method untuk memasukkan data ke dalam tree dengan aturan binary search tree 
# Compare the new value with the parent node
        if self.data: # Jika node saat ini memiliki data
            if data < self.data:
                if self.left is None: # Jika anak kiri dari node saat ini kosong, buat node baru dengan data yang akan dimasukkan
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data: 
                if self.right is None: # Jika anak kanan dari node saat ini kosong, buat node baru dengan data yang akan dimasukkan
                    self.right = Node(data)
                else:
                    self.right.insert(data) # Jika anak kanan dari node saat ini tidak kosong, panggil method insert pada anak kanan
        else:
            self.data = data # Jika node saat ini tidak memiliki data, isi data pada node dengan data yang akan dimasukkan
# Print the tree
    def PrintTree(self): # Membuat method untuk mencetak isi tree dengan cara traversal 
        if self.left: 
            self.left.PrintTree() # Panggil method PrintTree pada anak kiri terlebih dahulu (traversal ke kiri)
        print(self.data) # Cetak data pada node saat ini
        if self.right: #
            self.right.PrintTree() # Panggil method PrintTree pada anak kanan (traversal ke kanan)
# Use the insert method to add nodes
root = Node(12) # Membuat root node dengan data 12
root.insert(6) # Memasukkan data 6 ke dalam tree
root.insert(14) # Memasukkan data 14 ke dalam tree
root.insert(3) # Memasukkan data 3 ke dalam tree

root.PrintTree() # Memanggil method PrintTree untuk mencetak isi tree, yang akan menghasilkan urutan 3, 6, 12, 14 karena data pada tree diurutkan secara ascending sesuai aturan binary search tree