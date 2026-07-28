'''STATICMETHOD DAN CLASS METHOD'''

# class Hero:
#     __jumlah = 0
    
#     def __init__(self,name):
#         self.__name = name
#         Hero.__jumlah += 1
    
#     # method ini berlaku hanya untuk objek
#     def getJumlah(self):
#         return Hero.__jumlah
    
#     # method ini tidak berlaku untuk objek tapi berlaku untuk class
#     def getJumlah1():
#         return Hero.__jumlah 
    
#     # method static (decorator) nempel ke objek dan class
#     @staticmethod
#     def getJumlah2():
#         return Hero.__jumlah
    
#     @classmethod
#     def getJumlah3(cls):
#         return cls.__jumlah
    
    
# Beatrix = Hero("Beatrix")
# print(Hero.getJumlah1())

# Lukas = Hero("Lukas")
# print(Hero.getJumlah2())
# Adi = Hero("Adi")
# print(Hero.getJumlah3())


'''contoh lain getter setter dan deleter '''

class Hero:
    def __init__(self,name,health,armor):
        self.name = name
        self.__health = health
        self.__armor = armor
        # self.indo = "name {} : \nhealth : {}".format(self.__name,self.__health)
    
    @property
    def info(self):
        return "name {} : \nhealth : {}".format(self.name,self.__health)
    
    @property
    def armor(self):
        pass
    
    @armor.getter
    def armor(self):
        return self.__armor
    
    @armor.setter
    def armor (self,input):
        self.__armor = inputf
        
    @armor.deleter
    def armor(self):
        print("armor di delete")
        self.__armor = None
        


Beatrix = Hero("Beatrix",100,50)

print("merubah info")
print(Beatrix.info)
Beatrix.name = "Balmond"
print(Beatrix.info)

print("getter dan setter untuk __armor:")
print(Beatrix.armor)
Beatrix.armor = 90
print(Beatrix.armor)

print("men delete armor")
del Beatrix.armor
print(Beatrix.__dict__)