# Memanipulasi list seperti yang kita mau

data = ["anang", "asep", "hadi"]


# ============================
# Mengambil data dari list
# ============================

print("\n===== MENGAMBIL DATA DARI LIST =====")

data_0 = data[0]
print(f"Data pertama = {data_0}")

data_terakhir = data[2]
print(f"Data terakhir = {data_terakhir}")


# ============================
# Mengambil panjang list
# ============================

print("\n===== PANJANG LIST =====")

panjang_data = len(data)
print(f"Panjang data = {panjang_data}")


# ============================
# Menambahkan data
# ============================

print("\n===== MENAMBAHKAN DATA =====")

data_baru = ["indi", "indri", "yamin"]
data.extend(data_baru)

print(f"Data setelah ditambahkan = {data}")


# ============================
# Menghapus data berdasarkan nilai
# ============================

print("\n===== REMOVE DATA =====")

data.remove("hadi")
print(f"Data setelah remove = {data}")


# ============================
# Menghapus data paling belakang
# ============================

print("\n===== POP DATA =====")

data.pop()
print(f"Data setelah pop = {data}")


# ============================
# Mengubah data
# ============================

print("\n===== MENGUBAH DATA =====")

data[2] = "sakung"
print(f"Data setelah diubah = {data}")

data.insert(0, "asep")
print(f"Data setelah insert = {data}")


# ============================
# Count pada list
# ============================

print("\n===== COUNT DATA =====")

data_angka = [1, 1, 1, 2, 3, 3, 4, 4, 5, 5, 6, 7, 8, 9]

data_4 = data_angka.count(4)
print(f"Jumlah angka 4 = {data_4}")

# ============================
# Posisi data
# ============================

print("\n===== POSISI DATA =====")

data = ["indi", "indri", "sakung"]
index_indi = data.index("indi")
print(f"index indi berada di = {index_indi}")

# ============================
# Mengurutkan list
# ============================

print("\n===== MENGURUTKAN LIST =====")

data_angka.sort()
data.sort()

print(data_angka)
print(data)

# ============================
# Mereverse list
# ============================

print("\n===== MEREVERSE LIST =====")

data.reverse()
data_angka.reverse()
print(data)
print(data_angka)

# ============================
# Menduplikat list
# ============================

print("\n===== MENDUPLIKAT LIST =====")

# ketika ingin menduplikat sebuah list dengan addres yang berbeda
# maka dilakukan copy ke data yang ingin di duplikat
# misalnya kita mempunyai sebuah data yaitu a
# ketika kita ingin menduplikatnya perhatikan pada sebuah addrenya

a = ["indi","indri","sakung"]
b = a
print(f"data a = {a}")
print(f"data b = {b}")

a[2] = "yamin" #addres yang sama akan ikut dengan variabel pertama
print(f"data a = {a}")
print(f"data b = {b}")

#ketika ingin menduplikatnya harus menggunakan .copy()
c = a.copy()
c[0] = "hadi"
print(f"data a = {a}")
print(f"data b = {b}")
print(f"data c = {c}")

print(f"addres a = {hex(id(a))}")
print(f"addres b = {hex(id(b))}")
print(f"addres c = {hex(id(c))}")
