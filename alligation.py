from appPharma import pkg
"""
	parameter for alligation 
	a        pa
	    c    pc
	b        pb	
	
	avec a > b
	pX = parties de x
	"""

class alligation:
    
    def __init__(self, *args, **kwargs):
        self.a = 0
        self.b = 0
        self.c = 0
        self.pa = 0
        self.pb = 0
        self.pc = 0
        self.pera = 0
        self.perb = 0
        self.perc = 0
        if any(d in kwargs for d in ('a', 'b')):
            A = pkg.ureg(kwargs['a']).to(pkg.ureg(kwargs['b']).units)
            if A < pkg.ureg(kwargs['b']):
                self.a = pkg.ureg(kwargs['b']) 
                self.b = A
            else:
                self.a = A
                self.b = pkg.ureg(kwargs['b']) 
        if 'c' in kwargs:
            self.c = pkg.ureg(kwargs['c']) 
        if 'pa' in kwargs:
            self.pa = kwargs['pa']
        if 'pb' in kwargs:
            self.pb = kwargs['pb']
        if 'pc' in kwargs:
            self.pc = kwargs['pc']
        self.alliCalcul()
        self.percent()
        
    def alliCalcul(self):
        if self.a !=0 and self.c !=0:
            self.pb = float(self.a.magnitude) - float(self.c.magnitude) 
        if self.b !=0 and self.c !=0:
            self.pa = float(self.c.magnitude) - float(self.b.magnitude) 
        if self.pa !=0 and self.pc !=0:
            self.pb = float(self.pc) - float(self.pa)
        if self.pb !=0 and self.pc !=0:
            self.pa = float(self.pc) - float(self.pb) 
        if self.pa !=0 and self.pb !=0:
            self.pc = float(self.pa) + float(self.pb) 

    def percent(self):
        if self.pa != 0 and self.pc != 0:
            self.pera = pkg.ureg(str(self.pa / self.pc * 100) + 'percent')
        if self.pb != 0 and self.pc != 0:
            self.perb = pkg.ureg(str(self.pb / self.pc * 100) + 'percent') 
        
        

if __name__ == '__main__':
    a = alligation(a='1g/l', b='4mg/ml', c='3mg/ml', pc='3')
    print(a.a)
    print(a.b)
    print(a.c)
    print(a.pa)
    print(a.pb)
    print(a.pc)
    #a.alliCalcul()
    print(a.pa)
    print(a.pb)
    print(a.pc)
    #a.percent()
    print(a.pera)
    print(a.perb)