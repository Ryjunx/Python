"""
Soal 29: Menggeser Array Satu Langkah
Buatlah program untuk menggeser semua elemen array satu langkah ke kanan. Elemen terakhir akan dipindahkan ke posisi pertama.

Input:
Baris pertama berisi bilangan bulat n (2 ≤ n ≤ 50), yaitu banyaknya bilangan dalam array.
Baris kedua berisi n bilangan bulat a₁, a₂, ..., aₙ (1 ≤ aᵢ ≤ 100).

Output:
Satu baris berisi n bilangan bulat hasil pergeseran array satu langkah ke kanan.

Contoh 1:
Input:
5
1 2 3 4 5
Output:
5 1 2 3 4

Contoh 2:
Input:
3
10 20 30
Output:
30 10 20
"""

# Input
n = int(input())
arr = list(map(int, input().split()))

# Simpan elemen terakhir
terakhir = arr[-1]

# Geser semua elemen satu langkah ke kanan
for i in range(n-1, 0, -1):
    arr[i] = arr[i-1]

# Tempatkan elemen terakhir di posisi pertama
arr[0] = terakhir

# Output
print(*arr)

"""
Penjelasan:
1. Program menerima input jumlah bilangan n dan array arr.
2. Untuk menggeser semua elemen array satu langkah ke kanan:
   - Simpan elemen terakhir (arr[-1]) ke dalam variabel terakhir
   - Mulai dari elemen terakhir, geser setiap elemen ke posisi setelahnya
   - Tempatkan nilai terakhir ke posisi pertama (arr[0])
3. Cetak array hasil pergeseran.

Ilustrasi untuk array [1, 2, 3, 4, 5]:
- Simpan arr[4] = 5 ke variabel terakhir
- Geser elemen:
  - arr[4] = arr[3] → arr[4] = 4
  - arr[3] = arr[2] → arr[3] = 3
  - arr[2] = arr[1] → arr[2] = 2
  - arr[1] = arr[0] → arr[1] = 1
- Tempatkan terakhir di posisi pertama: arr[0] = 5
- Hasil: [5, 1, 2, 3, 4]

Catatan:
- Kita mulai menggeser dari belakang untuk menghindari hilangnya nilai-nilai dalam array
- Jika kita mulai dari depan, nilai-nilai akan ditimpa sebelum bisa disalin

Implementasi alternatif menggunakan slicing:
```python
def rotate_right(arr):
    return [arr[-1]] + arr[:-1]
```

Implementasi alternatif menggunakan deque:
```python
from collections import deque

def rotate_right(arr):
    d = deque(arr)
    d.rotate(1)
    return list(d)
```

Implementasi alternatif menggunakan list comprehension:
```python
def rotate_right(arr):
    return [arr[-1]] + [arr[i] for i in range(len(arr)-1)]
```

Kompleksitas waktu: O(n), karena kita hanya perlu melewati semua elemen array satu kali
Kompleksitas ruang: O(1) tambahan (selain input), karena kita hanya menggunakan satu variabel tambahan
""" 