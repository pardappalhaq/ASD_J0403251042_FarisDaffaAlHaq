class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

# Fungsi Traversal yang mengembalikan list
def inorderTraversal(root, res=None):
    if res is None:
        res = []
    if root:
        inorderTraversal(root.left, res)
        res.append(root.data)
        inorderTraversal(root.right, res)
    return res

def preorderTraversal(root, res=None):
    if res is None:
        res = []
    if root:
        res.append(root.data)
        preorderTraversal(root.left, res)
        preorderTraversal(root.right, res)
    return res

def postorderTraversal(root, res=None):
    if res is None:
        res = []
    if root:
        postorderTraversal(root.left, res)
        postorderTraversal(root.right, res)
        res.append(root.data)
    return res

# 1. Identitas Mahasiswa
nama = "Faris Daffa Al Haq"
nim = "J0403251042"

print(f"Nama : {nama}")
print(f"NIM  : {nim}")
print("-" * 30)

# 2. Inisialisasi Data berdasarkan 2 digit terakhir NIM (42)
data_list = [42, 22, 62, 12, 32, 52, 72, 27]

# Membangun Tree
root = Node(data_list[0])
for d in data_list[1:]:
    root.insert(d)

# 3 & 4. Menampilkan hasil traversal dalam bentuk list
print(f"In-order Traversal   : {inorderTraversal(root)}")
print(f"Pre-order Traversal  : {preorderTraversal(root)}")
print(f"Post-order Traversal : {postorderTraversal(root)}")