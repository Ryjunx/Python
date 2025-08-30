"""
Soal 13: Insertion Sort
Buatlah program untuk mengurutkan array menggunakan algoritma Insertion Sort.

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

# Insertion Sort
for i in range(1, n):
    nilai = arr[i]
    j = i - 1
    
    # Geser elemen yang lebih besar dari nilai ke kanan
    while j >= 0 and arr[j] > nilai:
        arr[j + 1] = arr[j]
        j -= 1
    
    # Masukkan nilai ke posisi yang benar
    arr[j + 1] = nilai

# Output array terurut
print(*arr)

"""
Penjelasan:
1. Program menerima input jumlah bilangan n.
2. Input n bilangan dan simpan dalam list arr.
3. Lakukan pengurutan dengan Insertion Sort:
   - Mulai dari elemen kedua (indeks 1)
   - Simpan elemen saat ini dalam variabel nilai
   - Bandingkan nilai dengan elemen-elemen sebelumnya
   - Geser elemen yang lebih besar dari nilai ke kanan
   - Masukkan nilai ke posisi yang tepat
4. Cetak array yang sudah terurut.

Cara Kerja Insertion Sort:
- Algoritma ini membangun array terurut secara bertahap
- Pada setiap iterasi, kita mengambil satu elemen dari bagian yang belum terurut dan memasukkannya ke posisi yang tepat di bagian yang sudah terurut
- Seperti menyusun kartu dalam permainan kartu

Contoh untuk array [5, 2, 9, 1, 7]:
- Iterasi 1 (i=1):
  - Nilai saat ini: 2
  - Bandingkan dengan 5, geser 5 ke kanan
  - Masukkan 2 di posisi 0 → [2, 5, 9, 1, 7]
- Iterasi 2 (i=2):
  - Nilai saat ini: 9
  - 9 lebih besar dari 5, tidak perlu pergeseran
  - Array tetap → [2, 5, 9, 1, 7]
- Iterasi 3 (i=3):
  - Nilai saat ini: 1
  - Bandingkan dengan 9, 5, 2 dan geser semuanya ke kanan
  - Masukkan 1 di posisi 0 → [1, 2, 5, 9, 7]
- Iterasi 4 (i=4):
  - Nilai saat ini: 7
  - Bandingkan dengan 9, geser 9 ke kanan
  - Masukkan 7 di posisi 3 → [1, 2, 5, 7, 9]
- Hasil akhir: [1, 2, 5, 7, 9]

Kompleksitas waktu: 
- Kasus terburuk: O(n²) saat array terurut terbalik
- Kasus terbaik: O(n) saat array sudah terurut
Kompleksitas ruang: O(n) untuk menyimpan array dengan n elemen
""" 