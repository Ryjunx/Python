"""
Soal 7: Kelipatan Persekutuan Terkecil (KPK)
Buatlah program untuk mencari Kelipatan Persekutuan Terkecil (KPK) atau Least Common Multiple (LCM)
dari dua bilangan bulat.

Input:
Dua bilangan bulat positif a dan b (1 ≤ a, b ≤ 1.000.000.000)

Output:
KPK dari a dan b

Contoh:
Input: 4 6
Output: 12
"""

print(40 // 1)


def gcd(a, b):
    """Fungsi untuk mencari FPB menggunakan algoritma Euclidean"""
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a

# Input
a, b = [14, 21]


# Menghitung KPK menggunakan hubungan dengan FPB
fpb = gcd(a, b)
kpk = (a // fpb) * b  # Rumus: KPK(a,b) = (a*b) / FPB(a,b)

print("fpb :",fpb)


# Output
print(kpk)

"""
Penjelasan:
1. Program menerima input dua bilangan bulat positif a dan b.
2. Mencari FPB (Faktor Persekutuan Terbesar) menggunakan algoritma Euclidean.
3. Menghitung KPK menggunakan rumus: KPK(a,b) = (a*b) / FPB(a,b).
   - Namun untuk menghindari overflow pada tipe data long long, kita bisa menulis ulang rumus tersebut:
   - KPK(a,b) = (a/FPB(a,b)) * b
   - Dengan membagi a dengan FPB terlebih dahulu, kita bisa mengurangi kemungkinan overflow

Contoh untuk KPK(4, 6):
- FPB(4, 6) = 2
- KPK(4, 6) = (4*6) / 2 = 24 / 2 = 12
- atau KPK(4, 6) = (4/2) * 6 = 2 * 6 = 12

Kompleksitas waktu: O(log(min(a, b))) karena algoritma Euclidean memiliki kompleksitas logaritmik
Kompleksitas ruang: O(1) karena hanya menggunakan variabel dengan jumlah tetap
""" 