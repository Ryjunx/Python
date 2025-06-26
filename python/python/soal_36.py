"""
Soal 36: Menggeser Daftar Angka
Buatlah program untuk menggeser semua elemen dalam daftar angka ke kanan sebanyak 1 posisi, dengan elemen terakhir dipindahkan ke posisi pertama.

Input:
Baris pertama berisi integer n (2 ≤ n ≤ 20), jumlah elemen daftar.
Baris kedua berisi n integer a₁, a₂, ..., aₙ (-100 ≤ aᵢ ≤ 100).

Output:
Satu baris berisi n integer hasil penggeseran daftar.

Contoh 1:
Input:
7
1 2 3 4 5 6 7
Output:
7 1 2 3 4 5 6

Contoh 2:
Input:
4
10 20 30 40
Output:
40 10 20 30

Contoh 3:
Input:
3
5 10 15
Output:
15 5 10
"""

# Input
n = int(input())
daftar = list(map(int, input().split()))

# Simpan elemen terakhir
terakhir = daftar[-1]

# Geser semua elemen ke kanan 1 posisi
for i in range(n - 1, 0, -1):
    daftar[i] = daftar[i - 1]

# Elemen terakhir menjadi elemen pertama
daftar[0] = terakhir

# Output
print(*daftar)

"""
Penjelasan:
1. Program menerima input n (jumlah elemen daftar) dan daftar angka.
2. Untuk menggeser daftar satu posisi ke kanan dengan elemen terakhir menjadi elemen pertama:
   - Simpan elemen terakhir (daftar[-1]) ke variabel terakhir
   - Geser setiap elemen dari kanan ke kiri, dimulai dari indeks n-1 sampai 1
   - Letakkan nilai terakhir ke posisi pertama (daftar[0])
3. Cetak daftar setelah digeser.

Contoh untuk daftar [1, 2, 3, 4, 5, 6, 7]:
- Simpan elemen terakhir: terakhir = 7
- Geser elemen:
  - daftar[6] = daftar[5] -> daftar[6] = 6
  - daftar[5] = daftar[4] -> daftar[5] = 5
  - daftar[4] = daftar[3] -> daftar[4] = 4
  - daftar[3] = daftar[2] -> daftar[3] = 3
  - daftar[2] = daftar[1] -> daftar[2] = 2
  - daftar[1] = daftar[0] -> daftar[1] = 1
- Elemen terakhir menjadi elemen pertama: daftar[0] = 7
- Hasil: [7, 1, 2, 3, 4, 5, 6]

Implementasi alternatif menggunakan slicing:
```python
daftar = [daftar[-1]] + daftar[:-1]
```

Implementasi alternatif menggunakan deque:
```python
from collections import deque
daftar = deque(daftar)
daftar.rotate(1)
daftar = list(daftar)
```

Implementasi alternatif menggunakan list comprehension:
```python
daftar = [daftar[-1]] + [daftar[i] for i in range(len(daftar) - 1)]
```

Kompleksitas waktu: O(n) karena kita memproses setiap elemen dalam daftar sekali
Kompleksitas ruang: O(1) karena kita hanya menggunakan variabel tambahan untuk menyimpan elemen terakhir
""" 