#========================================================================
# Nama  : Faris Daffa Al Haq
# NIM   : J0403251042
# Kelas : A1
#========================================================================

#========================================================================
# Material : Shell Sort
#========================================================================

def shell_sort(data):
    gaps = [4, 2, 1] #menentukan gap
    
    print(f"Data awal: {data}\n")
    
    for gap in gaps:
        print(f"gap: {gap}") #mengambil satu per satu gapnya
        
        for i in range(gap, len(data)):
            temp = data[i] #menyimpan nilai sementara
            j = i
            
            while j >= gap and data[j - gap] > temp:
                data[j] = data[j - gap]
                j -= gap #mengurangi gap berikutnya
                
            data[j] = temp #menaro nilai
            
        print(f"Hasil sementara: {data}\n") #mencetak hasil sementara
        
    return data

data_angka = [45, 12, 89, 33, 21, 5, 76, 1] #data angka yang mau kita urutkan

hasil_akhir = shell_sort(data_angka) #memanggil fungsi angka yang mau kita urutkan

print(f"Data akhir yang sudah terurut: {hasil_akhir}") #mencetak hasil akhirnya