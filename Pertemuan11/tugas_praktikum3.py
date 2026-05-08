# Praktikum 3 - Konversi Matrix ke List
# Nama: Faris Daffa Al Haq
# NIM: J0403251042

def convert_matrix_to_list(matrix):
    V = len(matrix)
    # Inisialisasi list of lists kosong sejumlah V node
    adj_list = [[] for _ in range(V)]
    
    # Melakukan iterasi pada baris (i) dan kolom (j) matriks
    for i in range(V):
        for j in range(V):
            # Jika bernilai 1, tambahkan node j ke dalam adjacency list node i
            if matrix[i][j] == 1:
                adj_list[i].append(j)
                
    return adj_list

if __name__ == "__main__":
    # Matriks yang mau di ubah ke adjacency list
    matrix = [
        [0, 1, 1, 0],
        [1, 0, 1, 0],
        [1, 1, 0, 1],
        [0, 0, 1, 0]
    ]
    
    # Memanggil fungsi konversi
    hasil_adj_list = convert_matrix_to_list(matrix)
    
    # Menampilkan hasil akhir
    print("Hasil Perubahan ke Adjacency List:\n")
    for i in range(len(hasil_adj_list)):
        print(f"Node {i} terhubung dengan: {hasil_adj_list[i]}")