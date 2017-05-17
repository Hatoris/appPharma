# this script old all method to perform calcul
# class calculPharma take a sting as input
from .pkg import *

class convertPharma():

    def __init__(self, p):
        self._value, self._converts = p.split(' to ')
        self._listConverts = self._converts.split(' ') 
    
    @property
    def value(self):
        return self._value
        
    @property
    def converts(self):
        return self._converts
        
    @property
    def listConverts(self):
        return self._listConverts
    
    @property    
    def results(self):
        r = {}
        l = []
        a = Q_(self.value)
        for convert in self.listConverts:
            l.append(str(a.to(convert))) 
        r[self.value] = l
        return r
            
        
    




if __name__ == '__main__' :
    c = convertPharma('180cm to inch foot m')
    c.value
    c.converts
    print(c.listConverts)
    print(c.results())
    