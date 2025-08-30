"""
Soal 25: Jumlah Subarray Maksimum
Buatlah program untuk mencari jumlah maksimum dari subarray (rangkaian bilangan berurutan) dalam sebuah array.

Input:
Baris pertama berisi sebuah bilangan bulat n (1 ≤ n ≤ 100000), yaitu banyaknya bilangan dalam array.
Baris kedua berisi n bilangan bulat ai (-10^9 ≤ ai ≤ 10^9).

Output:
Jumlah maksimum dari semua kemungkinan subarray.

Contoh 1:
Input:
8
-2 1 -3 4 -1 2 1 -5
Output: 6
(subarray dengan jumlah maksimum adalah [4, -1, 2, 1] dengan jumlah 6)

Contoh 2:
Input:
3
-1 -2 -3
Output: -1
(subarray dengan jumlah maksimum adalah [-1] dengan jumlah -1)
"""

# Input
n = int(input())
arr = list(map(int, input().split()))

# Implementasi algoritma Kadane
max_so_far = float('-inf')
max_ending_here = 0

for num in arr:
    max_ending_here += num
    
    if max_so_far < max_ending_here:
        max_so_far = max_ending_here
    
    if max_ending_here < 0:
        max_ending_here = 0

# Kasus khusus: semua elemen negatif
if max_so_far == float('-inf'):
    max_so_far = max(arr)

# Output
print(max_so_far)

"""
Penjelasan:
1. Program menerima input jumlah bilangan n dan array arr.
2. Implementasi algoritma Kadane untuk mencari jumlah subarray maksimum:
   - max_so_far: menyimpan jumlah subarray maksimum yang ditemukan sejauh ini
   - max_ending_here: menyimpan jumlah subarray maksimum yang berakhir di posisi saat ini
3. Lakukan iterasi pada array:
   - Tambahkan elemen saat ini ke max_ending_here
   - Update max_so_far jika max_ending_here lebih besar
   - Reset max_ending_here ke 0 jika nilainya negatif (lebih baik memulai subarray baru)
4. Tangani kasus khusus: semua elemen negatif
   - Jika max_so_far tetap float('-inf'), berarti semua elemen negatif
   - Dalam kasus ini, cari elemen dengan nilai maksimum
5. Cetak jumlah subarray maksimum.

Algoritma Kadane:
- Algoritma ini menggunakan pendekatan dynamic programming
- Ide utamanya adalah mempertahankan subarray dengan jumlah maksimum di setiap posisi i
- Untuk setiap posisi, kita memutuskan apakah melanjutkan subarray sebelumnya atau memulai subarray baru

Logika algoritma:
- Untuk setiap posisi i, ada dua pilihan:
  1. Melanjutkan subarray sebelumnya (max_ending_here += arr[i])
  2. Memulai subarray baru jika jumlah sebelumnya negatif (max_ending_here = 0, kemudian max_ending_here += arr[i])
- Selalu catat jumlah subarray maksimum yang ditemukan (max_so_far)

Contoh untuk array [-2, 1, -3, 4, -1, 2, 1, -5]:
- Inisialisasi: max_so_far = float('-inf'), max_ending_here = 0
- i = 0: arr[0] = -2 → max_ending_here = 0 + (-2) = -2 → max_ending_here < 0, reset ke 0
- i = 1: arr[1] = 1 → max_ending_here = 0 + 1 = 1 → max_so_far = 1
- i = 2: arr[2] = -3 → max_ending_here = 1 + (-3) = -2 → max_ending_here < 0, reset ke 0
- i = 3: arr[3] = 4 → max_ending_here = 0 + 4 = 4 → max_so_far = 4
- i = 4: arr[4] = -1 → max_ending_here = 4 + (-1) = 3 → max_so_far = 4 (tidak berubah)
- i = 5: arr[5] = 2 → max_ending_here = 3 + 2 = 5 → max_so_far = 5
- i = 6: arr[6] = 1 → max_ending_here = 5 + 1 = 6 → max_so_far = 6
- i = 7: arr[7] = -5 → max_ending_here = 6 + (-5) = 1 → max_so_far = 6 (tidak berubah)
- Hasil: max_so_far = 6

Implementasi alternatif menggunakan pendekatan divide and conquer:
```python
def max_subarray_divide_conquer(arr, low, high):
    if low == high:
        return arr[low]
    
    mid = (low + high) // 2
    
    # Cari jumlah maksimum di subarray kiri
    left_max = max_subarray_divide_conquer(arr, low, mid)
    
    # Cari jumlah maksimum di subarray kanan
    right_max = max_subarray_divide_conquer(arr, mid + 1, high)
    
    # Cari jumlah maksimum yang melintasi tengah
    left_sum = float('-inf')
    sum_so_far = 0
    for i in range(mid, low - 1, -1):
        sum_so_far += arr[i]
        left_sum = max(left_sum, sum_so_far)
    
    right_sum = float('-inf')
    sum_so_far = 0
    for i in range(mid + 1, high + 1):
        sum_so_far += arr[i]
        right_sum = max(right_sum, sum_so_far)
    
    # Kembalikan maksimum dari ketiga nilai
    return max(left_max, right_max, left_sum + right_sum)
```

Implementasi alternatif menggunakan pendekatan brute force (kurang efisien):
```python
def max_subarray_brute_force(arr):
    n = len(arr)
    max_sum = float('-inf')
    
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += arr[j]
            max_sum = max(max_sum, current_sum)
    
    return max_sum
```

Kompleksitas waktu: O(n) dimana n adalah jumlah elemen dalam array
Kompleksitas ruang: O(n) untuk menyimpan array input
""" 