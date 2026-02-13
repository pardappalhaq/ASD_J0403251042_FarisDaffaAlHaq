class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        """Menambahkan elemen di akhir linked list"""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def display(self):
        """Menampilkan linked list dalam format: 1 -> 2 -> 3 -> null"""
        if self.head is None:
            return "kosong"
        
        result = []
        current = self.head
        while current:
            result.append(str(current.data))
            current = current.next
        return " -> ".join(result) + " -> null"
    
    def merge(self, other_list):
        """Menggabungkan linked list saat ini dengan linked list lain"""
        # Jika linked list saat ini kosong, ambil head dari linked list lain
        if self.head is None:
            self.head = other_list.head
            return
        
        # Jika linked list lain kosong, tidak ada yang perlu dilakukan
        if other_list.head is None:
            return
        
        # Temukan node terakhir dari linked list saat ini
        current = self.head
        while current.next:
            current = current.next
        
        # Hubungkan node terakhir dengan head dari linked list lain
        current.next = other_list.head


def main():
    # Input untuk Linked List 1
    input1 = input("Masukkan elemen untuk Linked List 1: ")
    list1 = LinkedList()
    
    if input1.strip():
        elements1 = [int(x.strip()) for x in input1.split(",")]
        for elem in elements1:
            list1.append(elem)
    
    # Input untuk Linked List 2
    input2 = input("Masukkan elemen untuk Linked List 2: ")
    list2 = LinkedList()
    
    if input2.strip():
        elements2 = [int(x.strip()) for x in input2.split(",")]
        for elem in elements2:
            list2.append(elem)
    
    # Tampilkan kedua linked list
    print("Linked List 1:", list1.display())
    print("Linked List 2:", list2.display())
    
    # Gabungkan linked list
    list1.merge(list2)
    
    # Tampilkan hasil penggabungan
    print("Linked List setelah digabungkan:", list1.display())


if __name__ == "__main__":
    main()
