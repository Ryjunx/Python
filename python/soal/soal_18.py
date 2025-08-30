"""
Soal 18: Konversi Biner ke Desimal
Buatlah program untuk mengkonversi bilangan biner ke bilangan desimal.

Input:
Sebuah string s yang merepresentasikan bilangan biner (panjang maksimal 60 karakter).

Output:
Hasil konversi bilangan biner tersebut ke bilangan desimal.

Contoh 1:
Input: 1010
Output: 10

Contoh 2:
Input: 11111
Output: 31
"""

# Input
biner = input()

# Inisialisasi
desimal = 0
pangkat = 1

# Iterasi dari belakang (bit paling rendah) ke depan
for bit in reversed(biner):
    if bit == '1':
        desimal += pangkat
    pangkat *= 2

# Output
print(desimal)

"""
Penjelasan:
1. Program menerima input string biner.
2. Inisialisasi desimal = 0 dan pangkat = 1 (2^0).
3. Iterasi dari bit paling rendah (paling kanan) ke bit paling tinggi (paling kiri):
   - Jika bit saat ini adalah '1', tambahkan nilai pangkat ke desimal
   - Kalikan pangkat dengan 2 untuk bit berikutnya
4. Cetak hasil konversi.

Cara kerja konversi biner ke desimal:
- Setiap digit dalam bilangan biner mewakili pangkat dari 2
- Posisi paling kanan (bit paling rendah) mewakili 2^0 = 1
- Posisi kedua dari kanan mewakili 2^1 = 2
- Posisi ketiga dari kanan mewakili 2^2 = 4
- dan seterusnya
- Jumlahkan semua nilai bit yang bernilai 1

Contoh untuk biner "1010":
- Bit 0 (paling kanan): 0 * 2^0 = 0 * 1 = 0
- Bit 1: 1 * 2^1 = 1 * 2 = 2
- Bit 2: 0 * 2^2 = 0 * 4 = 0
- Bit 3 (paling kiri): 1 * 2^3 = 1 * 8 = 8
- Hasil: 0 + 2 + 0 + 8 = 10

Implementasi alternatif menggunakan pendekatan dari kiri ke kanan:
```python
desimal = 0
for bit in biner:
    desimal = desimal * 2 + int(bit)
```

Implementasi alternatif menggunakan fungsi bawaan Python:
```python
desimal = int(biner, 2)
```

Kompleksitas waktu: O(n) dimana n adalah panjang string biner
Kompleksitas ruang: O(n) untuk menyimpan string biner
""" 