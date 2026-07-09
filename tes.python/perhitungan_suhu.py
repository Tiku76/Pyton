# Menghitung suhu dari satu jenis ke jenis lainnya
print("=====Fahrenheit ke kelvin=====")
fahrenheit = float(input("Masukan Suhu Fahrenheit : "))
celcius    = (5/9) * (fahrenheit - 32)
kelvin     = (celcius + 273)
print("Suhu dalam Kelvin : ", kelvin)

print("=====kelvin ke fahrenheit======")
kelvin     = float(input("Masukan Suhu Dalam kelvin : "))
celcius    = kelvin - 273
fahrenheit = ((9/5) * celcius) + 32
print("suhu dalam fahrenheit : ", fahrenheit)