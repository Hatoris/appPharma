# class calculPharma take a sting as input
from appPharma import pkg
import re

class convertPharma():
    """use it to convert an information to multiple one by using "xx to yy ll mm" """

    def __init__(self, values):
        self._value, self._unitToConvert = values.split(" to ") 
        print(self._unitToConvert) 
        self._unitToConvert = re.findall(r"\b[a-zA-Z]+\b" , self._unitToConvert)
        
    
    @property
    def value(self):
        return self._value
        
    @property
    def unitToConvert(self):
        return self._unitToConvert
    
    @property    
    def results(self):
        r = {}
        l = []
        v = pkg.Q_(self.value)
        for convert in self._unitToConvert:
            l.append(str(v.to(convert))) 
        r[self.value] = l
        return r
            
    @property
    def humanRead(self):
        read = self.results
        for k in read:
            for val in read[k]:
                print(k + " = " + val) 


if __name__ == '__main__' :
    c = convertPharma('180cm to inch foot m')
    print(c.value) 
    print(c.unitToConvert)
    print(c.results)
    print(c.humanRead)
    