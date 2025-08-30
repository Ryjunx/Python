"""
Soal 14: Counting Sort
Buatlah program untuk mengurutkan array bilangan bulat positif menggunakan algoritma Counting Sort.

Input:
Baris pertama berisi sebuah bilangan bulat n (1 ≤ n ≤ 1000), yaitu banyaknya bilangan dalam array.
Baris kedua berisi n bilangan bulat ai (0 ≤ ai ≤ 1000).

Output:
Array yang sudah terurut dari kecil ke besar.

Contoh:
Input:
8
5 2 9 5 2 3 5 1

Output:
1 2 2 3 5 5 5 9
"""

# Input
n = int(input())
arr = list(map(int, input().split()))

# Menentukan nilai maksimum dalam array
maksimum = max(arr)

# Counting Sort
count = [0] * (maksimum + 1)  # Array untuk menghitung frekuensi setiap elemen

# Hitung frekuensi setiap elemen
for x in arr:
    count[x] += 1

# Rekonstruksi array terurut
index = 0
for i in range(maksimum + 1):
    for j in range(count[i]):
        arr[index] = i
        index += 1

# Output array terurut
print(*arr)

"""
Penjelasan:
1. Program menerima input jumlah bilangan n.
2. Input n bilangan dan simpan dalam list arr.
3. Cari nilai maksimum dalam array.
4. Lakukan pengurutan dengan Counting Sort:
   - Inisialisasi list count dengan ukuran maksimum+1 dan isi dengan 0
   - Hitung frekuensi setiap elemen dalam array arr
   - Rekonstruksi array terurut berdasarkan frekuensi elemen
5. Cetak array yang sudah terurut.

Cara Kerja Counting Sort:
- Counting Sort adalah algoritma pengurutan non-komparatif, artinya tidak membandingkan elemen secara langsung
- Algoritma ini efisien ketika kita tahu rentang nilai elemen (biasanya rentang kecil)
- Ide utamanya adalah menghitung berapa kali setiap elemen muncul, lalu membentuk array terurut berdasarkan informasi tersebut

Contoh untuk array [5, 2, 9, 5, 2, 3, 5, 1]:
- Nilai maksimum = 9
- Inisialisasi array count[10] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
- Hitung frekuensi:
  - count[1] = 1 (satu buah angka 1)
  - count[2] = 2 (dua buah angka 2)
  - count[3] = 1 (satu buah angka 3)
  - count[4] = 0 (tidak ada angka 4)
  - count[5] = 3 (tiga buah angka 5)
  - count[6] = 0 (tidak ada angka 6)
  - count[7] = 0 (tidak ada angka 7)
  - count[8] = 0 (tidak ada angka 8)
  - count[9] = 1 (satu buah angka 9)
- Rekonstruksi array: [1, 2, 2, 3, 5, 5, 5, 9]

Keunggulan Counting Sort:
- Kompleksitas waktu O(n + k) dimana n adalah jumlah elemen dan k adalah rentang nilai (maksimum - minimum + 1)
- Stabil, artinya urutan elemen yang sama dipertahankan
- Sangat efisien untuk rentang nilai yang kecil

Keterbatasan:
- Membutuhkan memori ekstra untuk array count
- Kurang efisien jika rentang nilai besar dan jumlah elemen sedikit
- Hanya bisa digunakan untuk mengurutkan bilangan bulat atau karakter

Kompleksitas waktu: O(n + k) dimana n adalah jumlah elemen dan k adalah rentang nilai
Kompleksitas ruang: O(n + k) untuk menyimpan array input dan array count
""" 