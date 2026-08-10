class Hero:
    
    def __init__(self,name):
        self.health_pool = [0,100,200,300,400,500]
        self.attackPower_pool = [0,10,20,30,40,50]
        self.armor_pool = [0,5,10,15,20,25]
        self.__name = name
        self.__exp = 0
        self.__level = 0
        
    def show_info(self):
        print(f"{self.__name} \n\tlevel = {self.__level} \n\thealth = {self.__health} \n\tattack = {self.__attack} \n\tarmor = {self.__armor}")
        
    
    @property
    def health_pool(self):
        pass
    
    @property
    def attackPower_pool(self):
        pass
    
    @property
    def armor_pool(self):
        pass
    
    @property
    def gainExp(self):
        pass
    
    @property
    def levelUp(self):
        pass
    
    @health_pool.setter
    def health_pool(self,input):
        self.__health_pool = input
        
    @attackPower_pool.setter
    def attackPower_pool(self,input):
        self.__attackPower_pool = input
        
    @armor_pool.setter
    def armor_pool(self,input):
        self.__armor_pool = input
        
    @gainExp.setter
    
    def gainExp(self,input):
        print("level up")
        self.__exp += input
        if(self.__exp >= 100):
            self.levelUp = self.__exp// 100
            self.__exp %= 100
            
    @levelUp.setter
    def levelUp(self,input):
        self.__level += input
        self.__health = self.__health_pool[self.__level]
        self.__attack = self.__attackPower_pool[self.__level]
        self.__armor = self.__armor_pool[self.__level]
        


class Hero_kekuatan(Hero):
    def __init__(self, name):
        super().__init__(name)
        self.health_pool = [0,100,200,300,400,500]
        self.attackPower = [0,30,60,90,120,150]
        self.armor_pool = [0,20,40,60,80,100]
        self.levelUp = 1
        

class Hero_kelincahan(Hero):
    def __init__(self, name):
        super().__init__(name)
        self.health_pool = [0,50,100,150,200,250]
        self.attackPower_pool = [0,50,100,150,200,250]
        self.armor_pool = [0,10,20,30,40,50]
        self.levelUp = 1
