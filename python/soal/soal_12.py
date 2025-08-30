"""
Soal 12: Selection Sort
Buatlah program untuk mengurutkan array menggunakan algoritma Selection Sort.

Input:
Baris pertama berisi sebuah bilangan bulat n (1 ≤ n ≤ 1000), yaitu banyaknya bilangan dalam array.
Baris kedua berisi n bilangan bulat ai (-10^9 ≤ ai ≤ 10^9).

Output:
Array yang sudah terurut dari kecil ke besar.

Contoh:
Input:
5
5 2 9 1 7

Output:
1 2 5 7 9
"""

# Input
n = int(input())
arr = list(map(int, input().split()))

# Selection Sort
for i in range(n - 1):
    # Cari elemen minimum di array yang belum terurut
    indeks_min = i
    for j in range(i + 1, n):
        if arr[j] < arr[indeks_min]:
            indeks_min = j
    
    # Tukar elemen minimum dengan elemen pertama dari array yang belum terurut
    if indeks_min != i:
        arr[i], arr[indeks_min] = arr[indeks_min], arr[i]

# Output array terurut
print(*arr)

"""
Penjelasan:
1. Program menerima input jumlah bilangan n.
2. Input n bilangan dan simpan dalam list arr.
3. Lakukan pengurutan dengan Selection Sort:
   - Lakukan perulangan sebanyak n-1 kali (i)
   - Pada setiap iterasi i, cari elemen minimum di bagian array yang belum terurut (dari indeks i hingga n-1)
   - Setelah menemukan elemen minimum, tukar dengan elemen di posisi i
   - Pada akhir iterasi i, elemen terkecil ke-(i+1) akan berada di posisi ke-i
4. Cetak array yang sudah terurut.

Cara Kerja Selection Sort:
- Algoritma ini mencari elemen minimum pada setiap iterasi
- Setiap iterasi akan menempatkan elemen terkecil yang belum terurut ke posisi berikutnya
- Setelah i iterasi, i elemen pertama sudah berada di posisi yang benar

Contoh untuk array [5, 2, 9, 1, 7]:
- Iterasi 1:
  - Cari minimum dari [5, 2, 9, 1, 7] → 1 (indeks 3)
  - Tukar 5 dengan 1 → [1, 2, 9, 5, 7]
- Iterasi 2:
  - Cari minimum dari [2, 9, 5, 7] → 2 (indeks 1)
  - Elemen sudah di posisi yang benar, tidak perlu menukar
- Iterasi 3:
  - Cari minimum dari [9, 5, 7] → 5 (indeks 2)
  - Tukar 9 dengan 5 → [1, 2, 5, 9, 7]
- Iterasi 4:
  - Cari minimum dari [9, 7] → 7 (indeks 4)
  - Tukar 9 dengan 7 → [1, 2, 5, 7, 9]
- Hasil akhir: [1, 2, 5, 7, 9]

Kompleksitas waktu: O(n²) untuk semua kasus karena selalu harus mencari elemen minimum pada setiap iterasi
Kompleksitas ruang: O(n) untuk menyimpan array dengan n elemen
""" 