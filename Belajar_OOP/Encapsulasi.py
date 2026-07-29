'''ENCAPSULAI'''

'''Encapsulai adalah sebuah konsep oop yang membungkus atribut (data) dan method dalam satu unit(class)
sekaligus membatasi akses langsung ke data tersebut dari luar class,tujuannya untuk menjaga supaya data tidak diubah sembarangan'''


class Hero:
    def __init__(self,name,health,power):
        self.__name = name
        self.__health = health
        self.__power = power
    
    # getter
    def getName(self):
        return self.__name
    
    def getHealth(self):
        return self.__health
    
    # setter
    
    def diserang(self,serang):
        self.__health -= serang
        
    def setAttack(self,nilai_baru):
        self.__power = nilai_baru
        
# awal game
Beatrix = Hero("Beatrix",100,30)

# pertengahan game
print(f"ini adalah darah awal : {Beatrix.getHealth()}") # ini adalah getter
Beatrix.diserang(20) 
print(f"ini darah akhir : {Beatrix.getHealth()}")  # ini adalah setter

# Getter → method untuk membaca nilai atribut.
# Setter → method untuk mengubah/mengisi nilai atribut, biasanya disertai validasi.

