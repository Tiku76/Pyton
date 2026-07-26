from . import Operasi

def delete_console():
    read_console()
    while(True):
            print("silahkan pilih nomor buku yang mau di delete")
            no_buku = int(input("nomor buku :"))
            data_buku = Operasi.read(index=no_buku)
            
            if data_buku:
                data_break = data_buku.split(',')
                pk = data_break[0]
                data_add = data_break[1]
                penulis = data_break[2]
                judul = data_break[3]
                tahun = data_break[4][:-1]
                
                print("\n"+"="*100)
                print("silahkan pilih data yang mau dihapus")
                print(f"1. judul \t: {judul:.40}")
                print(f"2. penulis \t: {penulis:.40}")
                print(f"3. tahun\t :{tahun:4}")
                
                is_done = input("apakah yakin dihapus (y/n):")
                if is_done == "y" or is_done == "Y":
                    Operasi.delete(no_buku)
                    break
            else:
                print("nomor tidak valid")
    print("data berhasil di hapus")


def update_console():
    read_console()
    while(True):
        print("silahkan pilih nomor buku yang mau di update")
        no_buku = int(input("nomor buku :"))
        data_buku = Operasi.read(index=no_buku)
        data_break = data_buku.split(',')
        pk = data_break[0]
        data_add = data_break[1]
        penulis = data_break[2]
        judul = data_break[3]
        tahun = data_break[4][:-1]
        
        if data_buku:
            break
        else:
            print("nomor tidak valid")
    
    while(True):
        # data yang mau di update
            print("\n"+"="*100)
            print("silahkan pilih data yang mau diupdate")
            print(f"1. judul \t: {judul:.40}")
            print(f"2. penulis \t: {penulis:.40}")
            print(f"3. tahun\t :{tahun:4}")
            
            # memilih yang mau diupdate
            user_option = input("pilih 1,2,3 :")
            print("\n"+"="*100)
            match user_option:
                case "1" : judul = input("judul\t:")
                case "2" :penulis = input("penulis\t:")
                case "3" :
                    while(True):
                            try:
                                tahun = int(input("tahun \t:"))
                                if len(str(tahun)) == 4:
                                    break
                                else:
                                    print("tahun harus berupa angka,silahkan masukan lagi")
                    
                            except:
                                print("tahun harus berupa angka,silahkan masukan lagi")
                case  _:print("index tidak cocok")
                
                
            print("data baru anda")
            print(f"1. judul \t: {judul:.40}")
            print(f"2. penulis \t: {penulis:.40}")
            print(f"3. tahun\t :{tahun:4}")
                
            is_done = input("apakah data sudah sesuai (y/n):")
            if is_done == "y" or is_done == "Y":
                break  
    Operasi.update(no_buku,pk,data_add,tahun,judul,penulis)


def create_console():
    print("\n\n"+"="*100)
    print("Silahkan tambah data buku\n")
    penulis = input("penulis \t:")
    judul = input("judul \t:")
    while(True):
        try:
            tahun = int(input("tahun \t:"))
            if len(str(tahun)) == 4:
                break
            else:
                print("tahun harus berupa angka,silahkan masukan lagi")

        except:
            print("tahun harus berupa angka,silahkan masukan lagi")
            
    Operasi.create(tahun,judul,penulis)
    print("\nBerikut data baru anda")
    read_console()
    

def read_console():
    data_file = Operasi.read()
    index = "no"
    judul = "judul"
    penulis = "penulis"
    tahun = "tahun"
    
    # header
    print("\n"+"="*100)
    print(f"{index:4} | {judul:40} | {penulis:40} | {tahun:4}")
    print("-"*100)
    
    # data
    for index,data in enumerate(data_file):
        data_break = data.split(",")
        pk = data_break[0]
        date_add = data_break[1]
        penulis = data_break[2]
        judul = data_break[3]
        tahun = data_break[4]
        print(f"{index+1:4} | {judul:.40} | {penulis:.40} | {tahun:4}",end="")
        
    
    
    print("="*100+"\n")