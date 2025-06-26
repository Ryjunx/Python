"""
Soal 24: Rangkaian Terpanjang
Buatlah program untuk mencari panjang rangkaian bilangan berurutan terpanjang dalam sebuah array.

Input:
Baris pertama berisi sebuah bilangan bulat n (1 ≤ n ≤ 100000), yaitu banyaknya bilangan dalam array.
Baris kedua berisi n bilangan bulat ai (-10^9 ≤ ai ≤ 10^9).

Output:
Panjang rangkaian bilangan berurutan terpanjang dalam array.

Contoh 1:
Input:
9
100 4 200 1 3 2 5 10 7
Output: 5
(rangkaian terpanjang adalah 1, 2, 3, 4, 5)

Contoh 2:
Input:
6
5 1 9 3 8 12
Output: 1
(tidak ada bilangan berurutan, panjang maksimal adalah 1)
"""

# Input
n = int(input())
arr = list(map(int, input().split()))

# Masukkan semua elemen ke dalam set untuk akses O(1)
num_set = set(arr)

panjang_maks = 0

# Cek setiap kemungkinan awal rangkaian
for num in arr:
    # Jika ini adalah awal rangkaian (tidak ada num-1 dalam set)
    if num - 1 not in num_set:
        panjang_sekarang = 1
        nilai = num + 1
        
        # Cek berapa panjang rangkaian dari num
        while nilai in num_set:
            panjang_sekarang += 1
            nilai += 1
        
        # Update panjang maksimum
        panjang_maks = max(panjang_maks, panjang_sekarang)

# Output
print(panjang_maks)

"""
Penjelasan:
1. Program menerima input jumlah bilangan n dan array arr.
2. Masukkan semua elemen array ke dalam set untuk akses O(1).
3. Untuk setiap bilangan num dalam array:
   a. Cek apakah num-1 ada dalam set
   b. Jika tidak ada, berarti num adalah awal dari kemungkinan rangkaian
   c. Cek berapa panjang rangkaian mulai dari num dengan mencari num+1, num+2, ... dalam set
   d. Update panjang maksimum jika ditemukan rangkaian yang lebih panjang
4. Cetak panjang rangkaian terpanjang.

Logika algoritma:
- Untuk menemukan rangkaian terpanjang, kita perlu mencari semua rangkaian yang mungkin
- Namun, kita hanya perlu memulai pencarian dari elemen yang merupakan "awal" dari rangkaian (tidak ada elemen sebelumnya)
- Dengan begitu, kita menghindari pengecekan rangkaian yang sama berulang kali

Optimasi:
- Menggunakan set untuk pengecekan keberadaan elemen dalam O(1) time
- Hanya memeriksa rangkaian dari elemen "awal", bukan dari setiap elemen

Contoh untuk array [100, 4, 200, 1, 3, 2, 5, 10, 7]:
- Masukkan semua elemen ke dalam set
- Iterasi elemen-elemen:
  - 100: Tidak ada 99 dalam set → awal rangkaian potensial
    - Cek rangkaian: 100, 101, ... → tidak ada 101 → panjang = 1
  - 4: Tidak ada 3 dalam set (kita belum mengecek elemen 3) → awal rangkaian potensial
    - Cek rangkaian: 4, 5, ... → ada 5 → panjang = 2
  - 200: Tidak ada 199 dalam set → awal rangkaian potensial
    - Cek rangkaian: 200, 201, ... → tidak ada 201 → panjang = 1
  - 1: Tidak ada 0 dalam set → awal rangkaian potensial
    - Cek rangkaian: 1, 2, 3, 4, 5, ... → ada 2, 3, 4, 5 → panjang = 5
  - 3: Ada 2 dalam set → bukan awal rangkaian
  - 2: Ada 1 dalam set → bukan awal rangkaian
  - 5: Ada 4 dalam set → bukan awal rangkaian
  - 10: Tidak ada 9 dalam set → awal rangkaian potensial
    - Cek rangkaian: 10, 11, ... → tidak ada 11 → panjang = 1
  - 7: Tidak ada 6 dalam set → awal rangkaian potensial
    - Cek rangkaian: 7, 8, ... → tidak ada 8 → panjang = 1
- Panjang maksimum = 5

Implementasi alternatif menggunakan sorting (kurang efisien):
```python
def longest_consecutive_sort(arr):
    if not arr:
        return 0
    
    arr.sort()
    panjang_sekarang = 1
    panjang_maks = 1
    
    for i in range(1, len(arr)):
        if arr[i] == arr[i-1] + 1:
            panjang_sekarang += 1
        elif arr[i] != arr[i-1]:
            panjang_sekarang = 1
        
        panjang_maks = max(panjang_maks, panjang_sekarang)
    
    return panjang_maks
```

Kompleksitas waktu: O(n) dimana n adalah jumlah elemen dalam array
- Meskipun ada nested loop, setiap elemen hanya diperiksa sekali sebagai awal rangkaian
Kompleksitas ruang: O(n) untuk menyimpan semua elemen dalam set
""" 