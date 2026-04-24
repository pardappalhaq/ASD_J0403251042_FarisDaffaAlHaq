# ==========================================================
# Nama      : Faris Daffa Al Haq
# NIM       : J0403251042
# Kelas     : A1
# ==========================================================

# ==========================================================
# Contoh Binary Tree: Buat Root
# ==========================================================

class Node: # Membuat class Node untuk merepresentasikan node pada binary tree
    def __init__(self, data): # Membuat constructor untuk inisialisasi node dengan data dan pointer ke anak kiri dan kanan
        self.left = None    
        self.right = None   
        self.data = data  # Menyimpan data pada node

    def PrintTree(self): # Membuat method untuk mencetak isi tree dengan cara traversal
        print(self.data) # Mencetak data pada node saat ini
root = Node(10) # Membuat root node dengan data 10
root.PrintTree() # Memanggil method PrintTree untuk mencetak isi tree, yang hanya berisi root node dengan data 10