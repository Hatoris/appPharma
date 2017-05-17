from . import pkg, wrapper
       

@wrapper.changeUnits('kg', 'm') 
def bmi(weight, size):
    """ return the body mass index """
    return (weight / (size**2)).to('bmi')

@wrapper.changeUnits('kg', 'cm') 
def bsa(weight, size):
    """return the body surface area (bsa)"""
    BSA = ( weight * size / 3600) ** 0.5
    BSA = pkg.ureg(str(BSA.magnitude) + 'm**2') 
    return BSA
    
@wrapper.changeUnits('g', 'ml') 
def content(mass, volume):
   " return teneur in % (g/100mL)"
   return '{0} %'.format((mass * 100 / volume).magnitude)
   
    
@wrapper.changeUnits('inch', F = 'ignore')
def pi(size, F = False):
    if F:
        PI = 45.5 + 2.3 * (size.magnitude - 60)
    else:
        PI = 50 + 2.3 * (size.magnitude - 60)
    return pkg.ureg(str(PI) + 'kg')
    
@wrapper.changeUnits('kg', 'ignore', F = 'ignore')
def PA(weight, piorsize, F = False):
    w = weight
    p = pkg.ureg(piorsize)
    if str(p.dimensionality) == '[mass]':
        pa = p + 0.4 * (w - p)
    elif str(p.dimensionality) == '[length]':
        pi = PI(p, F = F)
        pa = pi + 0.4 * (w - pi)
    return pa
    	
    	
@wrapper.changeUnits('ignore', 'kg', 'umol/l', F = 'ignore', min = 'ignore', size = 'inch') 
def clairanceC(age, masse, crea, F = False, min = False, size = False):
    """    this function Calcul clairance of patient
        require parameters :
        - age : integer (58)
        - weight : string ('75kg') 
        - creatine serique : string ('140umol/l')
        optional parameters :
        - F : boolean (F = True) [F = False] *specify sex
        - min : boolean (min = True) [min = False] *specify if you want results in minute
        - size : string (size = '180cm') [size = False] *specify size if patient is above 80 year or bmi > 30 
    """
    clai = 0
    bmis = 0
    if size:
        bmis = bmi(masse, size)
        bmis = bmis.magnitude
    if bmis < 30:
        if F:      
            clai = str((((140 - age) * masse.magnitude) / (50 * crea.magnitude) * 0.85)) + 'ml/s'
        else: 
            clai = str(((140 - age) * masse.magnitude) / (50 * crea.magnitude)) + 'ml/s'
        if min:
            clai = pkg.ureg(clai) * pkg.ureg('60s/min') 
        else:
            clai = pkg.ureg(clai)
    elif bmis > 30 or age > 80:
        IdeP = pi(size, F)
        if F:
            if age > 80:
                clai = str((((140 - age) * IdeP.magnitude) / (49 * crea.magnitude) * 0.85)) + 'ml/s' 
            else:
                clai = str((((140 - age) * IdeP.magnitude) / (50 * crea.magnitude) * 0.85)) + 'ml/s' 
        else:
            if age > 80:
                clai = str(((140 - age) * IdeP.magnitude) / (49 * crea.magnitude)) + 'ml/s'
            else:
                clai = str(((140 - age) * IdeP.magnitude) / (50 * crea.magnitude)) + 'ml/s'
        if min:
            clai = pkg.ureg(clai) * pkg.ureg('60s/min') 
        else:
            clai = pkg.ureg(clai)
    return clai


