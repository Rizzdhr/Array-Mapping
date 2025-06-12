import main
import libs
from time import sleep
import numpy as np

def array3D():
    # Membuat class bernama Array3D untuk merepresentasikan array 3 dimensi
    class Array3D:
        # Menyiapkan dan menyimpan data array, nama, dimensi, dan ukuran byte elemen.(inisialisasi objek)
        def __init__(self, array, name): 
            self.array = array  # Menyimpan array 3 dimensi
            self.name = name    # Menyimpan nama array (misal: "A")
            
            # Menyimpan jumlah dimensi array
            self.jum_lapisan = len(self.array)               # Jumlah lapisan (depth)
            self.jum_baris = len(self.array[0])              # Jumlah baris per lapisan
            self.jum_kolom = len(self.array[0][0])           # Jumlah kolom per baris
            
            # Menentukan ukuran byte tiap elemen berdasarkan tipe data
            if (isinstance(self.array[0][0][0], int)):  
                self.byte = 2   # Jika tipe datanya Integer: dianggap 2 byte
            elif (isinstance(self.array[0][0][0], float)):
                self.byte = 4   # Jika tipe datanya Float: dianggap 4 byte
            elif (isinstance(self.array[0][0][0], str)):
                self.byte = 1   # Jika tipe datanya String/Char: dianggap 1 byte (per karakter)
        
        # Membuat tampilan array saat objek dicetak agar mudah dibaca, bukan alamat memori objek.
        def __str__(self):
            # Mengembalikan representasi string dari array menggunakan numpy agar lebih rapi
            return str(np.array(self.array))
        
        # menghitung jumlah total elemen dalam array
        def jumlah_elemen(self):
            print(f"\nJumlah elemen array {self.name}")
            hasil_jumlah = self.jum_lapisan * self.jum_baris * self.jum_kolom
            # Menampilkan hasil perhitungan
            print("=", hasil_jumlah)
        
        # Menghitung alamat penyimpanan berdasarkan indeks array dan memori awal  
        def mapping(self, memori_awal, lapisan, baris, kolom):
            hasil = memori_awal + ((lapisan * (self.jum_baris * self.jum_kolom)) + 
                                    (baris * (self.jum_kolom)) + 
                                    kolom) * self.byte
            return hasil
        
        # meminta input indeks dari user dan menampilkan elemen & alamatnya
        def akses_elemen(self):
            print("\nMapping array dimensi 3 ke storage")
                
            # Alamat memori awal (dalam heksadesimal)
            m = 0x11
            
            # Meminta input dari user untuk menentukan indeks
            l = int(input("Lapisan: "))
            b = int(input("Baris: "))
            k = int(input("Kolom: "))
            
            # Memastikan indeks yang dimasukkan valid (tidak kurang dan tidak lebih dari jumlah elemen)
            if (0 <= l < self.jum_lapisan and 0 <= b < self.jum_baris and 0 <= k < self.jum_kolom):
                # Menampilkan nilai array pada indeks yang dimasukkan
                print(f"{self.name}[{l}][{b}][{k}] = {self.array[l][b][k]}")
                
                # Menghitung alamat memori berdasarkan indeks
                alamat = self.mapping(m, l, b, k)
                
                # Menampilkan alamat memori dalam format heksadesimal
                print("alamat =", hex(alamat))
            else:
                # Jika indeks tidak valid
                print("Data Tidak Ada!")
            

    # Data array 3 dimensi yang digunakan (2 lapisan, 4 baris, 3 kolom)
    array = [[[1,2,3],
            [4,5,6],
            [7,8,9],
            [10,11,12]],

            [[13,14,15],
            [16,17,18],
            [19,20,21],
            [22,23,24]]]

    # Membuat objek dari class Array3D dengan nama "A"
    array3d = Array3D(array, "A")

    # Menampilkan isi array
    print(array3d)

    # Menampilkan jumlah elemen dari array
    array3d.jumlah_elemen()

    # Meminta user mengakses elemen tertentu dan menghitung alamatnya
    array3d.akses_elemen()
        
    sleep(0.5)

    while True:
        opsi = int(input("\nIngin Melanjutkan?...\n1. Lanjutkan\n2. Menu\n\nPilih: "))
        if opsi == 1:
            array3D()
        elif opsi == 2:
            print("Kembali ke menu...")
            sleep(0.5)
            main.menu()
        else:
            print("Pilih sesuai opsi!")