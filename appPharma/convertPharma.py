# class calculPharma take a sting as input
import re
from typing import List, Generator

from appPharma.pkg import Q_, ureg



class convertPharma():
    """use it to convert an information to multiple one by using "xx to yy ll mm" """

    def __init__(self, values):
        self._value, self._unitToConvert = values.split(" to ")
        self._unitToConvert = re.findall(r"\b[a-zA-Z]+\b" , self._unitToConvert)
           
    @property
    def value(self) -> str:
        return self._value
        
    @property
    def unitToConvert(self) -> List:
        return self._unitToConvert
    
    @property    
    def results(self):
        r = {}
        l = []
        v = Q_(self.value)
        for convert in self._unitToConvert:
            l.append(str(v.to(convert))) 
        r[self.value] = l
        return r
            
    @property
    def humanRead(self) -> Generator:
        read = self.results
        for k in read:
            for val in read[k]:
                val = ureg(val)
                yield f"{k} = {val.magnitude:.2f} {val.units}"

    