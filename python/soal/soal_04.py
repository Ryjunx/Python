"""
Soal 4: Deret Fibonacci
Buatlah program untuk mencari bilangan ke-n dalam deret Fibonacci.
Deret Fibonacci adalah deret bilangan yang dimulai dari 0 dan 1, kemudian bilangan berikutnya merupakan
jumlah dari dua bilangan sebelumnya. Deret Fibonacci: 0, 1, 1, 2, 3, 5, 8, 13, ...

Input:
Sebuah bilangan bulat n (1 ≤ n ≤ 45)

Output:
Bilangan Fibonacci ke-n

Contoh:
Input: 7
Output: 8
"""

# Input
n = int(input())

# Handle kasus khusus
if n == 1:
    print(0)
    exit()
if n == 2:
    print(1)
    exit()

# Hitung Fibonacci menggunakan metode iteratif
a, b = 0, 1
for i in range(3, n + 1):
    c = a + b
    a = b
    b = c

print(b)

"""
Penjelasan:
1. Program menerima input bilangan bulat n.
2. Handle kasus khusus:
   - Jika n = 1, maka keluarkan bilangan Fibonacci ke-1 yaitu 0
   - Jika n = 2, maka keluarkan bilangan Fibonacci ke-2 yaitu 1
3. Untuk n >= 3, kita gunakan metode iteratif untuk menghitung Fibonacci:
   - Mulai dengan a = 0 (Fibonacci ke-1) dan b = 1 (Fibonacci ke-2)
   - Lakukan perulangan dari i = 3 sampai n
   - Pada setiap iterasi, hitung c = a + b
   - Kemudian geser a ke b dan b ke c
4. Hasil akhir Fibonacci ke-n adalah nilai b.

Catatan:
- Python dapat menangani bilangan bulat dengan ukuran tak terbatas, jadi tidak perlu khawatir tentang overflow.
- Namun, untuk konsistensi dengan versi C++, kita tetap membatasi n ≤ 45.

Kompleksitas waktu: O(n) karena melakukan n iterasi untuk menghitung Fibonacci ke-n
Kompleksitas ruang: O(1) karena hanya menggunakan variabel dengan jumlah tetap
""" 