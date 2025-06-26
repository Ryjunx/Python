"""
Soal 20: Bilangan Prima dengan Sieve of Eratosthenes
Buatlah program untuk mencari semua bilangan prima dari 1 hingga n menggunakan algoritma Sieve of Eratosthenes.

Input:
Sebuah bilangan bulat positif n (1 ≤ n ≤ 10^6).

Output:
Semua bilangan prima dari 1 hingga n, dipisahkan oleh spasi.

Contoh:
Input: 20
Output: 2 3 5 7 11 13 17 19
"""

# Input
n = int(input())

# Membuat list boolean untuk menandai bilangan prima
is_prima = [True] * (n + 1)

# 0 dan 1 bukan bilangan prima
if n >= 0:
    is_prima[0] = False
if n >= 1:
    is_prima[1] = False

# Implementasi Sieve of Eratosthenes
for i in range(2, int(n ** 0.5) + 1):
    if is_prima[i]:
        # Tandai semua kelipatan i sebagai bukan prima
        for j in range(i * i, n + 1, i):
            is_prima[j] = False

# Cetak semua bilangan prima
prima = [str(i) for i in range(2, n + 1) if is_prima[i]]
print(" ".join(prima))

"""
Penjelasan:
1. Program menerima input bilangan bulat positif n.
2. Inisialisasi list boolean is_prima dengan ukuran n+1 dan semua nilai diset True.
3. Set is_prima[0] dan is_prima[1] menjadi False karena 0 dan 1 bukan bilangan prima.
4. Implementasi algoritma Sieve of Eratosthenes:
   - Untuk setiap bilangan prima i (dimulai dari 2), tandai semua kelipatannya sebagai bukan prima
   - Kita hanya perlu memeriksa hingga akar kuadrat dari n, karena jika i tidak memiliki faktor <= sqrt(n), maka i pasti prima
   - Untuk optimasi, mulai menandai kelipatan dari i*i (bukan 2*i), karena semua kelipatan i yang lebih kecil dari i*i sudah ditandai
5. Cetak semua bilangan yang masih bertanda True (bilangan prima).

Algoritma Sieve of Eratosthenes:
- Algoritma ini efisien untuk mencari semua bilangan prima hingga batas tertentu
- Ide dasarnya adalah "menyaring" bilangan yang bukan prima dengan menandai semua kelipatan dari bilangan prima yang sudah ditemukan

Contoh untuk n = 20:
- Inisialisasi is_prima[0] = is_prima[1] = False, is_prima[2...20] = True
- i = 2: Tandai 4, 6, 8, 10, 12, 14, 16, 18, 20 sebagai bukan prima
- i = 3: Tandai 9, 12, 15, 18 sebagai bukan prima
- i = 4: Sudah ditandai sebagai bukan prima, lewati
- i = 5: Tandai 25 (di luar batas) sebagai bukan prima
- Bilangan yang masih bertanda True: 2, 3, 5, 7, 11, 13, 17, 19

Keunggulan Sieve of Eratosthenes:
- Sangat efisien untuk mencari banyak bilangan prima sekaligus
- Kompleksitas waktu optimal untuk masalah ini

Implementasi alternatif menggunakan list comprehension:
```python
prima = [i for i in range(2, n + 1) if all(i % j != 0 for j in range(2, int(i ** 0.5) + 1))]
```
Namun implementasi ini kurang efisien karena memeriksa setiap bilangan secara terpisah.

Kompleksitas waktu: O(n log log n) 
- Pembuktian matematisnya cukup kompleks, tapi ini jauh lebih efisien dari O(n√n) yang didapat jika kita memeriksa setiap bilangan satu per satu
Kompleksitas ruang: O(n) untuk menyimpan array boolean
""" 