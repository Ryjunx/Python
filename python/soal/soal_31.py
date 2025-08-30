"""
Soal 31: Menghitung Huruf Berurutan
Buatlah program untuk menghitung berapa kali suatu huruf muncul secara berurutan dalam sebuah kata.

Input:
Sebuah string s (panjang maksimal 100 karakter, hanya berisi huruf kecil).

Output:
Baris pertama berisi jumlah karakter unik dalam string.
Baris-baris berikutnya berisi karakter dan jumlah kemunculan berurutan terbanyak untuk karakter tersebut.

Contoh 1:
Input: aabcccaaa
Output:
3
a 3
b 1
c 3

Contoh 2:
Input: hello
Output:
4
h 1
e 1
l 2
o 1
"""

# Input
s = input()

# Jika string kosong
if not s:
    print(0)
    exit()

# Dictionary untuk menyimpan karakter unik dan kemunculan berurutan terbanyak
char_count = {}

# Proses string
i = 0
while i < len(s):
    current_char = s[i]
    count = 1
    
    # Hitung kemunculan berurutan
    while i + 1 < len(s) and s[i + 1] == current_char:
        count += 1
        i += 1
    
    # Update jumlah kemunculan berurutan terbanyak
    if current_char in char_count:
        char_count[current_char] = max(char_count[current_char], count)
    else:
        char_count[current_char] = count
    
    i += 1

# Output
print(len(char_count))  # Jumlah karakter unik
for char in sorted(char_count.keys()):  # Urutkan karakter
    print(f"{char} {char_count[char]}")

"""
Penjelasan:
1. Program menerima input string s.
2. Jika string kosong, langsung output 0 dan keluar.
3. Gunakan dictionary char_count untuk menyimpan:
   - Key: karakter unik
   - Value: jumlah kemunculan berurutan terbanyak
4. Proses string dengan pendekatan sliding window:
   - Untuk setiap karakter, hitung berapa kali muncul secara berurutan
   - Update nilai di dictionary jika jumlah kemunculan berurutan saat ini lebih besar
5. Cetak jumlah karakter unik dan daftar karakter beserta jumlah kemunculan berurutan terbanyaknya.

Contoh untuk string "aabcccaaa":
- Proses 'a': count = 2 → char_count['a'] = 2
- Proses 'b': count = 1 → char_count['b'] = 1
- Proses 'c': count = 3 → char_count['c'] = 3
- Proses 'a': count = 3 → char_count['a'] = max(2, 3) = 3

Hasil:
3 (jumlah karakter unik: a, b, c)
a 3
b 1
c 3

Implementasi alternatif menggunakan groupby dari itertools:
```python
from itertools import groupby

def count_consecutive(s):
    char_count = {}
    for char, group in groupby(s):
        count = len(list(group))
        char_count[char] = max(char_count.get(char, 0), count)
    return char_count
```

Implementasi alternatif menggunakan list comprehension:
```python
def count_consecutive(s):
    return {char: max(len(list(g)) for _, g in groupby(s) if _ == char) 
            for char in set(s)}
```

Kompleksitas waktu: O(n) dimana n adalah panjang string
Kompleksitas ruang: O(k) dimana k adalah jumlah karakter unik (maksimal 26 untuk huruf kecil)
""" 