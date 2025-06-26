"""
Soal 19: Konversi Desimal ke Biner
Buatlah program untuk mengkonversi bilangan desimal ke bilangan biner.

Input:
Sebuah bilangan bulat positif n (0 ≤ n ≤ 10^18).

Output:
Hasil konversi bilangan desimal tersebut ke bilangan biner.

Contoh 1:
Input: 10
Output: 1010

Contoh 2:
Input: 31
Output: 11111
"""

# Input
n = int(input())

# Kasus khusus untuk n = 0
if n == 0:
    print("0")
    exit()

# Inisialisasi string biner
biner = ""

# Konversi dari desimal ke biner
while n > 0:
    if n % 2 == 0:
        biner = "0" + biner
    else:
        biner = "1" + biner
    n //= 2

# Output
print(biner)

"""
Penjelasan:
1. Program menerima input bilangan desimal n.
2. Tangani kasus khusus: jika n = 0, outputnya adalah "0".
3. Inisialisasi string biner kosong.
4. Lakukan konversi dari desimal ke biner:
   - Bagi n dengan 2 dan ambil sisa pembagian (modulo)
   - Jika sisa 0, tambahkan "0" di depan string biner
   - Jika sisa 1, tambahkan "1" di depan string biner
   - Lanjutkan pembagian n dengan 2 hingga n = 0
5. Cetak hasil konversi.

Cara kerja konversi desimal ke biner:
- Pembagian berulang dengan 2 dan mencatat sisa pembagian
- Sisa pembagian (0 atau 1) membentuk digit biner dari kanan ke kiri (bit terendah ke tertinggi)

Contoh untuk desimal 10:
- 10 ÷ 2 = 5 sisa 0 → biner = "0"
- 5 ÷ 2 = 2 sisa 1 → biner = "10"
- 2 ÷ 2 = 1 sisa 0 → biner = "010"
- 1 ÷ 2 = 0 sisa 1 → biner = "1010"
- Hasil: 1010

Implementasi alternatif menggunakan fungsi bawaan Python:
```python
biner = bin(n)[2:]  # [2:] untuk menghapus prefix '0b'
```

Implementasi alternatif menggunakan list dan join:
```python
biner = []
while n > 0:
    biner.append(str(n % 2))
    n //= 2
biner = ''.join(reversed(biner))
```

Keuntungan Python:
- Python dapat menangani bilangan bulat dengan ukuran arbitrer
- Tidak ada batasan ukuran seperti long long di C++
- Fungsi bawaan bin() tersedia untuk konversi cepat

Kompleksitas waktu: O(log n) karena setiap iterasi membagi n dengan 2
Kompleksitas ruang: O(log n) untuk menyimpan string biner (panjang output sekitar log₂(n))
""" 