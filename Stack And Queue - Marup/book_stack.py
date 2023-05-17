
stack = []

def tambahBuku(stack, bukuBaru, pengarangBaru):
    stack.append(bukuBaru)
    stack.append(pengarangBaru)
    print(f"{bukuBaru} karya {pengarangBaru} berhasil ditambahkan ke dalam stack.")

def hapus_bukuTerakhir(stack):
    if len(stack) == 0:
        print("Stack kosong, tidak ada buku yang dapat dihapus")
    else:
        bukuTerakhir = stack.pop()
        bukuTerakhir = stack.pop()
        print(f"{bukuTerakhir} berhasil dihapus dari stack.")

def tampilkan_bukuTeratas(stack):
    if len(stack) == 0:
        print("Stack kosong, tidak ada buku yang dapat ditampilkan.")
    else:
        bukuTeratas = stack[-2]
        pengarangTeratas = stack[-1]
        print(f"Barang teratas di dalam stack adalah {bukuTeratas} karya {pengarangTeratas}.")

while True:
    print("\nGudang saat ini : ",stack)
    print("Menu : ")
    print("1. Tambah Buku dan pengarang")
    print("2. Hapus Buku Terakhir")
    print("3. Tampilkan Buku Teratas")
    print("4. Keluar")

    pilihan = input("Masukkan pilihan Anda (1/2/3/4) : ")
    
    if pilihan =="1":
        bukuBaru = input("Masukkan buku baru  yang akan ditambahkan : ")
        pengarangBaru = input("Masukan pengarang baru yang akan ditambahkan : ")
        tambahBuku(stack, bukuBaru, pengarangBaru)
    elif pilihan =="2":
        hapus_bukuTerakhir(stack)
    elif pilihan =="3":
        tampilkan_bukuTeratas(stack)
    elif pilihan =="4":
        print("Terima kasih telah menggunakan program ini.")
        break
    else:
        print("Pilihan tidak Valid. Silahkan masukkan pilihan yang benar.")

