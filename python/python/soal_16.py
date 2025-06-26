"""
Soal 16: Bilangan Sempurna
Buatlah program untuk memeriksa apakah sebuah bilangan merupakan bilangan sempurna atau bukan.
Bilangan sempurna adalah bilangan yang jumlah semua faktor positifnya (kecuali bilangan itu sendiri) sama dengan bilangan itu sendiri.

Input:
Sebuah bilangan bulat positif n (1 ≤ n ≤ 10^8).

Output:
"YA" jika n adalah bilangan sempurna
"BUKAN" jika n bukan bilangan sempurna

Contoh 1:
Input: 6
Output: YA
(karena faktor dari 6 adalah 1, 2, 3, dan 6; jumlah faktor kecuali 6 adalah 1 + 2 + 3 = 6)

Contoh 2:
Input: 10
Output: BUKAN
(karena faktor dari 10 adalah 1, 2, 5, dan 10; jumlah faktor kecuali 10 adalah 1 + 2 + 5 = 8 ≠ 10)
"""

import math

# Input
n = int(input())

# Kasus khusus
if n == 1:
    print("BUKAN")
    exit()

# Inisialisasi jumlah faktor dengan 1 (karena 1 selalu menjadi faktor)
jumlah_faktor = 1

# Cari semua faktor dan jumlahkan
for i in range(2, int(math.sqrt(n)) + 1):
    if n % i == 0:
        jumlah_faktor += i
        
        # Jika i dan n/i berbeda, tambahkan juga n/i
        if i != n // i:
            jumlah_faktor += n // i

# Cek apakah bilangan sempurna
print("YA" if jumlah_faktor == n else "BUKAN")

"""
Penjelasan:
1. Program menerima input bilangan bulat positif n.
2. Tangani kasus khusus: 1 bukan bilangan sempurna (jumlah faktor selain dirinya adalah 0).
3. Inisialisasi jumlah_faktor = 1 (karena 1 selalu menjadi faktor dari semua bilangan).
4. Cari semua faktor dari n, tetapi hanya perlu memeriksa hingga akar kuadrat dari n:
   - Jika i adalah faktor dari n, maka n/i juga merupakan faktor
   - Tambahkan kedua faktor ke jumlah_faktor
   - Perhatikan kasus ketika i = n/i (akar kuadrat sempurna), jangan menghitung dua kali
5. Bandingkan jumlah_faktor dengan n untuk menentukan apakah n adalah bilangan sempurna.

Efisiensi algoritma:
- Kita hanya perlu memeriksa hingga akar kuadrat dari n untuk menemukan semua faktor
- Ini mengurangi kompleksitas waktu dari O(n) menjadi O(sqrt(n))

Contoh bilangan sempurna:
- 6 = 1 + 2 + 3
- 28 = 1 + 2 + 4 + 7 + 14
- 496 = 1 + 2 + 4 + 8 + 16 + 31 + 62 + 124 + 248
- 8128 = 1 + 2 + 4 + 8 + 16 + 32 + 64 + 127 + 254 + 508 + 1016 + 2032 + 4064

Catatan:
- Bilangan sempurna sangat langka
- Hingga saat ini, hanya sekitar 50 bilangan sempurna yang diketahui
- Semua bilangan sempurna genap mengikuti pola 2^(p-1) * (2^p - 1) dimana (2^p - 1) adalah bilangan prima (bilangan prima Mersenne)
- Belum ada bilangan sempurna ganjil yang ditemukan, dan tidak diketahui apakah ada

Kompleksitas waktu: O(sqrt(n)) karena kita hanya memeriksa faktor hingga akar kuadrat dari n
Kompleksitas ruang: O(1) karena hanya menggunakan variabel dengan jumlah tetap
""" 