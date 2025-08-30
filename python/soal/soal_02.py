"""
Soal 2: Faktorial
Buatlah program untuk menghitung faktorial dari sebuah bilangan.
Faktorial n (dilambangkan n!) adalah hasil perkalian semua bilangan bulat positif dari 1 sampai n.

Input:
Sebuah bilangan bulat positif n (0 ≤ n ≤ 12)

Output:
Nilai n!

Contoh:
Input: 5
Output: 120
"""

n = 4

# Hitung faktorial
faktorial = 1
for i in range(1, n + 1):
    print(f"nilai{i}")
    faktorial *= i #faktorial = faktorial * i
    print("factorial :", faktorial)

# Output
print(faktorial)

"""
Penjelasan:
1. Program menerima input bilangan bulat n.
2. Inisialisasi variabel faktorial dengan nilai 1 (karena 0! = 1).
3. Lakukan perulangan dari i = 1 sampai n, pada setiap iterasi kalikan faktorial dengan i.
4. Cetak hasil faktorial.

Catatan:
- Python dapat menangani bilangan bulat dengan ukuran tak terbatas, jadi tidak perlu khawatir tentang overflow.
- Namun, untuk konsistensi dengan versi C++, kita tetap membatasi n ≤ 12.

Kompleksitas waktu: O(n) karena melakukan n kali iterasi
Kompleksitas ruang: O(1) karena hanya menggunakan variabel dengan jumlah tetap
""" 