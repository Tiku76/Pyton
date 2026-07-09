# === LIST ===

# kumpulan data angka 
data_angka = [0,1,2,3,4,5]
print(data_angka)

# kumpulan data string 
data_string = ["halo","hi","apakabar"]
print(data_string)

# kumpulan data boolean
data_boolean = [True,False,True,True]
print(data_boolean)

# kumpulan data campuran
data_campuran = [1,"ayam",2,"nasi",3,"mie",True]
print(data_campuran)

# cara alternatif membuat list
print  ("=" * 5,"ALTERNATIF LIST", "=" *5)
data_range = range(0,10,3)
print(data_range)
data_list = list(data_range)
print(data_list)

# Membuat data list dengan looping,comprehension
print  ("=" * 5,"LIST LOOPING", "=" *5)
list_for = [i**2 for i in range(0,10)]
print(list_for)

# membuat list pake for pake if
print  ("=" * 5,"LIST PAKE FOR IF", "=" *5)
list_for_if = [i for i in range(0,10) if i !=5]
print(list_for_if)

list_for_if = [i for i in range(0,10) if i%2 ==0]
print(list_for_if)

list_for_if = [i for i in range(0,10) if i%2 !=0]
print(list_for_if)
