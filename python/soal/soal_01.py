"""
Soal 1: Mencari Nilai Maksimum
Buatlah program untuk mencari nilai maksimum dari tiga bilangan bulat.

Input:
Tiga bilangan bulat a, b, dan c

Output:
Nilai maksimum dari ketiga bilangan tersebut

Contoh:
Input: 10 7 15
Output: 15
"""

a = 5
b = 6
c = 7

# Mencari nilai maksimum
maksimum = a
if b > maksimum:
    maksimum = b
if c > maksimum:
    maksimum = c

# Output
print(maksimum)

"""
Penjelasan:
1. Program menerima input tiga bilangan bulat a, b, dan c.
2. Inisialisasi variabel maksimum dengan nilai a.
3. Bandingkan maksimum dengan b, jika b lebih besar, update nilai maksimum.
4. Bandingkan maksimum dengan c, jika c lebih besar, update nilai maksimum.
5. Cetak nilai maksimum.

Kompleksitas waktu: O(1) karena jumlah operasi tetap
Kompleksitas ruang: O(1) karena hanya menggunakan variabel dengan jumlah tetap
""" 