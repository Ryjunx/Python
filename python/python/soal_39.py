"""
Soal 39: Menghitung Jumlah Digit
Buatlah program untuk menghitung jumlah digit dari suatu bilangan bulat positif.

Input:
Sebuah bilangan bulat positif n (1 ≤ n ≤ 1.000.000).

Output:
Jumlah digit dari bilangan n.

Contoh 1:
Input: 123
Output: 6
(karena 1 + 2 + 3 = 6)

Contoh 2:
Input: 9999
Output: 36
(karena 9 + 9 + 9 + 9 = 36)
"""

# Input
n = int(input())

# Jumlahkan digit satu per satu
sum_digit = 0
while n > 0:
    digit = n % 10
    sum_digit += digit
    n //= 10

print(sum_digit)

"""
Penjelasan:
1. Program menerima input bilangan bulat positif n.
2. Untuk menghitung jumlah digit dari n, kita menggunakan pendekatan berikut:
   - Inisialisasi variabel sum_digit = 0 untuk menyimpan jumlah digit
   - Selama n > 0, lakukan:
     - Ambil digit terakhir (satuan) dengan operasi modulo 10 (n % 10)
     - Tambahkan digit tersebut ke sum_digit
     - Buang digit terakhir dengan membagi n dengan 10 (operasi pembagian integer)
   - Setelah loop selesai, semua digit sudah dijumlahkan ke sum_digit
3. Cetak jumlah digit (sum_digit).

Contoh untuk bilangan 123:
- Inisialisasi: sum_digit = 0
- n = 123:
  - digit = 123 % 10 = 3
  - sum_digit = 0 + 3 = 3
  - n = 123 // 10 = 12
- n = 12:
  - digit = 12 % 10 = 2
  - sum_digit = 3 + 2 = 5
  - n = 12 // 10 = 1
- n = 1:
  - digit = 1 % 10 = 1
  - sum_digit = 5 + 1 = 6
  - n = 1 // 10 = 0
- n = 0, loop berhenti
- Hasil: sum_digit = 6

Alternatif menggunakan string:
```python
n = input()
sum_digit = sum(int(d) for d in n)
print(sum_digit)
```

Kompleksitas waktu: O(log n), karena jumlah iterasi sebanding dengan jumlah digit bilangan n
Kompleksitas ruang: O(1), karena kita hanya menggunakan beberapa variabel
""" 