def baca_nilai(nama_file):
    try:
        with open(nama_file, "r", encoding="utf-8") as file:
            isi = file.read()
            print(isi)
    except FileNotFoundError:
        print("File tidak ditemukan.")

baca_nilai("nilai.txt")