"""
Soal 37: Pencarian Nilai dalam Array
Buatlah program untuk mencari apakah sebuah nilai ada dalam array, dan jika ada, berapa kali nilai tersebut muncul.

Input:
Baris pertama berisi bilangan bulat n (1 ≤ n ≤ 100), yaitu banyaknya bilangan dalam array.
Baris kedua berisi n bilangan bulat a₁, a₂, ..., aₙ (1 ≤ aᵢ ≤ 100).
Baris ketiga berisi bilangan bulat x (1 ≤ x ≤ 100) yang akan dicari dalam array.

Output:
Jika nilai x ditemukan dalam array, cetak "ADA" dan banyaknya kemunculan nilai tersebut.
Jika tidak ditemukan, cetak "TIDAK ADA".

Contoh 1:
Input:
8
5 2 7 2 9 2 5 3
2
Output:
ADA 3

Contoh 2:
Input:
5
10 20 30 40 50
15
Output:
TIDAK ADA
"""

# Input
n = int(input())
arr = list(map(int, input().split()))
x = int(input())

# Cari nilai x dalam array
count = 0
for num in arr:
    if num == x:
        count += 1

# Output
if count > 0:
    print(f"ADA {count}")
else:
    print("TIDAK ADA")

"""
Penjelasan:
1. Program menerima input jumlah bilangan n, array arr, dan nilai x yang akan dicari.
2. Untuk mencari nilai x dalam array, kita melakukan iterasi (perulangan) dari elemen pertama hingga elemen terakhir:
   - Jika nilai yang sedang diperiksa sama dengan x, kita tambahkan penghitung (count)
3. Setelah iterasi selesai, kita periksa nilai count:
   - Jika count > 0, berarti nilai x ditemukan dalam array
   - Jika count = 0, berarti nilai x tidak ditemukan

Contoh untuk array [5, 2, 7, 2, 9, 2, 5, 3] dan x = 2:
- Iterasi array:
  - arr[0] = 5, tidak sama dengan 2, count tetap 0
  - arr[1] = 2, sama dengan 2, count = 1
  - arr[2] = 7, tidak sama dengan 2, count tetap 1
  - arr[3] = 2, sama dengan 2, count = 2
  - arr[4] = 9, tidak sama dengan 2, count tetap 2
  - arr[5] = 2, sama dengan 2, count = 3
  - arr[6] = 5, tidak sama dengan 2, count tetap 3
  - arr[7] = 3, tidak sama dengan 2, count tetap 3
- Hasil: count = 3, jadi nilai 2 ditemukan sebanyak 3 kali

Implementasi alternatif menggunakan count():
```python
count = arr.count(x)
```

Kompleksitas waktu: O(n), karena kita hanya perlu memeriksa semua elemen array satu kali
Kompleksitas ruang: O(1) tambahan (selain input), karena kita hanya menggunakan satu variabel tambahan (count)
""" 