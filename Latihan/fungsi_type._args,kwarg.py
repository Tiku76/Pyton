'''Beberapa type dari fungsi'''

'''Type fungsi type hints,args dan kwargs'''
import os
import string

os.system("cls")
print(f'-'*10,"Contoh type hints",'-'*10)
def fungsi(argument:int) -> int:
    print(argument)
    
fungsi(2)

def fungsi(argument:string) -> str:
    print(argument)
    
fungsi("sakung")

print(f'-'*10,"Contoh fungsi pada umumnya",'-'*10)

'''contoh fungsi pada umumnya'''
def fungsi(nama,tinggi,berat):
    print(f"{nama} tinggi {tinggi} dan mempunyai berat badan {berat}")
    
fungsi("sakung",180,90)

'''contoh fungsi list'''
def fungsi(data_list):
    data = data_list.copy()
    nama = data[0]
    tinggi = data[1]
    berat = data[2]
    print(f"{nama} tinggi {tinggi} dan mempunyai berat badan {berat}")

fungsi(["sakung",190,80]) # <- terlalu panjang jika terlalu banyak data


print(f'-'*10,"Contoh *args",'-'*10)
'''contoh fungsi *args'''
def tambah(*data):
    output = 0
    for angka in data:
        output += angka
    return output

hasil = tambah(1,2,3,4,5,6,7,8,9)
print(f"hasil = {hasil}")

hasil = tambah(10,100,1000)
print(f"hasil = {hasil}")

print(f'-'*10,"Contoh **kwargs",'-'*10)

def fungsi(**kwargs):
    nama  = kwargs["nama"]
    tinggi = kwargs["tinggi"]
    berat = kwargs["berat"]
    
    print(f"{nama} tinggi {tinggi} dan mempunyai berat badan {berat}")
    
    
fungsi(nama="sakung",tinggi=190,berat=90)

print(f'-'*10,"Contoh study kasus kwargs dan args",'-'*10)


def math(*args,**kwargs):
    
    output = 0 
    if kwargs ["option"] == "tambah":
        for angka in args:
            output += angka
            
    elif kwargs["option"] == "kali":
        output = 1
        for angka in args:
            output *= angka
    else:
        print("yang bener dong")
    return output

hasil = math(1,2,3,4,5,option="tambah")
print(f"hasil jumlah = {hasil}")

hasil = math(1,2,3,4,5,option="kali")
print(f"hasil kali = {hasil}")
