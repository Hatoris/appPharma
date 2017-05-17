from .pkg import *

class concentration():
    """ This class calculate a missing concentration or volume 
        Given by a list
    """
    
    def __init__(self, value):
        results = []
        if len(value) == 4:
            try:
                self.c2 = ureg(value[2]).to(ureg(value[0]).units)
                self.c1 = ureg(value[0])
                self.v2 = ureg(value[3]).to(ureg(value[1]).units)
                self.v1 = ureg(value[1])
            except pint.errors.DimensionalityError as e:
                print(e)
            except pint.errors.UndefinedUnitError as e:
                print(e)
            return
        if len(value) == 3:
            try:
                if (self.dimensionCheck(value[0]) == 1 or self.dimensionCheck(value[0]) == 2) and (self.dimensionCheck(value[2]) == 1 or self.dimensionCheck(value[2]) == 2) :
                    self.c1 = ureg(value[0]) 
                    self.c2 = ureg(value[2]).to(ureg(value[0]).units)
                    self.v1 = ureg(value[1])
                    self.v2 = ureg(0)
                elif self.dimensionCheck(value[0]) == 3 and self.dimensionCheck(value[2]) == 3:
                    self.c1 = ureg(0)
                    self.c2 = ureg(value[1])
                    self.v1 = ureg(value[0])
                    self.v2 = ureg(value[2]).to(ureg(value[0]).units)
                elif (self.dimensionCheck(value[0]) == 1 or self.dimensionCheck(value[0]) == 2) and self.dimensionCheck(value[2]) == 3:
                    if self.dimensionCheck(value[1]) == 3:
                        self.c1 = ureg(value[0])
                        self.c2 = ureg(0)
                        self.v1 = ureg(value[1])
                        self.v2 = ureg(value[2]).to(ureg(value[1]).units)
                    else:
                        self.c1 = ureg(value[0])
                        self.c2 = ureg(value[1]).to(ureg(value[0]).units)
                        self.v1 = ureg(0)
                        self.v2 = ureg(value[2])
                self.tc1 = 0
                self.tc2 = 0
            except pint.errors.DimensionalityError as e:
                print(e)
            except pint.errors.UndefinedUnitError as e:
                print(e)
         
    
    def c1(self):
        return self.c1
        
    
    def c2(self):
        return self.c2
        
    
    def v1(self):
        return self.v1
        
    
    def v2(self):
        return self.v2
        
    
    def all(self):
        data = []
        data.append(self.c1)
        data.append(self.v1)
        data.append(self.c2)
        data.append(self.v2)
        data.append(self.tc1)
        data.append(self.tc2)
        return data
                
                
    def dimensionCheck(self, ch):
        if str(ureg(ch).dimensionality) == '[mass] / [length] ** 3':
            return 1
        elif str(ureg(ch).dimensionality) == '[substance] / [length] ** 3':
            return 2
        elif str(ureg(ch).dimensionality) == '[length] ** 3':
            return 3
        elif str(ureg(ch).dimensionality) == '[mass]' or str(ureg(ch).dimensionality) == '[substance]':
            return 4
            
    def find(self, CorV):
        """find the missing value by given a string of what you looking for"""
        try:
            if self.dimensionCheck(CorV) == 1 or self.dimensionCheck(CorV) == 2:
                if str(self.c1.dimensionality) == 'dimensionless' :
                    self.c1 = (self.c2 * self.v2 / self.v1).to(CorV)
                    return self.c1
                else:
                    self.c2 = (self.c1 * self.v1 / self.v2).to(CorV)
                    return self.c2
            elif self.dimensionCheck(CorV) == 3:
                if str(self.v1.dimensionality) == 'dimensionless':
                    self.v1 = (self.c2 * self.v2 / self.c1).to(CorV)
                    return self.v1
                else:
                    self.v2 = (self.c1 * self.v1 / self.c2).to(CorV)
                    return self.v2
        except pint.errors.DimensionalityError as e:
            print(e)
        except pint.errors.UndefinedUnitError as e:
            print(e)
        except AttributeError as e:
            print(e)

    def quantity(self, MorV):
        "return volume or quantity for a mass you want or a volume used" 
        c1M, c1V = str(self.c1.units).split('/')
        c2M, c2V = str(self.c2.units).split('/')
        try:
            results = {}
            if self.dimensionCheck(MorV) == 4:
                results[str(self.c1)] = ureg(MorV).to(c1M) / self.c1 
                results[str(self.c2)] = ureg(MorV).to(c2M) / self.c2
            elif self.dimensionCheck(MorV) == 3:
                results[str(self.c1)] = self.c1 * ureg(MorV).to(c1V)
                results[str(self.c2)] = self.c2 * ureg(MorV).to(c2V)
            return results
        except pint.errors.UndefinedUnitError as e:
            print(e)
        except pint.errors.DimensionalityError as e:
            print(e)
            
    def teneurC(self, c = 0, mw=[]):
        "return teneur in % (g/100mL)"
        if c == 0:
            if not mw:
                c1M, c1V = str(self.c1.units).split('/')
                c2M, c2V = str(self.c2.units).split('/')
                c1M = ureg(str(self.c1.magnitude)+c1M).to('g')
                c2M = ureg(str(self.c2.magnitude)+c2M).to('g')
                c1V = ureg('1'+c1V).to('ml')
                c2V = ureg('1'+c2V).to('ml')
                self.tc1 = str(c1M.magnitude * 100 / c1V.magnitude) + ' %' 
                self.tc2 = str(c2M.magnitude * 100 / c2V.magnitude) + ' %'
                #print('{} {}'.format(self.tc1, self.tc2))           
                #return '{0} %'.format((mass * 100 / volume).magnitude)
            else:
                c1M, c1V = str(self.c1.units).split('/')
                c2M, c2V = str(self.c2.units).split('/')
                M1 = ureg(str(self.c1.magnitude)+c1M) * ureg(mw[0])
                M2 = ureg(str(self.c2.magnitude)+c2M) * ureg(mw[1])
                c1M = M1.to('g')
                c2M = M2.to('g')
                c1V = ureg('1'+c1V).to('ml')
                c2V = ureg('1'+c2V).to('ml')
                self.tc1 = str(c1M.magnitude * 100 / c1V.magnitude) + ' %' 
                self.tc2 = str(c2M.magnitude * 100 / c2V.magnitude) + ' %'
                #print('{} {}'.format(self.tc1, self.tc2))
        else:
            M, V = str(ureg(c).units).split('/')
            M = ureg(str(ureg(c).magnitude)+M).to('g')
            V = ureg('1'+V).to('ml')
            return(str(M.magnitude * 100 / V.magnitude) + ' %' ) 
            

if __name__ == '__main__':
    value = ['2mol/l', '200 mmol/l', '100l']
    conc = concentration(value)
    #print(conc.find('ul'))
    #conc.teneurC()
    #print(conc.all())
    print(conc.teneurC(c = 0, mw=['10g/mol', '20g/mol']))
    #print(conc.quantity('2mmol'))

