'''LAMBDA FUNCTION DAN ANONYMOUSE'''
import os
os.system("cls")


'''fungsi biasa'''
def kuadrat(angka):
    return angka**2

print(f"hasil kuadrat = {kuadrat(3)}")

'''menggunakan lambda'''
# output = lambda argument:expresion
kuadrat = lambda angka : angka**2
print(f"hasil lambda kuadrat = {kuadrat(2)}")

pangkat = lambda num,pow:num**pow
print(f"hasil lambda pangkat = {pangkat(4,2)}")

'''kegunaan lambda'''

# sort list biasa
data_list = ["sakung","indi","ikas"]
data_list.sort()
print(f"sort list = {data_list}")

#sort list pakai panjang
def panjang_nama(nama):
    return len(nama)

data_list.sort(key=panjang_nama)
print(f"sort by panjang = {data_list}")

# sort pakai lambda
data_list = ["sakung","indi","ikas"]
data_list.sort(key=lambda nama:len(nama))
print(f"sort by lambda = {data_list}")

'''filter'''
data_angka = [1,2,3,4,5,6,7,8,9,10,11,12]

def angka(angka):
    return angka < 8

data_baru = list(filter(angka,data_angka))
data_baru = list(filter(lambda x:x<8,data_angka))
print(data_baru)

'''kasus genap'''
angka_genap = list(filter(lambda x:(x%2==0),data_angka))
print(f"angka genap = {angka_genap}")

angka_ganjil = list(filter(lambda x:(x%2!=0),data_angka))
print(f"angka ganjil = {angka_ganjil}")


kelipatan_3 = list(filter(lambda x:(x%3==0),data_angka))
print(f"kelipatan 3 = {kelipatan_3}")


'''anonymous function'''
'''currying <- Haskell curry'''

'''fungsi biasa'''
def pangkat(angka,n):
    hasil = angka**2
    return hasil
data_hasil = pangkat(5,2)
print(f"fungsi biasa = {data_hasil}")

'''fungsi dengan currying'''
def pangkat(n):
    return lambda angka:angka**n

pangkat2 = pangkat(2)
print(f'pangkat 2 = {pangkat2(2)}')
pangkat3 = pangkat(3)
print(f"pangkat 3 = {pangkat3(3)}")
print(f"pangkat bebas = {pangkat(10)(10)}")
