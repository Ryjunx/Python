"""
Soal 17: Menghitung Banyak Faktor
Buatlah program untuk menghitung banyaknya faktor (pembagi) dari sebuah bilangan.

Input:
Sebuah bilangan bulat positif n (1 ≤ n ≤ 10^12).

Output:
Banyaknya faktor dari bilangan n.

Contoh 1:
Input: 12
Output: 6
(karena faktor dari 12 adalah 1, 2, 3, 4, 6, dan 12)

Contoh 2:
Input: 7
Output: 2
(karena faktor dari 7 adalah 1 dan 7)
"""

import math

# Input
n = int(input())

# Inisialisasi banyak faktor
banyak_faktor = 0

# Hitung banyaknya faktor
for i in range(1, int(math.sqrt(n)) + 1):
    if n % i == 0:
        # Jika i dan n/i berbeda, hitung keduanya
        if i != n // i:
            banyak_faktor += 2
        else:
            banyak_faktor += 1

# Output
print(banyak_faktor)

"""
Penjelasan:
1. Program menerima input bilangan bulat positif n.
2. Inisialisasi banyak_faktor = 0.
3. Cari semua faktor dari n dengan algoritma efisien:
   - Hanya perlu memeriksa bilangan hingga akar kuadrat dari n
   - Jika i adalah faktor dari n, maka n/i juga merupakan faktor
   - Untuk setiap i yang merupakan faktor n, tambahkan 2 ke banyak_faktor (untuk i dan n/i)
   - Perhatikan kasus khusus ketika i = n/i (akar kuadrat sempurna), hanya tambahkan 1 ke banyak_faktor
4. Cetak banyak_faktor.

Efisiensi algoritma:
- Kita hanya perlu memeriksa hingga akar kuadrat dari n untuk menemukan semua faktor
- Ini mengurangi kompleksitas waktu dari O(n) menjadi O(sqrt(n))

Contoh untuk n = 12:
- i = 1: 12 % 1 = 0, tambahkan 2 ke banyak_faktor (untuk 1 dan 12)
- i = 2: 12 % 2 = 0, tambahkan 2 ke banyak_faktor (untuk 2 dan 6)
- i = 3: 12 % 3 = 0, tambahkan 2 ke banyak_faktor (untuk 3 dan 4)
- i = 4: 4 >= sqrt(12), berhenti
- Hasil akhir: banyak_faktor = 6

Contoh untuk n = 16:
- i = 1: 16 % 1 = 0, tambahkan 2 ke banyak_faktor (untuk 1 dan 16)
- i = 2: 16 % 2 = 0, tambahkan 2 ke banyak_faktor (untuk 2 dan 8)
- i = 3: 16 % 3 ≠ 0, lewati
- i = 4: 16 % 4 = 0, tambahkan 1 ke banyak_faktor (untuk 4 saja, karena 4 = 16/4)
- i = 5: 5 > sqrt(16), berhenti
- Hasil akhir: banyak_faktor = 5

Kompleksitas waktu: O(sqrt(n)) karena kita hanya memeriksa faktor hingga akar kuadrat dari n
Kompleksitas ruang: O(1) karena hanya menggunakan variabel dengan jumlah tetap
""" 