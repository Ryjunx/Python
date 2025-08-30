"""
Soal 9: Pencarian Linear
Buatlah program untuk mencari posisi sebuah bilangan dalam array menggunakan algoritma pencarian linear.

Input:
Baris pertama berisi sebuah bilangan bulat n (1 ≤ n ≤ 1000), yaitu banyaknya bilangan dalam array.
Baris kedua berisi n bilangan bulat ai (1 ≤ ai ≤ 10^9).
Baris ketiga berisi sebuah bilangan bulat x (1 ≤ x ≤ 10^9), yaitu bilangan yang dicari.

Output:
Posisi bilangan x dalam array (indeks dimulai dari 1).
Jika bilangan x tidak ditemukan, keluarkan "TIDAK ADA".
Jika bilangan x muncul lebih dari sekali, keluarkan posisi kemunculan pertama.

Contoh 1:
Input:
5
4 2 7 8 3
7

Output:
3

Contoh 2:
Input:
5
4 2 7 8 3
5

Output:
TIDAK ADA
"""

# Input
n = int(input())
arr = list(map(int, input().split()))
x = int(input())

# Pencarian linear
posisi = -1
for i in range(n):
    if arr[i] == x:
        posisi = i + 1  # Indeks dimulai dari 1
        break

# Output
print(posisi if posisi != -1 else "TIDAK ADA")

"""
Penjelasan:
1. Program menerima input jumlah bilangan n.
2. Input n bilangan dan simpan dalam list arr.
3. Input bilangan x yang akan dicari.
4. Lakukan pencarian linear:
   - Iterasi array dari awal hingga akhir
   - Periksa apakah elemen saat ini sama dengan x
   - Jika iya, simpan posisinya (indeks + 1 karena indeks dimulai dari 1) dan hentikan pencarian
5. Cetak posisi jika ditemukan, atau "TIDAK ADA" jika tidak ditemukan.

Algoritma Pencarian Linear:
- Merupakan algoritma pencarian paling sederhana
- Memeriksa setiap elemen array satu per satu hingga menemukan elemen yang dicari
- Efisien untuk array kecil atau array yang tidak terurut

Kompleksitas waktu: 
- Kasus terbaik: O(1) jika elemen yang dicari berada di awal array
- Kasus terburuk: O(n) jika elemen yang dicari berada di akhir array atau tidak ada dalam array
Kompleksitas ruang: O(n) untuk menyimpan array dengan n elemen
""" 