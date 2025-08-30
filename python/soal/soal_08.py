"""
Soal 8: Bilangan Terbesar Kedua
Buatlah program untuk mencari bilangan terbesar kedua dari n bilangan.

Input:
Baris pertama berisi sebuah bilangan bulat n (3 ≤ n ≤ 1000), yaitu banyaknya bilangan.
Baris kedua berisi n bilangan bulat ai (-10^9 ≤ ai ≤ 10^9).

Output:
Bilangan terbesar kedua dari n bilangan tersebut.

Contoh:
Input:
5
1 5 3 8 2

Output:
5
"""

# Input
n = 3
bilangan = [4,6,6,5]

# Inisialisasi variabel
terbesar = float('-inf')       # Nilai terkecil yang mungkin
terbesar_kedua = float('-inf') # Nilai terkecil yang mungkin

# Mencari bilangan terbesar kedua
for x in bilangan:
    if x > terbesar:
        terbesar_kedua = terbesar
        terbesar = x
    elif x > terbesar_kedua and x < terbesar:
        terbesar_kedua = x
    elif x == terbesar and terbesar > terbesar_kedua:
        terbesar_kedua = x
    elif x < terbesar and terbesar_kedua > x:
        terbesar_kedua = x

# Output
print(terbesar_kedua)

"""
Penjelasan:
1. Program menerima input jumlah bilangan n.
2. Inisialisasi variabel terbesar dan terbesar_kedua dengan nilai terkecil yang mungkin.
3. Untuk setiap bilangan yang dibaca:
   - Jika bilangan > terbesar, maka terbesar_kedua menjadi terbesar, dan terbesar menjadi bilangan.
   - Jika bilangan > terbesar_kedua dan bilangan < terbesar, maka terbesar_kedua menjadi bilangan.
   - Jika bilangan sama dengan terbesar, dan terbesar > terbesar_kedua, maka terbesar_kedua menjadi bilangan.
4. Cetak nilai terbesar_kedua.

Catatan:
- Kita perlu menangani kasus ketika ada bilangan yang sama.
- Dalam Python, kita bisa menggunakan float('-inf') untuk merepresentasikan nilai terkecil yang mungkin.

Contoh untuk input: 1 5 3 8 2
- Awal: terbesar = -inf, terbesar_kedua = -inf
- Bilangan 1: terbesar = 1, terbesar_kedua = -inf
- Bilangan 5: terbesar = 5, terbesar_kedua = 1
- Bilangan 3: terbesar = 5, terbesar_kedua = 3
- Bilangan 8: terbesar = 8, terbesar_kedua = 5
- Bilangan 2: terbesar = 8, terbesar_kedua = 5 (tidak berubah)
- Hasil akhir: terbesar_kedua = 5

Kompleksitas waktu: O(n) karena kita melakukan satu kali iterasi untuk semua bilangan
Kompleksitas ruang: O(1) karena hanya menggunakan variabel dengan jumlah tetap
""" 