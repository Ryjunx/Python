"""
Soal 38: Cocktail Shaker Sort
Program untuk mengurutkan array menggunakan algoritma Cocktail Shaker Sort.

Input:
Baris pertama berisi sebuah bilangan bulat n (1 ≤ n ≤ 1000), yaitu banyaknya bilangan dalam array.
Daftar n bilangan bulat ai (-10^9 ≤ ai ≤ 10^9).

Output:
Array yang sudah terurut dari kecil ke besar.

Contoh:
Untuk nilai:
n = 5
arr = [5, 2, 9, 1, 7]
Output: 1 2 5 7 9
"""

# Nilai yang akan digunakan (bisa diubah sesuai kebutuhan)
n = 5
arr = [5, 2, 9, 1, 7]

def cocktail_shaker_sort(arr):
    """Mengurutkan array menggunakan algoritma Cocktail Shaker Sort."""
    n = len(arr)
    swapped = True
    start = 0
    end = n - 1
    
    while swapped:
        swapped = False
        
        # Forward pass
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        
        if not swapped:
            break
        
        swapped = False
        end -= 1
        
        # Backward pass
        for i in range(end - 1, start - 1, -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        
        start += 1
    
    return arr

# Lakukan pengurutan
arr = cocktail_shaker_sort(arr)

# Output array terurut
print(" ".join(map(str, arr)))

"""
Penjelasan:
1. Program menggunakan variabel n dan list arr dengan nilai yang sudah ditentukan
2. Cocktail Shaker Sort menggunakan pendekatan:
   - Forward pass: bubble sort dari kiri ke kanan
   - Backward pass: bubble sort dari kanan ke kiri
   - Ulangi sampai array terurut

Cara Kerja Cocktail Shaker Sort:
- Algoritma ini adalah variasi dari bubble sort
- Menggunakan dua arah pengurutan
- Forward pass: bubble sort normal
- Backward pass: bubble sort terbalik

Contoh untuk array [5, 2, 9, 1, 7]:
1. Forward pass:
   - Bandingkan 5 dan 2: [2, 5, 9, 1, 7]
   - Bandingkan 5 dan 9: [2, 5, 9, 1, 7]
   - Bandingkan 9 dan 1: [2, 5, 1, 9, 7]
   - Bandingkan 9 dan 7: [2, 5, 1, 7, 9]
   - Hasil: [2, 5, 1, 7, 9]

2. Backward pass:
   - Bandingkan 7 dan 1: [2, 5, 1, 7, 9]
   - Bandingkan 5 dan 1: [2, 1, 5, 7, 9]
   - Bandingkan 2 dan 1: [1, 2, 5, 7, 9]
   - Hasil: [1, 2, 5, 7, 9]

3. Forward pass:
   - Bandingkan 1 dan 2: [1, 2, 5, 7, 9]
   - Bandingkan 2 dan 5: [1, 2, 5, 7, 9]
   - Bandingkan 5 dan 7: [1, 2, 5, 7, 9]
   - Bandingkan 7 dan 9: [1, 2, 5, 7, 9]
   - Hasil: [1, 2, 5, 7, 9]

Catatan:
- Cocktail Shaker Sort adalah algoritma pengurutan yang efisien
- Menggunakan dua arah pengurutan
- Stabil dalam pengurutan
- Lebih cepat dari bubble sort

Kompleksitas waktu: 
- Kasus terbaik: O(n) saat array sudah terurut
- Kasus terburuk: O(n²) saat array terurut terbalik
Kompleksitas ruang: O(1) karena tidak memerlukan ruang tambahan
"""

"""
Soal 38: Menggabungkan Dua Array
Buatlah program untuk menggabungkan dua array menjadi satu array baru.

Input:
Baris pertama berisi bilangan bulat n (1 ≤ n ≤ 50), yaitu banyaknya bilangan dalam array pertama.
Baris kedua berisi n bilangan bulat a₁, a₂, ..., aₙ (1 ≤ aᵢ ≤ 100).
Baris ketiga berisi bilangan bulat m (1 ≤ m ≤ 50), yaitu banyaknya bilangan dalam array kedua.
Baris keempat berisi m bilangan bulat b₁, b₂, ..., bₘ (1 ≤ bᵢ ≤ 100).

Output:
Satu baris berisi n+m bilangan bulat, yaitu hasil penggabungan array pertama dan array kedua.

Contoh:
Input:
3
10 20 30
4
5 15 25 35
Output:
10 20 30 5 15 25 35
"""

# Input
n = int(input())
arr1 = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))

# Gabungkan kedua array
gabungan = arr1 + arr2

# Output
print(*gabungan)

"""
Penjelasan:
1. Program menerima input ukuran dan elemen-elemen dari dua array: arr1 dan arr2.
2. Untuk menggabungkan dua array, kita membuat array baru (gabungan) dan melakukan dua langkah:
   - Salin semua elemen array pertama ke array gabungan
   - Salin semua elemen array kedua ke array gabungan mulai dari indeks n
3. Cetak array hasil penggabungan.

Contoh untuk array pertama [10, 20, 30] dan array kedua [5, 15, 25, 35]:
- n = 3, m = 4
- Salin array pertama ke gabungan:
  - gabungan[0] = arr1[0] = 10
  - gabungan[1] = arr1[1] = 20
  - gabungan[2] = arr1[2] = 30
- Salin array kedua ke gabungan mulai dari indeks n = 3:
  - gabungan[3] = arr2[0] = 5
  - gabungan[4] = arr2[1] = 15
  - gabungan[5] = arr2[2] = 25
  - gabungan[6] = arr2[3] = 35
- Hasil: [10, 20, 30, 5, 15, 25, 35]

Alternatif Pythonic:
```python
print(*(arr1 + arr2))
```

Kompleksitas waktu: O(n+m), karena kita perlu menyalin n elemen dari array pertama dan m elemen dari array kedua
Kompleksitas ruang: O(n+m) untuk menyimpan array hasil penggabungan
""" 