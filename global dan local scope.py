'''GLOBAL DAN LOCAL SCOPE'''
import os
os.system("cls")

'''GLOBAL'''

nama_global = "sakung"

def fungsi_1():
    print(f"fungsi menampilkan {nama_global}")
fungsi_1()

'''akses variable global dalam scope'''
for i in range(0,5):
    print(f"loop {i} - {nama_global}")

'''percabangan'''
if True:
    print(f"if menampilkan {nama_global}")

'''variable local scope'''

def fungsi_2():
    nama_local = "indi" # <- variable local scope 
fungsi_2()
# print(nama_local) <- tidak bisa digunakan karena variablenya local scope

'''contoh 1 : penggunaan'''
def say_hi():
    print(f"hello {nama}")
    
nama = "indi"
say_hi()

'''merubah variable global'''
'''contoh 2 : penggunaan'''
angka = 0
name = "sakung"

def ubah(nilai,nama):
    global angka
    global name
    angka = nilai
    name = nama
print(f"sebelum {angka,name}")
ubah(10,"indi")
print(f"sesudah {angka,name}")

'''contoh 3 : penggunaan'''
angka = 0 
for i in range(0,10):
    angka += i
    angka_dummy = 0
    
print(f"angka = {angka}")
print(f"angka dummy = {angka_dummy}")

if True:
    angka = 10
    angka_dummy = 10

print(f"angka = {angka}")
print(f"angka_dummy = {angka_dummy}")


# catatan : mengubah variable local dan global scoop bisa dilakukan dari luar jika loop (for,if)
# berbeda dengan fungsi yang mana harus memanggil global jika ingin merubah isi dari dalam
