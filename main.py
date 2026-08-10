# import io

# file = open("tes.txt", "r")
# print(file.read())

# class Hero:
#     __private = "private"
    
# print(Hero)

# data_int = 10
# data_str = float(data_int)
# print (data_str)


# #testing
# print("=====")
# data_float = 11.5
# data_str = int(data_float)
# print (data_str)

# print("====")
# data_bool = 0
# print(bool,data_bool)

# print("ambil\n" * 100)

# data = 1,2,3,4
# print(data)

# print("saya")

# data = (data)
# print(data)

# data = data
# print (data)


# def input_data(*data):
#     output = 0
#     for angka in data:
#         output += angka
#     return output

# angka = list(map(int, input("Masukkan beberapa angka (pisahkan dengan spasi): ").split()))

# hasil = input_data(*angka)
# print("Hasil:", hasil)

# class B(Exception):
#     pass

# class C(B):
#     pass

# class D(C):
#     pass

# for cls in [B, C, D]:
#     try:
#         raise cls()
#     except D:
#         print("D")
#     except C:
#         print("C")
#     except B:
#         print("B")



# umur = input("masukan umur anda : ")

# if umur == type(int):
#     print("mantap")
# elif umur == type(str):
#     print("umur harus angka")
# # else:
# #     print("masukan yang bener dong")
    
# print(umur)
# # print(f"umur anda adalah {umur}")

def profil(nama, umur, kota, pekerjaan):
    print(f"PROFIL {nama}")
    print(f"Umur : {umur} tahun")
    print(f"Kota : {kota}")
    print(f"Pekerjaan : {pekerjaan}")

input_nama = input("masukan nama :")
input_umur = input("masukan umur :")
input_kota = input("masukan kota anda :")
input_pekerjaan = input("masukan pekerjaan anda :")

# panggil fungsi dengan memasukkan variabel input sebagai argumen
profil(input_nama, input_umur, input_kota, input_pekerjaan)