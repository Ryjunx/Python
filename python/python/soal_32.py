"""
Soal 32: Mencari Palindrom
Buatlah program untuk memeriksa apakah sebuah kata adalah palindrom (dibaca sama dari depan dan belakang).

Input:
Sebuah string s (panjang maksimal 100 karakter, hanya berisi huruf kecil).

Output:
"YA" jika string s adalah palindrom, "TIDAK" jika bukan.
Jika "YA", cetak juga panjang palindrom tersebut pada baris berikutnya.

Contoh 1:
Input: katak
Output:
YA
5

Contoh 2:
Input: mobil
Output:
TIDAK

Contoh 3:
Input: aba
Output:
YA
3
"""

# Input
s = input()

# Fungsi untuk memeriksa palindrom
def is_palindrome(s):
    left = 0
    right = len(s) - 1
    
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    
    return True

# Cek apakah string adalah palindrom
if is_palindrome(s):
    print("YA")
    print(len(s))
else:
    print("TIDAK")

"""
Penjelasan:
1. Program menerima input string s.
2. Fungsi is_palindrome memeriksa apakah string adalah palindrom:
   - Gunakan dua pointer, 'left' dimulai dari awal string dan 'right' dari akhir string
   - Bandingkan karakter yang ditunjuk kedua pointer
   - Jika ada yang tidak sama, string bukan palindrom
   - Jika semua sama sampai kedua pointer bertemu di tengah, string adalah palindrom
3. Jika string adalah palindrom, cetak "YA" dan panjang string tersebut.
   Jika bukan, cetak "TIDAK".

Contoh untuk string "katak":
- left = 0, right = 4: s[0] = 'k', s[4] = 'k', sama → left = 1, right = 3
- left = 1, right = 3: s[1] = 'a', s[3] = 'a', sama → left = 2, right = 2
- left = 2, right = 2: left tidak < right, keluar dari loop
- Semua karakter yang dibandingkan sama, jadi "katak" adalah palindrom
- Output: "YA" dan panjang = 5

Contoh untuk string "mobil":
- left = 0, right = 4: s[0] = 'm', s[4] = 'l', berbeda → bukan palindrom
- Output: "TIDAK"

Implementasi alternatif menggunakan slicing:
```python
def is_palindrome(s):
    return s == s[::-1]
```

Implementasi alternatif menggunakan reversed():
```python
def is_palindrome(s):
    return s == ''.join(reversed(s))
```

Implementasi alternatif menggunakan list:
```python
def is_palindrome(s):
    s_list = list(s)
    s_list.reverse()
    return s == ''.join(s_list)
```

Kompleksitas waktu: O(n) dimana n adalah panjang string, karena kita hanya perlu memeriksa setiap karakter sekali
Kompleksitas ruang: O(1) karena kita hanya menggunakan variabel sederhana
""" 