from time import sleep
import array_1d
import array_2d
import array_3d
import libs

def menu():
    opsi_user = int(input("Silakan pilih menu program mapping storage array:\n1. Array 1d\n2. Array 2d\n3. Array 3d\n4. Exit Program\n\nSilakan Pilih: "))
    print()
    if opsi_user == 1:
        sleep(0.3)
        sleep(0.3)
        array_1d.array1D()
    elif opsi_user == 2:
        sleep(0.3)
        array_2d.array2D()
    elif opsi_user == 3:
        sleep(0.3)
        array_3d.array3D()
    elif opsi_user == 4:
        sleep(0.3)
        libs.exit_program()
    else:
        print("Pilih opsi yang ada di menu!!\n")
        sleep(0.3)
        menu()

def main():        
    libs.welcome_messege()
    menu()
 
    
if __name__ == '__main__':
    main()
