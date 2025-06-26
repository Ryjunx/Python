"""
Soal 15: Jumlah Digit
Buatlah program untuk menghitung jumlah semua digit dari sebuah bilangan.

Input:
Sebuah bilangan bulat positif n (1 ≤ n ≤ 10^18).

Output:
Jumlah semua digit dari bilangan n.

Contoh 1:
Input: 12345
Output: 15

Contoh 2:
Input: 9876543210
Output: 45
"""

# Input
n = input()

# Menjumlahkan semua digit
jumlah = sum(int(digit) for digit in n)

# Output
print(jumlah)

"""
Penjelasan:
1. Program menerima input berupa string n karena bilangan bisa sangat besar (hingga 10^18).
2. Menggunakan list comprehension dan fungsi sum() untuk menjumlahkan semua digit:
   - Konversi setiap karakter digit menjadi nilai numerik dengan int()
   - Jumlahkan semua nilai digit
3. Cetak hasil penjumlahan digit.

Teknik pengolahan digit:
- Dalam Python, kita bisa langsung mengkonversi karakter digit menjadi nilai numerik dengan int()
- Tidak perlu mengurangkan dengan '0' seperti dalam C++ karena Python menangani konversi ini secara otomatis

Metode alternatif (jika menggunakan tipe data numeric):
```python
n = int(input())
jumlah = 0
    
while n > 0:
    jumlah += n % 10  # Ambil digit terakhir
    n //= 10         # Hapus digit terakhir
```
Namun pendekatan ini terbatas pada rentang tipe data int.

Contoh untuk n = 12345:
- digit = '1' → nilai = 1 → jumlah = 0 + 1 = 1
- digit = '2' → nilai = 2 → jumlah = 1 + 2 = 3
- digit = '3' → nilai = 3 → jumlah = 3 + 3 = 6
- digit = '4' → nilai = 4 → jumlah = 6 + 4 = 10
- digit = '5' → nilai = 5 → jumlah = 10 + 5 = 15
- Hasil akhir: 15

Kompleksitas waktu: O(d) dimana d adalah jumlah digit dalam bilangan n
Kompleksitas ruang: O(d) untuk menyimpan string dengan d digit
""" 