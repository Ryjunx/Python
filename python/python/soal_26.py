"""
Soal 26: Membalik Kata
Buatlah program untuk membalik urutan huruf dalam sebuah kata.

Input:
Sebuah kata (panjang maksimal 20 karakter, hanya berisi huruf kecil).

Output:
Kata tersebut setelah dibalik.

Contoh 1:
Input: halo
Output: olah

Contoh 2:
Input: sekolah
Output: halokes
"""

# Input
kata = input()

# Buat string kosong untuk menyimpan hasil
hasil = ""

# Loop dari karakter terakhir ke karakter pertama
for i in range(len(kata) - 1, -1, -1):
    hasil += kata[i]

# Output
print(hasil)

"""
Penjelasan:
1. Program menerima input sebuah kata.
2. Untuk membalik kata, kita mulai dari huruf terakhir dan tambahkan satu per satu ke string hasil.
3. Loop berjalan dari karakter terakhir (indeks length-1) sampai karakter pertama (indeks 0).
4. Pada setiap langkah, karakter pada posisi i ditambahkan ke string hasil.
5. Hasilnya adalah kata yang dibalik.

Contoh untuk kata "halo":
- len(kata) = 4
- Loop dari i = 3 sampai i = 0:
  - i = 3: hasil += 'o' → hasil = "o"
  - i = 2: hasil += 'l' → hasil = "ol"
  - i = 1: hasil += 'a' → hasil = "ola"
  - i = 0: hasil += 'h' → hasil = "olah"
- Hasil akhir: "olah"

Implementasi alternatif menggunakan slicing:
```python
hasil = kata[::-1]
```

Implementasi alternatif menggunakan reversed():
```python
hasil = ''.join(reversed(kata))
```

Implementasi alternatif menggunakan list:
```python
kata_list = list(kata)
kata_list.reverse()
hasil = ''.join(kata_list)
```

Kompleksitas waktu: O(n), dimana n adalah panjang kata
Kompleksitas ruang: O(n), untuk menyimpan kata yang dibalik
""" 