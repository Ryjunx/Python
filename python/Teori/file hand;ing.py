NAMA_FILE = "catatan.txt"

def tampilkan_catatan():
    """Fungsi untuk membaca dan menampilkan semua catatan."""
    print("\n--- Isi Buku Catatan ---")
    try:
        with open(NAMA_FILE, 'r') as file:
            catatan = file.read()
            if not catatan:
                print("(Catatan masih kosong)")
            else:
                print(catatan)
    except FileNotFoundError:
        print("(Buku catatan belum ada, silakan buat catatan pertama Anda)")
    print("------------------------")

def tambah_catatan():
    """Fungsi untuk menambahkan catatan baru ke file."""
    catatan_baru = input("Tulis catatan baru Anda: ")
    # Menggunakan mode 'a' (append) untuk menambahkan di akhir
    with open(NAMA_FILE, 'a') as file:
        file.write(catatan_baru + "\n") # \n untuk baris baru
    print("Catatan berhasil disimpan!")

# --- Program Utama ---
while True:
    print("\nMenu Buku Catatan:")
    print("1. Lihat Semua Catatan")
    print("2. Tambah Catatan Baru")
    print("3. Keluar")
    pilihan = input("Pilih menu (1/2/3): ")

    if pilihan == '1':
        tampilkan_catatan()
    elif pilihan == '2':
        tambah_catatan()
    elif pilihan == '3':
        print("Sampai jumpa!")
        break
    else:
        print("Pilihan tidak valid.")