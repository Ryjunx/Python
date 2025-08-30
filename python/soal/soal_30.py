"""
Soal 30: Nilai yang Paling Sering Muncul
Buatlah program untuk mencari nilai yang paling sering muncul dalam sebuah array.

Input:
Baris pertama berisi bilangan bulat n (1 ≤ n ≤ 50), yaitu banyaknya bilangan dalam array.
Baris kedua berisi n bilangan bulat a₁, a₂, ..., aₙ (1 ≤ aᵢ ≤ 100).

Output:
Nilai yang paling sering muncul dalam array. Jika ada beberapa nilai dengan frekuensi tertinggi yang sama, keluarkan nilai yang lebih kecil.

Contoh 1:
Input:
8
5 2 7 2 9 2 5 3
Output:
2
(nilai 2 muncul 3 kali, paling banyak)

Contoh 2:
Input:
5
1 2 3 1 2
Output:
1
(nilai 1 dan 2 sama-sama muncul 2 kali, tetapi 1 lebih kecil)
"""

# Input
n = int(input())
arr = list(map(int, input().split()))

# Array untuk menghitung frekuensi kemunculan setiap nilai (1-100)
frekuensi = [0] * 101  # inisialisasi semua nilai dengan 0

# Hitung frekuensi kemunculan setiap nilai
for num in arr:
    frekuensi[num] += 1

# Cari nilai dengan frekuensi tertinggi
nilai_terbanyak = 0
frekuensi_tertinggi = 0

for i in range(1, 101):
    if frekuensi[i] > frekuensi_tertinggi:
        frekuensi_tertinggi = frekuensi[i]
        nilai_terbanyak = i

# Output
print(nilai_terbanyak)

"""
Penjelasan:
1. Program menerima input jumlah bilangan n dan array arr.
2. Kita menggunakan array frekuensi untuk menghitung berapa kali setiap nilai muncul:
   - Inisialisasi array frekuensi dengan ukuran 101 (indeks 0-100) dan semua nilai awal 0
   - Loop melalui array input, dan untuk setiap nilai arr[i], tambahkan frekuensi[arr[i]]
   - Nilai pada frekuensi[i] menunjukkan berapa kali nilai i muncul dalam array
3. Cari nilai yang paling sering muncul:
   - Loop dari 1 sampai 100 (sesuai batasan nilai)
   - Bandingkan frekuensi setiap nilai dengan frekuensi tertinggi yang sudah ditemukan
   - Jika menemukan frekuensi yang lebih tinggi, update nilai_terbanyak dan frekuensi_tertinggi
4. Cetak nilai yang paling sering muncul.

Contoh untuk array [5, 2, 7, 2, 9, 2, 5, 3]:
- Frekuensi:
  - frekuensi[2] = 3 (nilai 2 muncul 3 kali)
  - frekuensi[3] = 1 (nilai 3 muncul 1 kali)
  - frekuensi[5] = 2 (nilai 5 muncul 2 kali)
  - frekuensi[7] = 1 (nilai 7 muncul 1 kali)
  - frekuensi[9] = 1 (nilai 9 muncul 1 kali)
- Nilai dengan frekuensi tertinggi: 2 (muncul 3 kali)

Catatan:
- Karena kita mencari nilai dari yang terkecil, loop kita dimulai dari 1 hingga 100
- Dengan demikian, jika ada beberapa nilai dengan frekuensi yang sama, kita akan mengambil yang lebih kecil
- Metode ini efisien karena kita hanya perlu melewati array sekali

Implementasi alternatif menggunakan Counter:
```python
from collections import Counter

def find_most_frequent(arr):
    # Hitung frekuensi menggunakan Counter
    frekuensi = Counter(arr)
    
    # Cari nilai dengan frekuensi tertinggi
    nilai_terbanyak = min(frekuensi.items(), key=lambda x: (-x[1], x[0]))[0]
    
    return nilai_terbanyak
```

Implementasi alternatif menggunakan dictionary:
```python
def find_most_frequent(arr):
    # Hitung frekuensi menggunakan dictionary
    frekuensi = {}
    for num in arr:
        frekuensi[num] = frekuensi.get(num, 0) + 1
    
    # Cari nilai dengan frekuensi tertinggi
    nilai_terbanyak = min(frekuensi.items(), key=lambda x: (-x[1], x[0]))[0]
    
    return nilai_terbanyak
```

Kompleksitas waktu: O(n + k), dimana n adalah jumlah elemen array dan k adalah rentang nilai (dalam hal ini 100)
Kompleksitas ruang: O(k), untuk menyimpan array frekuensi
""" 