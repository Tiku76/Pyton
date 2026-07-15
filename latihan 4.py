# PROGGRAM SEDERHANA DARI DICTIONARY
# LATIHAN
import datetime
import random
import string
import os

os.system("cls")

mahasiswa_template = {
    'nama': 'nama',
    'nim' : '00000000',
    'sks_lulus': 0,
    'lahir':datetime.datetime(1111,1,11)
}

data_mahasiswa = {}

while True:
    print(f"{'SELAMAT DATANG DI DATA MAHASISWA'}")
    print('-'*20)
    
    mahasiswa = dict.fromkeys(mahasiswa_template.keys())
    mahasiswa['nama'] = input("Masukan nama :")
    mahasiswa['nim'] = input("Masukan nim :")
    mahasiswa['sks_lulus'] = int(input('sks lulus :'))
    tahun_lahir = int(input("Tahun lahir : "))
    bulan_lahir =int(input("Bulan lahir :"))
    tanggal_lahir = int(input("Tanggal lahir :"))
    mahasiswa ['lahir'] = datetime.datetime(1111,1,11)
    
    key = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))
    data_mahasiswa.update({key:mahasiswa})
    
    print(f"{'key':<6} {'nama':<17} {'nim':<10} {'sks':<3} {'beasiswa':<9} {'lahir':<10}")
    print('-'*55)
    
    for mahasiswa in data_mahasiswa:
        key = mahasiswa
        nama = data_mahasiswa[key]['nama']
        nim = data_mahasiswa[key]['nim']
        sks = data_mahasiswa[key] ['sks_lulus']
        lahir = data_mahasiswa[key]['lahir'].strftime("%x")
        print(f"{key:^6} {nama:<17} {nim:<10} {sks:^3} {lahir:^10}")

    print("\n")
    selesai = input("Mau tambah lagi? (y/n)")
    if selesai == 'n':
        break
    
print("SELESAI")
    