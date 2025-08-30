hobi_budi = {"membaca", "berenang", "bermain game"}
hobi_citra = {"memasak", "berenang", "melukis"}

# Union (|): Gabungan semua hobi unik dari keduanya
hobi_bersama = hobi_budi | hobi_citra

# Intersection (&): Hobi yang sama-sama mereka miliki
hobi_yang_sama = hobi_budi & hobi_citra

# Difference (-): Hobi yang dimiliki Budi tapi tidak dimiliki Citra
hobi_unik_budi = hobi_budi - hobi_citra

hobi_unik_citra = hobi_citra - hobi_budi

print(hobi_yang_sama)

print(hobi_unik_budi)

print(hobi_unik_citra)