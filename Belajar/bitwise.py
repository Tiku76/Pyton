# Operasi bitwise adalah operasi yang bekerja pada setiap bit (0 dan 1) dari bilangan biner
# Operasi ini sering digunakan dalam pemrograman tingkat rendah, pengolahan data, dan optimasi
# TANDA OPERASI BINER >> OR(|),AND(&),NOT(~),XOR(^)
# 00000000
# 2 ** 0 = 1
# 2 ** 1 = 2
# 2 ** 2 = 4
# 2 ** 3 = 8
# 2 ** 4 = 16
# 2 ** 5 = 32
# 2 ** 6 = 64
# 2 ** 7 = 128
# setelah semua hasilnya dipangkatkan setelahnya ditambahkan 
a = 5
print(a,format(a,'08b'))

a = 15
b = 100
c = a | b
print(a,format(a,'08b'))

a = 15
b = 100
c = a & b
print(c,format(c,'08b'))

a = 15
b = 100
c = a ^ b
print(c,format(c,'08b'))

a = 1000
print(a,format(a,'08b'))
