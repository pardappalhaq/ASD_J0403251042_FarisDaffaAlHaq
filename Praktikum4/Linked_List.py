#======================================================
#       NAMA : FARIS DAFFA ALHAQ
#       NIM  : J0403251042
#       KELAS: A1
#======================================================

#======================================================
#Implementasi Dasar : Node pada Linked List
#======================================================

class Node:
    #konstruktor yang dijalankan secara otomatis saat class Node dipanggil / diinstantiasi
    def __init__(self, data):
        self.data = data #menyimpan nilai atau data pada list
        self.next = None #pointer ini merujuk ke note berikutnya (awal=none)

#1) membuat node dengan instantiasi class Node
nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")

#2) mendeklarasi node dan menghubungkan Node : A -> B -> C -> None
head = nodeA
nodeA.next = nodeB
nodeB.next = nodeC

#3) Traversal : menelusuri node dari head sampai ke None
current = head
while current is not None:
    print(current.data) #menampilkan data pada node saat ini
    current = current.next #memindahkan pointer ke node berikutnya