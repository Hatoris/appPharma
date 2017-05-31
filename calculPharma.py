"""
this module aim to perform stand alone calculation :
- bmi : body mass index
- bsa : body surface area
- content : percent of solute in solvant
- iw : ideal weight 
- aw : adjusted weight
- clairanceC : creatine's clairance
"""

from appPharma import pkg, wrapper
       

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
        volume wich contain element  '180ml' or '2ozl'

    Returns
    -------
    	pint.quantity
        quantity in percent

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
    """
    calcul ideal weight 

    Parameters
    ----------
    size : string 
        size of patient '180cm' or '65inch' 
    F : boolean, optional
        specify sex by default is False for man, pass True if patient is woman

    Returns
    -------
    pint.quantity
        quantity in kilogram 

    Raises
    ------

    Exemple
    --------
    >>>calculPharma.iw('180cm', F = True)
    >>><Quantity(70.4921, 'kilogram')>
    """
    if F:
        PI = 45.5 + 2.3 * (size.magnitude - 60)
    else:
        PI = 50 + 2.3 * (size.magnitude - 60)
    return pkg.ureg(str(PI) + 'kg')
    
@wrapper.changeUnits('kg', 'ignore', F = 'ignore')
def aw(weight, iwORsize, F = False):
    """
    calcul adapted weight 

    Parameters
    ----------
    weight : string
        weight of patient '90kg' or '180lb'
    iwORsize : string
        iw of patient '75.2kg' or '182lb' OR size of patient '1.80m' or '6foot'
    F : boolean, optional
        specify sex by default is False for man, pass True if patient is woman

    Returns
    -------
    pint.quantity
        quantity in kilogram 

    Raises
    ------

    Exemple
    --------
    >>>calculPharma.iw('180cm', F = True)
    >>><Quantity(70.4921, 'kilogram')>
    """
    w = weight
    p = pkg.ureg(iwORsize)
    if str(p.dimensionality) == '[mass]':
        pa = p.to('kg') + 0.4 * (w - p.to('kg'))
    elif str(p.dimensionality) == '[length]':
        pi = iw(p, F = F)
        pa = pi + 0.4 * (w - pi)
    return pa
    	
    	
@wrapper.changeUnits('ignore', 'kg', 'umol/l', F = 'ignore', min = 'ignore', size = 'inch')
def clairanceC(age, weight, crea, F = False, min = False, size = False):
    """
    calcul adapted weight 

    Parameters
    ----------
    age : integer
        patient age
    weight : string
        weight of patient '90kg' or '180lb'
    crea : string
        patient concentration of creatine serique of patient '145umol/l'
    F : boolean, optional
        specify sex by default is False for man, pass True if patient is woman
    min : boolean, optional
        specify if you want result in second by default is False, pass True if you want it in minute
    size : string, optional
        size of patient '1.80m' or '6foot' mendatory if patient have a BMI > 30 or age > 80

    Returns
    -------
    pint.quantity
        quantity in milliter / second OR milliter / minute

    Raises
    ------

    Exemple
    --------
    >>>calculPharma.clairanceC(27, "80kg", "145umol/l", F = True, min = True, size = "160cm")
    >>><Quantity(41.63818354602227, 'milliliter / minute')>
    """
    clai = 0
    bmis = 0
    if size:
        bmis = bmi(weight, size)
        bmis = bmis.magnitude
    if bmis < 30:
        if F:
            clai = str((((140 - age) * weight.magnitude) / (50 * crea.magnitude)) * 0.85) + 'ml/s'
        else:
            clai = str(((140 - age) * weight.magnitude) / (50 * crea.magnitude)) + 'ml/s'
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
    
def imperialSize(ftinch, conv = False):
    try :
        #str(pkg.ureg(ftinch).dimensionality) == "[length]":
        if conv:
            return pkg.ureg(ftinch).to(conv)
        else:
           f = pkg.ureg(ftinch)
           inc = f.to("inch")
           ft = f.to("feet") 
           ic = round(inc.magnitude) - round(ft.magnitude) * 12
           if ic < 0:
               return str(round(ft.magnitude) - 1) + "'" + str(12 + ic)
           else:
               return str(round(ft.magnitude)) + "'" + str(ic)
    except:
        foot, inch = ftinch.split("'")
        if conv:
            val = pkg.ureg(foot+"foot").to('inch') + pkg.ureg(inch + "inch") 
            return val.to(conv)
        else:
            return ftinch
    
    
