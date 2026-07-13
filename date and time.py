# # import datetime as dt
# # print ("masukan Tanggal,\nbulan,\ntahun lahir anda :")
# # tanggal = int(input("Tanggal lahir anda :"))
# # bulan = int(input("Bulan lahir anda :"))
# # tahun = int(input("Tahun lahir anda :"))
# # tanggal_lahir = dt.date(tahun,bulan,tanggal)
# # print(f"tanggal lahir anda : {tanggal_lahir}" )

# # hari_ini = dt.date.today()
# # print(f"hari ini tanggal : {hari_ini}")
# # umur_hari = hari_ini - tanggal_lahir
# # umur_tahun = umur_hari.days // 365
# # umur_bulan_sisa = (umur_hari.days % 365) // 30
# # print(f"harinya adalah : {tanggal_lahir:%A}")
# # print(f"umur anda adalah : {umur_tahun} tahun, {umur_bulan_sisa} bulan")

# from datetime import date

# tgl = int(input("Tanggal lahir: "))
# bln = int(input("Bulan lahir: "))
# thn = int(input("Tahun lahir: "))

# lahir = date(thn, bln, tgl)
# hari_ini = date.today()

# selisih = hari_ini - lahir
# umur_tahun = selisih.days // 365
# umur_bulan = (selisih.days % 365) // 30

# print("\nTanggal lahir :", lahir)
# print("Hari ini      :", hari_ini)
# print("Hari lahir    :", lahir.strftime("%A"))
# print(f"Umur          : {umur_tahun} tahun {umur_bulan} bulan")

for i in range(5):
    print(i)