# Multi keys dan nested dictionary
# Contoh sebuah database

import datetime

mahasiswa1 = {
    'nama' : 'sakung',
    'nim' : '20200201',
    'sks_lulus': 135,
    'beasiswa': True,
    'lahir':datetime.datetime(2000,2,10)
}


mahasiswa2 = {
    'nama' : 'indi',
    'nim' : '20200202',
    'sks_lulus': 130,
    'beasiswa': False,
    'lahir':datetime.datetime(2002,1,10)
}


mahasiswa3 = {
    'nama' : 'ikas',
    'nim' : '20200203',
    'sks_lulus': 140,
    'beasiswa': True,
    'lahir':datetime.datetime(2001,8,10)
    
}

data_mahasiswa = {
    'MAH001': mahasiswa1,
    'MAH002':mahasiswa2,
    'MAH003':mahasiswa3
    
}


print(f"{'key':<6} {'nama':<17} {'nim':<10} {'sks':<3} {'beasiswa':<9} {'lahir':<10}")
print('-'*55)

for mahasiswa in data_mahasiswa:
    key = mahasiswa
    nama = data_mahasiswa[key]['nama']
    nim = data_mahasiswa[key]['nim']
    sks = data_mahasiswa[key] ['sks_lulus']
    beasiswa = data_mahasiswa[key]['beasiswa']
    lahir = data_mahasiswa[key]['lahir'].strftime("%x")
    print(f"{key:^6} {nama:<17} {nim:<10} {sks:^3} {beasiswa:^9} {lahir:^10}")
    
