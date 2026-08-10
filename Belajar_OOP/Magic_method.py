'''Contoh magic method'''
class A:
    
    def __init__(self,nama,jumlah): # <-- ini adalah magic method yang standar
        self.nama = nama
        self.jumlah = jumlah
    
    def __repr__(self):  # <-- untuk debugging atau menyelesaikan masalah
        return f"Buah : {self.nama} dengan jumlah {self.jumlah}"
    
    def __str__(self): # <-- unutuk tampilan user
        return f"Buah : {self.nama} dengan jumlah {self.jumlah}" 
    
    # ketika repr tidak dapat didefinisikan atau eror maka akan mengambil dari str untuk ditampilkan
    
    def __add__(self, objek):
        return f"total buah yang dibeli adalah : {self.jumlah + objek.jumlah}"
    
    @property
    def __dict__(self):
        return f"objek ini mempunyai nama dan jumlah : {self.__add__}"

    
belanja_1 = A("Nanas",10)
belanja_2 = A("Durian",5)
print(belanja_1)

print(belanja_1 + belanja_2)
print(belanja_1.__dict__)