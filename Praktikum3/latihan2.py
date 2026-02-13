class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        
        # Jika list kosong
        if self.head is None:
            self.head = new_node
            new_node.next = self.head  # Menunjuk ke dirinya sendiri
        else:
            # Traversal ke node terakhir
            current = self.head
            while current.next != self.head:
                current = current.next
            
            # Tambahkan node baru di akhir
            current.next = new_node
            new_node.next = self.head  # Node baru menunjuk ke head

    def search(self, key):
        # Jika list kosong
        if self.head is None:
            return False
        
        # Mulai dari head
        current = self.head
        
        # Cek node pertama
        if current.data == key:
            return True
        
        # Traversal circular linked list
        current = current.next
        while current != self.head:
            if current.data == key:
                return True
            current = current.next
        
        # Elemen tidak ditemukan
        return False

    def display(self):
        if self.head is None:
            print("Circular Linked List kosong")
            return
        
        current = self.head
        elements = []
        while True:
            elements.append(str(current.data))
            current = current.next
            if current == self.head:
                break
        print(" -> ".join(elements) + " -> (kembali ke head)")


# Program utama
if __name__ == "__main__":
    cll = CircularLinkedList()
    
    # Input elemen
    input_str = input("Masukkan elemen ke dalam Circular Linked List: ")
    
    # Cek apakah input kosong
    if input_str.strip():
        # Parse input yang dipisahkan koma
        elements = [int(x.strip()) for x in input_str.split(",")]
        
        # Tambahkan setiap elemen ke circular linked list
        for element in elements:
            cll.append(element)
        
        # Input elemen yang dicari
        search_key = int(input("Masukkan elemen yang ingin dicari: "))
        
        # Lakukan pencarian
        if cll.search(search_key):
            print(f"Elemen {search_key} ditemukan dalam Circular Linked List.")
        else:
            print(f"Elemen {search_key} tidak ditemukan dalam Circular Linked List.")
    else:
        print("Circular Linked List kosong.")
        search_key = int(input("Masukkan elemen yang ingin dicari: "))
        print(f"Elemen {search_key} tidak ditemukan dalam Circular Linked List.")
