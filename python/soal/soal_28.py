"""
Soal 28: Mencari Huruf yang Sama
Buatlah program untuk menemukan berapa huruf yang sama di awal dari dua kata.

Input:
Dua kata (masing-masing panjang maksimal 20 karakter, hanya berisi huruf kecil).

Output:
Baris pertama berisi jumlah huruf yang sama di awal kedua kata.
Baris kedua berisi huruf-huruf yang sama tersebut, atau "TIDAK ADA" jika tidak ada huruf yang sama.

Contoh 1:
Input:
program
proses
Output:
3
pro

Contoh 2:
Input:
apel
jeruk
Output:
0
TIDAK ADA
"""

# Input
kata1 = input()
kata2 = input()

# Cari jumlah huruf yang sama di awal
jumlah_sama = 0

# Bandingkan karakter satu per satu dari awal
while (jumlah_sama < len(kata1) and jumlah_sama < len(kata2) and 
       kata1[jumlah_sama] == kata2[jumlah_sama]):
    jumlah_sama += 1

# Output jumlah huruf yang sama
print(jumlah_sama)

# Output huruf-huruf yang sama atau "TIDAK ADA"
if jumlah_sama > 0:
    # Ambil substring dari awal sampai jumlah_sama
    awalan = kata1[:jumlah_sama]
    print(awalan)
else:
    print("TIDAK ADA")

"""
Penjelasan:
1. Program menerima input dua kata: kata1 dan kata2.
2. Untuk mencari berapa huruf yang sama di awal kedua kata:
   - Inisialisasi variabel jumlah_sama = 0
   - Bandingkan karakter yang sama posisinya dari awal kedua kata
   - Selama karakter masih sama dan belum mencapai akhir kata, tambah jumlah_sama
   - Berhenti jika menemukan karakter yang berbeda atau salah satu kata habis
3. Cetak jumlah huruf yang sama.
4. Cetak huruf-huruf yang sama atau "TIDAK ADA" jika tidak ada yang sama.

Contoh untuk kata "program" dan "proses":
- Karakter di posisi 0: 'p' == 'p' → jumlah_sama = 1
- Karakter di posisi 1: 'r' == 'r' → jumlah_sama = 2
- Karakter di posisi 2: 'o' == 'o' → jumlah_sama = 3
- Karakter di posisi 3: 'g' != 's' → berhenti
- Jumlah huruf yang sama: 3
- Huruf-huruf yang sama: "pro"

Contoh untuk kata "apel" dan "jeruk":
- Karakter di posisi 0: 'a' != 'j' → berhenti
- Jumlah huruf yang sama: 0
- Cetak: "TIDAK ADA"

Implementasi alternatif menggunakan zip:
```python
def find_common_prefix(kata1, kata2):
    common_chars = []
    for c1, c2 in zip(kata1, kata2):
        if c1 == c2:
            common_chars.append(c1)
        else:
            break
    return len(common_chars), ''.join(common_chars) if common_chars else "TIDAK ADA"
```

Implementasi alternatif menggunakan list comprehension:
```python
def find_common_prefix(kata1, kata2):
    common_chars = [c1 for c1, c2 in zip(kata1, kata2) if c1 == c2]
    return len(common_chars), ''.join(common_chars) if common_chars else "TIDAK ADA"
```

Kompleksitas waktu: O(min(n, m)), dimana n dan m adalah panjang kedua kata
Kompleksitas ruang: O(k), dimana k adalah jumlah huruf yang sama di awal, untuk menyimpan substring
""" 