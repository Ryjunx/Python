"""
Soal 6: Faktor Persekutuan Terbesar (FPB)
Buatlah program untuk mencari Faktor Persekutuan Terbesar (FPB) atau Greatest Common Divisor (GCD)
dari dua bilangan bulat.

Input:
Dua bilangan bulat positif a dan b (1 ≤ a, b ≤ 1.000.000.000)

Output:
FPB dari a dan b

Contoh:
Input: 24 36
Output: 12
"""

# Input
a, b = [40, 56]

print(14 % 21)

# Algoritma Euclidean untuk mencari FPB
while b != 0:
    temp = b
    print("temp :", temp)
    b = a % b
    a = temp
    print(a)
    

# Output
print(a)

"""
Penjelasan:
1. Program menerima input dua bilangan bulat positif a dan b.
2. Menggunakan algoritma Euclidean untuk mencari FPB:
   - Algoritma ini berdasarkan pada prinsip bahwa FPB(a, b) = FPB(b, a % b)
   - Kita lakukan perulangan selama b tidak sama dengan 0
   - Pada setiap iterasi, kita ganti a dengan b dan b dengan a % b
   - Ketika b menjadi 0, maka a adalah FPB dari kedua bilangan asli

Contoh langkah-langkah untuk FPB(24, 36):
- Iterasi 1: a = 24, b = 36 → a % b = 24 % 36 = 24 → a = 36, b = 24
- Iterasi 2: a = 36, b = 24 → a % b = 36 % 24 = 12 → a = 24, b = 12
- Iterasi 3: a = 24, b = 12 → a % b = 24 % 12 = 0 → a = 12, b = 0
- b = 0, sehingga FPB = a = 12

Kompleksitas waktu: O(log(min(a, b))) karena algoritma Euclidean memiliki kompleksitas logaritmik
Kompleksitas ruang: O(1) karena hanya menggunakan variabel dengan jumlah tetap
""" 