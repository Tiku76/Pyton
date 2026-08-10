class Hewan:
    def __init__(self,nama):
        self.nama = nama
    
    def suara(self):
        print(f"{self.nama} Suara hewan")
    
class Kucing(Hewan):
    def suara(self):
        print(f"{self.nama} meeooww")
    
class Sapi(Hewan):
    def suara(self):
        print(f"{self.nama} moooo")
        
class Anjing(Hewan):
    def suara(self):
        print(f"{self.nama} guk guk")

    
hewan_list = [
    Anjing("anjing"),
    Sapi("sapi"),
    Kucing("kucing")
]

for hewan in hewan_list:
    hewan.suara()
    
'''DUCK TYPING'''

class Mobil:
    def start(self):
        print("mobil berjalan")
        
class Kapal:
    def start(self):
        print("kapal berjalan")
        
class Pesawat:
    def start(self):
        print("pesawat berjalan")
        
def operasi_kendaraan(kendaraan):
    kendaraan.start()
    
kendaraan_list = [
    Mobil(),
    Kapal(),
    Pesawat()
]

for kendaraan in kendaraan_list:
    operasi_kendaraan(kendaraan)
    
'''ABSTRACT BASE CLASS'''

from abc import ABC,abstractclassmethod
import math

class Shape(ABC):
    @abstractclassmethod
    def area(self):
        pass
    
class Rectangle(Shape):
    def __init__(self,panjang,lebar):
        self.panjang = panjang
        self.lebar = lebar
        
    def area(self):
        return self.panjang * self.lebar


class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2
    
shape = [
    Rectangle(10,10),
    Circle(100)
]

for s in shape:
    print(f"area is {s.area()}")