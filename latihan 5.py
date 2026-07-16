# LATIHAN FUNGSI SEDERHANA
''' LATIHAN FUNGSI'''
'''MENGHITUNG LUAS DARI USER'''

import os


def header():
    '''HEADER'''
    os.system("cls")
    print(f"{'PROGRAM MENGHITUNG LUAS DAN KELILING PERSEGI PANJANG':^40}")
    print('-'*55)
    

def input_user():
    '''MENGAMBIL INPUT USER'''
    lebar = int(input("masukan nilai lebar :"))
    panjang = int(input("masukan nilai panjang :"))
    return lebar,panjang
    

def hitung_luas(lebar,panjang):
    '''hitung luas'''
    return lebar*panjang

def hitung_keliling(lebar,panjang):
    '''hitung keliling'''
    return 2*(lebar+panjang)


def display(message,value):
    '''fungsi dispaly'''
    print(f"hasil perhitungan {message} = {value}")
    
    
while True:
    header()
    lebar,panjang = input_user()
    luas = hitung_luas(lebar,panjang)
    keliling = hitung_keliling(lebar,panjang)
    
    display("luas" ,luas)
    display("keliling",keliling)
    
    lanjut = input("apakah lanjut? (y/n):")
    if lanjut == "n":
        break

print("program selesai,terimakasih")


