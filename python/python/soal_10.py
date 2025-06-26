"""
Soal 10: Pencarian Biner
Buatlah program untuk mencari posisi sebuah bilangan dalam array terurut menggunakan algoritma pencarian biner.

Input:
Baris pertama berisi sebuah bilangan bulat n (1 ≤ n ≤ 100,000), yaitu banyaknya bilangan dalam array.
Baris kedua berisi n bilangan bulat ai (1 ≤ ai ≤ 10^9) yang terurut dari kecil ke besar.
Baris ketiga berisi sebuah bilangan bulat x (1 ≤ x ≤ 10^9), yaitu bilangan yang dicari.

Output:
Posisi bilangan x dalam array (indeks dimulai dari 1).
Jika bilangan x tidak ditemukan, keluarkan "TIDAK ADA".
Jika bilangan x muncul lebih dari sekali, keluarkan posisi kemunculan pertama.

Contoh 1:
Input:
5
1 3 5 7 9
5

Output:
3

Contoh 2:
Input:
5
1 3 5 7 9
4

Output:
TIDAK ADA
"""

# Input
n = int(input())
arr = list(map(int, input().split()))
x = int(input())

# Pencarian biner
kiri = 0
kanan = n - 1
posisi = -1

while kiri <= kanan:
    tengah = kiri + (kanan - kiri) // 2
    
    if arr[tengah] == x:
        posisi = tengah + 1  # Indeks dimulai dari 1
        
        # Mencari kemunculan pertama jika ada duplikat
        while posisi > 1 and arr[posisi - 2] == x:
            posisi -= 1
        
        break
    elif arr[tengah] < x:
        kiri = tengah + 1
    else:
        kanan = tengah - 1

# Output
print(posisi if posisi != -1 else "TIDAK ADA")

"""
Penjelasan:
1. Program menerima input jumlah bilangan n.
2. Input n bilangan terurut dan simpan dalam list arr.
3. Input bilangan x yang akan dicari.
4. Lakukan pencarian biner:
   - Inisialisasi batas kiri = 0 dan batas kanan = n-1
   - Selama batas kiri <= batas kanan:
     - Hitung tengah = kiri + (kanan - kiri) // 2
     - Jika arr[tengah] == x, kita temukan x
     - Jika arr[tengah] < x, cari di setengah kanan (kiri = tengah + 1)
     - Jika arr[tengah] > x, cari di setengah kiri (kanan = tengah - 1)
   - Jika kita menemukan x, kita perlu mencari kemunculan pertama dengan menggeser ke kiri
5. Cetak posisi jika ditemukan, atau "TIDAK ADA" jika tidak ditemukan.

Algoritma Pencarian Biner:
- Hanya bisa digunakan pada array yang sudah terurut
- Membagi array menjadi dua bagian dan menentukan di bagian mana elemen yang dicari berada
- Jauh lebih efisien daripada pencarian linear untuk array besar

Penanganan Duplikat:
- Saat menemukan nilai x, kita perlu mengecek apakah ada nilai yang sama di sebelah kirinya
- Jika ada, kita geser posisi ke kiri sampai menemukan kemunculan pertama

Kompleksitas waktu: O(log n) karena pencarian biner membagi array menjadi dua pada setiap iterasi
Kompleksitas ruang: O(n) untuk menyimpan array dengan n elemen
""" 