'''Latihan Encapsulai dengan contoh hero game'''


class Hero:
    __jumlah = 0
    
    def __init__(self,name,health,attPower,armor):
        self.__name = name
        self.__healthStandar = health
        self.__attPowerStandar = attPower
        self.__armorstandar = armor
        self.__level = 1
        self.__exp = 0
        
        self.__healthMax = self.__healthStandar * self.__level
        self.__attPOwer = self.__attPowerStandar * self.__level
        self.__armor = self.__armorstandar * self.__level
        self.__health = self.__healthMax
        
        Hero.__jumlah += 1
        
    @property
    def info(self):
        return f"nama : {self.__name},\n\t level : {self.__level},\n\thealth = {self.__health}/{self.__healthMax}, \n\tPower = {self.__attPOwer},\n\tarmor = {self.__armor}"
        # return "{} level {}: \n\thealth = {}/{}\n\tattack = {} \n\tarmor = {}".format(self.__name,self.__level,self.__health,self.__healthMax,self.__attPOwer,self.__armor)
    
    @property
    def gainExp(self):
        pass
    
    @gainExp.setter
    def gainExp(self,addExp):
        self.__exp += addExp
        if (self.__exp >= 200):
            print("level up!")
            self.__level += 1
            self.__exp -= 200
            
            self.__healthMax = self.__healthStandar * self.__level
            self.__attPOwer = self.__attPowerStandar * self.__level
            self.__armor = self.__armorstandar * self.__level
            
    def attack(self,musuh):
        self.gainExp = 50
        
Beatrix = Hero("Beatrix",200,50,30)
Balmond = Hero("Balmond",200,30,80)

print(Beatrix.info)
print(Balmond.info)


Beatrix.attack(Balmond)
Beatrix.attack(Balmond)
Beatrix.attack(Balmond)
Beatrix.attack(Balmond)
print(Beatrix.info)

Balmond.attack(Beatrix)
Balmond.attack(Beatrix)
Balmond.attack(Beatrix)
Balmond.attack(Beatrix)
print(Balmond.info)


Beatrix.attack(Balmond)
Beatrix.attack(Balmond)
Beatrix.attack(Balmond)
Beatrix.attack(Balmond)
print(Beatrix.info)

Balmond.attack(Beatrix)
Balmond.attack(Beatrix)
Balmond.attack(Beatrix)
Balmond.attack(Beatrix)
print(Balmond.info)


Beatrix.attack(Balmond)
Beatrix.attack(Balmond)
Beatrix.attack(Balmond)
Beatrix.attack(Balmond)
print(Beatrix.info)

Balmond.attack(Beatrix)
Balmond.attack(Beatrix)
Balmond.attack(Beatrix)
Balmond.attack(Beatrix)
print(Balmond.info)

'''Program sederhana dengan contoh hero game dengan sistem level up'''