'''Inherintance adalah sebuah pewarisan dari class ke class yang mau diwairskan,
class utama disebut super class dan class yang diwariskan adalah subclass,
sifat inheritance dapat di wariskan dari class utama ke kelas yang mau di wariskan'''

# class Hero:
    
#     def __init__(self,name,health):
#         self.name = name
#         self.health = health
    
    
# # sub class yang mau diwariskan 
# class Hero_kelincahan(Hero): # <-- masukan class utama menggunakan kurun ()
#     pass
    
    
# class Hero_kekuatan(Hero): # <-- contoh kedua
#     pass

# Miya = Hero("Miya",100)
# Lancelot = Hero_kelincahan("Lancelot",100)
# Tigreal = Hero_kekuatan("Tigreal",200)

# print(Miya.__dict__)
# print(Lancelot.__dict__)
# print(Tigreal.__dict__)


'''Contoh kedua'''

class Hero:
    
    def __init__(self,name,health):
        self.name = name
        self.health = health
    
    def showInfo(self):
        print("{} dengan health : {}".format( self.name,self.health))

class Hero_kekuatan(Hero):
    def __init__(self,name): # <-- memanggil super classnya
        super().__init__(name,100) # <-- memanggil superclassnya dan menambahakan info objek
        super().showInfo()
        
        
class Hero_kelincahan(Hero):
    def __init__(self, name): # <-- memanggil super classnya
        super().__init__(name,200) # <-- memanggil superclassnya dan menambahakan info objek
        super().showInfo()

Alu = Hero_kekuatan("Alu")
Ling = Hero_kelincahan("Ling")

'''Super class dan subclass berfungsi untuk ketika ingin membuat sebuah objek dengan yang baru
dengan template class utama untuk di wariskan atau diteruskan tanpa mengubah template utamanya
dengan memasukan superclass ke subclassnya menggunakan (classutama) pada subclassnya '''