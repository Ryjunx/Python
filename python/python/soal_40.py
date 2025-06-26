"""
Soal 40: Pola Bintang Segitiga
Buatlah program untuk menampilkan pola bintang berbentuk segitiga siku-siku.

Input:
Sebuah bilangan bulat n (1 ≤ n ≤ 15), yaitu banyaknya baris.

Output:
Pola bintang segitiga siku-siku dengan tinggi n baris.

Contoh 1:
Input: 5
Output:
*
**
***
****
*****

Contoh 2:
Input: 3
Output:
*
**
***
"""

# Input
n = int(input())

# Pola bintang segitiga siku-siku
def print_triangle(n):
    for i in range(1, n + 1):
        print('*' * i)

print_triangle(n)

"""
Penjelasan:
1. Program menerima input bilangan bulat n, yaitu jumlah baris pola.
2. Untuk membuat pola bintang segitiga, kita menggunakan satu loop dari 1 sampai n:
   - Pada baris ke-i, kita mencetak i buah bintang dengan print('*' * i)
   - Setelah mencetak bintang pada suatu baris, otomatis pindah ke baris berikutnya
3. Hasilnya adalah pola bintang berbentuk segitiga siku-siku dengan tinggi n baris.

Contoh untuk n = 5:
- i = 1: cetak 1 bintang → *
- i = 2: cetak 2 bintang → **
- i = 3: cetak 3 bintang → ***
- i = 4: cetak 4 bintang → ****
- i = 5: cetak 5 bintang → *****

Variasi pola:
- Kita juga bisa membuat pola segitiga terbalik, segitiga sama kaki, dll. dengan modifikasi sederhana pada loop
- Contoh segitiga terbalik:
```python
for i in range(n, 0, -1):
    print('*' * i)
```

Kompleksitas waktu: O(n²), karena kita memiliki dua loop bersarang dan jumlah total operasi adalah 1+2+3+...+n = n(n+1)/2
Kompleksitas ruang: O(1), karena kita hanya menggunakan beberapa variabel
""" 