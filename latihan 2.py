# Kalkulator sederhana

print (10*"=")
print("Selamat datang")
print (10*"=")

angka_1 = float(input("masukan angka : "))
operator = input("(+ - * /) :")
angka_2 = float(input("masukan angka :"))

if operator == "+":
    hasil = angka_1 + angka_2
    print(f"hasilnya :{hasil:,}")
elif operator == "-":
    hasil = angka_1 - angka_2
    print(f"hasilnya :{hasil:,}")
elif operator == "*":
    hasil = angka_1 * angka_2
    print(f"hasilnya :{hasil:,}")
elif operator == "/":
    hasil = angka_1 / angka_2
    print(f"hasilnya :{hasil:,}")
else:
    print("masukan yang bener dong")
print(10*"=")
