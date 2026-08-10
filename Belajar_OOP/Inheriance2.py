class Kendaraan:
    def __init__(self,merek,tahun):
        self.merek = merek
        self.tahun = tahun
        
    def info(self):
        return f"Merek {self.merek}, tahun : {self.tahun} "
    
    def nyalakan(self):
        print(f"{self.merek} dinyalakan")
        
class Mobil(Kendaraan):
    def klakson(self):
        print(f"mobil {self.info()} memiliki klakson")


Avanza = Mobil("Avanza",2012)
Avanza.nyalakan()
Avanza.klakson()
