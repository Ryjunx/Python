"""
Soal 27: Tim Sort
Program untuk mengurutkan array menggunakan algoritma Tim Sort.

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

def insertion_sort(arr, left, right):
    """Mengurutkan subarray menggunakan insertion sort."""
    for i in range(left + 1, right + 1):
        temp = arr[i]
        j = i - 1
        while j >= left and arr[j] > temp:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = temp

def merge(arr, left, mid, right):
    """Menggabungkan dua subarray terurut."""
    # Buat salinan subarray kiri dan kanan
    left_arr = arr[left:mid + 1]
    right_arr = arr[mid + 1:right + 1]
    
    i = j = 0
    k = left
    
    # Gabungkan subarray
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1
    
    # Salin sisa elemen
    while i < len(left_arr):
        arr[k] = left_arr[i]
        i += 1
        k += 1
    
    while j < len(right_arr):
        arr[k] = right_arr[j]
        j += 1
        k += 1

def tim_sort(arr):
    """Mengurutkan array menggunakan algoritma Tim Sort."""
    n = len(arr)
    min_run = 32
    
    # Urutkan subarray dengan insertion sort
    for i in range(0, n, min_run):
        insertion_sort(arr, i, min(i + min_run - 1, n - 1))
    
    # Gabungkan subarray dengan merge sort
    size = min_run
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(left + size - 1, n - 1)
            right = min(left + 2 * size - 1, n - 1)
            merge(arr, left, mid, right)
        size *= 2

# Lakukan pengurutan
tim_sort(arr)

# Output array terurut
print(" ".join(map(str, arr)))

"""
Penjelasan:
1. Program menggunakan variabel n dan list arr dengan nilai yang sudah ditentukan
2. Tim Sort menggunakan pendekatan hybrid:
   - Bagi array menjadi run (subarray terurut)
   - Urutkan run dengan insertion sort
   - Gabungkan run dengan merge sort

Cara Kerja Tim Sort:
- Algoritma ini adalah kombinasi insertion sort dan merge sort
- Menggunakan insertion sort untuk run kecil
- Menggunakan merge sort untuk menggabungkan run
- Mengoptimalkan performa untuk data yang hampir terurut

Contoh untuk array [5, 2, 9, 1, 7]:
1. Bagi array menjadi run (min_run = 32):
   - Run 1: [5]
   - Run 2: [2]
   - Run 3: [9]
   - Run 4: [1]
   - Run 5: [7]

2. Urutkan run dengan insertion sort:
   - Run 1: [5]
   - Run 2: [2]
   - Run 3: [9]
   - Run 4: [1]
   - Run 5: [7]

3. Gabungkan run dengan merge sort:
   - Merge [5] dan [2] → [2, 5]
   - Merge [9] dan [1] → [1, 9]
   - Merge [7] → [7]
   - Merge [2, 5] dan [1, 9] → [1, 2, 5, 9]
   - Merge [1, 2, 5, 9] dan [7] → [1, 2, 5, 7, 9]

Catatan:
- Tim Sort adalah algoritma pengurutan yang efisien
- Digunakan dalam Python's built-in sort
- Stabil dalam pengurutan
- Cocok untuk berbagai jenis data

Kompleksitas waktu: 
- Kasus terbaik: O(n) saat array sudah terurut
- Kasus terburuk: O(n log n)
Kompleksitas ruang: O(n) untuk menyimpan array tambahan saat merge
""" 