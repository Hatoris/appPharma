from appPharma import pkg, wrapper

class concentration:
    @wrapper.changeUnits("ignore", c1 = "ignore", v1 ="ignore", c2 ="ignore", v2="ignore") 
    def __init__(self, c1 = "0", v1 = "0", c2 = "0", v2 = "0"):
        try:
            self.c1 = c1
            self.v1 = v1
            self.c2 = c2
            self.v2 = v2
        except Exception as e:
            print(e)
        if self.c1 == 0:
            self.c1 = self.c2 * self.v2 / self.v1.to(self.v2.units)
            pass
        elif self.v1 == 0:
            self.v1 = self.c2 * self.v2 / self.c1.to(self.c2.units)
            pass
        elif self.c2 == 0:
            self.c2 = self.c1 * self.v1 / self.v2.to(self.v1.units)
            pass
        elif self.v2 == 0:
            self.v2 = self.c1 * self.v1 / self.c2.to(self.c1.units)
            pass
    
    @property
    def value(self):
        print("c1 = {} v1 = {} c2 = {} v2 = {}".format(self.c1, self.v1, self.c2, self.v2)) 

    def changeUnits(self, conc = False, volume = False):
        if conc:
            self.c1 = self.c1.to(conc)
            self.c2 = self.c2.to(conc)
        if volume:
            self.v1 = self.v1.to(volume)
            self.v2 = self.v2.to(volume)
    
    @property       
    def volumeToTake(self):
        return("{} of {} and add {} to get {}".format(self.v1, self.c1, self.v2 - self.v1, self.c2))
    

    def cascadeDilution(self, initConc = "0", finalVolume = "1000ul", dilution = (3/4, 1/2, 1/4, 1/10, 3/40, 1/20, 1/40, 3/400, 1/200, 1/400)):
        I = pkg.ureg(initConc)
        conc = {}
        conc[1] = {"concF" : I, "concI" : I, "volumeI" : finalVolume, "volumeD" : 0} 
        try:
            for x in range(len(dilution)):
                dil = {}
                dil["concF"] = I * dilution[x]
                conc[dilution[x]] = dil
        except Exception as e:
            print(e) 
        for d in sorted(conc, reverse = True):
            for u in conc[d]:
                print ("take {} ".format(conc[d][u]))
        
        
        
        
if __name__ == '__main__':
    A = concentration( c1 = "1pct", v1="1ul", c2 = "1ng/ml", v2 = "10ml")
    B = concentration( v1="1ul", c2 = "1ng/ml", v2 = "10ml")
    C = concentration( c1 = "10ug/ml", c2 = "1ng/ml", v2 = "10ml")
    D = concentration( c1 = "10ug/ml", v1="1ul", v2 = "10ml")
    E = concentration( c1 = "10ug/ml", v1="1ul", c2 = "1ng/ml")
    print(A.value)
    #B.value
    #C.value
    #D.value
    #E.value
    #A.changeUnits(conc = "ug/ml")
    #A.value
    #print(A.volumeToTake)
    #print(A.cascadeDilution(initConc = "1000ug/ml"))


