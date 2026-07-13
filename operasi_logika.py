# Membandingkan nilai boolean True atau False
#not,or,and,xor
print("==NOT==")
x = False
y = True
z = not y
print('data z = ',z) 

print("==OR==") # (jika salah satu true maka hasilnya true)
x = False
y = True
z = x or y
print(x, 'or',y, '=',z)

print("==and==") # (jika dua buah nlai true maka hasilnya true)
x = False
y = True
z = x and y
print(x, 'and',y, '=',z)

x = True
y = True
z = x and y
print(x, 'and',y, '=',z)

print("==xor==") #(akan true jika salah satu true,kalau dua"nya true maka false)
x = True
y = True
z = x ^ y
print(x, 'xor',y, '=',z)

x = False
y = False
z = x ^ y
print(x, 'xor',y, '=',z)