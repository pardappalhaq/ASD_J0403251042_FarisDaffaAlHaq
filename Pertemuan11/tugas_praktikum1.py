# Praktikum 1 - Membuat Adjacency Matrix
# Nama: Faris Daffa Al Haq
# NIM: J0403251042

def create_adjacency_matrix(V, edges):
    # Inisialisasi matriks berukuran V x V dengan nilai 0
    matrix = [[0 for _ in range(V)] for _ in range(V)]
    
    # Menambahkan setiap edge ke dalam matrix
    for u, v in edges:
        matrix[u][v] = 1
        matrix[v][u] = 1 # Karena graph undirected (kolaborasi berlaku dua arah)
        
    return matrix

if __name__ == "__main__":
    V = 4 # Terdapat 4 akun (node 0, 1, 2, 3)
    
    # Daftar interaksi "Collab Post" antar akun (u, v)
    edges = [[0, 1], [0, 2], [1, 2], [2, 3]]
    
    # Membangun adjacency matrix
    adj_matrix = create_adjacency_matrix(V, edges)
    
    print("Adjacency Matrix Collab Post Instagram:\n")
    print("    0  1  2  3")
    print("   -----------")
    for i in range(V):
        print(f"{i} | {adj_matrix[i]}")