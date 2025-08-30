"""
Soal 5: Palindrom
Buatlah program untuk memeriksa apakah sebuah kata adalah palindrom atau bukan.
Palindrom adalah kata yang jika dibaca dari depan maupun belakang memiliki susunan huruf yang sama.

Input:
Sebuah kata (string) dengan panjang maksimal 100 karakter

Output:
"YA" jika kata tersebut adalah palindrom
"BUKAN" jika kata tersebut bukan palindrom

Contoh 1:
Input: katak
Output: YA

Contoh 2:
Input: mobil
Output: BUKAN
"""

# Input
kata = "katak" #enter random prase

# Cek palindrom
is_palindrom = True
panjang = len(kata)

for i in range(panjang // 2):
    if kata[i] != kata[panjang - 1 - i]:
        is_palindrom = False
        break

# Output
print("YA" if is_palindrom else "BUKAN")

"""
Penjelasan:
1. Program menerima input sebuah kata (string).
2. Inisialisasi variabel is_palindrom dengan nilai True (asumsi awal kata adalah palindrom).
3. Lakukan perulangan dari i = 0 sampai setengah panjang kata:
   - Bandingkan karakter ke-i dari depan dengan karakter ke-i dari belakang
   - Jika ada pasangan karakter yang tidak sama, maka kata bukan palindrom
4. Cetak hasil pengecekan.

Cara kerja algoritma:
- Kita hanya perlu mengecek setengah dari panjang kata karena kita membandingkan secara simetris.
- Untuk kata dengan panjang ganjil, karakter tengah tidak perlu dibandingkan karena pasangannya adalah dirinya sendiri.

Kompleksitas waktu: O(n) dimana n adalah panjang kata
Kompleksitas ruang: O(1) karena hanya menggunakan variabel dengan jumlah tetap
""" 