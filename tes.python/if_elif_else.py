user = int(input("Masukkan nilai Anda: "))

if user == 100:
    print(user, "nilai Anda di grade A")
elif 80 <= user <= 99:
    print(user, "nilai Anda di grade B")
elif 71 <= user <= 79:
    print(user, "nilai Anda di grade C")
else:
    print(user, "nilai Anda di grade D")

print("Terima kasih")