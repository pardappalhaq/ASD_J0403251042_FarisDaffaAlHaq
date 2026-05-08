# Praktikum 2 - Membuat Adjacency List
# Nama: Faris Daffa Al Haq
# NIM: J0403251042

def createGraphDict(nodes, edges):
    # 1. Gunakan dictionary Python
    # Inisialisasi dictionary kosong untuk setiap node
    adj = {node: [] for node in nodes}
    
    # Menambahkan setiap interaksi kolaborasi (edge) ke dalam dictionary
    for u, v in edges:
        adj[u].append(v)
        # Karena graph undirected (kolaborasi berlaku dua arah)
        adj[v].append(u)
        
    return adj

if __name__ == "__main__":
    # 2. Gunakan huruf sebagai node
    nodes = ['A', 'B', 'C', 'D']
    
    # Daftar interaksi "Collab Post" antar akun (u, v)
    edges = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D')]
    
    # Membangun graph menggunakan edges
    adj_list = createGraphDict(nodes, edges)
    
    # 3. Tampilkan adjacency list
    print("Adjacency List Representation Collab Post Instagram:\n")
    for akun, daftar_collab in adj_list.items():
        print(f"Akun {akun} berkolaborasi dengan: {daftar_collab}")