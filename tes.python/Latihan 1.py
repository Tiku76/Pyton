# #Latihan komparasi dan logika

# #soal nomor 1
# userInput = float(input("masukan angka lebih dari 0 dan kurang dari 5 :" ))

# jikalebihdari = userInput > 0
# jikakuranghdari = userInput < 5
# jawabanBenar = jikalebihdari and jikakuranghdari

# print("angka yang and masukan =", jawabanBenar)

# userInput = float(input("masukan angka lebih dari 8 dan kurang dari 11 :"))

# jikalebihdari = userInput > 8
# jikakuranghdari = userInput < 11
# jawabanbenar = jikalebihdari and jikakuranghdari

# print("angka yang anda masukan :", jawabanbenar)

# #soal nomor 2
# userInput = float(input("masukan angka kurang dari 0 :"))
# jikakurangdari = userInput < 0
# print("angka yang anda masukan: ",jikakurangdari)

# userInput = float(input("masukan angka lebih dari 5 dan kurang dari 8 :"))

# jikalebihdari = userInput > 5
# jikakurangdari = userInput < 8
# jawabanbenar = jikalebihdari and jikakurangdari 

# print("angka yang anda masukan : ",jawabanbenar)

# userInput = float(input("masukan angka lebih dari 11: "))

# jikalebihdari = userInput > 11
# print("angka yang anda masukan : ",jikalebihdari)

# Latihan Komparasi dan Logika

# =======Bentuk Yang lebih sederhana=======
# Soal Nomor 1
print("SOAL NOMOR 1")
userInput = float(input("Masukkan angka lebih dari 0 dan kurang dari 5: "))
print("Angka yang Anda masukkan:", 0 < userInput < 5)

userInput = float(input("Masukkan angka lebih dari 8 dan kurang dari 11: "))
print("Angka yang Anda masukkan:", 8 < userInput < 11)


# Soal Nomor 2
print("SOAL NOMOR 2")
userInput = float(input("Masukkan angka kurang dari 0: "))
print("Angka yang Anda masukkan:", userInput < 0)

userInput = float(input("Masukkan angka lebih dari 5 dan kurang dari 8: "))
print("Angka yang Anda masukkan:", 5 < userInput < 8)

userInput = float(input("Masukkan angka lebih dari 11: "))
print("Angka yang Anda masukkan:", userInput > 11)