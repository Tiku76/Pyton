# for looping
angka = range(101)

for i in angka:
    print(f"angka : {i}")
    
# while looping
angka = 1

while angka < 10:
    angka += 1
    print("gelo") # 
    
# looping pass,continue,break

angka = 0

# paas
while angka < 10:
    angka += 1
    print(f"angka : {angka}")
    
    if angka == 5:
        print("nice")
        pass
    
print("akhir pass\n")

# continue
angka = 0
while angka < 15:
    angka += 1
    print(f"angka : {angka}")
    
    if angka == 5:
        print("bagus")
        continue
    
print("akhir continue\n")

# gabungan dari pass continue dan break

angka = 0 
while angka < 20:
    angka += 1
    print(f"angka : {angka}")
    
    if angka == 5:
        print("good")
        break
print("akhir break\n")

angka = 0

user = int(input(f"masukan angka :"))

while True:
    angka += 1
    print(f"angka sekarang :{angka}")
    
    if angka == user:
        print("nice")
        break
    
print("akhir proggram")