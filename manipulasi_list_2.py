# Nested list memudahkan ketika ingin menggabungkan list ke dalam list

# contoh penggunaan 
peserta_1 = ["indi", 20,"wanita"]  
peserta_2 = ["indri",23 ,"Laki-laki"]
peserta_3 = ["sakung", 25,"Laki - laki"]

list_peserta = [peserta_1,peserta_2,peserta_3]

for peserta in list_peserta:
    print(f"\nnama\t: {peserta[0]}")
    print(f"usia\t: {peserta[1]}") 
    print(f"gender\t: {peserta[2]}\n")



print("\n===== FOR LOOP =====")

angka = [1,3,2,4,5,1,2,3,4,5]

for angka in angka:
    print(f"angka = {angka}")
    
print("\n===== FOR LOOP DAN RANGE =====")

angka = [1,2,1,2,3,4,5,5]

panjang = len(angka)
for i in range(panjang):
    print(f"angka = {angka[i]}")

print("\n===== WHILE LOOP =====")

angka = [1,2,1,2,3,4,3,4,5,2]
panjang = len(angka)
i = 0

while i < panjang:
    print(f"angka = {angka[i]}")
    i += 1 
    
print("\n===== LIST COMPREHENSION =====")

data = ["sakung",2,3,"indi",2]
[print(f"data = {i}") for i in data]

print("\n===== ENUMERATE =====")

data_list = ["sakung",2,1,2,3,4,"indi"]
for index,data in enumerate(data_list):
    print(f"index = {index},data = {data}")
