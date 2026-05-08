# Praktikum 4 - adjacency matrix
# Nama: Faris Daffa Al Haq
# NIM: J0403251042

def createGraph(V, edges):
    mat = [[0 for _ in range(V)] for _ in range(V)]

    # Add each edge to the adjacency matrix
    for it in edges:
        u = it[0]
        v = it[1]
        mat[u][v] = 1

        # since the graph is undirected
        mat[v][u] = 1
    return mat

if __name__ == "__main__":
    # Total node (Andi, Budi, Citra, Denis, Eka)
    V = 5 
    
    # Pemetaan indeks ke nama
    names = ["Andi", "Budi", "Citra", "Denis", "Eka"]

    # List of edges (u, v) berdasarkan relasi kolaborasi
    # 0=Andi, 1=Budi, 2=Citra, 3=Denis, 4=Eka
    edges = [
        [0, 1], # Andi collab dengan Budi
        [0, 2], # Andi collab dengan Citra
        [1, 2], # Budi collab dengan Citra
        [1, 3], # Budi collab dengan Denis
        [2, 4], # Citra collab dengan Eka
        [3, 4]  # Denis collab dengan Eka
    ]

    # Build the graph using edges
    mat = createGraph(V, edges)

    print("Adjacency Matrix Representation:")
    
    # Menampilkan header nama agar matriks mudah dibaca
    print("        " + " ".join(names))
    
    for i in range(V):
        # Menampilkan nama baris di sebelah kiri
        print(f"{names[i]:<6}:", end=" ")
        
        for j in range(V):
            # Format jarak agar angka sejajar dengan nama di header
            print(f"{mat[i][j]:<5}", end="") 
        print()