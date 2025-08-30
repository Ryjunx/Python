try:
    # Blok kode yang berpotensi menimbulkan error
    angka = int(input("Masukkan sebuah angka: "))
    hasil = 10 / angka
    print(f"Hasilnya adalah {hasil}")
except ValueError:
    # Blok ini hanya berjalan jika terjadi error konversi tipe data
    print("Error: Input yang Anda masukkan bukan angka!")
except ZeroDivisionError:
    # Blok ini hanya berjalan jika terjadi error pembagian dengan nol
    print("Error: Angka tidak boleh dibagi dengan nol!")
except Exception as e:
    # Menangkap semua jenis error lain yang mungkin terjadi
    print(f"Terjadi error tak terduga: {e}")
