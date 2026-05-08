# Praktikum 4 - Adjacency List
# Nama: Faris Daffa Al Haq
# NIM: J0403251042

def createGraph(V, edges):
    adj = [[] for _ in range(V)]

    # Add each edge to the adjacency list
    for it in edges:
        u = it[0]
        v = it[1]
        adj[u].append(v)

        # since the graph is undirected
        adj[v].append(u)
    return adj

if __name__ == "__main__":
    # Total node (Andi, Budi, Citra, Denis, Eka)
    V = 5 

    # Pemetaan indeks ke nama untuk mempermudah pembacaan output nanti
    names = ["Andi", "Budi", "Citra", "Denis", "Eka"]

    # List of edges (u, v) berdasarkan relasi kolaborasi
    edges = [
        [0, 1], # Andi collab dengan Budi
        [0, 2], # Andi collab dengan Citra
        [1, 2], # Budi collab dengan Citra
        [1, 3], # Budi collab dengan Denis
        [2, 4], # Citra collab dengan Eka
        [3, 4]  # Denis collab dengan Eka
    ]

    # Build the graph using edges
    adj = createGraph(V, edges)

    print("Adjacency List Representation:")
    for i in range(V):
        
        # Print the vertex (dengan tambahan nama agar lebih jelas)
        print(f"{names[i]} ({i}):", end=" ")
        
        for j in adj[i]:
            
            # Print its adjacent (menampilkan nama tetangganya)
            print(names[j], end=", ")
        print()