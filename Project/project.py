'''PROJECT DATABASE PERPUSTATAKAAN'''

import os
import CRUD as CRUD


if __name__ == "__main__":
    sistem_operasi = os.name
    match sistem_operasi:
        case "posix" : os.system("clear")
        case "nt" : os.system("cls")

    print("SELAMAT DATANG DI PROGRAM")
    print("DATABASE PERPUSTAKAAN")
    print("==========================")
    
    
    # mengecek data
    CRUD.init_console()
    
    while (True):
        match sistem_operasi:
                case "posix" : os.system("clear")
                case "nt" : os.system("cls")
        
        
        print("SELAMAT DATANG DI PROGRAM")
        print("DATABASE PERPUSTAKAAN")
        print("==========================\n")
        
        
        print("1. read data")
        print("2. create data")
        print("3. update data")
        print("4. delete data")
        

        user_option = input("masukan opsi :")

        match user_option:
            case "1": CRUD.read_console()
            case "2": CRUD.create_console()
            case "3": CRUD.update_console()
            case "4": CRUD.delete_console()
            
        is_done = input("apakah selesai? (y/n)")
        
        if is_done == "y" or is_done == "Y":
            break  
    print("Program berakhir terimakasih")