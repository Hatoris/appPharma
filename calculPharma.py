"""
this module aim to perform stand alone calculation :
- bmi : body mass index
- bsa : body surface area
- content : percent of solute in solvant
- iw : ideal weight 
- aw : adjusted weight
- clairanceC : creatine's clairance
"""

from . import pkg, wrapper
       

@wrapper.changeUnits('kg', 'm') 
def bmi(weight, size):
    """
    calcul the body mass index in kg/m**2

    Parameters
    ----------
    weight : string 
        string of body weight '75kg' or '150lb' 
    size : string
        string of body size '180cm' or '64inch'

    Returns
    -------
    pint.quantity
        quantity in kg/m**2 

    Raises
    ------

    Exemple
    --------
    >>>calculPharma.bmi('80kg', '180cm')
    >>><Quantity(24.6913580, 'kilogram / meter ** 2') >
    """
    return (weight / (size**2)).to('kg/m**2')

@wrapper.changeUnits('kg', 'cm') 
def bsa(weight, size):
    """
    calcul the body surface area in m**2

    Parameters
    ----------
    weight : string 
        string of body weight '75kg' or '150lb' 
    size : string
        string of body size '180cm' or '64inch'

    Returns
    -------
    pint.quantity
        quantity in m**2

    Raises
    ------

    Exemple
    --------
    >>>calculPharma.bsa('80kg', '180cm')
    >>><Quantity(2.0, 'meter ** 2') >
    """
    BSA = ( weight * size / 3600) ** 0.5
    BSA = pkg.ureg(str(BSA.magnitude) + 'm**2') 
    return BSA
    
@wrapper.changeUnits('g', 'ml') 
def content(mass, volume):
   """
    calcul the content of solution in %

    Parameters
    ----------
    mass : string 
        mass of element '7.5g' or '2oz' 
    volume : string
        volume wich contain element  '180ml' or '1l'

    Returns
    -------
    string
        results %

    Raises
    ------

    Exemple
    --------
    >>>calculPharma.content('2g', '1l')
    >>><Quantity(0.2, 'percent')>
    """
   return pkg.ureg('{0} percent'.format((mass * 100 / volume).magnitude)) 
   
    
@wrapper.changeUnits('inch', F = 'ignore')
def iw(size, F = False):
    if F:
        PI = 45.5 + 2.3 * (size.magnitude - 60)
    else:
        PI = 50 + 2.3 * (size.magnitude - 60)
    return pkg.ureg(str(PI) + 'kg')
    
@wrapper.changeUnits('kg', 'ignore', F = 'ignore')
def aw(weight, piorsize, F = False):
    w = weight
    p = pkg.ureg(piorsize)
    if str(p.dimensionality) == '[mass]':
        pa = p + 0.4 * (w - p)
    elif str(p.dimensionality) == '[length]':
        pi = iw(p, F = F)
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
        IdeP = iw(size, F = F)
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


