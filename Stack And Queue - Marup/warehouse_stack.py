stack = []

def tambahBarang(stack, barangBaru):
    stack.append(barangBaru)
    print(f"{barangBaru} berhasil menambahkan ke dalam stack.")
 
def hapusBarangTerakhir(stack):
    if len(stack) == 0 :
        print("Stack kosong, tidak berhasil ditambahkan ke dalam stack.")
    else:
        barangTerakhir = stack.pop()
        print(f"{barangTerakhir} berhasil dihapus dari stack.")

def tampilkanBarangTeratas(stack):
    if len(stack) == 0:
        print("Stack kosong, tidal ada barang yang dapat ditampilkan.")
    else:
        barangTeratas = stack[-1]
        print(f"Barang teratas di dalam stack adalah {barangTeratas}")

while True:
    print("\nGudang saat ini : ",stack)
    print("Menu :")
    print("1. Tambah barang")
    print("2. Hapus barang terakhir")
    print("3. Tampilkan barang teratas")
    print("4. Keluar")
    
    pilihan = input("Masukan pilihan Anda(1/2/3/4) : ")
    if pilihan == "1":
        barangBaru = input("Masukan naman barang yang akan ditambahkan : ")
        tambahBarang(stack, barangBaru)
    elif pilihan == "2":
        hapusBarangTerakhir(stack)
    elif pilihan == "3":
        tampilkanBarangTeratas(stack)
    elif pilihan == "4":
        print("Terima kasih telah menggunakan program ini")
        break
    else:
        print("Pilihan tidak valid. Silahkan masukan pilihan yang benar!.")