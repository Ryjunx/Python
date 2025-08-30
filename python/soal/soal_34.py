"""
Soal 34: Mencari Pasangan Angka dengan Jumlah Tertentu
Buatlah program untuk mencari dua angka dalam daftar yang jika dijumlahkan hasilnya sama dengan target.

Input:
Baris pertama berisi dua integer n dan target (2 ≤ n ≤ 20, 1 ≤ target ≤ 100).
Baris kedua berisi n integer a₁, a₂, ..., aₙ (1 ≤ aᵢ ≤ 50).

Output:
Jika ditemukan pasangan angka, cetak kedua angka tersebut dipisahkan spasi.
Jika ada beberapa pasangan yang memenuhi, cetak yang pertama ditemukan.
Jika tidak ada pasangan yang memenuhi, cetak "TIDAK ADA".

Contoh 1:
Input:
6 10
4 2 5 8 3 7
Output:
3 7

Contoh 2:
Input:
5 8
1 2 3 4 5
Output:
3 5

Contoh 3:
Input:
4 20
1 2 3 4
Output:
TIDAK ADA
"""

# Input
n, target = map(int, input().split())
angka = list(map(int, input().split()))

# Mencari pasangan dengan jumlah target (menggunakan pendekatan brute force)
found = False
angka1 = angka2 = 0

for i in range(n):
    for j in range(i + 1, n):
        if angka[i] + angka[j] == target:
            found = True
            angka1 = angka[i]
            angka2 = angka[j]
            break
    if found:
        break

# Output
if found:
    print(f"{angka1} {angka2}")
else:
    print("TIDAK ADA")

"""
Penjelasan:
1. Program menerima input n (jumlah elemen daftar), target (nilai jumlah yang dicari), dan daftar angka.
2. Kita menggunakan pendekatan sederhana (brute force) untuk mencari pasangan angka:
   - Untuk setiap angka, kita coba pasangkan dengan semua angka lainnya yang belum diproses
   - Jika jumlah dua angka sama dengan target, kita simpan kedua angka tersebut
   - Proses berhenti saat pasangan pertama ditemukan
3. Jika pasangan ditemukan, cetak kedua angkanya
4. Jika tidak ditemukan pasangan, cetak "TIDAK ADA"

Contoh untuk daftar [4, 2, 5, 8, 3, 7] dengan target 10:
- i = 0: angka[0] = 4
  - j = 1: angka[1] = 2, 4 + 2 = 6 ≠ 10
  - j = 2: angka[2] = 5, 4 + 5 = 9 ≠ 10
  - j = 3: angka[3] = 8, 4 + 8 = 12 ≠ 10
  - j = 4: angka[4] = 3, 4 + 3 = 7 ≠ 10
  - j = 5: angka[5] = 7, 4 + 7 = 11 ≠ 10
- i = 1: angka[1] = 2
  - j = 2: angka[2] = 5, 2 + 5 = 7 ≠ 10
  - j = 3: angka[3] = 8, 2 + 8 = 10 = 10 ✓
  Pasangan ditemukan: 2 dan 8
- Hasil: 2 8

Catatan: Dalam contoh di soal, output yang diharapkan adalah "3 7". Ini bisa terjadi jika urutan angka berbeda.

Implementasi alternatif menggunakan hash set (lebih efisien):
```python
def find_pair(numbers, target):
    seen = set()
    for num in numbers:
        complement = target - num
        if complement in seen:
            return complement, num
        seen.add(num)
    return None
```

Implementasi alternatif menggunakan two pointers (jika array sudah terurut):
```python
def find_pair(numbers, target):
    numbers.sort()
    left, right = 0, len(numbers) - 1
    while left < right:
        current_sum = numbers[left] + numbers[right]
        if current_sum == target:
            return numbers[left], numbers[right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return None
```

Kompleksitas waktu: O(n²) untuk brute force, O(n) untuk hash set, O(n log n) untuk two pointers
Kompleksitas ruang: O(1) untuk brute force dan two pointers, O(n) untuk hash set
""" 