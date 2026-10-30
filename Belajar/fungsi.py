# FUNGSI 
import os
os.system("cls")

def tambah(angka_1,angka_2):
    hasil = angka_1 = angka_2
    print(f"{angka_1} + {angka_2} = {hasil}")

tambah(1,2)

print('-'*10, "DEF LIST ",'-'*10)

def halo(nama_peserta):
    '''nama peserta'''
    data_peserta = nama_peserta.copy()
    for peserta in nama_peserta:
        print(f"selamat datang {peserta}")

list_nama = ["sakung","indi","hadi","ikas"]

halo(list_nama)

print('-'*10, "DEF KUADRAT",'-'*10)

def kuadrat(angka):
    '''fungsi kuadrat'''
    output_kuadrat = angka**2
    return output_kuadrat

y = kuadrat(5)
print(y)

print(kuadrat(10))

z = 10 +  kuadrat(10)
print(z)


print('-'*10, "DEF MULTI INPUT",'-'*10)

def operasi(angka_1,angka_2):
    return angka_1 + angka_2

a = operasi(10,10)
print(a)

print('-'*10, "FUNGSI DENGAN RETURN BANYAK",'-'*10)

def operasi_matematika(angka_1,angka_2):
    tambah = angka_1 + angka_2
    kurang = angka_1 - angka_2
    kali = angka_1 * angka_2
    bagi = angka_1 / angka_2
    return tambah,kurang,kali,bagi

k,l,m,n = operasi_matematika(10,10)

print(f"hasil tambah = {k}")
print(f"hasil kurang = {l}")
print(f"hasil kali = {m}")
print(f"hasil bagi = {n}")

print('-'*10, "DEFAULT ARGUMENT",'-'*10)

print("\nContoh 1")
def say_hello(nama = "ganteng"):
    print(f"halo {nama}")
    
say_hello("sakung")
say_hello()

print("\ncontoh 2")

def  sapa(nama,pesan = "halo apakabar"):
    print(f"hai {nama} ,{pesan}")
    
sapa("sakung","apakabar")
sapa("indi")

print("\ncontoh 3")
def hitung_pangkat(angka,pangkat):
    hasil = angka**pangkat
    return hasil

print(hitung_pangkat(10,10))
hasil = hitung_pangkat(pangkat=5,angka=10)
print(hasil)

print("\ncontoh 4")

def fungsi(input1=1,input2=2,input3=3,input4=4):
    hasil = input1 + input2 + input3 + input4
    return hasil

print(fungsi())
print(fungsi(input4=10))


def fungsi(angka_1,angka_2):
    hasil = angka_1 + angka_2
    return hasil

hasil = fungsi(angka_1=10,angka_2=90)
print(hasil)


