# .upper -> Mengubah menjadi huruf besar
# .lower -> Mengubah menjadi huruf kecil
# .isupper -> mengecek apakah hurufnya besar
# .islower -> mengecek apakah hurufnya kecil
# .isalpha -> mengecek apakah semuanya huruf (tanpa spasi)
# .isdecimal -> mengecek apakah semuanya angka aja

salam = ("halo apakabar")
isupper = salam.isupper()
print(str(isupper))

salam = ("23444342432234")
isupper = salam.isdecimal()
print(str(isupper))

# salam = ("halo apa kabar :")

# salam = salam.isupper()
# print(salam)

# is_alpha = salam.isupper()
# print(salam + str(is_alpha))

# is_alpha = salam.isalnum()
# print(salam + str(is_alpha))
