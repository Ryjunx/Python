"""
Soal 3: Bilangan Prima
Buatlah program untuk memeriksa apakah sebuah bilangan adalah bilangan prima atau bukan.
Bilangan prima adalah bilangan yang hanya habis dibagi oleh 1 dan dirinya sendiri.

Input:
Sebuah bilangan bulat positif n (1 ≤ n ≤ 1.000.000)

Output:
"YA" jika n adalah bilangan prima
"BUKAN" jika n bukan bilangan prima

Contoh 1:
Input: 7
Output: YA

Contoh 2:
Input: 8
Output: BUKAN
"""

# Input
n = 35 #input random

# Kasus khusus
if n <= 1:
    print("BUKAN")
    exit()

if n <= 3:
    print("YA")
    exit()

# Cek apakah habis dibagi 2 atau 3
if n % 2 == 0 or n % 3 == 0:
    print("BUKAN")
    exit()

# Cek semua kemungkinan pembagi lainnya
i = 5
while i * i <= n:
    print("nilai i")
    if n % i == 0 or n % (i + 2) == 0:
        print("BUKAN")
        exit()
    i += 6 # i = i + 6

print("YA")

"""
Penjelasan:
1. Program menerima input bilangan bulat n.
2. Cek kasus khusus: 
   - Bilangan <= 1 bukan prima
   - Bilangan 2 dan 3 adalah prima
3. Cek apakah n habis dibagi 2 atau 3. Jika ya, maka bukan prima.
4. Cek semua kemungkinan pembagi dengan pola 6k ± 1 (dengan k = 1, 2, ...) hingga akar n.
   - Kita mulai dari i = 5 (6*1 - 1)
   - Setiap iterasi, kita cek apakah n habis dibagi dengan i atau i+2
   - Jika habis dibagi salah satu, maka bukan prima
   - Increment i dengan 6 (untuk mendapatkan 6k - 1 berikutnya)
5. Jika lolos semua cek, maka n adalah bilangan prima.

Algoritma ini efisien karena:
- Sudah meng-handle kasus khusus untuk n ≤ 3
- Langsung menyaring bilangan genap dan kelipatan 3
- Hanya mengecek pembagi hingga akar n
- Menggunakan pola 6k ± 1 karena semua bilangan prima > 3 bisa ditulis dalam bentuk 6k ± 1

Kompleksitas waktu: O(√n) karena kita hanya mengecek pembagi hingga akar n
Kompleksitas ruang: O(1) karena hanya menggunakan variabel dengan jumlah tetap
""" 