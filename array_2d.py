import main
import libs
from time import sleep

def array2D():
    # Membuat array 3x3
    array_2d = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]

    # Menampilkan tanpa koma
    for array in array_2d:
        print("[{}]".format(" ".join(str(array_2d) for array_2d in array)))

        
    # hitung jumlah baris & kolom
    jumlah_baris = len(array_2d)
    jumlah_kolom = len(array_2d[0])

    # menentukan ukuran byte berdasarkan tipe data
    if isinstance(array_2d[0][0], str):
        bytes = 1
    elif isinstance(array_2d[0][0], float):
        bytes = 4
    elif isinstance(array_2d[0][0], int): 
        bytes = 2
        
    # metode rumus mapping CMO & RMO
    def cmo(kolom, baris, alamat_awal, jumlah_baris, bytes):
        mapping_cmo = alamat_awal + ((kolom * jumlah_baris) + baris) * bytes
        return mapping_cmo

    def rmo(baris, kolom, alamat_awal, jumlah_kolom, bytes):
        mapping_rmo = alamat_awal + ((baris * jumlah_kolom) + kolom) * bytes
        return mapping_rmo

    # asumsi alamat awal array (Misal alamat dasar 0x11)
    alamat_awal = 0x11

    print(f"\nAlamat Awal = {hex(alamat_awal)}")

    # buat variabel input agar user bisa memilih array yang akan dicari
    barisinput = int(input(f"Masukan Baris (0-{jumlah_baris-1}): "))
    kolominput = int(input(f"Masukan Kolom (0-{jumlah_kolom-1}): "))

    # buat variabel untuk memanggil metode
    mapping_cmo = cmo(kolominput, barisinput, alamat_awal, jumlah_baris, bytes)
    mapping_rmo = rmo(barisinput, kolominput, alamat_awal, jumlah_kolom, bytes)

    # membuat variabel untuk hasil decimal
    alamat_cmo = mapping_cmo
    alamat_rmo = mapping_rmo

    # output
    # (membuat validasi. Jika baris atau kolom melebihi panjang array, maka data tidak ditemukan)
    if 0 <= barisinput < jumlah_baris and 0 <= kolominput < jumlah_kolom:
        print(f"\nA[{barisinput}][{kolominput}]")
        print(f"CMO = {hex(mapping_cmo)} (Hexadecimal)")
        print(f"    = {alamat_cmo} (Decimal)")
        print(f"\nRMO = {hex(mapping_rmo)} (Hexadecimal)")
        print(f"    = {alamat_rmo} (Decimal)")
    else:
        print("Data tidak ditemukan!")
        sleep(0.5)

    while True:
        opsi = int(input("\nIngin Melanjutkan?...\n1. Lanjutkan\n2. Menu\n\nPilih: "))
        if opsi == 1:
            array2D()
        elif opsi == 2:
            print("Kembali ke menu...")
            sleep(0.5)
            main.menu()
        else:
            print("Pilih sesuai opsi!")
