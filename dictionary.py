# dictionary (sering disingkat dict) adalah struktur data yang menyimpan data dalam bentuk pasangan kunci (key) dan nilai (value).
# Berbeda dengan list yang diakses menggunakan indeks angka, dictionary diakses menggunakan key

# contoh list
print("\n===== LIST =====")

data_list = ['sakung','indi']
print(data_list[0])

# contoh dictionary
print("\n===== DICTIONARY =====")

data_dict = {
    '1':'sakung',
    '2':'indri',
    '3': 'indi',
}   

print(data_dict['2'])

lendict = len(data_dict)
print(lendict)

# Mengecek key exist ada atau tidak
print("\n===== MENGECEK KEYS =====")

key = "0"
checkkey = key in data_dict
print(f"apakah ada {key} di data_dict {checkkey}")

# Mengakses value (read) dengan get
print("\n===== MENGAKSES VALUE =====")


print(data_dict.get("1"))
print(data_dict.get("0","key tidak ditemukan"))

# Mengupdate data
print("\n===== MENGUPDATE DATA =====")


data_dict["1"] = "ganteng"
print(data_dict)
data_dict["4"] = "hadi"
print(data_dict)
data_dict.update({"5": "ikas"})
print(data_dict)

# Menghapus data
print("\n===== MENGHAPUS DATA =====")

del data_dict["5"]
print(data_dict)

# Loping dictionary
print("\n===== LOPING DICTIONARY =====")

kumpulan_data = {
    "1":'sakung',
    '2':"indi",
    "3":"ikas",
    "4":"hadi",
}
# Loping yang mengeluarkan keynya
for teman in kumpulan_data:
    print(teman)
    
# Operator untuk mengambil item / iterables
print("\n===== MENGAMBIL ITEM =====")

keys = kumpulan_data.keys()
print(keys)

print("\n===== MENGAMBIL ITEM YANG SPESIFIK =====")

for key in kumpulan_data.keys():
    print(kumpulan_data.get(key))

print("\n===== VALUES =====")

values = kumpulan_data.values()
print(values)

print("\n===== ITEM =====")

item =kumpulan_data.items()
print(item)

for item in kumpulan_data.items():
    print(item)
    
for key,value in kumpulan_data.items():
    print(f"key = {key}, value = {value}")
