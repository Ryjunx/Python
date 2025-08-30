def tambah(*daftar_angka):
    total = 0
    for angka in daftar_angka:
        total += angka
    return total

angka_list = []

while True:
    angka = int(input("masukan angka (0 untuk berhenti): "))

    if angka == 0:
        break

    angka_list.append(angka)

print(tambah(*angka_list))