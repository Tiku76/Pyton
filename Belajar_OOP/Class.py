'''CLASS OOP'''

class Hero:
    # class variable --> variable dari class
    jumlah = 0
    def __init__(self,inputname,inputhealth,inputpower,inputarmor): # Template
        # variable instance -->atribut dari object
        self.name = inputname
        self.health = inputhealth
        self.power = inputpower
        self.armor = inputarmor
        Hero.jumlah += 1
        print("membuat hero dengan nama",inputname)
        
    # void funtion, method tanpa return,tanpa argumen
    def nama(self):
        print(f"namaku adalah {self.name}")
    
    # method dengan argumen tanpa return
    def healthup(self,up):
        self.health += up
    
    # method dengan return
    def gethealth(self):
        return self.health


hero1 = Hero("Sakung",100,50,10)
hero2 = Hero("indi",100,80,100)

hero1.nama()
hero1.healthup(30)

print(f"ini adalah gethealth {hero1.gethealth()}")