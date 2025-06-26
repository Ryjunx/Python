"""
Soal 22: Menaiki Tangga
Buatlah program untuk menghitung jumlah cara berbeda untuk menaiki tangga dengan n anak tangga.
Setiap kali, kamu bisa menaiki 1 atau 2 anak tangga.

Input:
Sebuah bilangan bulat n (1 ≤ n ≤ 45), menyatakan jumlah anak tangga.

Output:
Jumlah cara berbeda untuk mencapai puncak tangga.

Contoh 1:
Input: 2
Output: 2
(karena bisa menaiki 1+1 anak tangga atau langsung 2 anak tangga)

Contoh 2:
Input: 3
Output: 3
(karena bisa menaiki 1+1+1, 1+2, atau 2+1 anak tangga)
"""

# Input
n = int(input())

# Kasus khusus
if n == 1:
    print(1)
    exit()

# Menggunakan pendekatan dynamic programming (Fibonacci)
a = 1  # Cara untuk menaiki 1 anak tangga
b = 2  # Cara untuk menaiki 2 anak tangga

for i in range(3, n + 1):
    c = a + b
    a = b
    b = c

# Output
print(b)

"""
Penjelasan:
1. Program menerima input jumlah anak tangga n.
2. Tangani kasus khusus: jika n = 1, hanya ada 1 cara (langsung naik 1 anak tangga).
3. Untuk n >= 2, gunakan pendekatan dynamic programming:
   - a menyimpan jumlah cara untuk menaiki (i-2) anak tangga
   - b menyimpan jumlah cara untuk menaiki (i-1) anak tangga
   - c menyimpan jumlah cara untuk menaiki i anak tangga
   - Setiap iterasi, hitung c = a + b, lalu geser a ke b dan b ke c
4. Cetak hasil akhir (nilai b untuk n anak tangga).

Logika algoritma:
- Untuk mencapai anak tangga ke-i, kita bisa:
  1. Dari anak tangga ke-(i-1), lalu naik 1 anak tangga
  2. Dari anak tangga ke-(i-2), lalu naik 2 anak tangga
- Jadi jumlah cara menaiki i anak tangga = jumlah cara menaiki (i-1) anak tangga + jumlah cara menaiki (i-2) anak tangga
- Ini adalah pola bilangan Fibonacci!

Contoh untuk n = 4:
- Untuk 1 anak tangga: 1 cara (1)
- Untuk 2 anak tangga: 2 cara (1+1, 2)
- Untuk 3 anak tangga: 3 cara (1+1+1, 1+2, 2+1)
- Untuk 4 anak tangga: 5 cara (1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 2+2)

Hubungan dengan Fibonacci:
- Jumlah cara untuk n anak tangga adalah bilangan Fibonacci ke-(n+1)
- F(1) = 1, F(2) = 1, F(3) = 2, F(4) = 3, F(5) = 5, ...

Implementasi alternatif menggunakan rekursi (tidak efisien):
```python
def climb_stairs(n):
    if n <= 2:
        return n
    return climb_stairs(n-1) + climb_stairs(n-2)
```

Implementasi alternatif menggunakan list (menggunakan lebih banyak memori):
```python
ways = [0] * (n + 1)
ways[1] = 1
ways[2] = 2
for i in range(3, n + 1):
    ways[i] = ways[i-1] + ways[i-2]
```

Optimasi:
- Kita hanya perlu menyimpan dua nilai terakhir dari deret (a dan b), bukan seluruh array
- Ini mengurangi kompleksitas ruang dari O(n) menjadi O(1)

Kompleksitas waktu: O(n) karena kita melakukan n-2 iterasi
Kompleksitas ruang: O(1) karena hanya menggunakan variabel dengan jumlah tetap
""" 