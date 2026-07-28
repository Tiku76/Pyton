'''LATIHAN SEDERHANA DENAGN CONTOH GAME'''
import os
import random
os.system("cls")


class Hero:
    def __init__(self,name,health,attackpower,armor):
        self.name = name
        self.health = health
        self.attackpower = attackpower
        self.armor = armor
    def serang(self,lawan):
        print(f"{self.name} menyerang {lawan.name}")
        lawan.diserang(self,self.attackpower)
        
    def diserang(self,lawan,attack_power_lawan):
        print(f"{self.name} diserang {lawan.name}")
        attack_diterima = attack_power_lawan//self.armor
        print(f"serangan terasa : {str(attack_diterima)}")
        self.health -= attack_diterima
        print(f"darah {self.name} tersisa {str(self.health)}")
    
    def upgrade(self):
        tambahan_attack = random.randint(1, 10)
        tambahan_armor = random.randint(1, 5)
        self.attackpower += tambahan_attack
        self.armor += tambahan_armor
        print(f" {self.name} UPGRADE! attack +{tambahan_attack} (jadi {self.attackpower}), "f"armor +{tambahan_armor} (jadi {self.armor})")


Balmond = Hero("Balmond",100,50,20)
Miya = Hero("Miya",90,40,10)

ronde = 1
# loop sampai salah satu hero darahnya habis (<= 0)
while Balmond.health > 0 and Miya.health > 0:
    print(f"\n--- Ronde {ronde} ---")

    Balmond.serang(Miya)
    if Miya.health <= 0:
        print(f"\n{Miya.name} kalah! {Balmond.name} menang!")
        break

    Miya.serang(Balmond)
    if Balmond.health <= 0:
        print(f"\n{Balmond.name} kalah! {Miya.name} menang!")
        break
    
    if ronde % 5 == 0:
        print(f"\n=== Ronde {ronde}: Waktunya upgrade! ===")
        Balmond.upgrade()
        Miya.upgrade()

    ronde += 1