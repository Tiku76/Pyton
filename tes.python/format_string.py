user_input = input(str("masukan nama anda:"))
alamat_user = input(str("alamat anda:"))
usia = input("usia anda:")

format_nama = f"hello  '{user_input}' selamat datang di perusahaan kami"
format_alamat = f"alamat anda di:{alamat_user}"
format_usia = f"usia anda: {usia}"

print(format_nama,'\n' + format_alamat,'\n' + format_usia ) 
