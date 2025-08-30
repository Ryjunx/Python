"""
Soal 23: Kembalian Uang
Buatlah program untuk menghitung jumlah koin minimum yang dibutuhkan untuk menghasilkan kembalian sejumlah n.
Tersedia koin dengan nilai 1, 5, 10, 25, dan 50.

Input:
Sebuah bilangan bulat positif n (1 ≤ n ≤ 10000), menyatakan jumlah kembalian yang dibutuhkan.

Output:
Jumlah koin minimum yang dibutuhkan.

Contoh 1:
Input: 42
Output: 4
(karena bisa menggunakan 25 + 10 + 5 + 2*1 = 42, total 4 koin)

Contoh 2:
Input: 100
Output: 2
(karena bisa menggunakan 2*50 = 100, total 2 koin)
"""

# Input
n = int(input())

# Nilai koin yang tersedia
koin = [1, 5, 10, 25, 50]

# Inisialisasi list dp untuk menyimpan jumlah koin minimum
dp = [float('inf')] * (n + 1)
dp[0] = 0  # Basis: 0 koin untuk menghasilkan kembalian 0

# Isi list dp dengan pendekatan bottom-up
for i in range(1, n + 1):
    for j in range(len(koin)):
        if koin[j] <= i and dp[i - koin[j]] != float('inf'):
            dp[i] = min(dp[i], dp[i - koin[j]] + 1)

# Output
print(dp[n])

"""
Penjelasan:
1. Program menerima input jumlah kembalian n.
2. Inisialisasi list koin dengan nilai koin yang tersedia (1, 5, 10, 25, 50).
3. Inisialisasi list dp dengan ukuran n+1:
   - dp[i] menyimpan jumlah koin minimum untuk menghasilkan kembalian i
   - Inisialisasi semua nilai dengan infinity
   - dp[0] = 0 karena tidak membutuhkan koin untuk menghasilkan kembalian 0
4. Isi list dp dengan pendekatan dynamic programming bottom-up:
   - Untuk setiap nilai kembalian i dari 1 hingga n:
     - Coba setiap jenis koin
     - Jika nilai koin <= i dan dp[i - koin] telah terdefinisi:
       - Update dp[i] dengan min(dp[i], dp[i - koin] + 1)
5. Cetak dp[n] sebagai hasil akhir.

Pendekatan dynamic programming:
- Submasalah: dp[i] = jumlah koin minimum untuk menghasilkan kembalian i
- Rekurens: dp[i] = min(dp[i], dp[i - koin[j]] + 1) untuk setiap koin[j] <= i
- Pendekatan bottom-up: menghitung dari nilai yang lebih kecil ke nilai yang lebih besar

Penjelasan rekurens:
- Untuk menghasilkan kembalian i, kita ambil satu koin dengan nilai koin[j]
- Kemudian kita butuh menghasilkan kembalian (i - koin[j])
- Jumlah koin total adalah dp[i - koin[j]] + 1

Contoh untuk n = 11:
- dp[0] = 0 (basis)
- dp[1] = dp[0] + 1 = 1 (satu koin 1)
- dp[2] = dp[1] + 1 = 2 (dua koin 1)
- dp[3] = dp[2] + 1 = 3 (tiga koin 1)
- dp[4] = dp[3] + 1 = 4 (empat koin 1)
- dp[5] = min(dp[4] + 1, dp[0] + 1) = min(5, 1) = 1 (satu koin 5)
- dp[6] = min(dp[5] + 1, dp[1] + 1) = min(2, 2) = 2 (satu koin 5 + satu koin 1)
- ...
- dp[10] = min(dp[9] + 1, dp[5] + 1, dp[0] + 1) = min(5, 2, 1) = 1 (satu koin 10)
- dp[11] = min(dp[10] + 1, dp[6] + 1, dp[1] + 1) = min(2, 3, 2) = 2 (satu koin 10 + satu koin 1)

Implementasi alternatif menggunakan rekursi dengan memoization:
```python
def coin_change(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 0:
        return 0
    if n < 0:
        return float('inf')
    
    min_coins = float('inf')
    for coin in koin:
        if coin <= n:
            min_coins = min(min_coins, coin_change(n - coin, memo) + 1)
    
    memo[n] = min_coins
    return min_coins
```

Implementasi alternatif menggunakan pendekatan greedy (tidak selalu optimal):
```python
def greedy_coin_change(n):
    coins = 0
    for coin in sorted(koin, reverse=True):
        while n >= coin:
            n -= coin
            coins += 1
    return coins
```

Kompleksitas waktu: O(n * k) dimana n adalah jumlah kembalian dan k adalah jumlah jenis koin
Kompleksitas ruang: O(n) untuk menyimpan list dp
""" 