"""
Soal 21: Anagram
Buatlah program untuk memeriksa apakah dua kata adalah anagram.
Anagram adalah kata yang dibentuk dengan mengatur ulang huruf-huruf dari kata lain.

Input:
Dua string s dan t (panjang masing-masing maksimal 100 karakter, hanya berisi huruf kecil).

Output:
"YA" jika s dan t adalah anagram
"BUKAN" jika s dan t bukan anagram

Contoh 1:
Input:
listen
silent
Output: YA

Contoh 2:
Input:
hello
world
Output: BUKAN
"""

# Input
s = input()
t = input()

# Jika panjang string berbeda, pasti bukan anagram
if len(s) != len(t):
    print("BUKAN")
    exit()

# Menggunakan array untuk menghitung frekuensi karakter
frekuensi = [0] * 26

# Menghitung frekuensi karakter pada string s
for c in s:
    frekuensi[ord(c) - ord('a')] += 1

# Mengurangi frekuensi karakter pada string t
for c in t:
    frekuensi[ord(c) - ord('a')] -= 1

# Cek apakah semua frekuensi karakter kembali ke 0
is_anagram = all(f == 0 for f in frekuensi)

# Output
print("YA" if is_anagram else "BUKAN")

"""
Penjelasan:
1. Program menerima input dua string s dan t.
2. Periksa apakah panjang s dan t sama. Jika berbeda, langsung simpulkan bahwa keduanya bukan anagram.
3. Inisialisasi list frekuensi dengan ukuran 26 (untuk 26 huruf alfabet) dan semua elemen diset 0.
4. Hitung frekuensi kemunculan setiap karakter dalam s:
   - Untuk setiap karakter c dalam s, tambahkan 1 ke frekuensi[ord(c) - ord('a')]
   - Pengurangan ord('a') mengubah karakter menjadi indeks 0-25 (a=0, b=1, ..., z=25)
5. Kurangi frekuensi kemunculan setiap karakter dalam t:
   - Untuk setiap karakter c dalam t, kurangi 1 dari frekuensi[ord(c) - ord('a')]
6. Cek apakah semua elemen dalam list frekuensi bernilai 0.
   - Jika ya, s dan t adalah anagram
   - Jika tidak, s dan t bukan anagram

Cara kerja algoritma:
- Jika s dan t adalah anagram, maka keduanya memiliki huruf dan frekuensi kemunculan yang sama
- Setelah menambahkan frekuensi untuk s dan mengurangi untuk t, semua nilai dalam list frekuensi harus kembali ke 0

Contoh untuk s = "listen" dan t = "silent":
- frekuensi['l'-'a'] = 1, frekuensi['i'-'a'] = 1, frekuensi['s'-'a'] = 1, frekuensi['t'-'a'] = 1, frekuensi['e'-'a'] = 1, frekuensi['n'-'a'] = 1
- Setelah memproses t: semua frekuensi kembali ke 0
- Kesimpulan: Keduanya adalah anagram

Metode alternatif menggunakan Counter dari collections:
```python
from collections import Counter
is_anagram = Counter(s) == Counter(t)
```

Metode alternatif menggunakan pengurutan:
```python
is_anagram = sorted(s) == sorted(t)
```
Namun, metode frekuensi lebih efisien secara waktu (O(n) vs O(n log n) untuk pengurutan)

Kompleksitas waktu: O(n) dimana n adalah panjang string
Kompleksitas ruang: O(1) karena ukuran list frekuensi selalu 26, tidak tergantung pada panjang input
""" 