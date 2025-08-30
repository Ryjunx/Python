"""
Soal 35: Huruf Penyusun Kata
Buatlah program untuk memeriksa apakah dua kata memiliki huruf-huruf penyusun yang sama, tanpa memperhatikan urutan.

Input:
Dua string s dan t (panjang maksimal 20 karakter, hanya berisi huruf kecil).

Output:
"YA" jika s dan t memiliki huruf-huruf penyusun yang sama, "TIDAK" jika tidak.

Contoh 1:
Input:
kasur
rusak
Output:
YA

Contoh 2:
Input:
halo
salam
Output:
TIDAK

Contoh 3:
Input:
mata
tama
Output:
YA
"""

# Input
s = input()
t = input()

def memiliki_huruf_sama(s, t):
    # Jika panjang berbeda, pasti bukan anagram
    if len(s) != len(t):
        return False
    
    # Hitung frekuensi huruf untuk string s
    hitung_huruf = [0] * 26  # Array untuk 26 huruf kecil a-z
    
    # Tambahkan frekuensi untuk setiap huruf di s
    for char in s:
        index = ord(char) - ord('a')  # Konversi karakter ke indeks 0-25
        hitung_huruf[index] += 1
    
    # Kurangi frekuensi untuk setiap huruf di t
    for char in t:
        index = ord(char) - ord('a')
        hitung_huruf[index] -= 1
        
        # Jika ada huruf di t yang tidak ada di s atau lebih banyak
        if hitung_huruf[index] < 0:
            return False
    
    # Cek apakah semua frekuensi bernilai 0
    return all(count == 0 for count in hitung_huruf)

# Output
if memiliki_huruf_sama(s, t):
    print("YA")
else:
    print("TIDAK")

"""
Penjelasan:
1. Program menerima input dua string s dan t.
2. Kita memeriksa apakah kedua string memiliki huruf-huruf penyusun yang sama dengan langkah-langkah:
   - Periksa apakah panjang kedua string sama (syarat pertama)
   - Gunakan array dengan 26 elemen untuk menghitung frekuensi setiap huruf
   - Tambahkan frekuensi untuk setiap huruf di string s
   - Kurangi frekuensi untuk setiap huruf di string t
   - Jika ada frekuensi yang negatif, berarti ada huruf di t yang tidak cukup di s
   - Jika semua frekuensi bernilai 0, berarti kedua string memiliki huruf yang sama
3. Cetak "YA" jika kedua string memiliki huruf yang sama, "TIDAK" jika tidak.

Contoh untuk string "kasur" dan "rusak":
- Panjang keduanya sama (5)
- Hitung frekuensi huruf "kasur":
  - k: 1, a: 1, s: 1, u: 1, r: 1
- Kurangi dengan huruf "rusak":
  - r: 0, u: 0, s: 0, a: 0, k: 0
- Semua frekuensi bernilai 0, jadi keduanya memiliki huruf yang sama

Contoh untuk string "halo" dan "salam":
- Panjang berbeda (4 dan 5), langsung kembalikan false

Implementasi alternatif menggunakan Counter:
```python
from collections import Counter

def memiliki_huruf_sama(s, t):
    return Counter(s) == Counter(t)
```

Implementasi alternatif menggunakan sorted:
```python
def memiliki_huruf_sama(s, t):
    return sorted(s) == sorted(t)
```

Kompleksitas waktu: O(n) untuk pendekatan frekuensi dan Counter, O(n log n) untuk pendekatan sorted
Kompleksitas ruang: O(1) untuk pendekatan frekuensi, O(n) untuk Counter dan sorted
""" 