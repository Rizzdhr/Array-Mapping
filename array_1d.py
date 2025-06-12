import main
import libs
from time import sleep

def array1D():
    a = [0,1,2,3,4,5]

    print(a)
    jumlah_elemen = len(a)
    print(f"Jumlah elemen array = {jumlah_elemen}")

    print("\nMapping array dimensi 1")

    i = int(input("masukan nilai i : "))
    

    memory_awal = 0x15

    if isinstance(a[0], int):
        byte = 2

    mapping = memory_awal + (i - 1) * byte

    if i <= 0 or i <= jumlah_elemen:
        print(f"[{i}]")
        print(f"Alamat = {hex(mapping)}")
    else:
        print("Data tidak ditemukan!")
        sleep(0.5)

    while True:
        opsi = int(input("\nIngin Melanjutkan?...\n1. Lanjutkan\n2. Menu\n\nPilih: "))
        if opsi == 1:
            array1D()
        elif opsi == 2:
            print("Kembali ke menu...")
            sleep(0.5)
            main.menu()
        else:
            print("Pilih sesuai opsi!")
            
