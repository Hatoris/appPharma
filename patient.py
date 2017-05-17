# patient class to play with it
from pkg import *
from wrapper import changeUnits
from calculPharma import *

class patient:
    
    def __init__(self, weight = '90kg', size= '180cm', sexe = 'M', age = 27):
        if sexe == 'M':
            self.PI = PI(size)
            self.PA = PA(weight, size) 
        else:
            self.PI = PI(size, F = True)
            self.PA = PA(weight, size, F = True) 
        self.BMI = bmi(weight, size)
        self.BSA = bsa(weight, size)
        self.weight = ureg(weight) 
        self.size = ureg(size) 
        self.sexe = sexe
        self.age = age
        self.Clairance = 1

    @property
    def allInformations(self):
        infos = {'weight' : self.weight, 'size' : self.size, 
        'sexe' : self.sexe, 'age' : self.age, 
        'BMI' : self.BMI, 'BSA' : self.BSA, 'PI' : self.PI, 'PA' : self.PA,
        'clairance' : self.Clairance
        }
        return infos
        
    def clairance(self, crea, min = False):
        if self.sexe == 'M':
            s = False
        else:
            s = True 
        clai = clairanceC(self.age, str(self.weight), crea, F = s, min = min, size = str(self.size))
        self.Clairance = clai 
        return clai
        
if __name__ == '__main__':
    Bob = patient('80kg', '180cm', 'M', 27)
    print(Bob.allInformations)
    print(Bob.clairance('145umol/l', min = False)) 
    Bob.Clairance
    

        