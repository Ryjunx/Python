"""
Soal 11: Bubble Sort
Buatlah program untuk mengurutkan array menggunakan algoritma Bubble Sort.

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

# Bubble Sort
for i in range(n - 1):
    for j in range(n - i - 1):
        if arr[j] > arr[j + 1]:
            # Tukar elemen
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Output array terurut
print(*arr)

"""
Penjelasan:
1. Program menerima input jumlah bilangan n.
2. Input n bilangan dan simpan dalam list arr.
3. Lakukan pengurutan dengan Bubble Sort:
   - Lakukan perulangan sebanyak n-1 kali (i)
   - Pada setiap iterasi i, bandingkan pasangan elemen yang berdekatan dari awal array hingga (n-i-1)
   - Jika elemen saat ini lebih besar dari elemen berikutnya, tukar keduanya
   - Pada akhir iterasi i, elemen terbesar akan berada di posisi akhir (n-i-1)
4. Cetak array yang sudah terurut.

Cara Kerja Bubble Sort:
- Algoritma ini membandingkan dan menukar elemen yang berdekatan jika urutannya salah
- Setiap iterasi akan menggeser elemen terbesar ke posisi paling kanan
- Setelah i iterasi, i elemen terakhir sudah berada di posisi yang benar

Contoh untuk array [5, 2, 9, 1, 7]:
- Iterasi 1:
  - [5, 2, 9, 1, 7] → [2, 5, 9, 1, 7] (tukar 5 dan 2)
  - [2, 5, 9, 1, 7] → [2, 5, 9, 1, 7] (tidak ada perubahan)
  - [2, 5, 9, 1, 7] → [2, 5, 1, 9, 7] (tukar 9 dan 1)
  - [2, 5, 1, 9, 7] → [2, 5, 1, 7, 9] (tukar 9 dan 7)
- Iterasi 2:
  - [2, 5, 1, 7, 9] → [2, 5, 1, 7, 9] (tidak ada perubahan)
  - [2, 5, 1, 7, 9] → [2, 1, 5, 7, 9] (tukar 5 dan 1)
  - [2, 1, 5, 7, 9] → [2, 1, 5, 7, 9] (tidak ada perubahan)
- Iterasi 3:
  - [2, 1, 5, 7, 9] → [1, 2, 5, 7, 9] (tukar 2 dan 1)
  - [1, 2, 5, 7, 9] → [1, 2, 5, 7, 9] (tidak ada perubahan)
- Iterasi 4:
  - [1, 2, 5, 7, 9] → [1, 2, 5, 7, 9] (tidak ada perubahan)
- Hasil akhir: [1, 2, 5, 7, 9]

Kompleksitas waktu: 
- Kasus terburuk: O(n²) saat array terurut terbalik
- Kasus terbaik: O(n) saat array sudah terurut
Kompleksitas ruang: O(n) untuk menyimpan array dengan n elemen
"""