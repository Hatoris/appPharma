from .pkg import *
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
        if any(d in kwargs for d in ('a', 'b')):
            A = ureg(kwargs['a']).to(ureg(kwargs['b']).units)
            if A < ureg(kwargs['b']):
                self.a = ureg(kwargs['b']) 
                self.b = A
            else:
                self.a = A
                self.b = ureg(kwargs['b']) 
        if 'c' in kwargs:
            self.c = ureg(kwargs['c']) 
        if 'pa' in kwargs:
            self.pa = kwargs['pa']
        if 'pb' in kwargs:
            self.pb = kwargs['pb']
        if 'pc' in kwargs:
            self.pc = kwargs['pc']
        
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
        
        
        

if __name__ == '__main__':
    a = alligation(a='1g/l', b='4mg/ml', c='3mg/ml', pc='3')
    print(a.a)
    print(a.b)
    print(a.c)
    print(a.pa)
    print(a.pb)
    print(a.pc)
    a.alliCalcul()
    print(a.pa)
    print(a.pb)
    print(a.pc)