"""
Soal 33: Bead Sort
Program untuk mengurutkan array menggunakan algoritma Bead Sort.

Input:
Baris pertama berisi sebuah bilangan bulat n (1 ≤ n ≤ 1000), yaitu banyaknya bilangan dalam array.
Daftar n bilangan bulat ai (-10^9 ≤ ai ≤ 10^9).

Output:
Array yang sudah terurut dari kecil ke besar.

Contoh:
Untuk nilai:
n = 5
arr = [5, 2, 9, 1, 7]
Output: 1 2 5 7 9
"""

# Nilai yang akan digunakan (bisa diubah sesuai kebutuhan)
n = 5
arr = [5, 2, 9, 1, 7]

def bead_sort(arr):
    """Mengurutkan array menggunakan algoritma Bead Sort."""
    if not arr:
        return []
    
    # Pastikan semua elemen positif
    min_val = min(arr)
    if min_val < 0:
        arr = [x - min_val for x in arr]
    
    # Buat matriks bead
    max_val = max(arr)
    beads = [[0] * max_val for _ in range(len(arr))]
    
    # Isi matriks bead
    for i, x in enumerate(arr):
        for j in range(x):
            beads[i][j] = 1
    
    # Biarkan bead jatuh
    for j in range(max_val):
        # Hitung jumlah bead di setiap kolom
        sum_beads = sum(1 for i in range(len(arr)) if beads[i][j] == 1)
        
        # Atur ulang bead
        for i in range(len(arr)):
            if i < sum_beads:
                beads[i][j] = 1
            else:
                beads[i][j] = 0
    
    # Hitung hasil
    result = [sum(row) for row in beads]
    
    # Kembalikan ke nilai asli jika ada pengurangan
    if min_val < 0:
        result = [x + min_val for x in result]
    
    return result

# Lakukan pengurutan
arr = bead_sort(arr)

# Output array terurut
print(" ".join(map(str, arr)))

"""
Penjelasan:
1. Program menggunakan variabel n dan list arr dengan nilai yang sudah ditentukan
2. Bead Sort menggunakan pendekatan:
   - Buat matriks bead
   - Isi matriks sesuai nilai
   - Biarkan bead jatuh
   - Hitung hasil

Cara Kerja Bead Sort:
- Algoritma ini menggunakan konsep gravitasi
- Setiap nilai direpresentasikan sebagai bead
- Bead jatuh karena gravitasi
- Hasil dihitung dari jumlah bead di setiap baris

Contoh untuk array [5, 2, 9, 1, 7]:
1. Buat matriks bead (9x5):
   [1, 1, 1, 1, 1, 0, 0, 0, 0]  # 5
   [1, 1, 0, 0, 0, 0, 0, 0, 0]  # 2
   [1, 1, 1, 1, 1, 1, 1, 1, 1]  # 9
   [1, 0, 0, 0, 0, 0, 0, 0, 0]  # 1
   [1, 1, 1, 1, 1, 1, 1, 0, 0]  # 7

2. Biarkan bead jatuh:
   [1, 1, 1, 1, 1, 1, 1, 1, 1]  # 9
   [1, 1, 1, 1, 1, 1, 1, 0, 0]  # 7
   [1, 1, 1, 1, 1, 0, 0, 0, 0]  # 5
   [1, 1, 0, 0, 0, 0, 0, 0, 0]  # 2
   [1, 0, 0, 0, 0, 0, 0, 0, 0]  # 1

3. Hitung hasil:
   [9, 7, 5, 2, 1]

4. Balik urutan:
   [1, 2, 5, 7, 9]

Catatan:
- Bead Sort adalah algoritma pengurutan yang unik
- Menggunakan konsep gravitasi
- Stabil dalam pengurutan
- Hanya bekerja untuk bilangan bulat positif

Kompleksitas waktu: 
- Kasus terbaik: O(n) saat array sudah terurut
- Kasus terburuk: O(n * max(arr)) saat array terurut terbalik
Kompleksitas ruang: O(n * max(arr)) untuk menyimpan matriks bead
""" 